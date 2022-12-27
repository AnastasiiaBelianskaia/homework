import json
import os
from dataclasses import dataclass
import pytest
from Test.things_to_test_hw import search_in_file
from Test.things_to_test_hw import add_from_json
from Test.things_to_test_hw import Storage

@pytest.fixture(name='_for_search_in_file')
def fixture_for_search_in_file():
    lines = ['first_line\n', 'second_line\n', 'third_line\n']
    with open('test.txt', 'w') as file:
        file.writelines(lines)
    yield 'test.txt'
    os.remove('test.txt')

@pytest.fixture(name='_for_add_from_json')
def fixture_for_add_from_json():
    data = {'a': 3, 'b': 4}
    with open('test.json', 'w') as file:
        json.dump(data, file)
    yield 'test.json'
    os.remove('test.json')


@pytest.mark.parametrize('search, result', [('first', ['first_line\n']),
                                            ('Hello', []),
                                            ('se', ['second_line\n'])])
def test_search_in_file_correct(search, result, _for_search_in_file):
    assert search_in_file('test.txt', search) == result


def test_search_in_file_not_correct(_for_search_in_file):
    with pytest.raises(FileNotFoundError):
        search_in_file('testT.txt', 'first')


def test_add_from_json_correct(_for_add_from_json):
    result = add_from_json('test.json', ['a', 'b'])
    assert result == 7


def test_add_from_json_not_correct_result(_for_add_from_json):
    result = add_from_json('test.json', ['a', 'b'])
    assert result != 3

def test_add_from_json_not_correct_error(_for_add_from_json):
    with pytest.raises(FileNotFoundError):
        add_from_json('testJson.json', ['a', 'b'])
    with pytest.raises(KeyError):
        add_from_json('test.json', ['c', 'd'])

@dataclass
class Structure:
    field: str


class TestStorage:
    first_storage = Storage()
    first_storage.add_table('first', Structure)

    def test_get_positive_first(self):
        result = self.first_storage.get_from_table('first')
        assert result == []

    def test_get_positive_second(self):
        self.first_storage.add_to_table('first', Structure(field='one'))
        result = self.first_storage.get_from_table('first')
        assert result == [Structure(field='one')]

    def test_add_to_negative(self):
        with pytest.raises(ValueError):
            self.first_storage.add_to_table('second', 'two')

        with pytest.raises(ValueError):
            self.first_storage.add_to_table('first', 2.5)

    def test_get_negative(self):
        with pytest.raises(ValueError):
            self.first_storage.get_from_table('second')

    def test_add_negative(self):
        with pytest.raises(ValueError):
            self.first_storage.add_table('first', int)
