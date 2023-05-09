string = 'Hello'
string2 = 'ell'
string3 = 'Hey'
string4 = 'Hello'
print(string2 in string) #in operator, returns a boolean value, True, if specified value is present. 
print(string3 not in string) #not in operator, returns a boolean value True, if specified value is not present. 
print(string not in string3) 
print(string in string3)

print('Identity Operators')
print(string is string4) #returns a boolean value
print(string is not string2) #returns a boolean value
print(string is string2) #returns a boolean value 