import os
import pandas as pd

all_data = pd.read_excel('JL_agg.xlsx')

df = pd.read_excel("JL_agg.xlsx")
## print(df)

## Handling Dup Count = 0
#df0  = df[df['Dup Count'] == 0]
#ofn = "Ph0.xlsx"
#df0.to_excel(ofn,index=False)

## Handling Dup Count >= 2

#df2  = df[df['Dup Count'] >= 2]
#ofn = "Ph2.xlsx"
#df2.to_excel(ofn,index=False)

## Handling Dup Count = 1

df1  = df[df['Dup Count'] == 1]
ofn = "Ph1.xlsx"
df1.to_excel(ofn,index=False)
