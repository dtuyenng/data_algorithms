import math

arr = [4, 1, 0, 9, 2, 7, 6]
arr1 = [0, 1, 3, 5]
arr2 = [2, 5, 8, 11]

def merge(a1, a2):
    combined = []
    j, i = 0, 0
    while i < len(a1) and j < len(a2):
        if a1[i] < a2[j]:
            combined.append(a1[i])
            i += 1
        else:
            combined.append(a2[j])
            j += 1

    if i >= len(a1):
        combined = combined + a2[j:]
    else:
        combined = combined + a1[i:]

    return combined

def mergesort(array):
    if len(array) == 1:
        return array
    mid_index = int(len(array) / 2)
    left = mergesort(array[0:mid_index])
    right = mergesort(array[mid_index:])
    return merge(left, right)

print(mergesort(arr))