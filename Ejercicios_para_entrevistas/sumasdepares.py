# Pregunta:
# Dado un arreglo de números enteros, escribe un algoritmo en Python 
# para encontrar todos los pares de números cuya suma sea igual a un número objetivo (target). 
# Devuelve los pares como una lista de tuplas.
def solution(n, target):
    result = []

    for i in range(len(n)):
        for j in range(0, len(n)): 
            if n[i] + n[j] == target:
                result.append((n[i],n[j]))
                
    return result

numbers = [2, 4, 3, 7, 5, 9]
target = 9
print(solution(numbers,target))