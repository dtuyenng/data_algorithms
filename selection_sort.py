arr = [5, 2, 3, 1, 9, 1, 6]

def selection_sort(array):
    for i in range(len(array)):
        for j in range(i, len(array)):
            min_index = i
            if array[j] < array[i]:
                min_index = j
            array[i], array[min_index] = array[min_index], array[i]
            
selection_sort(arr)
print(arr)