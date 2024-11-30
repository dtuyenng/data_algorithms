def merge(left, right):
    result = []
    i = j = 0

    # Merge the two sorted arrays
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def mergesort(array):
    if len(array) <= 1:  # Base case: a single element is already sorted
        return array

    # Divide the array into two halves
    mid = len(array) // 2
    left = mergesort(array[:mid])  # Recursively sort the left half
    right = mergesort(array[mid:])  # Recursively sort the right half

    # Merge the sorted halves
    return merge(left, right)

# Example usage
arr = [4, 1, 0, 9, 2, 7, 6]
sorted_arr = mergesort(arr)
print(sorted_arr)  # Output: [0, 1, 2, 4, 6, 7, 9]
