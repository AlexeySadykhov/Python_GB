import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

unique = set(data['whoAmI'])
one_hot = data['whoAmI'].map(lambda x: [1 if x == item else 0 for item in unique])
print(pd.DataFrame.from_records(data=one_hot, columns=unique))
