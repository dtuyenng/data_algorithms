arr = [4, 1, 0, 9, 2, 7, 6, 5]


arr1 = [1, 3, 5]
arr2 = [2, 5, 8]

def merge(array1, array2):
    return_array = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            return_array.append(array1[i])
            i += 1
        else:
            return_array.append(array2[j])
            j += 1

    if i < len(array1):
        return_array = return_array + array1[i:len(array1)]
    else:
        return_array = return_array + array2[j:len(array2)]

    return return_array

# def merge(array1, array2):
#     return_array = []
#
#     value1 = array1.pop(0)
#     value2 = array2.pop(0)
#     while len(array1) > 0 or len(array2) > 0:
#         if value1 < value2:
#             return_array.append(value1)
#             value1 = array1.pop(0)
#         else:
#             return_array.append(value2)
#             value2 = array2.pop(0)
#     print(array1, array2)
#     print(return_array)


print(merge(arr1, arr2))
