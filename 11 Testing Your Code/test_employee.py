import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    """Tests the 'Employee.py' Class"""

    def setUp(self):
        """Set up an employee to work in the tests."""
        self.eric = Employee('eric', 'matthews', 60000)

    def test_default_raise(self):
        self.eric.give_raise()
        self.assertEqual(self.eric.salary, 65000)

    def test_custom_raise(self):
        self.eric.give_raise(15000)
        self.assertEqual(self.eric.salary, 75000)


unittest.main()
