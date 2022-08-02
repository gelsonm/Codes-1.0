# Sum of array using recursion

def sumArray(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]
    val = arr[0] + arr[1]
    return val + sumArray(arr[2:])
