import unittest
import time
from ones import OnesTestRunner


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("FOO", 'FOO')

    def test_isupper(self):
        self.assertTrue("FOO","FOO")


if __name__ == '__main__':
    runner = OnesTestRunner()
    unittest.main()