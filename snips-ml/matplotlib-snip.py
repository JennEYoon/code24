# matplotlib snip

import matplotlib.pyplot as plt

# plot single vector as y-axis, index position is x-axis by default  
plt.plot([1, 2, 4, 9, 5, 3])
plt.show()

import numpy as np  

# color & tick marks shortcut   
x = np.linspace(-1.4, 1.4, 30)
plt.plot(x, x, 'g--', x, x**2, 'r:', x, x**3, 'b^')
plt.show()

### subplots function, fig, ax explicit  



### pylab implicit figure, gcf(), plt.subplot(row, col, index)   
"""
Subplots
A matplotlib figure may contain multiple subplots. 
These subplots are organized in a grid. 
To create a subplot, call the * subplot * function, and specify the number of rows and columns
in the figure, and the index of the subplot you want to draw on (starting from 1, 
then left to right, and top to bottom). 
Note that pyplot keeps track of the currently active subplot 
(which you can get a reference to by calling plt.gca()), so when you call the plot function, 
it draws on the active subplot.
"""

x = np.linspace(-1.4, 1.4, 30)
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot = top left
plt.plot(x, x)
plt.subplot(2, 2, 2)  # 2 rows, 2 columns, 2nd subplot = top right
plt.plot(x, x**2)
plt.subplot(2, 2, 3)  # 2 rows, 2 columns, 3rd subplot = bottom left
plt.plot(x, x**3)
plt.subplot(2, 2, 4)  # 2 rows, 2 columns, 4th subplot = bottom right
plt.plot(x, x**4)
plt.show()


