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



### pylab implicit figure, gcf()  


