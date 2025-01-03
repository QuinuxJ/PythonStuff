def count_sheeps(sheep):
    return sum(1 for i in sheep if i == True)


arr = [True,  True,  True,  False,
        True,  True,  True,  True ,
        True,  False, True,  False,
        True,  False, False, True ,
        True,  True,  True,  True ,
        False, False, True,  True ]
print(count_sheeps(arr))