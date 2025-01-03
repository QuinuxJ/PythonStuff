def points(games):
    ps = 0
    for g in range(len(games)):
        gg = games[g].split(':')
        if gg[0] > gg[1]:
            ps +=3
        if gg[0] < gg[1]:
            ps +=0
        if gg[0] == gg[1]:
            ps +=1
    
    return ps
    
print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))