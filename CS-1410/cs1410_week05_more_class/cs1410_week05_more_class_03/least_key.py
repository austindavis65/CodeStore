def least_key(dictionary):
    thelist = []
    for key in dictionary:
        thelist.append(key)
    smooll = thelist[0]
    for key in dictionary:
        if key < smooll:
            smooll = key
    return smooll