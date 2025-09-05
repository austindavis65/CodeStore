import sys

def createIndex():
    return {}

def recordBook(index,isbn,title):
    index[isbn] = title

def findBook(index,isbn):
    if isbn in index:
        return index[isbn]
    else:
        return ''

def listBooks(index):
    books = []
    sequence = 0
    for key in index:
        sequence += 1
        string = str(sequence) + ') ' +key+': '+index[key]
        books.append(string)
    return books

def formatMenu():
    return [
        "What would you like to do?",
        '[r] Record a Book',
        "[f] Find a Book",
        '[l] List all Books',
        "[q] Quit"
        ]

def formatMenuPrompt():
    return "Enter an option: "

def getUserChoice(choice):
    string = ''
    while string == "":
        string = input(choice).strip()
    return string

def getISBN():
    ISBN = getUserChoice('Type an ISBN: ')
    return ISBN

def getTitle():
    title = getUserChoice('Type a title: ')
    return title

def recordBookAction(index):
    ISBN = getISBN()
    title = getTitle()
    recordBook(index,ISBN,title)

def findBookAction(index):
    ISBN = getISBN()
    book = findBook(index,ISBN)
    if book:
        print(book)
    else:
        print('Book not found')

def listBooksAction(index):
    book = listBooks(index)
    if index == []:
        print('No books have been recorded.')
    else:
        for b in book:
            print(b)

def quitAction(index):
    print("You have quit the program. Have a nice day.")
    sys.exit(0)

def applyAction(index,userInput):
    if userInput == "r":
        recordBookAction(index)
    elif userInput == 'f':
        findBookAction(index)
    elif userInput == "l":
        listBooksAction(index)
    elif userInput == 'q':
        quitAction(index)
    else:
        print("That option is invalid")

def main():
    index = createIndex()
    while True:
        for i in formatMenu():
            print(i)
        applyAction(index,getUserChoice(formatMenuPrompt()))
    
if __name__ == '__main__':
    main()
