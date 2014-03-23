from mailList import MailList
from subprocess import call
from glob import glob
from maillist_file_adapter import MailListFileAdapter
from file_maillist_adapter import FileMailListAdapter


def main():
    print("Hello Stranger! This is a cutting-edge, console-based mail-list! Type help, to see a list of commands.")
    while True:
        command = input(">")
        command = command.split()

        if command[0] == "help":
            call("python help.py", shell=True)

        if command[0] == "show_lists":
            lists = get_lists()
            if not len(lists) == 0:
                for i in range(len(lists)):
                    lists[i] = lists[i][0:len(lists[i]) - 4] #zashto 4
                    print("[" + str(i + 1) + "]" + " - " + lists[i])
            else:
                print ("There are no email lists!")

        if command[0] == "show_list":
            """trqbva da se oprawim da ne pokazwa [1] kogato nqma email"""
            lists = get_lists()
            i = int(command[1])
            try:
                l = open("%s" % (lists[i - 1]), "r")
            except IndexError:
                print("List with unique identifier %s was not found!" %(i))
            else:
                list = l.read()
                list = list.split('\n')
                if not list == ['']:
                    for i in range(len(list)):
                        print("[" + str(i + 1) + "]" + " " + list[i])
                else:
                    print ("The mail list is empty!")

        if command[0] == "add":
            lists = get_lists()
            i = int(command[1]) - 1

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
            if i <= len(lists):
                f = FileMailListAdapter(lists[i - 1])
                mail = f.getMail()
                subscribers = mail.get_subscribers()
                if j <= len(subscribers):
                    old_name = subscribers[j - 1][0]

                    name = input("enter new name> ")
                    email = input("enter new email> ")

                    if name == "":
                        mail.update_subscriber(old_name, old_name, email)
                    else:
                        mail.update_subscriber(old_name, name, email)
                    adapter = MailListFileAdapter(mail)
                    adapter.save()
                else:
                    print ("There is not " + str(j) + " subscriber in\
                        the mail")
            else:
                print("There is not " + str(i) + "the mail list")

        if command[0] == "remove_subscriber":
            lists = get_lists()
            i = int(command[1])
            j = int(command[2])

            if i <= len(lists):
                f = FileMailListAdapter(lists[i - 1])
                mail = f.getMail()
                subscribers = mail.get_subscribers()
                if j <= len(subscribers):
                    mail.remove_subscriber(subscribers[j - 1][0])

                    adapter = MailListFileAdapter(mail)
                    adapter.save()
                else:
                    print ("There is not " + str(j) + "the subscriber in the mail")
            else:
                print("There is not " + str(i) + "the mail list")

        if command[0] == "exit":
            break

        if command[0] == "create":
            lists = get_lists()
            if command[1] + ".txt" in lists:
                print ("A list with name <" + command[1] + "> already exists!")
            else:
                mail = MailList(command[1] + ".txt")
                f = MailListFileAdapter(mail)
                f.save()
                print ("New list <" + command[1] + "> was created")

        if command[0] == "update":
            lists = get_lists()
            i = int(command[1])
            if i > len(lists):
                print("List with unique identifier <" + str(i) + "> \
was not found")
            else:
                f = FileMailListAdapter(lists[i - 1])
                mail = f.getMail()
                mail.set_name(command[2])

                adapter = MailListFileAdapter(mail)
                adapter.save()
                print("Updated " + lists[i - 1] + " to " + command[2])

        if command[0] == "delete":
            lists = get_lists()
            i = int(command[1]) - 1
            if i <= len(lists):
                print ("Are you sure you want to delete " + lists[i])
                choice = input("(Y/N)>")
                if choice == 'Y':
                    if i <= len(lists):
                        call("rm " + lists[i], shell=True)
                else:
                    print("You crazy bastard. Stop playing with fire!")
            else:
                print("List with unique identifier <" + str(i) + "> \
was not found.")

        if command[0] == "search_email":
            lists = get_lists()
            result = []
            for i in range(len(lists)):
                f = FileMailListAdapter(lists[i])
                mail = f.getMail()
                subscribers = mail.get_subscribers()
                for j in range(len(subscribers)):
                    if command[1] == subscribers[j][1]:
                        result.append(lists[i][:len(lists[i]) - 4:])
            if len(result) == 0:
                print("<" + command[1] + "> was not found in the \
current mailing lists.")
            else:
                for k in range(len(result)):
                    print("[" + str(k + 1) + "] " + result[k])


def get_lists():
    lists = glob("*.txt")
    lists.remove("help.txt")
    return lists

# def main():
#     create_subscribers("HackBg")
if __name__ == '__main__':
    main()
