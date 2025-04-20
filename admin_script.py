#!/usr/bin/python3
import subprocess
from subprocess import run

def usage():
    print("Invalid input please use number 1-5")

def menu():
    print('Usage:')
    print("     1: prints list of users")
    print("     2: given a user it prints when user last logged in")
    print("     3: prints list of active processes")
    print("     4: gives disk usage data")
    print("     5: quit")

def one(x):
    logon=x
    print("Gathering users...")
    print("\n")
    command = "rm ./usersnames.txt 2>/dev/null"
    run(command, shell=True)
    COMMAND = logon+" 'who' > usersnames.txt"
    run(COMMAND, shell=True)
    thislist=[]
    names=open("./usersnames.txt")
    for line in names:
        thing = line.split(' ', 1)
        thislist.append(thing[0])
        thislist.sort()
    for line in thislist:
        print(line)
    names.close()
    run(command, shell=True)
    numb=str(len(thislist))
    print('Total users: '+numb)
    print("\n")


def two(x):
    logon=x
    print("User Login")
    user = input("Please input a user: ")
    print("\n")
    COMMAND=logon+" 'lastlog -u "+user+"'"
    run(COMMAND, shell=True)
    print("\n")

def three(x):
    print("\n")
    print("Gathering processes...")
    logon=x
    command=logon+" 'ps aux'"
    run(command, shell=True)
    print("\n")

def four(x):
    logon=x
    print("Gathering disk information...")
    print("\n")
    command=logon+" 'df'"
    run(command, shell=True)
    print("\n")
    
def main():
    print("Please give the logon credentials for the remote host: ")
    sshuser=input("User: ")
    sship=input("IP: ")
    logon="ssh "+sshuser+"@"+sship
    while True:
        menu()
        x=input("Please input a number: ")
        if x not in "12345":     
            usage()
        elif x == "1":
            one(logon)
        elif x == "2":
            two(logon)
        elif x == "3":
            three(logon)
        elif x == "4":
            four(logon)
        elif x == "5":
            print("Quiting...")
            break 

if __name__ == "__main__":
    main()
