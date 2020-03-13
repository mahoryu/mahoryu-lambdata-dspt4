# lambdata_mahoryu/my_mod.py

import pandas as pd

def enlarge(n):
    
    '''
    Multiplies a number by 100
    :param n: (numeric) the number to enlarge
    :return: the enlarged number (numeric)
    '''
    return n * 100

def split_date(X, date_column):
    X.copy()
    X[date_column] = pd.to_datetime(X[date_column])
    X['Month'] = X[date_column].dt.month
    X['Day'] = X[date_column].dt.day
    X['Year'] = X[date_column].dt.year
    X = X.drop(columns=date_column)
    return X

def double_data(X):
    X.copy()
    X = X.append(X, ignore_index=True)
    return X

if __name__ == "__main__":
    # only if run from the command line, invoke the following,
    # otherwise don't

    print("JUNK")
    print("GLOBAL SCOPE")

    y = float(input("Please input a number to enlarge"))
    print(enlarge(y))