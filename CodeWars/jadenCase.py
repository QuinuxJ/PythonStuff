def to_jaden_case(string):
    word = []
    string = string.split()
    for i in range(len(string)):
        word.append(string[i].capitalize())
    return ' '.join(word)

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))