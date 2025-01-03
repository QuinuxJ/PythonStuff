def descending_order(num):
    nn = [int(n) for n in str(num)]
    nn.sort(reverse=True)
    num = int(''.join(map(str, nn)))
    return num

print(descending_order(42145))
print(descending_order(15))
print(descending_order(0))