# test/my_mod_test.py

import unittest
from lambdata_mahoryu.my_mod import enlarge
from lambdata_mahoryu.my_mod import double_data
import pandas as pd


class TestMyModMethods(unittest.TestCase):

    def test_enlarge(self):
        self.assertEqual(enlarge(5), 500)

    def test_double_data(self):
        df = pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6], "date": [
            "1/2/2018", "6/7/2019", "2/8/2007"]})
        self.assertEqual(df.shape[0] * 2, double_data(df).shape[0])


if __name__ == '__main__':
    unittest.main()
