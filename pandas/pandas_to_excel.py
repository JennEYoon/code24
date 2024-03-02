# Practice, Pandas and Excel file format   

import pandas as pd  
import ExcelWriter as writer  

data = {('employees': 'Mary', 'Hank', 'Jennifer', 'Joo-In'), ('hire_date': '2000', '1998', '1992', '2012')}
df1 = pd.DataFrame(data)

print(df.head())
file ='/contents/salary.xls.sheet1')
df1.to_excel(writer, file)


salary = {'Mary': 102, 'Joo-In: 56, 'Hank: '115', 'Jennifer': 220}
df2 = pd.DataFrame(salary, colnames=('salary')).T  

df3 = pd.merge(df1, df2)  

# Save df1 to Sheet1, df2 to Sheet2  



