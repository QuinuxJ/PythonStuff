def solution(heights):
    first_position = 0
    last_position = len(heights) - 1 #last position in heights
    trappedWater = 0
    Lheight = 0
    Rheight = 0
    
    
    while first_position < last_position:
        
        if heights[first_position] < heights[last_position]:
            
            if heights[first_position] < Lheight:
                trappedWater += Lheight - heights[first_position]
            else:
                Lheight = heights[first_position]
                
            first_position += 1
        
        else:
            if heights[last_position] < Rheight:
                trappedWater += Rheight - heights[last_position]
            else:
                Rheight = heights[last_position]
                
            last_position -=1
            
    return trappedWater

heights = [0,1,0,2,1,0,1,3,2,1,2,1]
print(solution(heights))
       