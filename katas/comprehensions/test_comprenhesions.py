from unittest import TestCase

from katas.comprehensions.comprehensions import list_comprehension, dict_comprehension


class TestComprehensions(TestCase):



    def test_list_comps(self):
        COUNTRY_DIAL_CODES = [
            (14, 'China'),
            (13, 'India'),
            (11, 'Brazil'),
        ]
        expected = ['14 - CHINA', '13 - INDIA', '11 - BRAZIL']
        self.assertSequenceEqual(expected, list_comprehension(COUNTRY_DIAL_CODES))

    def test_dict_comprehension(self):
        COUNTRY_DIAL_CODES = [
            (14, 'China'),
            (13, 'India'),
            (11, 'Brazil'),
        ]
        expected = {14: 'CHINA', 13: 'INDIA', 11: 'BRAZIL' }

        self.assertDictEqual(expected, dict_comprehension(COUNTRY_DIAL_CODES))

    def test_list_comprehension_with_no_parameters(self):
        expected = ['86 - CHINA', '91 - INDIA', '55 - BRAZIL']
        self.assertSequenceEqual(expected, list_comprehension())

    def test_dict_comprehension_with_no_parameters(self):
        expected = {86: 'CHINA', 91: 'INDIA', 55: 'BRAZIL'}
        self.assertSequenceEqual(expected, dict_comprehension())

