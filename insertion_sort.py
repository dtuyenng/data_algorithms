arr = [ 5, 2, 3, 9, 1, 6]


def insertion_sort(array):
    for i in range(1, len(array)):
        curr = array[i]
        j = i - 1
        while j > -1 and curr < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j+1] = curr

insertion_sort(arr)
print(arr)