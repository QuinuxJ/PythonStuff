def solution(numbers, target):
    izquierda = 0
    derecha = len(numbers) - 1
    while izquierda <= derecha:
        mitad = izquierda + (derecha - izquierda) // 2
        if numbers[mitad] == target:
            return mitad
        
        
        if numbers[mitad] >= numbers[izquierda] and target <= numbers[mitad]:
            if target >= numbers[izquierda]:
                derecha = mitad - 1
            else:
                izquierda = mitad + 1
            
        elif numbers[mitad] <= numbers[derecha] and target >= numbers[mitad]:
            if target <= numbers[derecha]:
                izquierda = mitad + 1
            else:
                derecha = mitad - 1
    return -1
    
    
numbers = [4,5,6,7,0,1,2]

target = 0 
print(solution(numbers,target))