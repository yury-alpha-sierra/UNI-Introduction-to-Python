import pandas as pd

try:
    df1 = pd.read_csv('Economy Letters.csv', index_col=None, header=0)
    print(df1)
except FileNotFoundError:
    print('file "Economy Letters.csv" is not in the current directory or does not exsit')