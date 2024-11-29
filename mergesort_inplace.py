arr = [4, 1, 0, 9, 2, 7, 6]
arr1 = [0, 1, 3, 5, 7]
arr2 = [2, 5, 8, 11]

def merge(l, h):
    mid = (l + h) // 2
    print("low", l)
    print("high", h)
    print("mid", mid)

merge(0, len(arr1) - 1)