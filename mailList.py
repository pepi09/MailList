class MailList():
    """docstring for MailList"""
    def __init__(self, name):
        self.__name = name
        self.subscribers = {}

    def getName(self):
        return self.__name

    def get_subscribers(self):
        result = []
        for name in self.subscribers:
            result.append((name, self.subscribers[name]))
        return sorted(result)

    def get_emails(self):
        emails = []
        for name in self.subscribers:
            emails.append(self.subscribers[name])
        return emails

    def add_subscriber(self, name, mail):
        self.subscribers[name] = mail
        return sorted(self.subscribers)

    def update_subscriber(self, name, new_name, new_mail):
        del self.subscribers[name]
        self.subscribers[new_name] = new_mail
        return sorted(self.subscribers)

    def remove_subscriber(self, name):
        del self.subscribers[name]
        return sorted(self.subscribers)

    def set_name(self, name):
        self.__name = name
