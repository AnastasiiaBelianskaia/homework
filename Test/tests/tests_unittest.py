import unittest
import os
import json
from Test.things_to_test_hw import search_in_file
from Test.things_to_test_hw import add_from_json


class TestSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        lines = ['first_line\n', 'second_line\n', 'third_line\n']
        with open('test.txt', 'w') as file:
            file.writelines(lines)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove('test.txt')

    def test_positive(self):
        self.assertTrue(search_in_file('test.txt', 'first'))

    def test_negative(self):
        self.assertFalse(search_in_file('test.txt', 'Hello'))

class TestJson(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        data = {'a': 3, 'b': 4}
        with open('test.json', 'w') as file:
            json.dump(data, file)

    @classmethod
    def tearDownClass(cls) -> None:
        os.remove('test.json')

    def test_positive(self):
        self.assertTrue(add_from_json('test.json', ['a', 'b']), 7)

    def test_negative(self):
        self.assertIsNot(add_from_json('test.json', ['a', 'b']), 3)
        with self.assertRaises(FileNotFoundError):
            add_from_json('testJson.json', ['a', 'b'])
