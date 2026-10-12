import unittest
from Pipeline.workflow import assign_ticket

class TestAssignment(unittest.TestCase):
    def setUp(self):
        self.tickets = [{
            "id": "T001",
            "status": "open",
            "assigned_to": None
        }]

    def test_assigns_staff_member(self):
        ticket = assign_ticket(
            self.tickets, "T001", "Ada"
        )
        self.assertEqual(ticket["assigned_to"], "Ada")

    def test_rejects_blank_staff_name(self):
        with self.assertRaises(ValueError):
            assign_ticket(self.tickets, "T001", " ")

        self.assertIsNone(self.tickets[0]["assigned_to"])

if __name__ == "__main__":
    unittest.main()