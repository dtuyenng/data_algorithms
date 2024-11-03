

arr = [4, 2, 6, 5, 1, 3]




def bubble_sort2(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j+1]:
                tmp = array[j]
                array[j] = array[j+1]
                array[j+1] = tmp

def bubble_sort(array):
    for i in range(len(array)):
        for index in range(len(array) - 1 - i):
            curr  = array [index]
            after = array[index + 1]
            if curr > after:
                array[index], array[index+1] = array[index+1], array[index]


