def merge_sort(lst):
    n = len(lst)

    if n > 1:
        mid = n // 2
        left = lst[:mid]
        right = lst[mid:]

        # sort the left side
        merge_sort(left)
        
        # sort the right side
        merge_sort(right)
        
        # merge the sorted left and right sides together
        merge(left, right, lst)

    return lst

    
def merge(left, right, lst):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            lst[k] = left[i]
            i += 1

        else:
            lst[k] = right[j]
            j += 1

        k += 1

    #    set remaining entries in arr to remaining values in right
    if i == len(left):
        for _ in right[j:]:
            lst[k] = right[j] 
            j += 1
            k += 1

    #    set remaining entries in arr to remaining values in left
    else: 
        for _ in left[i:]:        
            lst[k] = left[i] 
            i += 1
            k += 1