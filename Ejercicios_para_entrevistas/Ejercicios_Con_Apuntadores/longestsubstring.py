def solution(stringws):
    lengthString = set()
    start = 0
    max_length = 0
    current_length = 0
    
    for position1 in range(len(stringws)):
        
        while stringws[position1] in lengthString:
            lengthString.remove(stringws[start])
            start +=1
       
        lengthString.add(stringws[position1])
        
        current_length = position1 - start + 1
        if current_length > max_length:
            max_length = current_length
            tope = position1
            
    return max_length, position1
        
s = "abcabcbb"
s = "jdkafnlcdsalkxcmpoiuytfccv"
print(solution(s))