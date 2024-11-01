arr = ["t", "u", "y", "e", "n"]

# for i in range(len(arr)):
#     print(" ")
#     for j in range(len(arr) - i):
#         print(arr[j+i])

for i in range(len(arr)):
    print(" ")
    for j in range(i, len(arr)):
        print(arr[j])