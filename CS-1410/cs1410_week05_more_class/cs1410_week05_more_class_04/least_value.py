def least_value(dictionary):
    thelist = []
    for key in dictionary:
        thelist.append(key)
    n = -1
    smoll = 1000
    for key in dictionary:
        n += 1
        if dictionary[thelist[n]] < smoll:
            smoll = dictionary[thelist[n]]
    return smoll