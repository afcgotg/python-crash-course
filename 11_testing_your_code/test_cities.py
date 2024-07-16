import unittest
from city_functions import get_formatted_city

# 10-11 City, Country
# 10-12 Population

class CitiesTestCase(unittest.TestCase):

	def test_city_country(self):
		formatted_city = get_formatted_city("Barcelona", "Spain")
		self.assertEqual(formatted_city, "Barcelona, Spain")

	def test_city_country_population(self):
		formatted_city = get_formatted_city("Barcelona", "Spain", 1_500_000)
		self.assertEqual(formatted_city, "Barcelona, Spain - population 1500000")

if __name__ == '__main__':
	unittest.main()
