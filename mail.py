from mailList import MailList
from subprocess import call
from glob import glob
from maillist_file_adapter import MailListFileAdapter
from file_maillist_adapter import FileMailListAdapter


def main():
    #mail = MailList()
    while True:
        command = input(">")
        command = command.split()

        if command[0] == "help":
            call("py help.py", shell=True)

        if command[0] == "show_lists":
            lists = get_lists()
            for i in range(len(lists)):
                lists[i] = lists[i][0:len(lists[i]) - 4]
                print("[" + str(i + 1) + "]" + " - " + lists[i])

        if command[0] == "show_list":
            lists = get_lists()
            i = int(command[1])
            l = open("%s" % (lists[i - 1]), "r")
            list = l.read()
            list = list.split('\n')
            for i in range(len(list)):
                print("[" + str(i + 1) + "]" + " " + list[i])

        if command[0] == "add":
            lists = get_lists()
            i = int(command[1]) - 1
            print (lists[i])
            name = input("Name: ")
            email = input("Email ")
            f = FileMailListAdapter(lists[i])
            mail = f.getMail()
            mail.add_subscriber(name, email)
            adapter = MailListFileAdapter(mail)
            adapter.save()

        if command[0] == "update_subscriber":
            lists = get_lists()
            i = int(command[1])
            j = int(command[2])

            print (str(i) + " " + str(j))
            print (lists[i - 1])

            f = FileMailListAdapter(lists[i - 1])
            mail = f.getMail()
            subscribers = mail.get_subscribers()
            old_name = subscribers[j - 1][0]
            print (subscribers)
            print (old_name)
            name = input("enter new name> ")
            email = input("enter new email> ")

            if name == "":
                mail.update_subscriber(old_name, old_name, email)
            else:
                mail.update_subscriber(old_name, name, email)
            adapter = MailListFileAdapter(mail)
            adapter.save()



        if command[0] == "exit":
            break


def get_lists():
    lists = glob("*.txt")
    lists.remove("help.txt")
    return lists

# def main():
#     create_subscribers("HackBg")
if __name__ == '__main__':
    main()
