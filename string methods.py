Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#concatenation
a="code"
b-"gnan"
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    b-"gnan"
NameError: name 'b' is not defined
b="gnan"
print(a+b)
codegnan
a="python"
b="course"
print(a+b)
pythoncourse
print(a+" "+b)
python course

# use case
fname="manoj"
lname='reddy"
SyntaxError: unterminated string literal (detected at line 1)
lname="reddy"
print(fname+" "+lname)
manoj reddy
print(fname.title()+" "+lname.title())
Manoj Reddy
(print(fname+" "+lname).title())
manoj reddy
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    (print(fname+" "+lname).title())
AttributeError: 'NoneType' object has no attribute 'title'
print((fname+" "+lname).title())
Manoj Reddy

#formatting
a=2
b=4
print(a+b)
6
print("the sum is ",a+b)
the sum is  6
city="hyderabad"
print("the city is",city)
the city is hyderabad
tourist place="goa"
SyntaxError: invalid syntax
touristplace="goa"
print("the tourist place is",touristplace)
the tourist place is goa

# format()
a="jack"
b="sparrow"
print("hello {}{}".format(a,b))
hello jacksparrow
print("hello {} {}".format(a,b))
hello jack sparrow
print("hello {} hello{}".format(a,b))
hello jack hellosparrow
print("hello {} hello {}".format(a,b))
hello jack hello sparrow


# fstring
a="sita"
b="ram"
print(f"hello {a}{b}")
hello sitaram
print(f"hello {a} {b}")
hello sita ram
print(f"hello {a} hello{b}")
hello sita helloram
print(f"hello {a} hello ram{b}")
hello sita hello ramram
print(f"hello {a} hello {b}")
hello sita hello ram


a=3
b=4
print("multiplication is {}{}".format(a*b)

 a=3
b=4
... print("multiplication is {}{}".format(a*b)
... 
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> a=3
...       
>>> b=4
...       
>>> print("multiplication is {}{}".format(3,4))
...       
multiplication is 34
>>> print("multiplication is {}{}".format(3*4))
...       
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    print("multiplication is {}{}".format(3*4))
IndexError: Replacement index 1 out of range for positional args tuple
>>> a=4
...       
>>> b=5
...       
>>> print(a*b)
...       
20
>>> c=a*b
...       
>>> print("the product is {}".format(c))
...       
the product is 20
>>> print("the product is {c}")
...       
the product is {c}
>>> print(f"the product is {c}")
...       
the product is 20
>>> print("the product is{}".format(a*b))
...       
the product is20
>>> print(f"the product is{c}")
...       
the product is20
>>> print(f"the product is{a*b})
...       
SyntaxError: unterminated f-string literal (detected at line 1)
>>> print(f"the product is{a*b}")
...       
the product is20
