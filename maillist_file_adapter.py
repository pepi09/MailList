from mailList import MailList


class MailListFileAdapter():
    """docstring for MailListFileAdapter"""
    def __init__(self, mail_list):
            self.__mail_list = mail_list

    def get_file_name(self):
        return self.__mail_list.getName().replace(" ", "_")

    def prepare_for_save(self):
        subscribers = self.__mail_list.get_subscribers()
        subscribers = map(lambda x: "{} - {}".format(x[0], x[1]), subscribers)

        return sorted(subscribers)

    def save(self):
        file_for_save = open(self.get_file_name(), "w")
        contents = "\n".join(self.prepare_for_save())

        file_for_save.write(contents)
        file_for_save.close()


def main():
    _list = MailList("Otbor Pochivka")
    _list.add_subscriber("Tsveta", "tsveta@tsveta")
    _list.add_subscriber("Pepa", "pepa@pepa")

    m = MailListFileAdapter(_list)

    print (m.get_file_name())
    m.save()

if __name__ == '__main__':
    main()
