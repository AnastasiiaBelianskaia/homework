import json
import os
import pytest
from Test.things_to_test_hw import search_in_file
from Test.things_to_test_hw import add_from_json

@pytest.fixture(name='_for_search_in_file')
def fixture_for_search_in_file():
    lines = ['first_line\n', 'second_line\n', 'third_line\n']
    with open('test.txt', 'w') as file:
        file.writelines(lines)
    yield
    os.remove('test.txt')

@pytest.fixture(name='_for_add_from_json')
def fixture_for_add_from_json():
    data = {'a': 3, 'b': 4}
    with open('test.json', 'w') as file:
        json.dump(data, file)
    yield
    os.remove('test.json')


def test_search_in_file_correct(_for_search_in_file):
    result = search_in_file('test.txt', 'first')
    assert result == ['first_line\n']

def test_search_in_file_not_correct(_for_search_in_file):
    result = search_in_file('test.txt', 'Hello')
    assert result == []


def test_add_from_json_correct(_for_add_from_json):
    result = add_from_json('test.json', ['a', 'b'])
    assert result == 7


def test_add_from_json_not_correct(_for_add_from_json):
    result = add_from_json('test.json', ['a', 'b'])
    assert result != 3
    with pytest.raises(FileNotFoundError):
        add_from_json('testJson.json', ['a', 'b'])
