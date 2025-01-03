def is_pangram(st):
    st = set(st.lower().replace(" ", ""))
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
    return True if alphabet.issubset(st) else False
    
            
    
    


print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("Cwm fjord bank glyphs vext quiz"))
print(is_pangram("abcdefghijklmopqrstuvwxyz"))
print(is_pangram("This isn't a pangram"))
