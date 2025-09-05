def longest_string(strings):
    big = 0
    springs = ''
    n = -1
    for string in strings:
        n+=1
        if len(string) > big:
            big = len(string)
            springs = string
    return springs