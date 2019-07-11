import pytest
from array_binary_search import binary_search

def test_even_list():
    lst = [1,2,3,4,5,6]
    val = 3
    assert return == 2

def test_odd_list():
    lst = [1,2,3,4,5,6,7]
    val = 5
    assert return == 4  

def test_not_in_list():
    lst = [1,2,3,4,5]
    val = 8
    assert return == -1

def test_empty_list():
    lst = []
    val = 3
    assert return == -1