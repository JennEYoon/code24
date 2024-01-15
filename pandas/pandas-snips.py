import pandas as pd  
import numpy as np

df = pd.read_csv('file1.csv')  
print(df.head())

df.to_csv('file2.csv')
