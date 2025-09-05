from cisc108 import assert_equal
def fifthchar(filename):
    file = open(filename)
    astring = ''
    for line in file:
        line.strip(' ')
        if len(line) >= 5:
            astring = astring.strip('\n ') + line[4]
        else:
            pass
    astring.strip('\n ')
    astring.strip(' ')
    return astring
assert_equal(fifthchar("nmdvydqu.txt"), 'bgfwsxlljqd')
