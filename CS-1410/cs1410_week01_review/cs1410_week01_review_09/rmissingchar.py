def missing_char(string, index):
    if string[index]:
        letter = string[index]
        word = string.replace(letter, '')
        return word
    else:
        pass



print(missing_char("fred", 0))
print(missing_char("fred", 1))
print(missing_char("fred", 2))
print(missing_char("fred", 3))