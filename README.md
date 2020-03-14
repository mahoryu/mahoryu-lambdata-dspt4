# lambdata_mahoryu

Install with: "pip install -i https://test.pypi.org/simple/ lambdata-mahoryu"

Test package used for class to try out uploading to test PyPi to make available.

Functions: 

    -enlarge(n)
        Multiplies a number by 100
        :param n: (numeric) the number to enlarge
        :return: the enlarged number (numeric)
    
    -split_date(X, date_column)
        Splits the date column of a data frame into month, day, and year
        :param X: (DataFrame) the data frame itself 
        :param date_column: (string) the name of the column that needs to be split.
        :return: (DataFrame) the new data frame with the new columns replacing the old.
   
    -double_data(X)
        Doubles the data in the data frame
        :param X: (DataFrame) the data frame that you want to double
        :return: (DataFrame) the new data frame with all values added as new rows.