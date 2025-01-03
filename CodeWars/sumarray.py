def sum_array(a):
    b = 0
    for i in range(len(a)):
        b += a[i]
    return b

    if len(a) == 0:
        return 0
    elif len(a) == 1:
        return a[0]
    

print(sum_array([1,2,3]))
print(sum_array([]))
print(sum_array([9]))