# Array to be sorted
arr = [3, 5, 1, 7, 10, 6]

def partition(array, low, high):
    """
    Partitions the array around a pivot, which is chosen as the last element in the given range.
    Parameters:
    - array: The list of elements to be partitioned.
    - low: The starting index of the range to partition.
    - high: The ending index of the range to partition (pivot is chosen as array[high]).
    Returns:
    - The index of the pivot after placing it in its correct position.
    """
    pivot_value = array[high]  # Choose the last element as the pivot
    j = low - 1  # Pointer for elements smaller than the pivot

    # Loop through the elements and partition based on the pivot
    for i in range(low, high):
        if array[i] < pivot_value:  # If element is smaller than pivot
            j += 1  # Move the pointer forward
            array[i], array[j] = array[j], array[i]  # Swap elements

    # Place the pivot in its correct position
    j += 1
    array[j], array[high] = array[high], array[j]
    return j  # Return the index of the pivot


def quicksort(array, low, high):
    """
    Sorts an array in place using the QuickSort algorithm.
    Parameters:
    - array: The list of elements to be sorted.
    - low: The starting index of the range to sort.
    - high: The ending index of the range to sort.
    This function sorts the array by recursively partitioning it into smaller sub-arrays
    and sorting those sub-arrays.
    """
    if low < high:
        # Partition the array and get the pivot index
        pivot = partition(array, low, high)

        # Recursively sort the elements before and after the pivot
        quicksort(array, low, pivot - 1)  # Sort the left partition
        quicksort(array, pivot + 1, high)  # Sort the right partition


# Call the quicksort function to sort the entire array
quicksort(arr, 0, len(arr) - 1)

# Print the sorted array
print(arr)  # Output: [1, 3, 5, 6, 7, 10]
