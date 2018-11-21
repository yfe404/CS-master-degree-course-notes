import re
import numpy as np
import pandas as pd

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori


def create_weather_df():
    attributes = []
    data = []

    data_start = False

    with open("./data/weather.nominal.arff", "r") as f:
        for line in f.readlines():
            line = line.strip()
            line = line.replace("TRUE", "windy")
            line = line.replace("FALSE", "not_windy")
            line = re.sub(r"yes$", "play", line)
            line = re.sub(r"no$", "no_play", line)
            
            if data_start:
                data.append(line.split(","))
                continue
            if line.startswith("@attribute"):
                attributes.append(line.split(" ")[1])
            if line.startswith("@data"):
                data_start = True   


    te = TransactionEncoder()
    te_ary = te.fit(data).transform(data)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    df.to_csv("./data/weather.nominal.csv", index=False)
    


def create_supermarket_df():
    attributes = []
    data = []

    data_start = False

    with open("./data/supermarket.arff", "r") as f:
        for line in f.readlines():
            line = line.strip()       
            if data_start:
                data.append(line.split(","))
                continue
            if line.startswith("@attribute"):
                attributes.append(line.split(" ")[1].replace("'",""))
            if line.startswith("@data"):
                data_start = True   

    df = pd.DataFrame(data, columns=attributes)
    df = df.replace({'?': 0}, regex=False)
    df = df.replace({'t': 1}, regex=False)
    df_total = df['total'].str.get_dummies()
    df = pd.concat([df, df_total], axis=1)
    df = df.drop(['total'], axis=1)
    df.to_csv("./data/supermarket.csv", index=False)
    

if __name__ == "__main__":
    create_weather_df()
    create_supermarket_df()
