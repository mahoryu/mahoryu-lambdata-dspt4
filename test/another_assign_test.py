# test/another_assign_test.py


from lambdata_mahoryu.assignment import CustomFrame


def test_add_state_names():
    custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    # assert "State_Names" should be a column
    assert "State_Names" not in list(custom_df.columns)
    custom_df.add_state_names()
    assert "State_Names" in list(custom_df.columns)
    # assert that first row, name is "California" in df
    assert custom_df["State_Names"][0] == "California"
    assert custom_df["abbrev"][0] == "CA"
