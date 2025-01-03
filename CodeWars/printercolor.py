def printer_error(s):
    errc = 0
    for char in s:
        if ord(char) < ord('a') or ord(char) > ord('m'):
            errc += 1
    
    return (f"{errc}/{len(s)}") 
    

print(printer_error("aaabbbbhaijjjm"))
print(printer_error("aaaxbbbbyyhwawiwjjjwwm"))
print(printer_error("aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"))