def alienDictionary(words, order):
    order_map = {char: index for index, char in enumerate(order)}
    
    def compare(word1, word2):
        for char1, char2 in zip(word1, word2):
            if order_map[char1] < order_map[char2]:
                return True
            elif order_map[char1] > order_map[char2]:
                return False
    
    for i in range(len(words) - 1):
        if not compare(words[i], words[i + 1]):
            return False
        
        
words = ["hello", "leetcode", "world", "row", "my"]
order = "hlabcdefgijkmnopqrstuvwxyz"

print(alienDictionary(words, order)) # True

words = ["word", "world", "row"]
order = "worldabcefghijkmnpqstuvxyz"

print(alienDictionary(words, order)) # False