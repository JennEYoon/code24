# A quick python code preactice  

name = "Jennifer"
greeting = "Good Morning, " + name  
print(greeting)  

name = "Bill"  
print(greeting)  # expect name is still Jennifer in greeting
assert greeting == "Good Morning, Jennifer"


greeting = "Good Morning, " + name  
print(greeting) # expect name is now Bill in greeting
assert greeting == "Good Morning, Bill"
