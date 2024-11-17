
arr = [3, 5, 1, 7, 10, 6]

def partition(array, low, high):
    pivot_value = array[high]
    j = low - 1
    for i in range(low, high):
        if array[i] < pivot_value:
            j += 1
            array[i], array[j] = array[j], array[i]
    j += 1
    array[j], array[high] = array[high], array[j]
    return j

def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot -1)
        quicksort(array, pivot + 1, high)

# partition(arr, 0, len(arr) - 1)
quicksort(arr, 0, len(arr) - 1)
print(arr)




























#
#
# def partition(array, low, high):
#     j = low - 1
#     pivot_value = array[high]
#     for i in range(low, high):
#         if array[i] < pivot_value:
#             j += 1
#             array[i], array[j] = array[j], array[i]
#     j += 1
#     array[j], array[high] = array[high], array[j]
#     return j
#
# def quicksort(array, low, high):
#     if low < high:
#         pivot = partition(array, low, high)
#         quicksort(array, low, pivot - 1)
#         quicksort(array, pivot + 1, high)
#
# quicksort(arr, 0, len(arr) - 1)
# print(arr)
#























#
# def partition3(array, low, high):
#     i = low - 1
#     pivot_value = array[high]
#
#     for j in range(low, high):
#         if array[j] < pivot_value:
#             i += 1
#             array[i], array[j] = array[j], array[i]
#     i += 1
#     array[i], array[high] = array[high], array[i]
#     return i
#
# def quick_sort3(array, low, high):
#     if low < high:
#         pivot = partition3(array, low, high)
#         quick_sort3(array, low, pivot - 1)
#         quick_sort3(array, pivot + 1, high)
#
# partition3(arr, 0 , len(arr) -1)
# # quick_sort3(arr, 0, len(arr) -1)
# print(arr)
#
#
#















#
# def swap(array, index1, index2):
#     array[index1], array[index2] = array[index2], array[index1]
#
# def partition(array, low, high):
#     i = low - 1
#     pivot_value =  array[high]
#
#     for j in range(low, high):
#         if array[j] < pivot_value: # if element is less than pivot, swap with i
#             i += 1
#             swap(array, i, j)
#     i += 1
#     swap(array, i, high) #swap with pivot
#     return i
#
# def quicksort(array, low, high):
#     if low < high:
#         pivot = partition(array, low, high)
#         quicksort(array,0, pivot - 1)
#         quicksort(array, pivot + 1, high)
#
# # quicksort(arr, 0, len(arr) - 1)
# partition(arr, 0, len(arr) -1)
# print(arr)
#
#
#
#
