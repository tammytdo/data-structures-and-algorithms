import math

list1 = [1,2,3,4,5]
val1 = 16


def insert_shift_array(lst, value):
    length = len(lst)
    half = length / 2
    half = int(math.ceil(length / 2))
    return lst[:half] + [value] + lst[half:]

print(insert_shift_array(list1, val1))