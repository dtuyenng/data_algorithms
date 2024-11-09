arr = [5, 2, 3, 1, 9, 1, 6]

def selection_sort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


selection_sort(arr)
print(arr)