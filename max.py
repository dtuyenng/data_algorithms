arr = [
    -5, 12, 37, -21, 56, -10, 3, 48, 24, -80,
    67, 19, -43, 92, 74, -56, 81, -99, 28, 44,
    -7, 33, 1, 58, -22, 72, -66, 88, 14, 49,
    39, 0, -15, 53, 16, 84, -11, 70, -34, 27,
    94, 6, 77, 61, -19, 46, 29, 8, 90, -59,
    73, -75, 95, -41, 4, 86, -12, 66, 32, -3,
    -64, 20, 54, -25, 42, 15, -17, 87, -88, 30,
    40, -71, 68, 10, 93, -20, 75, 59, -36, 22,
    -78, 9, 13, 38, 50, 62, 76, -57, 35, 72,
    -83, 69, 2, -8, 82, 91, -47, 34, 65, -4]

def largest(arr):
    max1 = arr[0]
    max2 = arr[0]
    for value in arr:
        if value > max1:
            max2 = max1
            max1 = value
        elif value > max2:
            max2 = value



    # for value in arr:
    #     if value > max2 and  value < max1:
    #         max2 = value


    return [max1, max2]

print(largest(arr))