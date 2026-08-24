from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "support_tickets.py"
SPEC = importlib.util.spec_from_file_location("support_tickets", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def manifest_for(account: str = "learner.pod-01.01@synthetic.neolabs.invalid") -> dict:
    return {
        "track": "SUPPORT",
        "pod_id": "pod-01",
        "scenario_id": "w02-ghost-login",
        "resources": {
            "queue_run_id": "abc123def456",
            "student_notice": "Synthetic ticket queue",
            "support_ticket_queue": [
                {
                    "ticket_id": "W02-POD-01-A",
                    "queue_position": 1,
                    "severity": "needs-triage",
                    "account_reference": account,
                    "user_statement": "Synthetic report",
                    "support_action_authority": ["preserve evidence"],
                }
            ],
        },
    }


class SupportTicketClientTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.original_manifest = MODULE.RUNTIME_MANIFEST
        MODULE.RUNTIME_MANIFEST = Path(self.temp.name) / "access-manifest.json"

    def tearDown(self) -> None:
        MODULE.RUNTIME_MANIFEST = self.original_manifest
        self.temp.cleanup()

    def write_manifest(self, value: dict) -> None:
        MODULE.RUNTIME_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        MODULE.RUNTIME_MANIFEST.write_text(json.dumps(value), encoding="utf-8")

    def test_reads_only_current_support_queue(self) -> None:
        self.write_manifest(manifest_for())
        manifest, tickets = MODULE.read_ticket_resource(refresh=False)
        self.assertEqual(manifest["pod_id"], "pod-01")
        self.assertEqual(len(tickets), 1)
        self.assertEqual(tickets[0]["ticket_id"], "W02-POD-01-A")

    def test_accepts_current_pod_synthetic_fixture_reference(self) -> None:
        self.write_manifest(manifest_for("syn-user-p01-03"))
        _, tickets = MODULE.read_ticket_resource(refresh=False)
        self.assertEqual(tickets[0]["account_reference"], "syn-user-p01-03")

    def test_rejects_cross_pod_ticket_account_reference(self) -> None:
        self.write_manifest(manifest_for("learner.pod-02.01@synthetic.neolabs.invalid"))
        with self.assertRaises(SystemExit) as context:
            MODULE.read_ticket_resource(refresh=False)
        self.assertIn("assigned-pod isolation check", str(context.exception))

    def test_rejects_cross_pod_synthetic_fixture_reference(self) -> None:
        self.write_manifest(manifest_for("syn-user-p02-04"))
        with self.assertRaises(SystemExit) as context:
            MODULE.read_ticket_resource(refresh=False)
        self.assertIn("assigned-pod isolation check", str(context.exception))

    def test_rejects_wrong_track_manifest(self) -> None:
        value = manifest_for()
        value["track"] = "SOC"
        self.write_manifest(value)
        with self.assertRaises(SystemExit):
            MODULE.read_ticket_resource(refresh=False)

    def test_missing_queue_has_clear_message(self) -> None:
        value = manifest_for()
        value["resources"].pop("support_ticket_queue")
        self.write_manifest(value)
        with self.assertRaises(SystemExit) as context:
            MODULE.read_ticket_resource(refresh=False)
        self.assertIn("missing the current Week 2 Support queue", str(context.exception))


if __name__ == "__main__":
    unittest.main()
