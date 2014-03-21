import sys
from mailList import MailList
from subprocess import call
from glob import glob

def main():
    #mail = MailList()
    while True:
        command = input(">")
        command = command.split()
        
        if command[0] == "help":
            call("py help.py",shell = True)
        
        if command[0] == "show_lists":
            lists = glob("*.txt")
            lists.remove("help.txt")
            for i in range(len(lists)):
                lists[i] = lists[i][0:len(lists[i])-4]
                print("[" + str(i+1) +"]"+ " - " + lists[i])
        
                






        if command[0] == "exit":
            break




if __name__ == '__main__':
    main()