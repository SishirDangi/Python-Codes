"""
print("Hello World...!")
if 5<7:
    print("Five is less than seven")
if 5 > 2:
    print("Five is greater than two!") 
if 5 > 2:
     print("Five is greater than two!") 
#This is python comment ok boss
print("Cheers Mate!")
#print("cheers mate")
'''This is python 
multiline comment  
'''
x=5
y="ram"
print(x)
print(y)

z="sally"
z=4
#print(a)
print(z)
a=4
A="urv"
print(A) 
r="zone"
t=4
print(type(r))
print(type(t))
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x)
print(z)
anocanda="Snake"
print(anocanda)
# Giving variables name in python
# camel case - each word except first start with capital letters 
#example- myVariableName= "Camel" 
# pascal case -each word starts with a capital letter
#example- MyVariableName= "Camel"
#Snake case - each word is separated by a underscore character
#example- my_var_name_is= "camel"
#python variables - assign multiple values
#many values to multiple variables
x, y, z ="ram" , "sita" , "gita"
print(x)
print(y)
print(z)     
#one value to multiple variables
x=y=z= "TESLA" 
print(x)
print(y)
print(z)
#unpack a collection 
fruits=["apple", "banana", "grapes"]
x, y, z= fruits
print(x)
print(y)
print(z)  
x="Python "
y="is "
z= "mostly used in desktop and web server-side development."
print(x+y+z)
e=5
i="rita"
print(e, i)

#global variables
x="awesome"
def myfunc():
    print("Python is "+x)
myfunc()
x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
n='thar'
def out():
    print("Output:-" +n)
out()
#data types in python
#Built in data types 
#list 
x=["banana", "apple", "Mango"]
#tuple
y=("ram","sarita","binod")
ran=range(7)
dic={"sankhuwasabha": "khandbari" , "khotang": "Diltel"}
#print(dic)
o = frozenset({"apple", "banana", "cherry"})
x = dict(name="John", age=36)
#x = 1    # int
#y = 2.8  # float
#z = 1j   # complex
#print(x,y,z)
x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z))
x = 1.10
y = 1.0
z = -35.59
print(type(x))
print(type(y))
print(type(z))
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#complex type 
x=5+ 4j
y=5j
z=-443+4j
print(type(x))
print(type(y))
print(type(z))

x=44
y=55.44 
z=5+5j
#conversion of integer to float
a=float(x)
print(a)
print(type(a))
#conversion of float to complex
b=complex(y)
print(b)
print(type(b))
c=z
print(c)
print(type(c))
import random
print(random.randrange(1,10))
import random
print(random.randrange(1,1000))
#python casting
x=2.4
y=444
z=23+7j
print(int(x))
print(float(y))
print(z)
c=str("string")
print(c)
p=int(5.43)
print(p)
import random
print(random.randrange(-1,1))
#Multi line string
a = Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
print(a)
a = "Hello, World!"
print(a[1])
for x in "banana":
  print(x)
  a = "Hello, World!"
print(len(a))
#txt = "The best things in life are free!"
#print("free" in txt)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])
#upper case
upp="hello, my name Is Sishir Dangi"
print(upp.upper())
print(upp.lower())
a = " Hello,                       World! "
print(a.strip()) # returns "Hello, World!"
a = "Hello, World!"
print(a.replace("H", "J"))
a = "Hello, World!"
print(a.replace("l", "g"))
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#concatenate string
a="Sishir "
b="Dangi"
print("My name is "+a+b)
a = "Hello"
b = "World"
c = a + " " + b
print(c)
#format string 
b=22
a="My name is Sishir Dangi and my age is {}"
print(a.format(b))
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
eccape="I live in Kathmandu \"Baneshwor\" from Nepal"
print(eccape)
text="Python basic is very easy\nThat's True !!!"
print(text)
print(4<5)
print(5>2)
print(5==7)
dal=500
masu=400
if dal>masu: 
    print("Dal masu bhanda sasto bhayo")
else:
    print("Masu ko bhau ghatako xaina")
    
print(bool("Hello"))
print(bool(15))

print(bool(False))
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#import random
#print(random.randrange(1,5))

def myFunction() :
  return True
if myFunction():
  print("YES!")
else:
  print("NO!")

x = 200.5
print(isinstance(x, int))

x=5 
y=6
z=2
if x<y &y>z:
    print(True)
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
food=["momo","pasta","chowemin"]
food.insert(0,"noodles")
print(food)

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop(0)
print(thislist)
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

name=str(input("Enter your name: "))
age=int(input("Enter your age: "))
Age="Your age is {}"
print("Your name is \n"+name)
print(Age.format(age))
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
for x in "banana":
  print(x)
  """