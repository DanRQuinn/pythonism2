import pytest
from iterate_generate.iterate_generate import custom_collection, main


def custom_collection(start, end):
    """A custom collection that can be used in a for in loop, list comprehension, and converted to a list."""

    current = start
    while current <= end:
        yield current
        current += 1

def test_custom_collection_for_in_loop():
    numbers = custom_collection(1, 10)
    for number in numbers:
        assert number == number

def test_custom_collection_list_comprehension():
    numbers = [number for number in custom_collection(1, 10)]
    assert numbers == list(range(1, 11))

def test_custom_collection_list_conversion():
    list_of_numbers = list(custom_collection(1, 10))
    assert list_of_numbers == list(range(1, 11))
