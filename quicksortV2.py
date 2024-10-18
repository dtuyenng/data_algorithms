my_array = [10, 16, 8, 12, 15, 6, 3, 9, 5]

def partition(arr, low, high):

    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    pivot = arr[low]  # Use the pivot from the index given
    i = low + 1  # Initialize i to the next position after the pivot
    j = high  # Initialize j

    while i <= j:

        # Move i until we find an element strictly greater than pivot
        # make sure i doesn't go over high
        while i <= high and arr[i] <= pivot:
            i += 1

        # Move j until we find an element smaller than or equal to the pivot
        # make sure j doesn't go below low
        while j >= low and arr[j] > pivot:
            j -= 1

        # Swap elements if i and j haven't crossed each other
        if i < j:
            swap(i, j)
    # Once i and j have crossed, we need to place the pivot in the correct position
    swap(low, j)
    print(f"Final: {arr} i({i}) j({j}) with value {arr[j]} is in position")

    return j  # Return the final position of the pivot

def quicksort(arr, low, high):
    if low < high:  # At least two elements
        j = partition(arr, low, high)
        quicksort(arr, low, j - 1)  # Sort the left part
        quicksort(arr, j + 1, high)  # Sort the right part

def sort_array(arr):
    quicksort(arr, 0, len(arr) - 1)

sort_array(my_array)
print(my_array)
