# test/assignment_test.py

import unittest
from lambdata_mahoryu.assignment import CustomFrame

class TestCustomFrameMethods(unittest.TestCase):

    def test_add_state_names(self):
        custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
        # assert "State_Names" should be a column
        self.assertTrue("State_Names" not in list(custom_df))
        custom_df.add_state_names()
        self.assertTrue("State_Names" in list(custom_df))
        # assert that first row, name is "California" in df
        self.assertEqual((custom_df["State_Names"][0], "California"))
        self.assertEqual((custom_df["abbrev"][0], "CA"))

if __name__ == '__main__':
    unittest.main()
