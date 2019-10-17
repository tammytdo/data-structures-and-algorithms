from quick_sort import quick_sort

def test_exists():
    assert quick_sort

def test_empty_list():
    assert quick_sort([]) == []

def test_one_pos_value():
    assert quick_sort([2]) == [2]

def test_two_pos_values():
    assert quick_sort([4,2]) == [2,4]

def test_six_pos_values():
    assert quick_sort([4,8,12,2,6,10]) == [2,4,6,8,10,12]

def test_one_neg_value():
    assert quick_sort([-2]) == [-2]

def test_two_neg_values():
    assert quick_sort([-2, -4]) == [-4, -2]

def test_six_neg_values():
    assert quick_sort([-4,-8,-12,-2,-6,-10]) == [-12,-10,-8,-6,-4,-2]

def test_one_value():
    assert quick_sort([2]) == [2]

def test_two_values():
    assert quick_sort([4,2]) == [2,4]

def test_six_values():
    assert quick_sort([4,8,-3,2,-1,6]) == [-3,-1,2,4,6,8]