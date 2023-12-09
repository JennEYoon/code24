# TextCodeEditor iPad app - test2
# testing ipad code editor.
# If I want to use it, I need to pay in-app.  

def func(a, nums):
  for n in nums:
    print(n*a)
    
# call func 
print('test1')
func(2, [3]) # Expect 6. Will it work as iterable without [] list form?
func(2, 3)  # Probabily error, int is not iterable???
print('\ntest2')
func(3, [1, 2, 3, 4, 5])  # Expect 3, 6, 9, 12, 15.
print('\ntest3')
#aset = set(1, 2, 3, 3, 3)  # error, set needs to have 1 object passed to it.  
#print(aset)
aset = set([1, 2, 3, 3, 3, 7])
func(2, aset)  # Expect 2, 4, 6 once, 14.
print('\ntest4')
func(4, set([5, 6, 6, 6, 7])) # Expect 20, 24 once, 28.

# Save and try running it.


