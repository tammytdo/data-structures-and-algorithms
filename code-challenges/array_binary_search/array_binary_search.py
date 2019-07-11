def binary_search(lst, val):
    length = len(lst)
    left_index = 0
    right_index = length -1

    for item in lst:
        if left_index <= right_index:
            mid_index = (left_index + right_index) // 2

            if lst[mid_index] < val:
                left_index = mid_index + 1

            elif lst[mid_index] > val:
                right_index = mid_index -1
            
            elif lst[mid_index] == val:
                return mid_index
        else:
            return -1


print(binary_search([1,2,3,4,5,6], 3))