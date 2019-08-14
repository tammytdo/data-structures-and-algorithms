def merge_sort(lst):
    n = len(lst)

    if n > 1:
        mid = n/2
        left = [:mid]
        right = [mid:]

      // sort the left side
      merge_sort(left)
      
      // sort the right side
      merge_sort(right)
      
      // merge the sorted left and right sides together
      Merge(left, right, lst)

    return lst
    
def Merge(left, right, lst)
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[i]:
            lst[k] = left[i]
            i = i + 1

        else:
            lst[k] = right[j]
            j = j + 1

        k = k + 1

    while i < len(left): 
        lst[k] = left[i] 
        i += 1
        k += 1
        
    while j < len(right): 
        lst[k] = right[j] 
        j += 1
        k += 1