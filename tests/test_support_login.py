from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from unittest import mock

MODULE_PATH = Path(__file__).resolve().parents[1] / "tools" / "support_login.py"
SPEC = importlib.util.spec_from_file_location("support_login", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class SupportLoginPromptTests(unittest.TestCase):
    def test_valid_code_is_returned_without_echo_logic(self) -> None:
        with mock.patch.object(MODULE.getpass, "getpass", return_value="NL-AbCdEf0123456789"):
            self.assertEqual(MODULE.prompt_access_code(), "NL-AbCdEf0123456789")

    def test_empty_first_attempt_reprompts(self) -> None:
        with mock.patch.object(MODULE.getpass, "getpass", side_effect=["", "NL-AbCdEf0123456789"]):
            self.assertEqual(MODULE.prompt_access_code(), "NL-AbCdEf0123456789")

    def test_whitespace_or_invalid_entry_is_not_accepted(self) -> None:
        with mock.patch.object(MODULE.getpass, "getpass", side_effect=["bad code", "still bad code", "also bad code"]):
            with self.assertRaises(SystemExit):
                MODULE.prompt_access_code()


if __name__ == "__main__":
    unittest.main()
