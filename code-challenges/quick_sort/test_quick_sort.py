import pytest
from quick_sort import quick_sort, partition, swap

def test_function_exists():
    assert quick_sort

def test_empty_list():
    lst = []
    left = []
    right = []
    assert quick_sort(lst, left, right) == []

# @pytest.mark.skip()
def test_list_with_values_one():
    lst = [1]
    left = [1]
    right = []
    
    assert quick_sort(lst, left, right) == [1]

@pytest.mark.skip()
def test_list_sorted():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert quick_sort(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.mark.skip()
def test_list_unsorted():
    lst = [1, 3, 2, 4, 5, 7, 6, 8, 9, 10]
    assert quick_sort(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.mark.skip()
def test_list_sorted_dupes():
    lst = [1, 3, 3, 3, 2, 4, 5, 6, 7, 8, 9, 10]
    assert quick_sort(lst) == [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]

@pytest.mark.skip()
def test_list_unsorted_dupes():
    lst = [1, 3, 5, 3, 2, 3, 4, 6]
    assert quick_sort(lst) == [1, 2, 3, 3, 3, 4, 5, 6]