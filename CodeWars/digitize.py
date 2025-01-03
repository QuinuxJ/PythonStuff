def digitize(n):
    num = [int(digit) for digit in str(n)]
    num.reverse()
    return num
    
print(digitize(35231))