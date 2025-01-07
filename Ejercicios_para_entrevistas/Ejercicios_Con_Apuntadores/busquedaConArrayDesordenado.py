def solution(numbers, target):
    izquierda = 0
    derecha = len(numbers) - 1
    while izquierda <= derecha:
        mitad = izquierda + (derecha - izquierda) // 2
        if numbers[mitad] == target:
            return mitad
        elif numbers[mitad] < target:
            izquierda = mitad + 1
        else:
                derecha = mitad - 1
    return -1
    
    
numbers = [16,23,40,56,72,99,1,5,8,11]
target = 16
print(solution(numbers,target))