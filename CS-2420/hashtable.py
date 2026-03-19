import math
import time

class Student: #student class

    A = ['mFirst', 'mLast', 'mSSN', 'mEmail', 'mAge']

    def __init__(self, last, first, ssn, email, age):
        self.mLast = last
        self.mFirst = first
        self.mSSN = ssn
        self.mEmail = email
        self.mAge = age        

    def __eq__(self, rhs):
        return self.mSSN == rhs.mSSN
    
    def __ne__(self, rhs):
        return self.mSSN != rhs.mSSN

    def __lt__(self, rhs):
        return self.mSSN < rhs.mSSN
    
    def __gt__(self, rhs):
        return self.mSSN > rhs.mSSN
    
    def __le__(self, rhs):
        return self.mSSN <= rhs.mSSN
    
    def __ge__(self, rhs):
        return self.mSSN >= rhs.mSSN
    
    def __hash__(self):
        return int(self.mSSN.replace('-',''))
    
    def getAge(self):
        return self.mAge

def IsPrime(x): #recieves an integer and returns a true or false whther it is a prime number
    if x == 2:
        return True
    s = int(math.sqrt(x))
    for i in range(2, s+1):
        if x % i == 0:
            return False
    return True

class HashTable: #creates hash table
    def __init__(self, numItem): #initializes table and asks for number of slots for the table
        self.size = 0
        slots = 2 * numItem + 1
        while not IsPrime(slots):
            slots+=2
        self.table = []
        for i in range(slots):
            self.table.append(None)

    def Exists(self, item): #checks if given item exists
        key = hash(item)
        index = key % len(self.table)
        keyindex = key % len(self.table)

        while True:
            if self.table[index] is None:
                return False
            if self.table[index] and self.table[index] == item:
                return True
            index+=1
            if index == len(self.table):
                index = 0
            if index == keyindex:
                return False

    def Size(self): #returns the total nuber of items in table
        count = 0
        for item in self.table:
            if item:
                count += 1
        return count

    def Delete(self, item): #deletes given item if exists in table
        if not self.Exists(item):
            return False
        key = hash(item)
        index = key % len(self.table)
        keyindex = key % len(self.table)
        while True:
            if self.table[index] and item == self.table[index]:
                self.table[index] = False
                self.size -= 1
                return True
            index += 1
            if index >= len(self.table):
                index = 0
            if index == keyindex:
                return False

        
    def Insert(self, item): #adds item to table
        if self.Exists(item):
            return False
        key = hash(item)
        index = key % len(self.table)
        keyindex = key % len(self.table)
        while True:
            if not self.table[index]:
                self.table[index] = item
                self.size += 1
                return True
            else:
                index+=1
                if index >= len(self.table):
                    index = 0
                if index == keyindex:
                    return False

        
    def Retrieve(self, item): #returns given item if it exists in the table
        key = hash(item)
        index = key % len(self.table)
        keyindex = key % len(self.table)

        while True:
            if self.table[index] is None:
                return False
            if self.table[index] and self.table[index] == item:
                return self.table[index]
            index+=1
            if index == len(self.table):
                index = 0
            if index == keyindex:
                return False
            
    def __iter__(self):
        for item in self.table:
            if item:
                yield item

def main():

    #Insert
    print('Input size of your table please:')
    c = HashTable(int(input()))
    thetime = time.time()
    print('\n', '\t', 'Insert', '\n')
    t1 = time.time()
    fin = open('/Users/austindavis/Desktop/cs2420/names/FakeNamesMedium.txt', 'r')
    tf = 0
    for line in fin:
        words = line.split()
        s = Student(words[0], words[1], words[2], words[3], words[4])
        ok = c.Insert(s)
        if not ok:
            tf += 1
    t2 = time.time()
    print("Total Time was: ", round(t2-t1, 4))
    print("Total Fails were: ", tf)
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
    fin = open('/Users/austindavis/Desktop/cs2420/names/DeleteNamesMedium.txt', 'r')
    tf = 0
    for line in fin:
        ssn = line.strip()
        dummyStudent = Student("", "", ssn, "", "")
        ok = c.Delete(dummyStudent)
        if not ok:
            tf += 1
    fin.close()
    t2 = time.time()
    print("Total Time was: ", round(t2-t1, 4))
    print("Total Fails were: ", tf)

    #retrieve

    print('\n', '\t', 'Retrieve', '\n')
    t1 = time.time()
    totalAge = 0
    rstudents = 0
    fin = open('/Users/austindavis/Desktop/cs2420/names/RetrieveNamesMedium.txt', 'r')
    tf = 0
    for line in fin:
        ssn = line.strip()
        dummyStudent = Student("", "", ssn, "", "")
        s2 = c.Retrieve(dummyStudent)
        if s2 and s2 is not None:
            totalAge += int(s2.getAge())
            rstudents += 1
        else:
            tf +=1
    print("Avergae of retrieved ages: ", round(totalAge / rstudents, 4))
    t2 = time.time()
    print("Total Time was: ", round(t2-t1, 4))
    print("Total Fails were: ", tf)
    thetime2 = time.time()
    print('\n',"Complete total time taken: ", round(thetime2 - thetime, 4))

main()