# declaration of different data types

num = 10                #integer
num1 = 3.5              #float
str1 = "virat kohli"            #string
complex = 1 + j              #complex
fruits = ["apple", "banana", "cherry"]	#list
another = ("apple", "banana", "cherry")	#tuple
info = {"name" : "satish", "age" : 36}	#dict	
fruits = {"apple", "banana", "cherry"}	#set
x = True	#boolean
z = range(6)	#range


#conditional statements

#if-elif-else

a = 50
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
    print("a and b are both equal")
else:
  print("a is grater than b")


#looping - statements

#while-loop

i = 0
while i < 6:
  print(i) #it prints from 0 to 5
  i += 1 


#for-loop

fruits = ["carrot", "papaya", "lemon"]
for x in fruits:
  print(x) 


#jumping-statements


#break


fruits = ["carrot", "papaya", "lemon"]
for x in fruits:
  print(x)   # it prints carrot and papaya
  if x == "papaya":
    break


#continue
fruits = ["carrot", "papaya", "lemon"]
for x in fruits:
  if x == "papaya":
    continue
  print(x) # it prints carrot and lemon which skip the papaya due to if condition

#functions

#function-definition with calling

def yes_function():       #this is function definition
  print("This is a function")

yes_function()  #this is function calling #prints the statement


#function with parameters and arguments

def yes_function(fname, lname): #function definition has 2 parameters
  print(fname + " " + lname)

yes_function("satish", "G") # it is a function calling which passes 2 arguments 



#function with return values

def yes_function(x):
  return 5 * x

print(yes_function(3))  # 15
print(yes_function(5))   #25
print(yes_function(9))   #45

#inbuilt-functions

#count()

virat = "I love virat, virat is an Indian cricket player"
x = virat.count("virat")
print(x)

#lower()

txt = "hello World!"
x = txt.lower()
print(x)

#upper()

txt = "hello World!"
x = txt.upper()
print(x)

#append()

items = ["apple", "banana", "cherry"]
items.append("orange")
print(items)

#extend()

items = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
items.extend(cars)
print(items)



