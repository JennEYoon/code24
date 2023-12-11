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

"""
Every time you call the plot function, pyplot just draws on the currently active subplot. 
This is implicit method. Fig, ax, and subplots are also created if they don't exist.  
Pyplot allows you to ignore the state machine entirely, so you can write beautifully explicit code.  
Call the * subplots * function and use the * figure * object and * axes * objects that are returned. 
Notice "s" in subplots vs no s in plt.subplot(r, c, i)  
fig, ax = plt.subplots() with s.  Don't need r, c for just 1 plot.  
"""

x = np.linspace(-2, 2, 200)
fig1, (ax_top, ax_bottom) = plt.subplots(2, 1, sharex=True)
fig1.set_size_inches(10,5)
line1, line2 = ax_top.plot(x, np.sin(3*x**2), "r-", x, np.cos(5*x**2), "b-")
line3, = ax_bottom.plot(x, np.sin(3*x), "r-")
ax_top.grid(True)

fig2, ax = plt.subplots(1, 1)
ax.plot(x, x**2)
plt.show()




### pylab implicit figure, gcf(), plt.subplot(row, col, subplot index)   

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

# It is easy to create subplots that span across multiple grid cells like so:
plt.subplot(2, 2, 1)  # 2 rows, 2 columns, 1st subplot = top left
plt.plot(x, x)
plt.subplot(2, 2, 2)  # 2 rows, 2 columns, 2nd subplot = top right
plt.plot(x, x**2)
plt.subplot(2, 1, 2)  # 2 rows, *1* column, 2nd subplot = bottom
# why is this not 3 for 3rd subplot?  But 2 for bottom out of 2 rows?  
plt.plot(x, x**3)
plt.show()
