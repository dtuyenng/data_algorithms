# Input array to be sorted
arr = [5, 2, 3, 1, 9, 1, 6]

def insertion_sort(array):
    """
    Sorts the input list in ascending order using the insertion sort algorithm.
    Parameters:
    array (list): The list of numbers to be sorted.
    Algorithm:
    - Iterate through the list starting from the second element.
    - For each element, compare it with the elements before it.
    - Shift elements larger than the current element to the right.
    - Insert the current element into its correct position in the sorted portion of the list.
    """
    for i in range(1, len(array)):  # Start iterating from the second element
        current_value = array[i]    # Current element to be inserted
        j = i - 1                   # Index of the previous element

        # Compare and shift elements greater than current_value to the right
        while j >= 0 and current_value < array[j]:
            array[j + 1] = array[j]
            j -= 1

        # Insert the current_value at its correct position
        array[j + 1] = current_value

insertion_sort(arr)
print(arr)
