import unittest
import os
import json
from dataclasses import dataclass
from Test.things_to_test_hw import search_in_file
from Test.things_to_test_hw import add_from_json
from Test.things_to_test_hw import Storage


class TestSearch(unittest.TestCase):
    file_name = 'test.txt'
    @classmethod
    def setUp(self) -> None:
        lines = ['first_line\n', 'second_line\n', 'third_line\n']
        with open(TestSearch.file_name, 'w') as file:
            file.writelines(lines)

    @classmethod
    def tearDown(self) -> None:
        os.remove(TestSearch.file_name)

    def test_positive(self):
        self.assertTrue(search_in_file(TestSearch.file_name, 'first'))

    def test_positive_second(self):
        self.assertFalse(search_in_file(TestSearch.file_name, 'Hello'))

    def test_negative_first(self):
        with self.assertRaises(FileNotFoundError):
            search_in_file('testT.txt', 'first')

class TestJson(unittest.TestCase):
    file_name = 'test.json'
    @classmethod
    def setUp(self) -> None:
        data = {'a': 3, 'b': 4}
        with open(TestJson.file_name, 'w') as file:
            json.dump(data, file)

    @classmethod
    def tearDown(self) -> None:
        os.remove(TestJson.file_name)

    def test_positive(self):
        self.assertEqual(add_from_json(TestJson.file_name, ['a', 'b']), 7)

    def test_negative_first(self):
        self.assertNotEqual(add_from_json(TestJson.file_name, ['a', 'b']), 3)

    def test_negative_second(self):
        with self.assertRaises(FileNotFoundError):
            add_from_json('testJson.json', ['a', 'b'])


@dataclass
class Structure:
    field: str


class TestStorage(unittest.TestCase):
    first_storage = None

    @classmethod
    def setUp(self) -> None:
        self.first_storage = Storage()
        self.first_storage.add_table('first', Structure)


    def test_get_positive_first(self):
        result = self.first_storage.get_from_table('first')
        self.assertEqual(result, [])

    def test_get_positive_second(self):
        self.first_storage.add_to_table('first', Structure(field='one'))
        result = self.first_storage.get_from_table('first')
        self.assertTrue(result, ['one'])

    def test_add_to_negative(self):
        with self.assertRaises(ValueError):
            self.first_storage.add_to_table('second', 'two')

        with self.assertRaises(ValueError):
            self.first_storage.add_to_table('first', 2.5)

    def test_get_negative(self):
        with self.assertRaises(ValueError):
            self.first_storage.get_from_table('second')

    def test_add_negative(self):
        with self.assertRaises(ValueError):
            self.first_storage.add_table('first', int)
