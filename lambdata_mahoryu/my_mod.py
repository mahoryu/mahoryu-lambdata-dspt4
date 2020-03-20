# lambdata_mahoryu/my_mod.py

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


if __name__ == "__main__":
    print("Happy Tuesday Night")

    df = pd.DataFrame({"x": [1, 2, 3, 5], "y": [4, 5, 6, 8], "date": [
        "1/2/2018", "6/7/2019", "2/8/2007", "2/8/2007"]})
    print(df.shape[0])

    x = 5
    print("ENLARGED", x, "TO", enlarge(x))

    print()
    print(split_date(df, "date"))

    print()
    print(double_data(df))
