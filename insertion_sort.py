arr = [5, 2, 3, 1, 9, 1, 6]

def insertion_sort(array):
    for i in range(1, len(array)):
        j = i - 1
        curr = array[i]
        while j >= 0 and array[j] > curr:
            array[j+1] = array[j]
            j -= 1
        j += 1
        array[j] = curr

insertion_sort(arr)
print(arr)