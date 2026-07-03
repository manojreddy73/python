Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# indexing
a="hyderabad"
a[0]
'h'
a[5]
'a'
a[6]+a[7]+a[8]
'bad'
a[0]+a[1]
'hy'

b="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[8]+a[9]+a[10]+a[11]+a[12]
IndexError: string index out of range
b[2]+b[3]
'am'
b[5]+b[6]
'in'
b[8]+b[9]+b[10]+b[11]+b[12]
'class'

a="simple is better than complex
SyntaxError: unterminated string literal (detected at line 1)
a="simple is better than complex"
a[10]+a[11]+a[12]+a[13]+a[14]+a[15]
'better'
a[22]+a[23]+a[24]+a[25]+a[26]+a[27]+a[28]
'complex'
a[0]+a[2]+a[3]+a[4]+a[5]
'smple'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'simple'


b="codegnan it solution"
b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]+b[21]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b[14]+b[15]+b[16]+b[17]+b[18]+b[19]+b[20]+b[21]
IndexError: string index out of range
b[12]+b[13]+b[14]+b[15]+b[16]+b[17]+b[18]+b[19]
'solution'
b[0]+b[1]+b[2]+b[3]+b[4]+b[5]+b[6]+b[7]
'codegnan'
b[9]+b[10]
'it'


#negative indexing
a="i am learning python"
a[-6]+a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'python'
a[-15]+a[-14]+a[-13]
'lea'










a[-15]+a[-14]+a[-13]+a[-12]+a[-11]
'learn'


a="pythonfullstack"
a[-5]+a[-4]+a[-3]+a[-2]+a[-1]
'stack'
a[-9]+a[-8]+a[-7]+a[-6]
'full'
a[-15]
'p'
=a[-15]+a[-14]+a[-13]+a[-12]+a[-11]+a[-10]
SyntaxError: invalid syntax
a[-15]+a[-14]+a[-13]+a[-12]+a[-11]+a[-10]
'python'


#slicing
a="time is very precious"
a[8:12]
'very'
a[0:4]
'time'
a[13:21]
'precious'

b=
SyntaxError: invalid syntax
b="work until you succeed"
b[15:22]
'succeed'
b[5:10]
'until'
b[0:4]
'work'
b[11:14]
'you'
b[4]
' '
b[4:10;14]
SyntaxError: invalid syntax
b[4:10:14]
' '


# Negative slicing
a="vizag is city of destiny"
a[-15:-11]
'city'
a[-7:-0]
''
[-7:0]
SyntaxError: invalid syntax
[-7:-1]
SyntaxError: invalid syntax
a[-7:-1]
'destin'
a[-24:-19]
'vizag'

b="hi hello how are you"
b[-17:12]
'hello how'
b[-17:-12]
'hello'
b[-11:-8]
'how'
b[-7:-4]
'are'
b[-3:]
'you'
>>> b[-20:-18]
'hi'
>>> 
>>> 
>>> #striding
>>> #[a:b:c]
>>> a="data science"
>>> a[::]
'data science'
>>> a[::1]
'data science'
>>> a[::2]
'dt cec'
>>> a[0:4:1]
'data'
>>> 
>>> a="machine learning"
>>> a[::5]
'mnag'
>>> a[::7]
'm n'
>>> a[::2]
'mcielann'
>>> a[3:1]
''
>>> a[3:11]
'hine lea'
>>> a[:8]
'machine '
>>> a[9:]
'earning'
>>> a[::4]
'miln'
>>> a[::10]
'ma'
>>> 
>>> a="cloud computing"
>>> a[2:13:3]
'o mt'
>>> a[6:14:4]
'cu'
>>> a[5:12:2]
' opt'
>>> a[3:9:5]
'um'
