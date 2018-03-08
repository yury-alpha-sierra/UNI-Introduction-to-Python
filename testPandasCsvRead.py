import pandas as pd

df1 = pd.read_csv('Economy Letters.csv', index_col=None, header=0)
print(df1._info_axis)
