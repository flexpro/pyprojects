import pandas as pd

data = pd.read_csv("/Users/vedprakashverma/PycharmProjects/Gryff_in/Sales_Data/HPPL/Companies owner database 2021.csv")
df = data.dropna(axis = 0, how = 'any') # axis = 0 to get rid of rows, columns otherwise. if some entries of a row are blank, use 'any' instead of 'all'
df.to_csv("Companies owner database 2021 Sheet 2.csv")
