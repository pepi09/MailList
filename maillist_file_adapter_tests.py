import unittest
from maillist_file_adapter import MailListFileAdapter
from mailList import MailList


class MailListFileAdapterTest(unittest.TestCase):
    """docstring for MailListFileAdapterTest"""

    def setUp(self):
        self.obj = MailList("Otbor Pochivka")
        self.obj.add_subscriber("Tsveta", "tsveta@tsveta")
        self.obj.add_subscriber("Pepa", "pepa@pepa")

        self.m = MailListFileAdapter(self.obj)

    def test_get_file_name(self):
        _str = self.m.get_file_name()
        self.assertEqual("Otbor_Pochivka", _str)

    def test_prepare_for_save(self):
        expected = sorted(["Tsveta - tsveta@tsveta", "Pepa - pepa@pepa"])

        self.assertEqual(expected, self.m.prepare_for_save())

if __name__ == '__main__':
    unittest.main()
