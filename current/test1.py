# quick test exercise.  
# code no run, debug later, 7/5/2022 1am  
# runs on vs code, windows C:\...\repos\code\, conda base env activated 

from winreg import REG_NO_LAZY_FLUSH
import numpy as np  
import matplotlib.pyplot as plt  

X1 = np.arange(10, 20, 1)
X2 = np.random.rand(10)
Y = np.linspace(1, 10, 10)
print(X1, '\n', X2, '\n', Y)

fig = plt.figure(1, figsize=(9, 6))
ax = plt.plot(Y, X1, 'go-') 
ax = plt.plot(Y, X2*25, 'rv-')
plt.show()
plt.savefig('test1.png')
#plt.close()
