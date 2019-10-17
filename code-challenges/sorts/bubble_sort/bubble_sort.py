def bubble_sort(lst):
    '''Implementation of a bubble sort'''

    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(len(lst)-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                sorted = False

    return lst