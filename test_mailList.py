import unittest
from mailList import MailList


class TestMailList(unittest.TestCase):

    def setUp(self):
        self.obj = MailList("someName")
        self.obj.add_subscriber("Pepa", "pepa@pepa")
        self.obj.add_subscriber("Tsveta", "tsveta@tsveta")

    def test_atributes(self):
        self.assertEqual("someName", self.obj.getName())

    def test_add_subscriber(self):
        _dict = {}
        _dict["Pepa"] = "pepa@pepa"
        _dict["Tsveta"] = "tsveta@tsveta"
        self.assertEqual(_dict, self.obj.getSubscribers())


if __name__ == '__main__':
    unittest.main()
