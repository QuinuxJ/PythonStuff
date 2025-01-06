def solution(array):
    position1 = 0
    k = 0
    
    while position1 < len(array):
        if array[position1] != 0:
            array[k], array[position1] = array[position1], array[k]
            k+=1
        position1+=1
        
    return array
    
nums = [0,1,0,3,12]
print(solution(nums))
    