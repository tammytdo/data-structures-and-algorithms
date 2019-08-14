import pytest

from merge_sort import merge_sort

def test_function_exists():
    assert merge_sort

def test_empty_list():
    lst = []
    assert merge_sort(lst) == []

@pytest.mark.skip()
def test_list_with_values_sorted():
    lst = [1, 2, 3, 4, 5, 6]
    assert merge_sort(lst) == [1, 2, 3, 4, 5, 6]

@pytest.mark.skip()
def test_list_with_values_unsorted():
    lst = [1, 3, 5, 2, 4, 6]
    assert merge_sort(lst) == [1, 2, 3, 4, 5, 6]

@pytest.mark.skip()
def test_list_with_values_sorted_dupes():
    lst = [1, 3, 3, 3, 5, 2, 4, 6]
    assert merge_sort(lst) == [1, 2, 3, 3, 3, 4, 5, 6]

@pytest.mark.skip()
def test_list_with_values_unsorted_dupes():
    lst = [1, 3, 5, 3, 2, 3, 4, 6]
    assert merge_sort(lst) == [1, 2, 3, 3, 3, 4, 5, 6]