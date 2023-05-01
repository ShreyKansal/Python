#Variables in Python can be of many types:
#Strings, Numbers, If Statements, Boolean Logic, Comments, Lists, Tuples, Unpacking, Dictionaries.

'''''Rules for defining variable: 
1.A variable name must start with an alphabet or an underscore. (_)
2.It should not start with anything different than these two for eg. Numbers symbols etc. 
3.It should not contain any spaces. 
4.Alphabets used must be small.
5.If there are two or more words in a variable then each word must be seperated with an underscore. '''''

var = 23 
print(var) #prints var value 
print(type(var)) #checks the var type / datatype class

#Recieving input
num = input ("Enter your number:")
print("Your number is:" + num) 

#typeconversion
#current_year = input("Enter the year:") #Throws an error as we are subtracting a string from a integer we use type conversion to fix this
current_year = int(input("Enter the year:"))
print(type(current_year))
diff = 2023 - current_year 
print("Difference in years will be:")
print(diff) 

#Sample Program: Convert kilograms to pounds 
weight = float(input("Enter your weight in kgs:"))
pounds = weight / 0.45 
print("Weight in pounds:")
print(pounds)

#Variable Updation
var2 = 12
var2 = 15 #updared value
print(var2) 

