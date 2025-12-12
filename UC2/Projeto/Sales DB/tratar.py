import pandas as pd

df = pd.read_csv("Online_Sales_Data.csv")
#df = df.replace(" ", "_", regex=True)

#for linha in df:
    #df.replace (" ","_")

df.columns = df.columns.str.replace(" ", "_")
