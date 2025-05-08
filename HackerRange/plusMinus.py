def plusMinus(arr):
    contP = 0
    contN = 0
    contZ = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            contP +=1
        elif arr[i] == 0:
            contZ +=1
        elif arr[i] < 0:
            contN +=1
    pN = contP / len(arr)
    nN = contN / len(arr)
    zN = contZ / len(arr)
    
    return f"{pN:.6f}\n{nN:.6f}\n{zN:.6f}"
arr = [1,1,0,-1,-1]
print(plusMinus(arr))