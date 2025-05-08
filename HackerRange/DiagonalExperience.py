def diagonalDifference(arr):
    left_diagonal = 0
    right_diagonal = 0
    n = len(arr)

    for i in range(n):
        left_diagonal += arr[i][i]
        right_diagonal += arr[i][n - i - 1]

    return abs(left_diagonal - right_diagonal)
    


arr = [
       [1, 2, 3], 
       [4, 5, 6], 
       [9, 8, 9]
       ]

print(diagonalDifference(arr)) # 15