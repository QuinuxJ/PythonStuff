def solution(text, ending):
    return True if text.endswith(ending) else False

print(solution("samurai", "ai"))
print(solution("ninja",   "ja"))
print(solution("sumo",    "omo"))
print(solution("abc",     "abcd"))