# New Pandas practice, 2023-1-7 date  
# Jennifer E Yoon author  

import pandas as pd  

# readin dataframe, create offline .csv file  
f = ./"data.csv"
df = pd.read_csv(f)
df.head()
df.describe()

