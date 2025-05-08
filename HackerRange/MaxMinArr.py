def miniMaxSum(arr):
    minSum = 0
    maxSum = 0
    arrMax = arr.copy()
    arrMin = arr.copy()
    arrMin.remove(max(arr))
    arrMax.remove(min(arr))
    
    for i in range(len(arrMin)):
        minSum = minSum + arrMin[i]
    for i in range(len(arrMax)):
        maxSum = maxSum + arrMax[i]
        
    return minSum, maxSum
    
arr = [7, 69, 2, 221, 8974]
print(miniMaxSum(arr))