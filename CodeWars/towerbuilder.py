def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        ast = '*' * (1+2*i)
        tower.append(f" {ast} ")
    
    return f"'{tower}'"

print(tower_builder(5))