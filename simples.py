#!/usr/bin/python3
import subprocess
from subprocess import run

def testssh():
    user=input("Please give me a user: ")
    ipad=input("Please give me an ip: ")
    command="ssh "+user+"@"+ipad +' "df"'
    run(command, shell=True)

def inputtest():
    print("Please give the logon credentials for the remote host: ")
    sshuser=input("User: ")
    sship=input("IP: ")
    user=input("give another user: ")
    logon="ssh "+sshuser+"@"+sship
    thing=logon+" 'lastlog -u "+user+"'"
    run(thing, shell=True)
def thing():
    thin=run("echo $TERM", shell=True)
    print(thin)


def main():
    thing()

if __name__ == "__main__":
    main()
