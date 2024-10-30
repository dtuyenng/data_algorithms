arr = [5, 6, 3, 1, 9, 6, 7, 0]

def bubble_sort(array):
    for _ in range(len(array)):
        for index in range(len(array) - 1):
            curr  = array [index]
            after = array[index + 1]
            if curr > after:
                array[index], array[index+1] = array[index+1], array[index]


bubble_sort(arr)
print(arr)
