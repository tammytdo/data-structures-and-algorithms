# Feature Tasks:

array1 = [1, 2, 3, 4, 5, 6]
array2 = [89, 2354, 3546, 23, 10, -923, 823, -12]	
array3 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

def reverse_arr(array):
    print(array[::-1])

print("Feature Tasks")
reverse_arr(array1) 
reverse_arr(array2) 
reverse_arr(array3) 

print("")

# Stretch Goal:
def reverse_arr2(array):
    list = []
    index = len(array) - 1
    for i in array:
        list.append(array[index])
        index -= 1
    print(list)

print("Stretch Goal")
reverse_arr2(array1) 
reverse_arr2(array2) 
reverse_arr2(array3)