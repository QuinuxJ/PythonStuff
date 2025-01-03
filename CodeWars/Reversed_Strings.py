def solution(word):
    nw = ''
    for i in range(0, len(word)):
        nw = word[::-1]
    return nw

print(solution("hello"))
print(solution(""))