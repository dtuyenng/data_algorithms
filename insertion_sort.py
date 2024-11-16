arr = [5, 2, 3, 1, 9, 1, 6]

def insertion_sort(array):
    for i in range(1, len(arr)):
        current_value = array[i]
        j = i - 1
        while j >= 0 and current_value < array[j]:
            array[j + 1] = array[j]
            j -= 1
        j += 1
        array[j] = current_value


insertion_sort(arr)
print(arr)