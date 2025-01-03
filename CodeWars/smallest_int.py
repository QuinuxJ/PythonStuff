def find_smallest_int(arr):
    n = arr[0]
    for i in range(1, len(arr)):
        if n > arr[i]:
            n = arr[i]
    return n