import matplotlib  
import matplotlib.pyplot as plt  
import numpy as np
import pandas as pd  
from pandas import Series, DataFrame  
import seaborn as sns  

df = pd.read_csv('file1.csv')  
print(df.head())

df.to_csv('file2.csv')
df.to_excel('file.xlsx', sheet_name='Sheet1')  

