def lonelyinteger(a):
    cont = {}
    
    for i in a:
        if i in cont:
            cont[i] += 1
        else:
            cont[i] = 1
    for key, value in cont.items():
        if value == 1:
            return key

a = [1,2,3,4,3,2,1]
print(lonelyinteger(a))