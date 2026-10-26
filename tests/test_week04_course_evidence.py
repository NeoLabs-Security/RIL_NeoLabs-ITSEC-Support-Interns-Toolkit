import copy
import unittest
from tools.support_tickets import validate_course_evidence


class Week04CourseEvidenceTests(unittest.TestCase):
    def setUp(self):
        self.manifest = {'pod_id': 'pod-01', 'scenario_id': 'w04-broken-gate'}
        self.ticket = {'ticket_id': 'SYN-W04-POD-01-A', 'account_reference': 'syn-user-p01-a',
                       'course_access': {'contract_version': '1.0.0', 'pod_id': 'pod-01',
                                         'scenario_id': 'w04-broken-gate', 'account_reference': 'syn-user-p01-a',
                                         'course_id': 'synthetic-course', 'enrolment_status': 'ACTIVE',
                                         'course_role': 'LEARNER', 'read_only': True,
                                         'observed_at': '2026-10-23T12:00:00Z'}}

    def test_evidence_projection_excludes_privileged_annotations(self):
        self.ticket['course_access'].update({'policy_expected_decision': 'deny', 'token': 'synthetic-secret'})
        result = validate_course_evidence(self.manifest, self.ticket)
        self.assertEqual(result['course_id'], 'synthetic-course')
        self.assertNotIn('policy_expected_decision', result)
        self.assertNotIn('token', result)

    def test_other_pod_account_or_scenario_is_refused(self):
        for field, value in [('pod_id', 'pod-02'), ('account_reference', 'syn-user-p02-b'),
                             ('scenario_id', 'w03-credential-storm'), ('read_only', False),
                             ('contract_version', 'unknown'), ('observed_at', 'not-a-date')]:
            ticket = copy.deepcopy(self.ticket); ticket['course_access'][field] = value
            with self.subTest(field=field), self.assertRaises(SystemExit):
                validate_course_evidence(self.manifest, ticket)

    def test_missing_evidence_is_not_interpreted_as_permission(self):
        with self.assertRaises(SystemExit): validate_course_evidence(self.manifest, {'ticket_id': 'missing'})


if __name__ == '__main__':
    unittest.main()
