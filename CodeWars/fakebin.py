def fake_bin(x):
    b = '0'
    nw= []
    for i in x:
        if int(i) < 5:
            b = '0'
            nw.append(b)
        elif int(i) >=5:
            b = '1'
            nw.append(b)
    return ''.join(nw)
        
    
print(fake_bin("45385593107843568"))
print(fake_bin("509321967506747"))