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
        return result

    def add_subscriber(self, name, mail):
        self.subscribers[name] = mail
        return self.subscribers

if __name__ == '__main__':
    main()
