from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


class Week03ArenaPackTests(unittest.TestCase):
    def test_validator_requires_approval_and_in_scope_account(self):
        script = Path(__file__).parents[1] / "scripts" / "validate-week03-response-ledger.py"
        header = "change_id,account_id,soc_alert_or_event_id,requested_time_utc,approved_by,action,original_state,completed_time_utc,response_event_or_rule_id,validation_result,rollback_owner,responder,notes\n"
        valid = "CH-1,syn-credential-storm-pod-01-01,E-1,2026-09-28T09:30:00Z,mentor,contain-account,active,2026-09-28T09:31:00Z,R-1,contained,mentor,responder,\n"
        with tempfile.TemporaryDirectory() as directory:
            ledger = Path(directory) / "response.csv"
            ledger.write_text(header + valid, encoding="utf-8")
            self.assertEqual(subprocess.run(["python3", str(script), str(ledger)], check=False).returncode, 0)
            ledger.write_text(header + valid.replace(",mentor,contain-account", ",,contain-account"), encoding="utf-8")
            self.assertEqual(subprocess.run(["python3", str(script), str(ledger)], check=False).returncode, 1)


if __name__ == "__main__":
    unittest.main()
