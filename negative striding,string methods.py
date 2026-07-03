Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> # negative striding
... a="python course"
... a[-1:-11:-3]
... 'eu h'
... a[-2:-12:-4]
... 'sch'
... a[-5:-13:-5]
... 'oh'
... 
... 
... # important points
... a="python course"
... a[8:4:2]
... ''
... a[4:8:2]
... 'o '
... a[-9:-3:-1]
... ''
... a[-3:-9:-1]
... 'ruoc n'
... a[::1]
... 'python course'
... a[::-1]
... 'esruoc nohtyp'
... 
... 
... # string methods
... #len()
... a="python"
... len(a)
... 6
... b="python course"
... len(b)
... 13
... c=""
... len(c)
... 0
... d="
... SyntaxError: unterminated string literal (detected at line 1)
... d=" "
... len(d)
... 1
... 
... # count
... a="twinkle twinkle little star"
count("twinkle")
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    count("twinkle")
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("teinkle")
0
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
b="twinkletwinkle"
b.count("twinkle")
2
b.count("twinkletwinkle")
1

c="twinkle.twinkle"
c.count("twinkle")
2
c.count("twinkle.twinkle")
1


# find a string
a="python"
a[2]
't'
a.find("t")
2
a.find("n")
5
b="hello"
b.find("l")
2
b[2:4]
'll'
a.find("m")
-1

#escape sequences
# \n-> new line
# \t-> tab space
a="name\nmobileno\tmailid\ncollege\tbranch
SyntaxError: unterminated string literal (detected at line 1)
a="name\nmobileno\tmailid\ncollege\tbranch"
print(a)
name
mobileno	mailid
college	branch
b="name:manojreddy\nmobileno:9346604828\tmailid:manojreddy2gmail.com\ncollage:mlrit\tbranch:cse"
print(b)
name:manojreddy
mobileno:9346604828	mailid:manojreddy2gmail.com
collage:mlrit	branch:cse

# replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="i love java"
b.replace("java","python")
'i love python'
c="learn learn"
c.replace("learn","today")
'today today'

#upper case and lower case
# upper()
a="hello"
a.upper()
'HELLO'
#lower
b="HI"
b.lower()
'hi'
c="python"
c[0].upper()
'P'
c.capitalize()
'Python'
d="python course"
d.title()
'Python Course'
e="i am in class"
e.capitalize()
'I am in class'
e.title()
'I Am In Class'


#conditions
a="python"
a.isupper()
False
a.islower()
True
a.isalpha()
True
b="python course"
b.isalpha()
False
c="pythoncourse"
c.isalpha()
True
e=1234
e.isdigit()
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    e.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
e="1234"
e.isdigit()
True
f="manoj"
f.isalnum()
True
g="manoj123"
g.isalnum()
True
h="manoj@123"
h.isalnum()
False
x="manoj_123"
x.isalnum()
False


a="java'
SyntaxError: unterminated string literal (detected at line 1)
a="java"
a.startswith("j")
True
a.endswith("a")
True
a.startswith("u")
False
a.endswith("r")
False

# strip()
#lstrip()->it will remove the left space
#rstrip()->it will remove the right space
a="        manoj         "
a.strip()
'manoj'
a.lstrip()
'manoj         '
a.rstrip()
'        manoj'


#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am working in delloite company"
b.split()
['i', 'am', 'working', 'in', 'delloite', 'company']


#join()
b="vja","hyd","vzg"
"".join(b)
'vjahydvzg'
" ".join(b)
'vja hyd vzg'
"k".join(b)
'vjakhydkvzg'
c="python"
"k".join(c)
'pkyktkhkokn'
