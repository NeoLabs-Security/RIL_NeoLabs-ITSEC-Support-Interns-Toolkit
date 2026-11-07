#!/usr/bin/env python3
"""Week 05 Support Incident Desk broker-session handoff (or mentor-only preview).

Official mode is deliberately gated on an authoritative STUDENT_READY W05
Support assignment, exact allowed SSH forwarding scope, and published support
operations. It NEVER asks for a second student access code or a server token.
"""
from __future__ import annotations
from datetime import datetime, timezone
import json
import re
import os
from pathlib import Path
import shutil
import subprocess
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener, ProxyHandler, HTTPRedirectHandler
from urllib.parse import urlsplit
import webbrowser

SCENARIO = "w05-poisoned-upload"
PREVIEW = "http://127.0.0.1:18600"
STUDENT = "http://127.0.0.1:18080"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, msg, headers, newurl):
        return None


def published_support_scope(manifest):
    if (not isinstance(manifest, dict)
            or manifest.get("protocol_version") != "2.0"
            or manifest.get("track") != "SUPPORT"
            or manifest.get("scenario_id") != SCENARIO
            or manifest.get("student_ready") is not True
            or manifest.get("lab_state") != "STUDENT_READY"
            or manifest.get("pod_id") not in {f"pod-{i:02d}" for i in range(1,6)}
            or not manifest.get("assignment_id")
            or not manifest.get("release_generation")):
        raise ValueError("Authoritative Week 05 Support assignment is not published")
    resources = manifest.get("resources")
    if not isinstance(resources,dict):
        raise ValueError("Support resources missing")
    tunnel=resources.get("tunnel")
    support=resources.get("week05_support")
    if (resources.get("resource_type") != "support_ticket_queue.v1"
            or resources.get("schema_version") != 1
            or resources.get("scope_status") != "LIVE_TUNNEL"
            or not isinstance(tunnel,dict)
            or tunnel.get("transport") != "ssh-local-forward"
            or tunnel.get("local_port") != 18080
            or tunnel.get("remote_host") != "127.0.0.1"
            or tunnel.get("remote_port") != 18600
            or not isinstance(tunnel.get("host"),str) or not tunnel.get("host")
            or not isinstance(tunnel.get("username"),str)
            or not re.fullmatch(r"nlw05sup_[0-9a-f]{12}",tunnel.get("username"))
            or not isinstance(support,dict)
            or support.get("contract_version") != "1.0.0"
            or support.get("scenario_id") != SCENARIO
            or support.get("target_url") != STUDENT
            or support.get("operations") != ["list","review","quarantine"]
            or support.get("artifact_scope") != "assigned_pod_only"
            or not any(isinstance(obj,dict) and obj.get("url") == STUDENT
                       for obj in resources.get("endpoints",[]))):
        raise ValueError("Current broker does not authorize the Week 05 Support incident endpoint")
    try:
        expiry=datetime.fromisoformat(support["expires_at"].replace("Z","+00:00"))
    except (ValueError, TypeError, KeyError, AttributeError) as error:
        raise ValueError("Published Support window invalid") from error
    if expiry.tzinfo is None or expiry <= datetime.now(timezone.utc):
        raise ValueError("Published Support window expired")
    return {"pod_id":manifest["pod_id"],"target_url":STUDENT}


def request_json(base,route,payload=None):
    parts=urlsplit(base)
    if parts.scheme!="http" or parts.hostname!="127.0.0.1" or parts.port not in (18080,18600):
        raise ValueError("Localhost-only Support gateway required")
    handler=build_opener(ProxyHandler({}),NoRedirect())
    data=json.dumps(payload).encode() if payload is not None else None
    headers={"Accept":"application/json"}
    if data is not None:
        headers["Content-Type"]="application/json"
    try:
        with handler.open(Request(base+route,data=data,method="POST" if data is not None else "GET",
                                  headers=headers),timeout=7) as response:
            if response.status != 200:
                raise ValueError("Week 05 local Support gateway not ready")
            body=response.read(65537)
    except (HTTPError,URLError,TimeoutError) as error:
        raise ValueError("No approved Support tunnel at localhost; establish it first") from error
    if len(body)>65536:
        raise ValueError("Oversized Support gateway response")
    try:
        result=json.loads(body)
    except (ValueError,UnicodeDecodeError) as error:
        raise ValueError("Invalid Support gateway response") from error
    if not isinstance(result,dict):
        raise ValueError("Invalid Support gateway response object")
    return result



def keygen(_args):
    """Create a distinct local W05 Support key; no credentials sent to the server."""
    from . import neolabs as cli
    folder = cli.HOME_STATE
    folder.mkdir(parents=True,exist_ok=True,mode=0o700)
    os.chmod(folder,0o700)
    secret=folder/"w05-tunnel-ed25519"
    public=Path(str(secret)+".pub")
    if secret.is_symlink() or public.is_symlink():
        cli.fail("Refusing symlinked SSH key files")
    if secret.exists() or public.exists():
        if not secret.is_file() or not public.is_file():
            cli.fail("W05 keypair incomplete: ask your mentor before modifying it")
        if secret.stat().st_mode & 0o077:
            cli.fail("W05 private key is accessible to others; change permissions to 0600")
        print("Existing W05 Support SSH public key:",public)
    else:
        sshgen=shutil.which("ssh-keygen")
        if not sshgen:
            cli.fail("Install OpenSSH (ssh-keygen) before generating the W05 identity")
        try:
            subprocess.run([sshgen,"-q","-t","ed25519","-N","","-f",str(secret),
                            "-C","neolabs-w05-support"],check=True)
        except subprocess.CalledProcessError as exc:
            cli.fail(f"Unable to generate W05 Support keypair: {exc.returncode}")
        os.chmod(secret,0o600)
        os.chmod(public,0o644)
        print("Generated dedicated Week 05 Support SSH keypair.")
    print("Give the following PUBLIC KEY ONLY privately to your mentor for approval:")
    print(public.read_text().strip())
    print("Never share the private key:",secret)
    print("This does NOT grant access until your broker assignment and SSH enrollment are approved.")
    return 0


def dashboard(args):
    from . import neolabs as cli
    if args.mentor_preview:
        base=PREVIEW
        info=request_json(base,"/health")
        if info.get("scenario_id")!=SCENARIO or info.get("service")!="w05-access-gateway":
            cli.fail("Incorrect mentor preview destination")
        uri=base+"/support"
        print("Mentor-only local preview. Use the mentor-issued Support preview code in the browser.")
    else:
        session=cli.read_session()
        manifest=cli.refresh(session)
        try:
            published=published_support_scope(manifest)
        except ValueError as error:
            cli.fail(str(error))
        base=published["target_url"]
        info=request_json(base,"/health")
        if info.get("scenario_id")!=SCENARIO:
            cli.fail("W05 SSH tunnel target is not the approved VCC gateway")
        reply=request_json(base,"/auth/broker-exchange",{"broker_session_token":session["session_token"]})
        ticket=reply.get("handoff")
        if not isinstance(ticket,str) or not re.fullmatch(r"[A-Za-z0-9_-]{43}",ticket):
            cli.fail("Current NeoLabs broker did not authorize the one-time Support handoff")
        uri=base+"/support#handoff="+ticket
        print(f"Broker authorized the {published['pod_id']} Support Incident Desk. One-time handoff expires in 45 seconds.")
    if args.no_open:
        print("Open this private localhost URL on the SAME machine that runs the SSH tunnel:")
        print(uri)
    else:
        if not webbrowser.open(uri):
            print("Browser unavailable; rerun with --no-open from the SSH-tunnel machine.")
    return 0
