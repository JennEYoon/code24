# test, windows c:/python/repos/code

import numpy as np
import matplotlib.pyplot as plt

# sine wave data
X = np.linspace(0, 6.283, 30)
Y = np.sin(X)
print("X: ", X, "\nY: ", Y)

# matplotlib without setup
plt.plot(X, Y, 'ro')
plt.show()
#plt.close()

plt.plot(X, 2*Y, 'g--')
plt.show()

# Windows- works! windows pop-up behind vs-code.   
# Reinstalled miniconda3 and libraries on Windows side C:\python  
# Reinstalled Spyder. Both works with plots.  