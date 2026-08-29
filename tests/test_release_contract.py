import unittest
from tools.release_contract import generation_changed, validate_manifest
from tools.discovery import resolve_gateway
from pathlib import Path
def manifest(**changes):
    value={"protocol_version":"2.0","deployment_id":"deployment-a","deployment_channel":"ril-current","scenario_id":"w02-ghost-login","scenario_release":"vulnerable","release_generation":"generation-a","student_ready":True,"lab_state":"STUDENT_READY","runtime_mode":"LIVE_REQUIRED","pod_id":"pod-01","track":"SUPPORT","assignment_id":"assignment-1","resources":{"resource_type":"support_ticket_queue.v1","schema_version":1}}
    value.update(changes); return value
class SupportContractTests(unittest.TestCase):
    def test_missing_readiness_fails_closed(self):
        value=manifest(); value.pop("student_ready")
        with self.assertRaises(ValueError): validate_manifest(value,"SUPPORT")
    def test_deployment_change_detected(self):
        self.assertTrue(generation_changed(manifest(),manifest(deployment_id="deployment-b")))
    def test_discovery_requires_tls(self):
        with self.assertRaises(ValueError):resolve_gateway("https://old.example",Path("."),discovery_url="http://unsafe.example")
