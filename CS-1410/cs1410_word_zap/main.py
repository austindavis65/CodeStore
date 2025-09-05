def getUserString(prompt):
    string = ''
    while string == "":
        string = input(prompt).strip()
    return string

def getUserInt(prompt):
    keepLooping = True
    while keepLooping:
        ans = input(prompt)
        try:
            num = int(ans)
            if num > 0:
                keepLooping = False;
        except:
            print("you can't convert that string to a integer")
    return num

def convertToLower(prompt):
    return prompt.lower()

def getPlayers():
    number = getUserInt('How many people are playing? ')
    


# if __name__ == '__main__':
#     main()
