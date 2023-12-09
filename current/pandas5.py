# Desc: quick python practice, Vamderplas book chp 2  
# Date: 9/2/2022 Friday
# Author: Jennifer E Yoon   

import pandas as pd

## Data Creation 

### data, Series object  
data = pd.Series([1, 2, 3, 4], index=['A', 'B', 'C', 'D'])
data
type(data)

### data, Column object  

### data, DataFrame object 



## Indexes (columns, index)
data
data[0]      # implicit indexing, by item order
data['C']    # explicit indexing, by item name
data[2:4]    # implicit slicing
data['C'::]  # explicit slicing
data[-1]     # implicit slicing, last item  
# multiple items selection, double brackets  
data[['A', 'C']]  # explicit, index by name  
data[[2, 0]]   # implicit, index by relative number  

## Masking, ex Series[('A' > 3)], also filtering  
# bracket for selection, data 'where' role.  
# inside parenthesis for multiple conditions. 
data[data > 1]  # data, where data is > 1
data[(data > 1) & (data < 4)]  # AND operator '&'
data[(data > 1) | (data < 4)]  # OR operator '|' vertical pipe

### 'in' 'keys', 'items' operators
(0 in data)  # 'in' operator only works with keys, not values.  
(4 in data)  # 'in' operator only works with keys, not values. 
('D' in data)
('0' in data)
(data.keys())
(list(data.items()))  # convert into list to see item values

### Assignment to Series  
data['A']
data['A'] = 5
data['A']
data
data[2:4] = 7
data

data['A', 'C'] = 1, 3
data
data[[1, 3]] = 10, 11  # double bracket works with implicit index number
data
data[[1]] = 'hello'
data

## Fancy Indexing, ex. [a, [3, 5]]?


