def complejidadLineal(lista):
    suma = 0    #        # O(1)
    multiplicacion = 1   # O(1)
    
    for num in range(len(lista)):
        suma += num    # O(n)
    
    or num in range(len(lista)):
        multiplicacion *= num   # O(n)
        
    return suma, multiplicacion  # O(1)

# O(1) + O(1) + O(n) + O(n) + O(1) = O(2 + 2n) = O(2n) = O(n)