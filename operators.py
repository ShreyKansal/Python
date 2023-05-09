"""
Arithmetic Operators:
Arithmetic operators are used to perform mathematical operations between numbers and float values.
"""
a = float(input("Enter value of a:"))
b = float(input("Enter value of b:"))
print(a + b) #addition
print(a - b) #substraction
print(a * b) #multiplication
print(a / b) #division 
print(a // b) #quotient only 
print(a % b) #modulo operator, gives remainder 
print (a ** b) #for exponent a^b 
# print (a | b) try for int data types

#Assignment Operator 
print('----------------------------------------------------')
print("Assignment Operator")
c = 5
c += 5 #c = c + 5
print(c)
c -= 6 #c = c -5 
print(c)
c *= 5 #c = c * 5
print(c)
c /= 8 #c = c / 8
print(c)
c %= 5 #c = c % 5
print(c) 
c **= 2 #c = c ** 2
print(c)
c //= 4 #c = c // 4
print(c) 

"""
Comparison Operator
"""
print('----------------------------------------------------')
print('Comparison Operators')
e = int(input("Enter first number"))
f = int(input("Enter second number"))
print(e==f) #returns boolean value
print(e!=f) #returns boolean value
print(e>f) #returns boolean value
print(e<f) #returns boolean value
print(e>=f) #returns boolean value
print(e<=f) #returns boolean value 

"""
Bitwise Operators
"""
print('----------------------------------------------------')
print("Bitwise Operators")
var1 = True
var2= True 
var3 = False
print(var1&var2) #Bitwise AND operator True when both true
print(var2&var3)
print(var1|var2) #Bitwise OR operator True when any of the value is true
print(var1|var3)
print(var1^var2) #Bitwise XOR operator True when each of the value is 1, false for both true both false. 
print(var1^var3)
print(~var1) #Bitwise NOT operator, inverts the value True becomes False, False becomes True. 
print(~var3) 

""" How this works? 
True gets converted into 1, and False gets converted into 0. For AND and OR operator, 
the concept of Logic Gates is used. 
In case of negation, 0 becomes 1 and 1 becomes 0.
Eg. ~(0101) = 1010  
"""

#Membership Operators 
print('----------------------------------------------------')
print('Membership Operators')
string = 'Hello'
string2 = 'ell'
string3 = 'Hey'
string4 = 'Hello'
print(string2 in string) #in operator, returns a boolean value, True, if specified value is present. 
print(string3 not in string) #not in operator, returns a boolean value True, if specified value is not present. 
print(string not in string3) 
print(string in string3)

#Identity Operators 
print('----------------------------------------------------')
print('Identity Operators')
print(string is string4) #returns a boolean value
print(string is not string2) #returns a boolean value
print(string is string2) #returns a boolean value 

#Logical Operators
print('----------------------------------------------------')
print('Logical Operators')
num1 = True 
num2 = True 
print(num1 and num2) #returns a bool value
print(num1 or num2) #returns a bool value
print (~(num1)) 

