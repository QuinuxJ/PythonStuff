def sum_array(arr):
    if  arr == None or len(arr) < 3:
        return 0
    for i in range(len(arr)):
        nm = arr[i]
        nmn = arr[i]
        for j in range(i+1, len(arr)):
            if nm < arr[j]:
                nm = arr[j]
            else: continue
        for k in range(i+1, len(arr)):
            if nmn > arr[k]:
                nmn = arr[k]
            else: continue
        
        arr.remove(nm)
        arr.remove(nmn)
    return sum(arr) - min(arr) - max(arr)

print(sum_array(None)) #Output ---> 0
print(sum_array([3])) #Output ---> 0
print(sum_array([3, 5])) #Output ---> 0
print(sum_array([6, 2, 1, 8, 10])) #Output ---> 16
print(sum_array([1, 1, 11, 2, 3])) #Output ---> 6
