from typing import List

arr = [4, 1, 0, 9, 2, 7, 6, 5]

def swap(array, index1, index2):
    array[index1], array[index2] = array[index2], array[index1]

def partition(array, low, high):
    i = low - 1
    pivot_value =  array[high]

    for j in range(low, high):
        if array[j] < pivot_value: # if element is less than pivot, it's moved to the left
            i += 1
            swap(array, i, j)
    i += 1
    swap(array, i, high) #swap with pivot
    return i

def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array,0, pivot - 1)
        quicksort(array, pivot + 1, high)

quicksort(arr, 0, len(arr) - 1)
print(arr)




