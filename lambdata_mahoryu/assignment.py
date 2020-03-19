import pandas as pd


def enlarge(n):
    """
    Multiplies a number by 100
    :param n: (numeric) the number to enlarge
    :return: the enlarged number (numeric)
    """
    return n * 100


def split_date(X, date_column):
    """
    Splits the date column of a data frame into month, day, and year
    :param X: (DataFrame) the data frame itself
    :param date_column: (string) the name of the column that needs to be split.
    :return: (DataFrame) the new data frame with the new columns replacing the old.
    """
    X.copy()
    X[date_column] = pd.to_datetime(X[date_column])
    X['Month'] = X[date_column].dt.month
    X['Day'] = X[date_column].dt.day
    X['Year'] = X[date_column].dt.year
    X = X.drop(columns=date_column)
    return X


def double_data(X):
    """
    Doubles the data in the data frame
    :param X: (DataFrame) the data frame that you want to double
    :return: (DataFrame) the new data frame with all values added as new rows.
    """
    X.copy()
    X = X.append(X, ignore_index=True)
    return X

# Functional approach
# def add_state_names(X, state_column):
#     """
#     Adds corresponding state names to a data frame
#     :param X: the dataframe
#     :param state_column: (string) the column name with the state abbreviations.
#     :return: a new df with the new column
#     """
#
#     # a map used for the conversion
#     names_map = {
#         "CA": "California",
#         "CT": "Connecticut",
#         "CO": "Colorado",
#         "TX": "Texas",
#         "DC": "Washington D.C.",
#         "OH": "Ohio",
#         "MI": "Missouri",
#         "ID": "Idaho",
#         "NY": "New York",
#         "WA": "Washington",
#     }
#     # make a new data frame
#     X = X.copy()
#
#     X["Full State Name"] = X[state_column].map(names_map)
#
#     return X

# # OOP approach
#
# class DataProcessor():
#     def __init__(self, df):
#         """
#         :param df: df
#         """
#         self.df = df
#
#     def add_state_names(self):
#         """
#         Adds corresponding state names to a data frame
#         :param X: the dataframe
#         :param state_column: (string) the column name with the state abbreviations.
#         :return: a new df with the new column
#         """
#
#         # a map used for the conversion
#         names_map = {
#             "CA": "California",
#             "CT": "Connecticut",
#             "CO": "Colorado",
#             "TX": "Texas",
#             "DC": "Washington D.C.",
#             "OH": "Ohio",
#             "MI": "Missouri",
#             "ID": "Idaho",
#             "NY": "New York",
#             "WA": "Washington",
#         }
#         self.df["State Names"] = self.df["abbrev"].map(names_map)

# OOP approach with inheritance

class CustomFrame(pd.DataFrame):
    """
    Notes on how this works
    """
    def add_state_names(self):
        """
        Adds corresponding state names to a data frame
        :param X: the dataframe
        :param state_column: (string) the column name with the state abbreviations.
        :return: a new df with the new column
        """

        # a map used for the conversion
        names_map = {
            "CA": "California",
            "CT": "Connecticut",
            "CO": "Colorado",
            "TX": "Texas",
            "DC": "Washington D.C.",
            "OH": "Ohio",
            "MI": "Missouri",
            "ID": "Idaho",
            "NY": "New York",
            "WA": "Washington",
        }
        self["State_Names"] = self["abbrev"].map(names_map)

if __name__ == "__main__":

    df1 = pd.DataFrame({"abbrev":["CA","CT","CO","TX","DC"]})
    # print(df1.head())

    # new_df = add_state_names(df, "abbrev")
    # print(new_df.head())
    # processor = DataProcessor(df1)
    # processor.add_state_names()
    # print(processor.df.head())
    #
    # df2 = pd.DataFrame({"abbrev": ["OH", "MI", "ID", "NY", "WA"]})
    # # print(df2.head())
    #
    # # new_df = add_state_names(df2, "abbrev")
    # # print(new_df.head())
    # processor = DataProcessor(df2)
    # processor.add_state_names()
    # print(processor.df.head())

    custom_df = CustomFrame({"abbrev":["CA","CT","CO","TX","DC"]})
    print(custom_df.head())
    custom_df.add_state_names()
    print(custom_df.head())