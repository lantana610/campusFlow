import unittest
from ticket_processor.ticket import calculate_priority
from ticket_processor.ticket import validate_title
from ticket_processor.ticket import calculate_priority, validate_title, validate_urgency
from ticket_processor.ticket import calculate_priority, validate_title, validate_urgency

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