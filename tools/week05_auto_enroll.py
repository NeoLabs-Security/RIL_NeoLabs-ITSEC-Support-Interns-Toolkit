"""Week05 hands-free SSH enrollment through the original NeoLabs HTTPS broker.

Invoked automatically by 'neolabs connect', never by a separate keygen or scp.
Private student keys stay on the student's device. Server host SSH fingerprint
is pinned from the AUTHENTICATED current broker manifest, not SSH TOFU.
"""
from __future__ import annotations
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import time


def auto_enroll(cli, manifest, filename):
    if manifest.get("scenario_id") != "w05-poisoned-upload":
        cli.fail("Automatic Week 05 SSH enrolment called on wrong scenario")
    if manifest.get("student_ready") is not True or manifest.get("lab_state") != "STUDENT_READY":
        cli.fail("Your Week 05 assignment is not student-ready")
    if manifest.get("track") not in ("PENTEST","SUPPORT"):
        cli.fail("This track cannot use Week 05 interactive SSH enrollment")
    key_path = cli.HOME_STATE / filename
    pub_path = Path(str(key_path) + ".pub")
    if key_path.is_symlink() or pub_path.is_symlink():
        cli.fail("Refusing symlinked SSH identity")
    if not key_path.exists() and not pub_path.exists():
        sshgen = shutil.which("ssh-keygen")
        if not sshgen:
            cli.fail("OpenSSH ssh-keygen is required; install the OpenSSH client")
        key_path.parent.mkdir(parents=True,exist_ok=True)
        try:
            subprocess.run([sshgen,"-q","-t","ed25519","-N","","-f",str(key_path),
                            "-C","neolabs-w05-automatic"],check=True)
        except subprocess.CalledProcessError:
            cli.fail("Could not generate local Week 05 restricted SSH key")
        os.chmod(key_path,0o600)
        print("✓ Generated your private SSH identity locally; no manual key setup needed.")
    if (not key_path.is_file() or not pub_path.is_file() or
        stat.S_IMODE(key_path.stat().st_mode) & 0o077):
        cli.fail("SSH key pair incomplete or private key permissions too broad")
    public = pub_path.read_text(encoding="utf-8").strip()
    if not re.fullmatch(r"ssh-ed25519 [A-Za-z0-9+/]+={0,2}(?: [A-Za-z0-9._@-]{1,100})?",public):
        cli.fail("Unexpected local Ed25519 public key")
    session = cli.read_session()
    base = cli.validate_base_url(str(session["base_url"]))
    cli.request_json(base,"/api/v1/lab-access/tunnel-key",
                     method="POST",payload={"public_key":public},
                     token=str(session["session_token"]))
    print("✓ Public key securely registered with your assigned NeoLabs broker.")
    print("✓ Waiting for automatic server SSH authorization...")
    for attempt in range(20):
        response = cli.request_json(base,"/api/v1/lab-access/tunnel-key/status",
                                    token=str(session["session_token"]))
        status = response.get("status")
        if status == "ready":
            refreshed = cli.refresh(cli.read_session())
            resources = refreshed.get("resources")
            tunnel = resources.get("tunnel") if isinstance(resources,dict) else None
            if (not isinstance(resources,dict) or resources.get("scope_status") != "LIVE_TUNNEL"
                or not isinstance(tunnel,dict) or tunnel.get("transport") != "ssh-local-forward"
                or tunnel.get("remote_host") != "127.0.0.1"
                or tunnel.get("remote_port") != 18600 or tunnel.get("local_port") != 18080
                or str(tunnel.get("username","")).startswith("nlw05") is False):
                cli.fail("Broker reported SSH ready but did not publish the expected restricted Week 05 target")
            pin = resources.get("ssh_host_key_ed25519")
            if not isinstance(pin,str) or not re.fullmatch(r"ssh-ed25519 [A-Za-z0-9+/]+={0,2}",pin):
                cli.fail("Broker did not provide a verified SSH host key")
            host = tunnel.get("host")
            port = tunnel.get("port")
            if not isinstance(host,str) or not re.fullmatch(r"[A-Za-z0-9.-]{4,253}",host):
                cli.fail("Broker published an invalid SSH host")
            if port != 22:
                cli.fail("Broker published an unexpected Week 05 SSH port")
            pinned_host = cli.HOME_STATE / "w05-known-hosts"
            cli.atomic_write(pinned_host, f"{host} {pin}\n",mode=0o600)
            print("✓ Server enrolled your key and broker-pinned its SSH host identity.")
            return refreshed, key_path, pinned_host
        if status != "pending":
            cli.fail("Unexpected Week 05 SSH key enrollment status")
        if attempt < 19:
            time.sleep(2)
    cli.fail("SSH enrollment has not completed. Contact the mentor to check the Week 05 server synchronizer.")
