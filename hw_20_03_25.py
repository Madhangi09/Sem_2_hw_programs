def rearrange_array(arr):
    n = len(arr)
    for i in range(n - 1):
        if i % 2 == 0 and arr[i] < arr[i + 1]:  # Even index: should be greater
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        elif i % 2 == 1 and arr[i] > arr[i + 1]:  # Odd index: should be smaller
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
arr = [5, 3, 1, 2, 3, 7, 6, 4]
print(rearrange_array(arr))
