Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# Arthematic
a=6
b=2
print(a+b)
8
print(a-b)
4
print(a//b)
3
print(a/b)
3.0
print(a**b)
36
print(a%b)
0

# Assignment
a=4
b=2
b+=a
d
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d
NameError: name 'd' is not defined. Did you mean: 'id'?
b
6
b-=2
b
4
b//=2
b
2
b/=2
b
1.0
b**=30
b
1.0
b%=10
b
1.0

# Comparision
a=7
b=3
a>b
True
a<b
False
b>a
False
b<a
True
a!=b
True
a>=b
True
a<=b
False
b>=a
False
b<=a
True

# logical
a=6
b=9
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
not True
False
not false
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    not false
NameError: name 'false' is not defined. Did you mean: 'False'?
not False
True

# identity
a=5
type(a) is int
True
type(a) is not int
False
b=3.14
type(b) is float
True
type(b) is not float
False
c='Alan'
type(c) is str
True
type(c) is not str
False
d=True
type(d) is bool
True
type(d) is not bool
False
e=2+3j
type(e) is complex
True
type(e) is not complex
False

# Membership
a=2,3,4,5,6,,7,8,9,10
SyntaxError: invalid syntax
7 in a
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    7 in a
TypeError: argument of type 'int' is not a container or iterable
a=2,3,4,5,6,7,8,9,10
7 in a
True
15 in a
False
20 in a
False

# Bitwise
a=2
b=4
a&b
0
a=6
b=4
a&b
4
bin(4)
'0b100'
bin(6)
'0b110'
a=3
b=5
bin(3)
'0b11'
bin
<built-in function bin>
bin(5)
'0b101'
a&b
1

a=3
b=5
a|b
7
a=2
b=8
a|b
10
bin(2)
'0b10'
bin(8)
'0b1000'

>>> a=2
>>> -(a+1)
-3
>>> a=4
>>> ~a
-5
>>> msd=7
>>> ~msd
-8
>>> msd=-7
>>> ~msd
6
>>> 
>>> a=8
>>> b=3
>>> a^b
11
>>> a=5
>>> b=7
>>> a^b
2
>>> 
>>> 
>>> a=3
>>> a<<2
12
>>> bin(3)
'0b11'
>>> b=7
>>> b<<<3
SyntaxError: invalid syntax
>>> b<<3
56
>>> bin(7)
'0b111'
>>> 
>>> a=5
>>> a>>2
1
>>> bin(5)
'0b101'
>>> b=6
>>> b>>3
0
>>> bin(6)
'0b110'
