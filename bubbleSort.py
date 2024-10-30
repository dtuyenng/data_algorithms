

arr = [4, 2, 6, 5, 1, 3]

def bubble_sort(array):
    for i in range(len(array)):
        for index in range(len(array) - 1 - i):
            curr  = array [index]
            after = array[index + 1]
            if curr > after:
                array[index], array[index+1] = array[index+1], array[index]

# arr = [4, 2, 6, 5, 1, 3]
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


selection_sort(arr)
print(arr)
