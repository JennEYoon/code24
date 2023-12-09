# Closure, chapter 7

### Definition:  
Closure is a function with an extended scope  
that encompass nonglobal variables  
referenced in the body of that function but not defined there.  
It can access non-global variables defined outside of its body.  

"Closing" when function is called and "sets" the value for a referenced but not defined variable.  

### Ex 1: cumulative average  
class example without closure

```python
class Averager():
  
  def __init__(self):
    # initialize class  
    self.series = []

  def __call__(self, new_value):
    # call method, allows class to be called like a function.  
    self.series.append(new_value)
    total = sum(self.series)
    units = len(self.series)
    return total/units
 
 # Call with values [10, 11, 12, 13]
 avg = Averager()
 avg(10)
 avg(11)
 avg(12)
 avg(13)

```
Debug: see "Closure_ch7.ipynb"

