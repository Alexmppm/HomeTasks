# | Задание 44 |
# | --- |
# | В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
df = pd.DataFrame({'whoAmI': lst})
print(df.head())


for k in list(df.whoAmI.unique ()):
    df[k] = int(0)
    df.loc[df['whoAmI'] == k, k] = 1

df.pop('whoAmI')
print(df)
