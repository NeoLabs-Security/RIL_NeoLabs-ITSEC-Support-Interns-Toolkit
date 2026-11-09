"""Offline client contract tests for automatic Week05 SSH registration and host pinning."""
import base64
import os
from pathlib import Path
import struct
import tempfile
import unittest
from unittest.mock import patch

from tools import week05_auto_enroll


def fixture(track):
    prefix = "nlw05p_" if track == "PENTEST" else "nlw05sup_"
    return {
      "scenario_id":"w05-poisoned-upload",
      "track":track,"student_ready":True,"lab_state":"STUDENT_READY",
      "resources":{
        "scope_status":"LIVE_TUNNEL",
        "ssh_host_key_ed25519":"ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILF2Nxc7YkQY3yrstE5Q4RtB6mvFwb6EV5n3o7mKkxei",
        "tunnel":{"transport":"ssh-local-forward","host":"192.0.2.20",
                  "username":prefix+"012345abcdef","port":22,
                  "remote_host":"127.0.0.1","remote_port":18600,"local_port":18080}
      }
    }


class FakeCli:
    def __init__(self, temp, manifest):
        self.HOME_STATE=Path(temp)
        self.manifest=manifest
        self.requests=[]
        self.polls=0

    def fail(self,msg):
        raise RuntimeError(msg)

    def read_session(self):
        return {"base_url":"https://test.example:18443","session_token":"token-not-real"}

    def validate_base_url(self,url):
        return url

    def request_json(self,base,path,**kwargs):
        self.requests.append((path,kwargs))
        if path.endswith("/status"):
            self.polls+=1
            return {"status":"ready"}
        return {"status":"registered"}

    def refresh(self,session):
        return self.manifest

    def atomic_write(self,path,text,mode=0o600):
        Path(path).write_text(text)
        os.chmod(path,mode)


class Week05AutomaticEnrollmentTests(unittest.TestCase):
    def _run(self,track):
        with tempfile.TemporaryDirectory() as temp:
            scenario=fixture(track)
            cli=FakeCli(temp,scenario)
            name="w04-tunnel-ed25519" if track=="PENTEST" else "w05-tunnel-ed25519"
            private=Path(temp)/name
            private.write_text("synthetic test fixture, not a real SSH private key")
            private.chmod(0o600)
            payload=struct.pack(">I",11)+b"ssh-ed25519"+struct.pack(">I",32)+bytes(range(32))
            public="ssh-ed25519 "+base64.b64encode(payload).decode()+" test"
            Path(str(private)+".pub").write_text(public+"\n")
            returned,key,known=week05_auto_enroll.auto_enroll(cli,scenario,name)
            self.assertEqual(returned,scenario)
            self.assertEqual(key,private)
            self.assertEqual(known.read_text(), "192.0.2.20 "+scenario["resources"]["ssh_host_key_ed25519"]+"\n")
            self.assertEqual(known.stat().st_mode & 0o777,0o600)
            self.assertEqual(cli.polls,1)
            self.assertEqual(cli.requests[0][0],"/api/v1/lab-access/tunnel-key")
            self.assertEqual(cli.requests[0][1]["payload"]["public_key"],public)
            self.assertEqual(cli.requests[1][0],"/api/v1/lab-access/tunnel-key/status")
            self.assertNotIn("private",str(cli.requests))

    def test_pentest_public_only_registration(self):
        self._run("PENTEST")

    def test_support_public_only_registration(self):
        self._run("SUPPORT")

    def test_wrong_scenario_fails_closed_without_registration(self):
        with tempfile.TemporaryDirectory() as temp:
            bad=fixture("SUPPORT"); bad["scenario_id"]="w04-broken-gate"
            cli=FakeCli(temp,bad)
            with self.assertRaisesRegex(RuntimeError,"wrong scenario"):
                week05_auto_enroll.auto_enroll(cli,bad,"w05-tunnel-ed25519")
            self.assertEqual(cli.requests,[])


if __name__=="__main__":
    unittest.main()
