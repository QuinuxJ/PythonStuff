def flippingMatrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    total_sum = 0

    for i in range(n // 2):
        for j in range(m // 2):
            # Get the four corners of the current 2x2 submatrix
            a = matrix[i][j]
            b = matrix[i][m - j - 1]
            c = matrix[n - i - 1][j]
            d = matrix[n - i - 1][m - j - 1]

            # Add the maximum of the four corners to the total sum
            total_sum += max(a, b, c, d)

    # If n or m is odd, we need to handle the middle row or column
    if n % 2 == 1:
        for j in range(m // 2):
            total_sum += max(matrix[n // 2][j], matrix[n // 2][m - j - 1])

    if m % 2 == 1:
        for i in range(n // 2):
            total_sum += max(matrix[i][m // 2], matrix[n - i - 1][m // 2])

    return total_sum