

import pandas as pd

data = [1, 2, 3]

# Creating series from python list
series = pd.Series(data)
print(series)

# locating the value
print(series[0])

# Changing the index
series = pd.Series(data,index=[1,2,3])
print(series)

