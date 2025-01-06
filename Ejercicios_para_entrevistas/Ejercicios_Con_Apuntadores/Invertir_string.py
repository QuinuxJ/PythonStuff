def solution(string):
    p1 = 0
    p2 = len(string) -1
    while p1 < p2:
        string[p1], string[p2] = string[p2], string[p1]
        p1 +=1
        p2 -=1             
    return string


s = ["h", "e", "l", "l", "o"]
print(solution(s))