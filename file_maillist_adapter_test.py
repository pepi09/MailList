import unittest
from file_maillist_adapter import FileMailListAdapter
from subprocess import call


class FileMailListAdapterTest(unittest.TestCase):
    """docstring for FileMailListAdapterTest"""

    def setUp(self):
        file = open("test.txt", "w")
        contents = "Pepa - pepa@pepa"
        file.write(contents)
        file.close()
        self.obj = FileMailListAdapter("test.txt")

    def test_make_subscribers(self):
        expected = {}
        expected["Pepa"] = "pepa@pepa"
        self.assertEqual(expected, self.obj.make_subscribers())

    def tearDown(self):
        call("rm " + "test.txt", shell=True)

if __name__ == '__main__':
    unittest.main()
