def high(x):
    return int(max(x.translate(x.maketrans(chr(i): str(i - 96) for i in range(97, 123)))))


print(high('man i need a taxi up to ubud'))