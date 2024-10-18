from quicksortV2 import quicksort

# arr = [10, 10, 16, 8, 12, 15, 6, 3, 9, 10, 5]
arr = [4, 2, 3, 4, 5, 4]

def partition(low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while i <= j:

        while arr[i] <= pivot: # while value of array at i is less or equal, skip and increment i
            print("first")
            i += 1

        while arr[j] > pivot: # while value of array at j is higher than pivot, skip and decrement j
            print("second")
            j -= 1

        if i < j:
            print("swap")
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]

    return j

def quicksort(low, high):
    if (low < high):
        j = partition(low, high)
        quicksort(low, j-1)
        quicksort(j+1, high)

quicksort(0, len(arr) -1)


print(arr)


