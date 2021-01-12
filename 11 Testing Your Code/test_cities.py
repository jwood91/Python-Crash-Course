import unittest
from city_functions import city_country


class TestCityFunction(unittest.TestCase):
    """Tests for city country name function"""

    def test_city_country(self):
        """Tests city, country name outputs"""
        formatted_city_country = city_country('santiago', 'chile')
        self.assertEqual(formatted_city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Tests city, country and population"""
        formatted_city_country_population = city_country(
            'santiago', 'chile', 500000)
        self.assertEqual(formatted_city_country_population,
                         'Santiago, Chile, Population = 500000')


unittest.main()
