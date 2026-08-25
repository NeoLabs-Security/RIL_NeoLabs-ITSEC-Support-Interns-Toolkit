from __future__ import annotations

import argparse
import importlib.util
import types
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
        with mock.patch.object(MODULE, "_SYSTEM_GETPASS", return_value="NL-AbCdEf0123456789"):
            self.assertEqual(MODULE.prompt_access_code(), "NL-AbCdEf0123456789")

    def test_empty_first_attempt_reprompts(self) -> None:
        with mock.patch.object(MODULE, "_SYSTEM_GETPASS", side_effect=["", "NL-AbCdEf0123456789"]):
            self.assertEqual(MODULE.prompt_access_code(), "NL-AbCdEf0123456789")

    def test_whitespace_or_invalid_entry_is_not_accepted(self) -> None:
        with mock.patch.object(MODULE, "_SYSTEM_GETPASS", side_effect=["bad code", "still bad code", "also bad code"]):
            with self.assertRaises(SystemExit):
                MODULE.prompt_access_code()

    def test_main_prompt_does_not_recurse_and_restores_client_getpass(self) -> None:
        original_prompt = mock.Mock(return_value="unused")
        fake_getpass_module = types.SimpleNamespace(getpass=original_prompt)
        observed: list[str] = []

        def fake_login(_: argparse.Namespace) -> None:
            observed.append(fake_getpass_module.getpass("NeoLabs Access Code: "))

        fake_client = types.SimpleNamespace(getpass=fake_getpass_module, login=fake_login)
        fake_parser = mock.Mock()
        fake_parser.parse_args.return_value = argparse.Namespace(pod="2", base_url=None)

        with (
            mock.patch.object(MODULE, "load_client", return_value=fake_client),
            mock.patch.object(MODULE, "parser", return_value=fake_parser),
            mock.patch.object(MODULE, "_SYSTEM_GETPASS", return_value="NL-AbCdEf0123456789"),
        ):
            self.assertEqual(MODULE.main(), 0)

        self.assertEqual(observed, ["NL-AbCdEf0123456789"])
        self.assertIs(fake_getpass_module.getpass, original_prompt)
        original_prompt.assert_not_called()


if __name__ == "__main__":
    unittest.main()
