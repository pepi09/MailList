import unittest
from mailList import MailList


class TestMailList(unittest.TestCase):

    def setUp(self):
        self.obj = MailList("someName")

    def test_atributes(self):
        self.assertEqual("someName", self.obj.getName())

if __name__ == '__main__':
    unittest.main()
