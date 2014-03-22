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

    def add_subscriber(self, name, mail):
        self.subscribers[name] = mail
        return sorted(self.subscribers)

    def update_subscriber(self, name, new_name, new_mail):
        del self.subscribers[name]
        self.subscribers[new_name] = new_mail
        return sorted(self.subscribers)
