create cheatsheet for Pandas.  

>>> import torch
>>> torch.__version__
'1.9.0'
>>> torch.cuda.is_available()
False
# PyTorch lib auto detects cpu or gpu

>>> x = torch.rand(5, 3)
# random numbers (row 5, col 3)
# Seems to be uniform distribution [0, 1] inclusive range?
>>> print(x)
tensor([[0.1186, 0.7075, 0.2514],
        [0.6658, 0.5293, 0.3661],
        [0.3173, 0.9019, 0.0296],
        [0.1823, 0.7564, 0.7556],
        [0.4757, 0.9795, 0.7359]])

>>> import pandas as pd

>>> df = pd.DataFrame(data={'state':['Ohio', 'Nevada'], 'pop':[1.5, 2.4], 'year':[2000, 2001]}, columns=['year', 'state', 'pop'], index=['first', 'second', 'third])
    raise construction_error(len(arrays), arrays[0].shape, axes, e)
ValueError: Shape of passed values is (2, 3), indices imply (3, 3)
# Index count 3, has to match data rows count 2, - error. 

>>> df = pd.DataFrame(data={'state':['Ohio', 'Nevada'], 'pop':[1.5, 2.4], 'year':[2000, 2001]}, columns=['year', 'state', 'pop'], index=['first', 'second'])  #correct index for 2 count.  
>>> df
        year   state  pop
first   2000    Ohio  1.5
second  2001  Nevada  2.4

>>> df.columns.name  # wrong
>>> print(df.columns.name)  # wrong
None
>>> df.columns  # correct  
Index(['year', 'state', 'pop'], dtype='object')
>>> df.name
AttributeError: 'DataFrame' object has no attribute 'name'
>>> df.index.name  # wrong, None. 
>>> ser = df[0]
# wrong, invalid slice for DataFrame  
>>> ser = df['state']  
# correct, bracket notation, column name with ' '.
>>> ser
first       Ohio
second    Nevada
Name: state, dtype: object
>>> ser2 = df.year
# correct, dot notation, attribute so no () and no ' '.
>>> ser2
first     2000
second    2001
Name: year, dtype: int64
>>> ser.name  # correct, column object has name
'state'
>>> ser2.name  # correct, dot notation, no ( ) and no ' '.
'year'
>>> ser.index  # correct, dot notation, default row name is "index".
Index(['first', 'second'], dtype='object')
>>> ser2.index
Index(['first', 'second'], dtype='object')

>>> debt = pd.Series([50000, 60000])
>>> debt
0    50000
1    60000
dtype: int64

>>> df['debt'] = debt
# Assign data to new column and name column. 
# Bracket notation with ' '. Belongs to DataFrame obj named df.  

>>> df
        year   state  pop  debt
first   2000    Ohio  1.5   NaN
second  2001  Nevada  2.4   NaN
# Didn't work.  Can't use pd.Series directly, need to be a list or dict. Quirk of library.  

>>> debt2 = [50000, 60000]
>>> df['debt2']=debt2
>>> df
        year   state  pop  debt  debt2
first   2000    Ohio  1.5   NaN  50000
second  2001  Nevada  2.4   NaN  60000
>>> debt.index = ['first', 'second']
>>> debt
first     50000
second    60000
dtype: int64
>>> df['debt'] = debt
# However, pd.Series values can be assigned to a column, 
# once it exists as part of the DataFrame. 
# debt column 'NaN' values replaced with debt Series values.  
>>> df
        year   state  pop   debt  debt2
first   2000    Ohio  1.5  50000  50000
second  2001  Nevada  2.4  60000  60000


>>> df.index.name = "order"
# Add explicit name to rows-group. No longer named "index".
>>> df
        year   state  pop   debt  debt2
order
first   2000    Ohio  1.5  50000  50000
second  2001  Nevada  2.4  60000  60000
# "order" is above row names.
>>> df.index.name
'order'

>>> df.columns
Index(['year', 'state', 'pop', 'debt', 'debt2'], dtype='object')
>>> df.columns.name = 'features'
# Add explicit name to columns-group.  
>>> df.columns.name
'features'
>>> df
features  year   state  pop   debt  debt2
order
first     2000    Ohio  1.5  50000  50000
second    2001  Nevada  2.4  60000  60000
# "features" is left of columns-group.  

>>> df.ix['first']
AttributeError: 'DataFrame' object has no attribute 'ix'
>>> debt.ix['first']
AttributeError: 'Series' object has no attribute 'ix'
# "ix" is gone as of Pandas v 1.3.  
# Was an explicit index name selection method. Redundant.   
>>> debt['first']  # works, no "ix" needed.  
50000

# df edits generally is a view, need to explicitly say inplace=True. 
# df2 = df is only a reference, both are one object. 
# edits to df2 also changes df.  
>>> df2 = df
>>> df2
features  year   state  pop   debt  debt2
order
first     2000    Ohio  1.5  50000  50000
second    2001  Nevada  2.4  60000  60000
# Contents same as df, looks like a true copy.

>>> df2['year'] = 2010
>>> df2
features  year   state  pop   debt  debt2
order
first     2010    Ohio  1.5  50000  50000
second    2010  Nevada  2.4  60000  60000
# year column values correctly changed to 2010 for 2 rows.  
>>> df
features  year   state  pop   debt  debt2
order
first     2010    Ohio  1.5  50000  50000
second    2010  Nevada  2.4  60000  60000
# Notice, original df also changed, year column values are now 2010.

>>> df = df2.copy()
# Explicit copy.  Now df and df2 are different objects.  
>>> df
features  year   state  pop   debt  debt2
order
first     2010    Ohio  1.5  50000  50000
second    2010  Nevada  2.4  60000  60000
>>> df['year'] = [2000, 2001]
>>> df
features  year   state  pop   debt  debt2
order
first     2000    Ohio  1.5  50000  50000
second    2001  Nevada  2.4  60000  60000
# correct, only df has year column values changed to 2000, 2001. 
>>> df2
features  year   state  pop   debt  debt2
order
first     2010    Ohio  1.5  50000  50000
second    2010  Nevada  2.4  60000  60000
# df2 year column is unchanged.
>>> df
features  year   state  pop   debt  debt2
order
first     2000    Ohio  1.5  50000  50000
second    2001  Nevada  2.4  60000  60000

>>> df[['first', 'pop']] = 3.3  
# [row, col] named selection. Double [[ ]] because it's a list.
# bracket notation with explicit names and ' '. 

>>> df[['first', 'pop']] = 3.3
>>> df
features  year   state  pop   debt  debt2  first
order
first     2000    Ohio  3.3  50000  50000    3.3
second    2001  Nevada  3.3  60000  60000    3.3
# not what I was expecting.  
# change values for 'pop' column both rows, but also added a column # named 'first' and added same values to that column.  

>>> df[['second', 'pop']] = 3.1
>>> df
features  year   state  pop   debt  debt2  first  second
order
first     2000    Ohio  3.1  50000  50000    3.3     3.1
second    2001  Nevada  3.1  60000  60000    3.3     3.1
# changed values for both rows of 'pop', not just 'second' row
# that I was expecting.  Again added a new 'second' column and 
# added values to that.  Might be useful on some weird times? 

# Have to use 'loc' and 'iloc'.  location and index location. 
# 'loc' for explicit names, 'iloc' for implicit row/col numbers.
>>> df.loc[['second', 'pop']] = 2.0
KeyError: "['pop'] not in index" # ? weird. column first?
>>> df['pop']['first'] = 2.0
<stdin>:1: SettingWithCopyWarning:
A value is trying to be set on a copy of a slice from a DataFrame
>>> df
features  year   state  pop   debt  debt2  first  second
order
first     2000    Ohio  2.0  50000  50000    3.3     3.1
second    2001  Nevada  3.1  60000  60000    3.3     3.1
# That did work, row-'first', col-'pop' value set to 2.0.
# column first order does work.  
# Maybe confused because first and second are also columns. 
# delete these cols.

>>> df.at['first', 'pop'] = 2.5  # at for single cell selection.
>>> df
features  year   state  pop   debt  debt2  first  second
order
first     2000    Ohio  2.5  50000  50000    3.3     3.1
second    2001  Nevada  3.1  60000  60000    3.3     3.1
# That worked. cell ('first, 'pop') value changed to 2.5.

>>> df.loc['pop', 'second'] = 5.0
>>> df
features    year   state  pop     debt    debt2  first  second
order
first     2000.0    Ohio  2.5  50000.0  50000.0    3.3     3.1
second    2001.0  Nevada  3.1  60000.0  60000.0    3.3     3.1
pop          NaN     NaN  NaN      NaN      NaN    NaN     5.0
# OK, not what I was expecting, added new row 'pop' and
# only changed value of new cell ('pop', 'second'). 
# did nothing to cell ('second', 'pop')
# Switching order was bad!  

>>> df.loc['second', 'pop'] = 5.5
>>> df
features    year   state  pop     debt    debt2  first  second
order
first     2000.0    Ohio  2.5  50000.0  50000.0    3.3     3.1
second    2001.0  Nevada  5.5  60000.0  60000.0    3.3     3.1
pop          NaN     NaN  NaN      NaN      NaN    NaN     5.0
# Worked!  changed value in cell ('second', 'pop') to 5.5  
# No new col or row added.  
# My error was [['rown', 'coln' ]] for list.  This is true without 
# 'loc', but single [ ] when using 'loc'.  

>>> df.iat[0, 2] = 3.0  
# iat with numbers.
# single [ ], col num starts at 0, row num starts at 0.
>>> df
features    year   state  pop     debt    debt2  first  second
order
first     2000.0    Ohio  3.0  50000.0  50000.0    3.3     3.1
second    2001.0  Nevada  5.5  60000.0  60000.0    3.3     3.1
pop          NaN     NaN  NaN      NaN      NaN    NaN     5.0

>>> df.at['first', 'pop'] = 3.3
# at with names.  
>>> df
features    year   state  pop     debt    debt2  first  second
order
first     2000.0    Ohio  3.3  50000.0  50000.0    3.3     3.1
second    2001.0  Nevada  5.5  60000.0  60000.0    3.3     3.1
pop          NaN     NaN  NaN      NaN      NaN    NaN     5.0

# df.drop(na) drop by values, full rows that match deleted
# to drop columns or row, must specify.
# df.drop(columns='first') or df.drop(columns=['first'])
>>> df.drop(columns=['first', 'second'])
features    year   state  pop     debt    debt2
order
first     2000.0    Ohio  3.3  50000.0  50000.0
second    2001.0  Nevada  5.5  60000.0  60000.0
pop          NaN     NaN  NaN      NaN      NaN
>>> df
features    year   state  pop     debt    debt2  first  second
order
first     2000.0    Ohio  3.3  50000.0  50000.0    3.3     3.1
second    2001.0  Nevada  5.5  60000.0  60000.0    3.3     3.1
pop          NaN     NaN  NaN      NaN      NaN    NaN     5.0
# came back.  Only temporary view was changed. 
# need inplace=True. 

>>> df.drop(columns=['first', 'second'], inplace=True)
>>> df
features    year   state  pop     debt    debt2
order
first     2000.0    Ohio  3.3  50000.0  50000.0
second    2001.0  Nevada  5.5  60000.0  60000.0
pop          NaN     NaN  NaN      NaN      NaN

>>> df.drop(index=['pop'], inplace=True)
# Used bracket with single item. Probably need [ ].
>>> df
features    year   state  pop     debt    debt2
order
first     2000.0    Ohio  3.3  50000.0  50000.0
second    2001.0  Nevada  5.5  60000.0  60000.0
