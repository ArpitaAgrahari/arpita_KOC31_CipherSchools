#Simple Calcutator
import math 
print(""" 
press -  
0 - Addition(x, y) 
1 - Subtraction(x,y) 
2-  Multiplication(x,y) 
3 - Division(x, y) 
""") 
num= input("Enter Your Choice=") 
if num== "0": 
    x = float(input("1st number -")) 
    y = float(input("2nd number -")) 
    print(x + y) 
elif num == "1": 
    x = float(input("1st number -")) 
    y = float(input("2nd number -")) 
   
    print(x-y) 
elif num == "2": 
    x = float(input("1st number -")) 
    y = float(input("2nd number -")) 
    print(x*y) 
elif num== "3": 
    x = float(input("1st number -")) 
    y = float(input("2nd number -")) 
    print(x/y) 
elif num=="4":
    x = float(input("1st number -")) 
    y = float(input("2nd number -")) 
    print(x % y) 
