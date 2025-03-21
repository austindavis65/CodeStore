import time

class Container:
    def __init__(self):
        self.hold = []

    def Add(self, item): #returns False on duplicate
        if self.Exists(item):
            return False
        else:
            self.hold.append(item)
            return True
        
    def Delete(self, item): #returns False on non existent
        if self.Exists(item):
            self.hold.remove(item)
            return True
        else:
            return False
        
    def Exists(self, item):
        for i in self.hold:
            if i == item:
                return True
        return False

    def Retrieve(self, item):
        for i in self.hold:
            if i == item:
                return i
        return None

    def Size(self):
        A = len(self.hold)
        return A


    def __iter__(self):
        for i in range(len(self.hold)):
            yield self.hold[i]

    

class Student:

    A = ['mFirst', 'mLast', 'mSSN', 'mEmail', 'mAge']

    def __init__(self, last, first, ssn, email, age):
        self.mLast = last
        self.mFirst = first
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age        

    def __eq__(self, rhs):
        return self.mSSN == rhs.mSSN
    
    def getAge(self):
        return self.mAge

def main():

    #Insert

    print('\n', '\t', 'Insert', '\n')
    c = Container()
    t1 = time.time()
    fin = open('FakeNames.txt', 'r')
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2], words[3], words[4])
        ok = c.Add(s)
        if not ok:
            print("Can't add")
    t2 = time.time()
    print("Total Time was: ", round(t2-t1, 4))
    fin.close()

    # Traverse

    print('\n', '\t', 'Traverse', '\n')
    t1 = time.time()
    totalAge = 0
    for item in c:
        age = int(item.getAge())
        totalAge+=age
    print('The average age is: ', round(totalAge / c.Size(), 4))
    t2 = time.time()
    print("Total Time was: ", round(t2-t1, 4))

    #Delete

    print('\n', '\t', 'Delete', '\n')
    t1 = time.time()
    fin = open('DeleteNames.txt', 'r')
    for line in fin:
        ssn = line.strip()
        dummyStudent = Student("", "", ssn, "", "")
        ok = c.Delete(dummyStudent)
        if not ok:
            print("Can't delete")
    fin.close()
    t2 = time.time()
    print("Total Time was: ", round(t2-t1, 4))

    #retrieve

    print('\n', '\t', 'Retrieve', '\n')
    t1 = time.time()
    totalAge = 0
    fin = open('RetrieveNames.txt', 'r')
    for line in fin:
        ssn = line.strip()
        dummyStudent = Student("", "", ssn, "", "")
        s2 = c.Retrieve(dummyStudent)
        if s2 is not None:
            totalAge += int(s2.getAge())
        else:
            print("Error")
    print("Avergae of retrieved ages: ", round(totalAge / c.Size(), 4))
    t2 = time.time()
    print("Total Time was: ", round(t2-t1, 4))


main()