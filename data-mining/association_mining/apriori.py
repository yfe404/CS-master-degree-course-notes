# coding: utf-8

import pandas as pd 
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori


df_weather = pd.read_csv("./data/weather.nominal.csv") 

frequent_itemsets = apriori(df_weather, min_support=0.4, use_colnames=True)

frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))


#frequent_itemsets[ frequent_itemsets['itemsets'] == {'fruit', 'vegetables'} ]
#frequent_itemsets[ frequent_itemsets['itemsets'] == {'fruit', 'vegetables'} ]

items = frequent_itemsets[ (frequent_itemsets['length'] >= 2) &
                   (frequent_itemsets['support'] >= 0.3) ]

#frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)
#frequent_itemsets = apriori(df_weather, min_support=0.4, use_colnames=True)
print(items)

