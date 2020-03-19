# test/my_mod.py

import unittest
from lambdata_mahoryu.my_mod import enlarge

class TestMyModMethods(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(5), 500)


if __name__ == '__main__':
    unittest.main()
