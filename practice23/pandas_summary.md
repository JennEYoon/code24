# Pandas Summary Notes  
July 10, 2021 by Jennifer E Yoon 

### A. imports  
```
import pandas as pd 
```

### B. create dataframe, series objects  
```
df = pd.DataFrame(data=(list or dict), columns=[names], index=[names])
# Dimensions need to match, index rows=data rows. 

df.columns  # prints col names
df.index.name = "rown"  # explicitly name rows. 
df.columns.name = "groupn"  # explicitly name column group.  

ser = df.coln  # create a series from a dataframe column.  
ser.index   # prints row names if any, defaults to row numbers.  
ser2 = pd.Series([list])
# Create from pd, any iterable object. 

```

### C. assign variable to column  
```
var = df['coln']
var2 = df.coln  # Can't use for more than 1 column.  
var3 = df[['coln1', 'coln2']]  # Can use for many columns, list brackets.

```


### D. select single cell, change value   
```
ser['rown'] = value  # assign to single row in one series. 
ser[numrow] = value  # Can use a row number.
df.at['rown', 'coln'] = value  # at for names.
df.iat[numrow, numcol] = value  # iat for numbers, counts from 0.

df.loc['rown', 'coln'] = value
df.loc['first', 'state'] = "Ohio" 
df.iloc[numrow, numcol] = value  # iloc for index numbers, counts from 0.
df.iloc[0, 0] = 2000  

```

### E. select, drop whole column(s) or row(s)  
```
df.drop(columns=['coln1', 'coln2'], inplace=True]  
# When doing large edits, default is a view, so inplace=True to modify.

df.drop(index=['rown'], inplace=True)
# Can drop multiple rows by name. 
# Can use numbers, slice notation. 
df.drop(index=[2:4])
```

### F. conditional filter, slice notation (by name and number) 
```
result = df[df['coln']>0, inplace=True] # do we need .copy(), inplace=True ?
# return dataframe object, select rows where coln values > 0. 

result2 = df[df['coln1':'coln5']] 

df.where()
df.sort() 
df.join()

# Add new column  
df = df[columns=['newcol']] = series 


df = df[index=['newrow']] = row_series  

```

### G. SQL database 
```

```

### H. JSON file input, output  
```

```


``` 