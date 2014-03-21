import sys
from mailList import MailList
from subprocess import call

def main():
    #mail = MailList()
    while True:
        command = input(">")
        command = command.split()
        
        if command[0] == "help":
            call("py help.py",shell = True)
        if command[0] == "show_lists":
            pass






        if command[0] == "exit":
            break




if __name__ == '__main__':
    main()