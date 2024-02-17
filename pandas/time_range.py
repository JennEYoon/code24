# Pandas Practice, Time Range    

import numpy as np 
import pandas as pd  
import matplotlib.pyplot as plt  

dates = pd.date_range('2016/10/29 5:30pm', periods=12, freq='H')
dates
