import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):

	def setUp(self):
		self.employee = Employee("Alex", "Fernandez", 27_000)

	def test_give_default_raise(self):
		self.employee.give_raise()
		self.assertEqual(self.employee.salary, 32_000)

	def test_give_custom_raise(self):
		self.employee.give_raise(3_000)
		self.assertEqual(self.employee.salary, 30_000)

if __name__ == '__main__':
	unittest.main()
		
