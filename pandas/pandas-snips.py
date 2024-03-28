import matplotlib  
import matplotlib.pyplot as plt  
import numpy as np
import pandas as pd  
from pandas import Series, DataFrame, ExcelWriter     
import seaborn as sns  

df = pd.read_csv('file1.csv')  
print(df.head())

df.to_csv('file2.csv')
df.to_excel('file.xlsx', sheet_name='Sheet1')   

# or import ExcelWriter, context window with open   
from pandas import ExcelWriter   
# worked on Colab without importing ExcelWriter   

with ExcelWriter('myexcel.xlsx') as f:   
    df1.to_excel(f, sheet_name="sheet1")  
    df2.to_excel(f, sheet_name='sheet2")   


