#!/usr/bin/env python3
from pathlib import Path

path = Path('tools/neolabs.py')
text = path.read_text(encoding='utf-8')
if 'import shutil\n' not in text:
    text = text.replace('import re\n', 'import re\nimport shutil\nimport subprocess\n')
old = '''def connect(_: argparse.Namespace) -> None:
    manifest = refresh(read_session())
    state = str(manifest.get("lab_state") or "LIVE")
    if state not in INTERACTIVE_STATES:
        print(f"NeoLabs state: {state}. No interactive Support endpoint is required/available in this window.")
        print("Use `neolabs replay` for archived telemetry and `neolabs evidence` for approved ticket/cloud/endpoint evidence.")
        return
    resources = manifest["resources"]
    endpoints = resources.get("endpoints", [])
    print(f"✓ {state} context refreshed for {manifest['pod_id']}.")
    print(f"✓ {len(endpoints) if isinstance(endpoints, list) else 0} authorised support endpoint(s) available.")
    print("Use only the resources displayed by `neolabs targets`.")
'''
new = '''def connect(_: argparse.Namespace) -> None:
    manifest = refresh(read_session())
    state = str(manifest.get("lab_state") or "LIVE")
    if state not in INTERACTIVE_STATES:
        print(f"NeoLabs state: {state}. No interactive Support endpoint is required/available in this window.")
        print("Use `neolabs replay` for archived telemetry and `neolabs evidence` for approved ticket/cloud/endpoint evidence.")
        return
    resources = manifest["resources"]
    tunnel = resources.get("tunnel")
    if isinstance(tunnel, dict) and tunnel.get("transport") == "ssh-local-forward":
        ssh = shutil.which("ssh")
        if not ssh:
            fail("OpenSSH client is required for the NeoLabs isolated tunnel. Install OpenSSH and run `neolabs connect` again.")
        host = str(tunnel.get("host") or "")
        username = str(tunnel.get("username") or "")
        remote_host = str(tunnel.get("remote_host") or "127.0.0.1")
        try:
            port = int(tunnel.get("port") or 22)
            local_port = int(tunnel.get("local_port") or 18080)
            remote_port = int(tunnel.get("remote_port"))
        except (TypeError, ValueError):
            fail("server returned an invalid tunnel manifest")
        if not host or not username or not (1 <= port <= 65535 and 1024 <= local_port <= 65535 and 1 <= remote_port <= 65535):
            fail("server returned an incomplete tunnel manifest")
        print(f"✓ Assigned pod: {manifest['pod_id']}")
        print(f"✓ Opening isolated NeoLabs support endpoint at http://127.0.0.1:{local_port}")
        print("When SSH asks for a password, enter the SAME private NeoLabs Access Code used for `neolabs login`.")
        print("Keep this terminal open while validating the learner service. Press Ctrl+C when finished.")
        command = [
            ssh, '-o', 'ExitOnForwardFailure=yes', '-o', 'ServerAliveInterval=30', '-o', 'ServerAliveCountMax=3',
            '-o', 'StrictHostKeyChecking=accept-new', '-o', 'PreferredAuthentications=password', '-o', 'PubkeyAuthentication=no',
            '-N', '-L', f'127.0.0.1:{local_port}:{remote_host}:{remote_port}', '-p', str(port), f'{username}@{host}'
        ]
        try:
            subprocess.run(command, check=True)
        except KeyboardInterrupt:
            print("\\n✓ NeoLabs live tunnel closed.")
        except subprocess.CalledProcessError as exc:
            fail(f"NeoLabs SSH tunnel exited with status {exc.returncode}; verify your Access Code and retry")
        return
    endpoints = resources.get("endpoints", [])
    print(f"✓ {state} context refreshed for {manifest['pod_id']}.")
    print(f"✓ {len(endpoints) if isinstance(endpoints, list) else 0} authorised support endpoint(s) available.")
    print("Use only the resources displayed by `neolabs targets`.")
'''
if new in text:
    print('Support tunnel client already enabled')
elif old not in text:
    raise SystemExit('expected Support connect function not found')
else:
    text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')
    print('Support tunnel client enabled')
