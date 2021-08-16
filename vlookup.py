import pandas as pd

# read csv data
df1 = pd.read_csv('path of the table to be looked up from.csv')
df2 = pd.read_csv('path of the table that requires look-up.csv')

type_join = pd.merge(df1,
                     df2,
                     on='lookup field',
                     how='type of join (inner, outer, left, right)')
type_join.to_csv("name of destination csv.csv",index = False)
