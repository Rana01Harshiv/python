#pyhton program 
print("hello python ")

#variables decalration
a = 5 
b = "rana"  #single or double quotes is not matter 

print(a)
print(b)

#printing the which type of variable is this 
print(type(a))
print(type(b))

#casting the variable value
a = str(5)  #it will become string not the integer
print(type(a))
b = int(10.35)  #it will become string not the integer
print(type(b))

#it's a case sensitive i mean " A " and " a " both are different
a= 5
A = 10
print(a)  #print 5
print(A)    #print 10

#unpacking the collection of variable
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#global variable
a = "king"      # a is a global variable

def kingdom():
    print( a +" is great") #semicolon is not required

kingdom()


#same name variable but scope is different
x = "awesome"  # this is global

def myfunc():
  x = "fantastic" # this is local
  print("Python is " + x)   

myfunc()

print("Python is " + x)

#make the global variable inside the function
def func():
    global a 
    a= "python "

func()
print("this is " + a)

#chaneg the value of the global varibale inside a function
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#get the random integer number
import random
print(random.randrange(1,10))

#slicing the string
a = "hellothisis"
print(a[2:5]) #print the position 2 to (5-1) remember like this // index is always 0

#upper case and lower case 
a = "hellothisis"
print(a.upper())
print(a.lower())

#remove the white spaces 
a = "  hello this is a without space "
print(a.strip())

#give the result in bool form true or false
print(10 > 9)
print(bool("Hello"))    # give true
print(bool())           #returns false

#continue with the operators topic in next day // date 25-11-2022 // 18:12PM
#Arithmetic operators  + - * / % ** // 
#Assignment operators   = += -= *= /= 
#Comparison operators   == != > < >= <= 
#Logical operators      and or not 
#Identity operators   is isnot 
#Membership operators   in notin
#Bitwise operators  & | ^ ~ << >>

#List data type
app = ["one","two","three"]  
print(app)    # it is changable, ordered and it allows the duplicate values 
print(len(app))    
print(type(app))
print(app[2])   #accessing the list by using thier index 
print(app[-2])
print(app[1:3])

#tuple data type 
app = ("one","two","three")
print(type(app))
for i in app:
  print(i)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#set data type 
app = {"one","two","three"}   #unchangable unindexed unordred 

#dict
app = {
  "name" : "helli",
  "age" : "19"
}
a = app.values()
b = app.keys()
print(a)
print(b)

print(app)
print(type(app))


