def invert(lst):
    lista = []
    for i in lst:
        lista.append(-i)
    return lista
    

print(invert([1,2,3,4,5]))
print(invert([1,-2,3,-4,5]))
print(invert([])) 