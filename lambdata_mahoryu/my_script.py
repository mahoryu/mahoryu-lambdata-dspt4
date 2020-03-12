# lambdata_mahoryu/my_script.py

import pandas
print("Happy Tuesday Night")

from lambdata_mahoryu.my_mod import enlarge

df = pandas.DataFrame({"x":[1,2,3],"y":[4,5,6]})
print(df.head())

x = 5
print ("ENLARGED",x, "TO", enlarge(x))