def consecutive(num):
    cont = 0
    for i in range(1,num):
        suma = 0
        for j in range(i,num):
            suma += j
            if suma == num:
                cont += 1
            elif suma > num:
                break
    return cont
        
print(consecutive(15)) 