#
#
# arr = [10, 16, 8, 12, 15, 6, 3, 9, 5]
# i = 0
# j = len(arr) - 1
#
#
# def swap(arr, i, j):
#     tmp = arr[j]
#     arr[j] = arr[i]
#     arr[i] = tmp
#     print(f"Swapped: {arr[j]} (i={i}) {arr[i]} (j={j}) {arr}")
#
#
#
# def partition(arr, index, i, j):
#     arr.append(float('inf'))                # set last element of array to infinity
#     i, j = 0, len(arr) - 1                  # set i and j to be at the beginning and end respectively
#     pivot = arr[index]
#
#     # print(f"index = {arr[index]}, i = {i}({arr[i]}), j = {j}({arr[j]}) ")
#
#     # increment i UNTIL find element BIGGER than pivot
#     # increment j UNTIL find element SMALLER than pivot
#     # exchange i <=> j values
#     # when i crosses j, don't swap
#     # the location of j is where the pivot should be. Swap j with pivot
#
#     while i < j:
#         print(f"Pivot: {pivot}")
#         print(f"i: {i} value= {arr[i]}")
#         print(f"j: {j} value= {arr[j]}")
#
#         i += 1
#         j -= 1
#
#         while arr[i] < pivot:
#             print(f"da, i at {i}")
#             i += 1
#
#         while arr[j] > pivot:
#             print(f"da, j at {j}")
#             j -= 1
#
#         if i < j:
#             swap(arr, i, j)
#
#     # swap(arr, pivot, j)
#     print(f"Pre Final: {arr} i({i}) at value {arr[i]} j({j}) at value {arr[j]}")
#     swap(arr, index, j)
#     print(f"Final: {arr} i({i}) at value {arr[i]} j({j}) at value {arr[j]}")
#
# partition(arr, 0, 0,0 )