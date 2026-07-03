Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a=10
print(a)
10
b=20
print(b)
20
x=40
print(x)
40
#python is a case sensitive means which variable is given to the data that variablr we have to write in print statement
a3=80
print(a3)
80
# we cannot give like this
3=80
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
6a=40
SyntaxError: invalid decimal literal




#special charecters are doent allowed except underscore
@=30
SyntaxError: invalid syntax
_=40
print(_)
40
 =20
 
SyntaxError: unexpected indent
_=100
print(_)
100
#we cannot use the keywords like a variable
if=20
SyntaxError: invalid syntax
a=20,b=9
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=4;b=6
print(a+b)
10
a,b=3,4
print(a,b)
3 4
#we can assign multiple values to a variable
a=2,3,4
print(a)
(2, 3, 4)
a,b,c=10
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    a,b,c=10
TypeError: cannot unpack non-iterable int object
a=b=c=10
print(a,b,c)
10 10 10
a=b=c=10
#we can give multiple variables to multiple values
a,b,c=(2,3,4)
print(a,b,c)
2 3 4
a,b,c=2,3,4,5
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    a,b,c=2,3,4,5
ValueError: too many values to unpack (expected 3, got 4)
#dont give spaces between words instead of space we can use underscore
first name=10
SyntaxError: invalid syntax
firstname=10
print(firstname)
10
secondname="manoj"
print(secondname)
manoj
fname="manoj"
1name="v"
SyntaxError: invalid decimal literal
lname="v"
print(fname+lname)
manojv
>>> print(fname+" "+lname
...       print(fname+" "+lname)
...       
SyntaxError: '(' was never closed
>>> name="manoj"
...       
>>> print(name)
...       
manoj
>>> city="hyd"
...       
>>> print(city)
...       
hyd
>>> #delete keyword
...       
>>> a=5
...       
>>> print(a)
...       
5
>>> del a
...       
>>> print(a)
...       
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'a3'?
>>> #case sensitive
...       
>>> name="manoj"
...       
>>> print(name)
...       
manoj
>>> NAME="alan"
...       
>>> print(NAME)
...       
alan
>>> Name="john"
...       
>>> print(Name)
...       
john
