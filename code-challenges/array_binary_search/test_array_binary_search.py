import pytest
from array_binary_search import binary_search

def test_exists():
    assert binary_search

def test_even_list():
    assert binary_search([1,2,3,4,5,6], 3)

def test_odd_list():
    assert binary_search([1,2,3,4,5,6,7], 5)

def test_not_in_list():
    assert binary_search([1,2,3,4,5], 8)