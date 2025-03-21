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
        
    def Exists(self, item):
        for i in self.hold:
            if i == item:
                return True
        return False

    def Retrieve(self, item):
        for i in self.hold:
            if i == item:
                return item
        return None

    def Size(self):
        A = len(self.hold)
        return A


    def __iter__(self):
        for i in range(len(self.hold)):
            yield self.hold[i]

    

class Student:

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
    
    def __iter__(self):
        yield


def main():

    #Insert

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
    print("Total Time was: ", t2-t1)
    fin.close()
    # Traverse
    """
    totalAge = 0
    for item in c:
        age = int(item.getAge())
        totalAge+=1
    print('The average age is: ', totalAge / c.Size())
    """
    #print how long it took

    #Delete
    """
    fin = open('DeleteNames.txt', 'r')
    for line in fin:
        ssn = line.strip()
        dummyStudent = Student("", "", ssn, "", "")
        ok = c.Delete(dummyStudent)
        if not ok:
            print("Can't delete")
    fin.close()
    """
    #print how long it took

    #retrieve
    """
    totalAge = 0
    fin = open('RetriveNames.txt', 'r')
    for line in fin:
        ssn = line.strip()
        dummyStudent = Student("", "", ssn, "", "")
        s2 = c.Retrieve(dummyStudent)
        if s2 is not None:
            totalAge += int(s2.age())
        else:
            print("Error")
    print("avergae of retrieved ages: ", totalAge / c.Size())
    """
    #print how long it took

main()