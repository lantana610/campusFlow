import unittest

from Pipeline.reports import generate_report


class TestReports(unittest.TestCase):

    def test_empty_report(self):
        report = generate_report([])

        self.assertEqual(report["total"], 0)

        for count in report["by_status"].values():
            self.assertEqual(count, 0)

        for count in report["by_priority"].values():
            self.assertEqual(count, 0)

    def test_report_counts_tickets_correctly(self):
        tickets = [
            {
                "id": "T001",
                "status": "open",
                "priority": "critical"
            },
            {
                "id": "T002",
                "status": "in_progress",
                "priority": "high"
            },
            {
                "id": "T003",
                "status": "resolved",
                "priority": "low"
            },
            {
                "id": "T004",
                "status": "open",
                "priority": "medium"
            }
        ]

        report = generate_report(tickets)

        self.assertEqual(report["total"], 4)

        self.assertEqual(
            report["by_status"],
            {
                "open": 2,
                "in_progress": 1,
                "resolved": 1
            }
        )

        self.assertEqual(
            report["by_priority"],
            {
                "critical": 1,
                "high": 1,
                "medium": 1,
                "low": 1
            }
        )


if __name__ == "__main__":
    unittest.main()