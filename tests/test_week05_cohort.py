"""Standalone Pod01 cohort forwarding never relies on W04 broker state or password SSH."""
from __future__ import annotations
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch, MagicMock
from tools import week05_cohort as cohort
from tools import neolabs


def valid_state(root):
    root=Path(root)
    key=root/"w05-tunnel-ed25519"
    key.write_text("synthetic test key")
    key.chmod(0o600)
    pub=Path(str(key)+".pub")
    pub.write_text("ssh-ed25519 synthetictestonly")
    known=root/"w05-known-hosts"
    known.write_text("example.invalid ssh-ed25519 synthetic")
    known.chmod(0o600)
    profile=root/"w05-cohort-profile.json"
    profile.write_text(json.dumps({
        "role":cohort.ROLE,"pod_id":"pod-01","host":"example.invalid",
        "username":"nlw05sup_012345abcdef","port":22,
        "fingerprint":"SHA256:" + "X"*43,
        "expires_at":"2026-11-16T06:00:00Z"
    }))
    profile.chmod(0o600)
    return key,pub,known,profile


class CohortTests(unittest.TestCase):
    def test_cli_parser_has_explicit_profile_commands(self):
        p=neolabs.parser()
        self.assertEqual(p.parse_args(["week05","keygen"]).week05_command,"keygen")
        self.assertEqual(p.parse_args(["week05","clear"]).week05_command,"clear")

    def test_connect_does_not_refresh_w04_when_profile_active(self):
        with tempfile.TemporaryDirectory() as folder:
            key,pub,known,profile=valid_state(folder)
            with patch.object(cohort,"PROFILE",profile), patch.object(cohort,"KEY",key), \
                 patch.object(cohort,"KNOWN",known), patch.object(cohort.shutil,"which",return_value="/usr/bin/ssh"), \
                 patch.object(cohort.subprocess,"run") as proc, \
                 patch.object(neolabs,"refresh") as refresh, \
                 patch.object(neolabs,"read_session") as read:
                neolabs.connect(MagicMock())
                refresh.assert_not_called()
                read.assert_not_called()
                args=proc.call_args.args[0]
                self.assertEqual(args[0],"/usr/bin/ssh")
                self.assertIn("StrictHostKeyChecking=yes",args)
                self.assertIn("PasswordAuthentication=no",args)
                self.assertIn("BatchMode=yes",args)
                self.assertIn("127.0.0.1:18080:127.0.0.1:18600",args)
                self.assertIn("nlw05sup_012345abcdef@example.invalid",args)
                self.assertNotIn("accept-new",args)

    def test_does_not_accept_wrong_track_or_pod(self):
        with tempfile.TemporaryDirectory() as folder:
            key,pub,known,profile=valid_state(folder)
            data=json.loads(profile.read_text())
            data["pod_id"]="pod-02"
            profile.write_text(json.dumps(data))
            with patch.object(cohort,"PROFILE",profile), patch.object(cohort,"KEY",key), \
                 patch.object(cohort,"KNOWN",known):
                with self.assertRaises(SystemExit):
                    cohort.profile()
            data["pod_id"]="pod-01"
            data["username"]="nlw05p_012345abcdef"
            profile.write_text(json.dumps(data))
            with patch.object(cohort,"PROFILE",profile), patch.object(cohort,"KEY",key), \
                 patch.object(cohort,"KNOWN",known):
                with self.assertRaises(SystemExit):
                    cohort.profile()

    def test_no_profile_does_not_migrate_w04(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.object(cohort,"PROFILE",Path(folder)/"absent"):
                self.assertIsNone(cohort.profile())
                self.assertFalse(cohort.connect())

    def test_expired_cohort_fails_closed(self):
        with tempfile.TemporaryDirectory() as folder:
            key,pub,known,profile=valid_state(folder)
            with patch.object(cohort,"PROFILE",profile), patch.object(cohort,"KEY",key), \
                 patch.object(cohort,"KNOWN",known), \
                 patch.object(cohort,"EXPIRY",datetime.now(timezone.utc)-timedelta(days=1)):
                with self.assertRaises(SystemExit):
                    cohort.connect()


if __name__ == "__main__":
    unittest.main()
