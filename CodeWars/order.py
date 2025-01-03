def order(sentence):
    words = sentence.split()
    sorted_words = sorted(words, key=lambda word: [int(char) for char in word if char.isdigit()])
    return ' '.join(sorted_words)

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))