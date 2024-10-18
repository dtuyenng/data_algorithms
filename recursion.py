from itertools import count


def countdown(i):
    if i < 0:
        return
    else:
        print(i)
        countdown(i-1)

# countdown(3)

arr = [2, 3, 4, 5, 6, 7, 3, 6] # make it [5, 6]

# def recursive_sum(arr):
#     if len(arr) != 2:
#         return_arr =  [arr[0] + arr[1]] + arr[2:]
#         print(return_arr)
#         recursive_sum(return_arr)
#     else:
#         print(f"Eq: {arr[0]} + {arr[1]}")
#         return arr[0] + arr[1]

def recursive_sum(arr):
    if len(arr) != 2:
        return_arr =  [arr[0] + arr[1]] + arr[2:]
        print(return_arr)
        return recursive_sum(return_arr)
    else:
        return_arr = arr[0] + arr[1]
        print(return_arr)
        return return_arr




print(recursive_sum(arr))

# Write a recursive function to count the item in a list. Base case is when the list has 0 element