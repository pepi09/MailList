import sys
from mailList import MailList
from subprocess import call
from glob import glob
from maillist_file_adapter import MailListFileAdapter

def main():
    #mail = MailList()
    while True:
        command = input(">")
        command = command.split()
        
        if command[0] == "help":
            call("py help.py",shell = True)
        
        if command[0] == "show_lists":
            lists = get_lists()
            for i in range(len(lists)):
                lists[i] = lists[i][0:len(lists[i])-4]
                print("[" + str(i+1) +"]"+ " - " + lists[i])

        if command[0] == "show_list":
            lists = get_lists()
            i = int(command[1])
            l = open("%s" %(lists[i-1]),"r")
            list = l.read()
            list = list.split('\n')
            for i in range(len(list)):
                print("[" + str(i+1) +"]"+ " " + list[i])

        if command[0] == "add":
            lists = get_lists()
            i = int(command[1])
           # list[i] = HackBg
            name = input("Name: ")
            email = input("Email ")
            subscribers = create_subscribers(lists[i-1])
            mail = MailList("%s" %(lists[i-1]),subscribers)
            mail.add_subscriber(name,email)
            adapter = MailListFileAdapter(mail)
            adapter.save_for_add(name,email)
        
                






        if command[0] == "exit":
            break



def get_lists():
    lists = glob("*.txt")
    lists.remove("help.txt")
    return lists


def create_subscribers(name):
    file = open(name,"r")
    subscribers = file.read()
    subscribers = subscribers.split('\n')
    subscribers = list(map(lambda x: x.split(), subscribers))
    sub = {}
    for i in range(len(subscribers)):
        sub[subscribers[i][0]] = subscribers[i][2]
    return sub

# def main():
#     create_subscribers("HackBg")
if __name__ == '__main__':
    main()