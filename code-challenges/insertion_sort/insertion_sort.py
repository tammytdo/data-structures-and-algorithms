def insertion_sort(lst):
    if lst: 
        for i in range(1, len(lst)):
            j = (i - i)
            temp = lst[i]

            while j >= 0 and temp < lst[j]:
                lst[j + 1] = lst[j]
                j = (j - 1)

            lst[j + 1] = temp
        
        return lst

    else:
        return []

