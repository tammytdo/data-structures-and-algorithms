from array_shift import insert_shift_array

def test_insert_shift_array_exists():
    assert insert_shift_array

def test_even_len_array():
    expected = [2,4,6,8], 5
    actual = [2,4,5,6,8]
    assert expected == actual

def test_odd_len_array():
    expected = [4,8,15,23,42], 16
    actual = [4,8,15,16,23,42]
    assert expected == actual

def test_empty_len_array():
    expected = []
    actual = []
    assert expected == actual