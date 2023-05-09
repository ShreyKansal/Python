
#Lists are used when we want to store multiple items inside a variable.
myFruitList = ["Banana", "Mango", "Peach", "Guava"]
print(myFruitList)

""" 
1.  Lists are ordered and changeable. 
2.  Items stored inside are known as List Items. 
3.  List items are repeatable and can be of any data type or multiple data types 
4.  The first item stored in List will have 0th index, second item will have 1st index and so on,
    if we traverse from right to left, first element on right will have -1 index. 
5.  Can also be defined using list() constructor. 
"""

myFruitList[2] = "Grapes" #2nd index position changed from "Peach" to "Grapes"
print(myFruitList)

listdata = ["abc", "123", "A", 2.36, "True"] #can store multiple data types
print(listdata)
print(type(listdata)) #prints class <datatype> 
print(type(listdata[3])) #prints class <datatype> of 3rd of index postion 
#declaration using list() constructor 
animals = list(("Dog", "Cats", "Cows", "Peacock", "Lion", "Giraffe"))
print(animals)
print(animals[1])
print(animals[-1]) 
print(animals[0:3]) 
print(animals[0:])
print(animals[-1:0])
print(animals[1:-2]) 

#Note that a list is never null, variable can be null, but list can't be null either way it can be empty. 
print("Empty List")
emp = []
print(emp)
print(type(emp))
print(len(emp))

#Declaration of list using Naive Method
N = int(input("Enter a integer:(>=1)")) 
list2 = [0]*N
print(list2)

#2D Lists
"""
Creating a matrix:
A matrix is a set of numbers arranged in the form of row and columns. 
"""
print("2D Lists")
matrix = [
    (1,2,3),
    (4,5,6),
    (7,8,9)
    ]
print(matrix)
print(type(matrix)) 





