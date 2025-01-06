def solution(heights):
    last_position = len(heights) - 1 #ultima posicion del arreglo
    first_position = 0
    max_area = 0
    
    for i in range(len(heights)):
        area = min(heights[last_position], heights[first_position]) * (last_position - first_position) # area = altura * ancho
        
        if area > max_area:
            max_area = area 
         
        if heights[first_position] < heights[last_position]:
            first_position += 1
        else:
            last_position -=1
            
        # Detén el bucle si los punteros se cruzan
        if first_position >= last_position:
            break
            
    return max_area    

heights = [1,8,6,2,5,4,8,3,7]
print(solution(heights))
       