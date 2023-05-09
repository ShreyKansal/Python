#String is a set of characters. 

str = 'I love Yellow' #use single quotes for single world or line
str1 = """  
Hello, How are you? 
My Name is Shrey! 
I am your learning buddy 
""" #use triple quotes for multiple lines. 
st1 = 'Let\'s talk about colors.\nA real quick.' #\n shifts the succeeding sentence into next line. 
print(str)
print(str1)
print(st1)

#indexing in strings
""" In strings we have index values, the first letter going left to right is considered as at index 0, 
second letter with index 1 and so on. If we start from right to left then letter comes first has index -1. 

Spaces are also considered as index position.
Let us look at some string functions.
"""

#print any index value
str2 = 'Orange is love' 
print(str2[0])
print(str2[-1])
print(str2[2])  
print(str2[6]) #prints nothing as at 6th index there is space. 

#print section of the string
print(str2[0:6]) #prints from 0th position to 6th position
print(str2[1:4]) #prints from 1st index position to 4th index position
print(str2[-1:1]) #PRINTS NOTHING
print(str2[-2:4]) #PRINTS NOTHING
print(str2[1:-1]) #prints everything excludes index value -1
print(str2[0:-2]) #prints everything excludes -1 and -2
print(str2[:]) #prints the whole string
print(str2[1:]) #prints everything excludes index value 1 
print(str2[:0]) #PRINTS NOTHING

#string concatenation 
str4 = 'Orange is a fruit'
str5 = ',it is orange in colour.'
final_str = str4 + str5 + " " + "It is healthy."
print(final_str) 
print(f'{str4}{str5}')

#String Functions 
str6 = 'I love green'
str7 = 'BLUE'
print(len(str6)) #print length of the string
print(str6.upper()) #prints all letters in uppercase
print(str6.lower()) #prints all letters in lowercase 
print(str7.title()) #first letter capital only

#find function
print(str6.find("love"))
print(str6.find("hate")) 

#replace function 
print(str6.replace("love", "hate")) 

#in operator in string
print("love" in str6) #returns a boolean value - True
print("hate" in str6) #returns a boolean value - False 









