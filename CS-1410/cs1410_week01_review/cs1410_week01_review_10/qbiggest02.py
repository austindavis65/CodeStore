def biggest02(x,y):
    list = [-100]
    max = list[0]
    n=-1
    stuff = x + y
    thing = x * y
    list.append(stuff)
    list.append(thing)
    for i in list:
        n+=1
        if i > max:
            max = i
    return max
print(biggest02(2,3))
print(biggest02(-2,3))
