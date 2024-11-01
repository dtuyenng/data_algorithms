

arr = [4, 2, 6, 5, 1, 3]

def bubble_sort2(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp


def insert_sort(array):
    for i in range(1, len(array)):
        curr = array[i]
        j = i - 1
        while j >= 0 and array[j] > curr:
            array[j+1] = array[j]
            j -= 1
        array[j + 1] = curr

def bubble_sort(array):
    for i in range(len(array)):
        for index in range(len(array) - 1 - i):
            curr  = array [index]
            after = array[index + 1]
            if curr > after:
                array[index], array[index+1] = array[index+1], array[index]

def selection_sort(array):
    for i in range(len(array)):
        min_index = i  # Start by assuming the minimum is the current position
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j  # Update min_index if a smaller element is found
        print("Current state of array:", array)
        # Swap only if the minimum index has changed
        if i != min_index:
            array[i], array[min_index] = array[min_index], array[i]


bubble_sort2(arr)
print(arr)
