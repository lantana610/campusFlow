import unittest
from ticket_processor.ticket import calculate_priority, validate_category
from ticket_processor.ticket import validate_title
from ticket_processor.ticket import calculate_priority, validate_title, validate_urgency
from ticket_processor.ticket import calculate_priority, validate_title, validate_urgency
from ticket_processor.ticket import validate_category, validate_affected_users
from ticket_processor.ticket import generate_ticket_id, create_ticket

class Testpriority(unittest.TestCase):
    def test_high_urgency_many_user_is_critical(self):
        self.assertEqual(calculate_priority("high", 12), "critical") 
        
    def test_high_urgency_with_2_user_is_high(self):
        self.assertEqual(calculate_priority("high", 2), "high")

    def test_medium_urgency_with_4_user_is_medium(self):
        self.assertEqual(calculate_priority("medium", 4), "medium")

    def test_low_urgency_with_1_user_is_low(self):
        self.assertEqual(calculate_priority("low", 1), "low")

    def test_low_urgency_with_4_user_is_medium(self):
        self.assertEqual(calculate_priority("low", 4), "medium")

    def test_high_urgency_with_9_users_is_high(self):
        self.assertEqual(calculate_priority("high", 9), "high")

    def test_high_urgency_with_10_users_is_critical(self):
        self.assertEqual(calculate_priority("high", 10), "critical")
    
    def test_low_urgency_with_2_users_is_low(self):
        self.assertEqual(calculate_priority("low", 2), "low") 

    def test_low_urgency_with_3_users_is_medium(self):
        self.assertEqual(calculate_priority("low", 3), "medium") 

class TestValidate(unittest.TestCase):
    def test_empty_title(self):
        with self.assertRaises(ValueError):
            validate_title(" ")
    def test_valid_title_is_returned(self):
        self.assertEqual(validate_title(" wi-fi down "), "wi-fi down")


    def test_urgency_is_normalized(self):
        self.assertEqual(validate_urgency("  HIGH "), "high")

    def test_invalid_urgency_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_urgency("urgent")

    def test_category_is_normalized(self):
        self.assertEqual(validate_category("  hardware "), "Hardware")

    def test_invalid_category_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_category("invalid")

    def test_zero_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_affected_users(0)

    def test_decimal_users_is_rejected(self):
        with self.assertRaises(TypeError):
            validate_affected_users(2.5)

    def test_boolean_users_is_rejected(self):
        with self.assertRaises(TypeError):
            validate_affected_users(True)

    def test_valid_users_is_returned(self):
        self.assertEqual(validate_affected_users(5), 5)

class TestCreate(unittest.TestCase):
    def test_create_ticket_calculates_priority(self):
        tickets = []
        ticket = create_ticket("Wi-Fi down", "network", "HIGH", 12, tickets)
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertEqual(len(tickets), 1)

    def test_next_id_follows_highest(self):
        tickets = [{"id": "T001"}, {"id": "T005"}]
        self.assertEqual(generate_ticket_id(tickets), "T006")

    def test_invalid_ticket_is_not_stored(self):
        tickets = []
        with self.assertRaises(ValueError):
            create_ticket("Wi-Fi down", "network", "high", 0, tickets)
        self.assertEqual(len(tickets), 0)