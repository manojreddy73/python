Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#integer()
#int()
int(5)
5
int(2.9)
2
int("Alan")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("Alan")
ValueError: invalid literal for int() with base 10: 'Alan'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0

#float()
float(6)
6.0
float(3.14)
3.14
float("Alan")
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float("Alan")
ValueError: could not convert string to float: 'Alan'
float(5+6j)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    float(5+6j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0

#str()
str(6)
'6'
str(4.5)
'4.5'
str("Alan")
'Alan'
str(3+5j)
'(3+5j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> 
>>> #complex()
>>> complex(6)
(6+0j)
>>> complex(3.6)
(3.6+0j)
>>> complex('Alan')
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    complex('Alan')
ValueError: complex() arg is a malformed string
>>> complex(4+5j)
(4+5j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> 
>>> boolean()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    boolean()
NameError: name 'boolean' is not defined
>>> #boolean()
>>> #bool()
>>> bool(6)
True
>>> boo1(2.6)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    boo1(2.6)
NameError: name 'boo1' is not defined. Did you mean: 'bool'?
>>> bool(2.6)
True
>>> bool('Alan')
True
>>> bool(3+4j)
True
>>> bool(True)
True
>>> bool(False)
False
