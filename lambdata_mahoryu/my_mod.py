# lambdata_mahoryu/my_mod.py

def enlarge(n):
    return n * 100

def split_date(X,date_column):
    X.copy()
    X[date_column] = pd.to_datetime(X[date_column])
    X['Year'] = X[date_column].dt.year
    X['Month'] = X[date_column].dt.month
    X['Day'] = X[date_column].dt.day
    X = X.drop(columns=date_column)
    return X


if __name__ == "__main__":
    # only if run from the command line, invoke the following,
    # otherwise don't

    print("JUNK")
    print("GLOBAL SCOPE")

    y = float(input("Please input a number to enlarge"))
    print(enlarge(y))