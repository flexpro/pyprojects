import os
import pandas as pd
##### Merging 22 csvs of GB Leads into a single sheet

df = pd.read_csv("./Sales_Data/JetLeads/GB1.csv")

all_cluster_data = pd.DataFrame()

files = [file for file in os.listdir('./Sales_Data/JetLeads')]

for file in files:
    df = pd.read_csv("./Sales_Data/JetLeads/"+file)
    all_cluster_data = pd.concat([all_cluster_data,df])

all_cluster_data.to_csv("all_cluster_data.csv",index = False)

all_data = pd.read_csv('all_cluster_data.csv')

df = pd.read_csv("all_cluster_data.csv")
print(df)