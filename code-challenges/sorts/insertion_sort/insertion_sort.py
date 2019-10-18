def insertion_sort(lst):
    ''' Implementation of an insertion sort '''
    for i in range(len(lst)):
        temp = lst[i]

        j = i - 1
        while j >= 0 and temp < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp

    return lst