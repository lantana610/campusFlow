import unittest
from ticket_processor.ticket import calculate_priority


class Testpriority(unittest.TestCase):
    def test_high_urgency_many_user_is_critical(self):
        self.assertEqual(calculate_priority("high", 12), "critical") 
