# Pandas Practice, Time Range    

import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt  

dates = pd.date_range('2016/10/29 5:30pm', periods=12, freq='H')
print(dates)  


temperatures = [4.4,5.1,6.1,6.2,6.1,6.1,5.7,5.2,4.7,4.1,3.9,3.5]
s7 = pd.Series(temperatures, name="Temperature")
s7.plot()
plt.show()
