
def is_isogram(word):
    word = word.lower()
    if word == '':
        return True
   
    for i in range(len(word)):
        lett = word[i]
        
        for j in range(i + 1, len(word)):
            if lett == word[j]:
                return False
    return True
           
           
       
    
    
print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))