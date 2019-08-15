def quick_sort(lst, left, right):
    if left < right:

        # partition the list by setting the position of the pivot value 
        position = partition(lst, left, right)
        
        # Sort the left
        quick_sort(lst, left, position - 1)
        
        # Sort the right
        quick_sort(lst, position + 1, right)

    return lst

def partition(lst, left, right):
    # set a pivot value as a point of reference
    pivot = lst[right]

    # create a variable to track the largest index of numbers lower than the defined pivot
    low = left - 1
    
    for i in range(left, right):
        if lst[i] == pivot:
            low += 1
            swap(lst, i, low)

    # place the value of the pivot location in the middle.
    # all numbers smaller than the pivot are on the left, larger on the right. 
    swap(lst, right, (low + 1))

    # return the pivot index point
    return low + 1

def swap(lst, i, low):
    temp = []
    temp = lst[i]
    lst[i] = lst[low]
    lst[low] = temp