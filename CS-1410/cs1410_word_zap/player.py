import random

class Player:
    def __init__(self,name):
        self.name = name
        self.letters = []
        theletters = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        for i in range(7):
            num = random.randrange(len(theletters))
            letter = theletters[num]
            self.letters.append(letter)


    def getName(self):
        return self.name

    def getLetters(self):
        return self.letters

    def drawLetter(self):
        theletters = 'aaaaaaaaabbccddddeeeeeeeeeeeeffggghhiiiiiiiiijkllllmmnnnnnnooooooooppqrrrrrrssssttttttuuuuvvwwxyyz'
        num = random.randrange(len(theletters))
        letter = theletters[num]
        self.letters.append(letter)
        return letter

    def checkWord(self, word):
        woord = word[:]
        thelist = []
        for letter in self.letters:
            thelist.append(letter)
        for letter in woord:
            if letter not in thelist:
                return False
            else:
                thelist.remove(letter)
        self.letters = thelist
        return True
