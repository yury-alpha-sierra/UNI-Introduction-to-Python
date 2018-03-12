import pandas as pd
df=pd.read_csv('.//data//Economy Letters Price Guide ($).csv', delimiter=',',header=None)
# print(df.shape[0:])
# print(df.ndim)

print(df.columns[0:])
print(df.index)
# print(df.data[0:])