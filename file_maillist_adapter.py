from mailList import MailList
from maillist_file_adapter import MailListFileAdapter


class FileMailListAdapter():
    """docstring for FileMailListAdapter"""
    def __init__(self, filename):
        self.__mail = MailList(filename)

    def make_subscribers(self):
        file = open(self.__mail.getName(), "r")
        contents = file.read()
        file.close()
        contents = list(map(lambda x: x.split(), contents.split('\n')))
        # contents = list(map(lambda x: (x[0], x[2]), contents))
        # self.__mail.subscribers = contents
        # return contents
        dict_ = {}
        for item in contents:
            dict_[item[0]] = item[2]
        return dict_

    def getMail(self):
        self.__mail.subscribers = self.make_subscribers()
        return self.__mail


def main():
    f = FileMailListAdapter("Otbor_Pochivka")
    mail = f.getMail()
    print (mail.get_subscribers())
    mail.add_subscriber("bla", "bla@bla")
    mail.add_subscriber("lqlq", "lqlq@lqlq")

    print (mail.get_subscribers())

    a = MailListFileAdapter(mail)
    a.save()

if __name__ == '__main__':
    main()
