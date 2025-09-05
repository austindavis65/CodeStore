def combo_string(a,b):
    counta = 0
    countb = 0
    astring = ""
    for i in a:
        counta += 1
    for i in b:
        countb += 1
    if counta > countb:
        bigger = a
        smaller = b
    else:
        bigger = b
        smaller = a
    astring = smaller + bigger + smaller
    return astring
print(combo_string('Hello', 'hi'))
print(combo_string('hi', 'Hello'))
print(combo_string('aaa', 'b'))