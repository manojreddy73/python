Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> a=10
>>> type(a)
<class 'int'>
>>> b=3.14
>>> type(b)
<class 'float'>
>>> c='manoj'
>>> type(c)
<class 'str'>
>>> d="Alan"
>>> type(d)
<class 'str'>
>>> e='''John'''
>>> type(e)
<class 'str'>
>>> f=5+2j
>>> type(f)
<class 'complex'>
>>> g=2+3j
>>> type(g)
<class 'complex'>
>>> h=2j
>>> type(h)
<class 'complex'>
>>> i=2+2i
SyntaxError: invalid decimal literal
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=False
>>> type(b)
<class 'bool'>
>>> #True and false must be in first letter capital
>>> c=true
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    c=true
NameError: name 'true' is not defined. Did you mean: 'True'?
