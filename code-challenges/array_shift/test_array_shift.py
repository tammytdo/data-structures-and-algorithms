from array_shift import insert_shift_array

def test_insert_shift_array_exists():
    assert insert_shift_array

def test_even_len_array():
    assert insert_shift_array([2,4,6,8], 5)

def test_odd_len_array():
    assert insert_shift_array([4,8,15,23,42], 16)

def test_expected_failure():
    assert insert_shift_array([2,4,6,8], 5)

def test_empty_len_array():
    assert insert_shift_array([],0)
