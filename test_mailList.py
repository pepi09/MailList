import unittest
from mailList import MailList


class TestMailList(unittest.TestCase):

    def setUp(self):
        self.obj = MailList("someName")
        self.obj.add_subscriber("Pepa", "pepa@pepa")

    def test_atributes(self):
        self.assertEqual("someName", self.obj.getName())

    def test_add_subscriber(self):
        self.obj.add_subscriber("Tsveta", "tsveta@tsveta")
        expected = [("Pepa", "pepa@pepa"), ("Tsveta", "tsveta@tsveta")]
        self.assertEqual(expected, self.obj.get_subscribers())

    def test_get_subscribers(self):
        self.obj.add_subscriber("Tsveta", "tsveta@tsveta")
        expected = [("Pepa", "pepa@pepa"), ("Tsveta", "tsveta@tsveta")]
        self.assertEqual(expected, self.obj.get_subscribers())


if __name__ == '__main__':
    unittest.main()
