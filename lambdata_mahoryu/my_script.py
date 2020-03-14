# lambdata_mahoryu/my_script.py

import pandas as pd
print("Happy Tuesday Night")

from lambdata_mahoryu.my_mod import enlarge
from lambdata_mahoryu.my_mod import split_date
from lambdata_mahoryu.my_mod import double_data

df = pd.DataFrame({"x":[1,2,3],"y":[4,5,6],"date":["1/2/2018","6/7/2019","2/8/2007"]})
print(df.head())

x = 5
print ("ENLARGED",x, "TO", enlarge(x))

print()
print(split_date(df,"date"))

print()
print(double_data(df))