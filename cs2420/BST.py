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
    
    def getAge(self):
        return self.mAge

class Node: #Node class for the Binary Search Tree class
    def __init__(self, item):
        self.item = item
        self.L = None
        self.R = None

class BST: #Binary Search Tree function
    def __init__(self):
        self.root = None
        self.size = 0

    def Exists(self, item): #checks if an item is in the search tree
        return self.ExistsR(item, self.root)
        
    def ExistsR(self, item, current): #recursion for the Exists command
        if current is None:
            return False
        elif current.item == item:
            return True
        elif item < current.item:
            return self.ExistsR(item, current.L)
        elif item > current.item:
            return self.ExistsR(item, current.R)

    def Retrieve(self, item): #returns an existing item in the search tree
        return self.RetrieveR(item, self.root)
        
    def RetrieveR(self, item, current): #recursion for the Retrieve command
        if current is None:
            return None
        elif current.item == item:
            return current.item
        elif item < current.item:
            return self.RetrieveR(item, current.L)
        elif item > current.item:
            return self.RetrieveR(item, current.R)

    def Insert(self, item): #inserts a Node into the tree
        if self.Exists(item):
            return False
        n = Node(item)
        self.root = self.InsertR(n, self.root)
        self.size += 1
        return True

    def InsertR(self, n, current): #recursion for the insert command
        if current is None:
            current = n
        elif n.item < current.item:
            current.L = self.InsertR(n, current.L)
        else:
            current.R = self.InsertR(n, current.R)
        return current

    def Delete(self, item): #Deletes a given item if it exists
        if not self.Exists(item):
            return False
        self.root = self.DeleteR(item, self.root)
        return True
    
    def DeleteR(self, item, current): #Recursion for the delete method
        if item < current.item:
            current.L = self.DeleteR(item, current.L)
        elif item > current.item:
            current.R = self.DeleteR(item, current.R)
        else:
            if not current.L and not current.R: #leaf case
                current = None
            elif not current.L and current.R: #one child right
                current = current.R
            elif current.L and not current.R: #one child left
                current = current.L
            else: #two childs
                s = current.R
                while s.L:
                    s = s.L
                current.item = s.item
                current.R = self.DeleteR(s.item, current.R)

        return current

    def Size(self): #return the size of the search tree
        # return self.size
        return self.SizeR(self.root)
    
    def SizeR(self, current): #recursion for the size function
        if current is None:
            return 0
        return 1 + self.SizeR(current.L) + self.SizeR(current.R)
    
    def __iter__(self):
        yield from self.IterRecursive(self.root)

    def IterRecursive(self, current): #recursion for the iter method
        if current is not None:
            yield from self.IterRecursive(current.L)
            yield current.item
            yield from self.IterRecursive(current.R)

def main():
    thetime = time.time()
    #Insert

    print('\n', '\t', 'Insert', '\n')
    c = BST()
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
        if s2 is not None:
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