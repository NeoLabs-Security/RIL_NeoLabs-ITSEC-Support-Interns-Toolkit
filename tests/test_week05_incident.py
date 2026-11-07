"""Support incident dashboard broker and release boundary regression tests."""
from datetime import datetime, timedelta, timezone
import unittest
from tools.neolabs import parser
from tools.week05_support import published_support_scope, request_json


def manifest():
    expiry=(datetime.now(timezone.utc)+timedelta(days=1)).isoformat().replace("+00:00","Z")
    return {
        "protocol_version":"2.0","deployment_id":"w05-demo",
        "deployment_channel":"ril-current","track":"SUPPORT",
        "scenario_id":"w05-poisoned-upload","scenario_release":"vulnerable",
        "student_ready":True,"lab_state":"STUDENT_READY","runtime_mode":"LIVE_REQUIRED",
        "release_generation":"w05-1","assignment_id":"assigned-01","pod_id":"pod-01",
        "resources":{
            "resource_type":"support_ticket_queue.v1","schema_version":1,
            "scope_status":"LIVE_TUNNEL",
            "endpoints":[{"url":"http://127.0.0.1:18080"}],
            "tunnel":{
                "transport":"ssh-local-forward","host":"192.0.2.20",
                "username":"nlw05sup_012345abcdef","port":22,"remote_host":"127.0.0.1",
                "local_port":18080,"remote_port":18600
            },
            "week05_support":{
                "contract_version":"1.0.0","scenario_id":"w05-poisoned-upload",
                "target_url":"http://127.0.0.1:18080",
                "expires_at":expiry,
                "operations":["list","review","quarantine"],
                "artifact_scope":"assigned_pod_only"
            }
        }
    }


class Week05SupportTests(unittest.TestCase):
    def test_published_support_scope(self):
        result=published_support_scope(manifest())
        self.assertEqual(result["pod_id"],"pod-01")
        self.assertEqual(result["target_url"],"http://127.0.0.1:18080")

    def test_broker_scope_fails_closed(self):
        for mutate in (
            lambda m:m.update(track="PENTEST"),
            lambda m:m.update(scenario_id="w04-broken-gate"),
            lambda m:m.update(student_ready=False),
            lambda m:m["resources"].update(scope_status="UNPUBLISHED"),
            lambda m:m["resources"]["tunnel"].update(remote_port=18601),
            lambda m:m["resources"]["tunnel"].update(username="nlw04_012345abcdef"),
            lambda m:m["resources"]["tunnel"].update(local_port=18600),
            lambda m:m["resources"]["week05_support"].update(operations=["list"]),
            lambda m:m["resources"]["week05_support"].update(artifact_scope="all_pods"),
            lambda m:m["resources"]["week05_support"].update(target_url="http://127.0.0.1:18600"),
            lambda m:m["resources"].pop("week05_support"),
            lambda m:m.update(pod_id="pod-77"),
            lambda m:m["resources"].update(resource_type="pentest_targets.v1"),
        ):
            x=manifest();mutate(x)
            with self.subTest(mutate=mutate):
                with self.assertRaises(ValueError):published_support_scope(x)

    def test_unsafe_transport_not_permitted(self):
        for url in ("http://192.0.2.4:18600","https://127.0.0.1:18080",
                    "http://localhost:18600","http://127.0.0.1:18601"):
            with self.subTest(url=url):
                with self.assertRaises(ValueError):request_json(url,"/health")

    def test_cli_parser_accepts_support_incident_dashboard(self):
        args=parser().parse_args(["incident","dashboard","--mentor-preview","--no-open"])
        self.assertTrue(args.mentor_preview)
        self.assertTrue(args.no_open)
        self.assertEqual(args.func.__name__,"dashboard")

    def test_support_keygen_command_is_separate_from_login(self):
        args=parser().parse_args(["incident","keygen"])
        self.assertEqual(args.func.__name__,"keygen")
        self.assertEqual(args.command,"incident")
        # Key creation never authorizes an arbitrary pod or establishes a broker session.
        self.assertFalse(hasattr(args,"pod"))

    def test_week04_ticket_surface_not_regressed(self):
        args=parser().parse_args(["tickets","--ticket","w04-demo"])
        self.assertEqual(args.ticket,"w04-demo")
        self.assertEqual(args.command,"tickets")


if __name__=="__main__":
    unittest.main()
