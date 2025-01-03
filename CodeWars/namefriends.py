def friend(x):
    names = []
    names.extend(i for i in x if len(i) == 4)
    return names
    
    

print(friend(["Peter", "Stephen", "Joes"]))