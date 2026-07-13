Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# dictionary {}
a={"anme":"jack","year":2026,"month":6}
print(a)
{'anme': 'jack', 'year': 2026, 'month': 6}
type(a)
<class 'dict'>
b={"name","jack"}
type(b)
<class 'set'>

c={2027:7}
type(c)
<class 'dict'>

# dict methods
a={"year":2026,"month":"july","date":4}
a.update({"time":7})
a
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7}
a.update({"name":"jack"},{"city":"hyd")
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a.update({"name":"jack","city":"hyd")
         
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a.update({"name":"jack","city":"hyd"})
         
a
         
{'year': 2026, 'month': 'july', 'date': 4, 'time': 7, 'name': 'jack', 'city': 'hyd'}

# setdefault ()
         
a={"course":"python"}
         
a.setdefault("duration",4)
         
4
a
         
{'course': 'python', 'duration': 4}

# accesing
         
a={"colour":"blue","food":"biryani","icecream":chocolate}
         
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a={"colour":"blue","food":"biryani","icecream":chocolate}
NameError: name 'chocolate' is not defined
a={"colour":"blue","food":"biryani","icecream":"chocolate"}
         
a["colour"]
         
'blue'

a.get("food")
         
'biryani'
a
         
{'colour': 'blue', 'food': 'biryani', 'icecream': 'chocolate'}
a.get("biryani")
         
a
         
{'colour': 'blue', 'food': 'biryani', 'icecream': 'chocolate'}


a={"month":7,"day":"sat","time":7}
         
a.keys()
         
dict_keys(['month', 'day', 'time'])
a.values()
         
dict_values([7, 'sat', 7])
a.items()
         
dict_items([('month', 7), ('day', 'sat'), ('time', 7)])

a={"city":"vja","country":"india","state":"ap"}
         
a.pop()
         
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("city")
         
'vja'
a
         
{'country': 'india', 'state': 'ap'}
a.popitem()
         
('state', 'ap')
a
         
{'country': 'india'}


a={"name":"jack","mail":"jack@gmail.com"}
         
len(a)
         
2
a.copy()
         
{'name': 'jack', 'mail': 'jack@gmail.com'}
a
         
{'name': 'jack', 'mail': 'jack@gmail.com'}
a.clear()
         
a
         
{}

# dictionary doesn't allows duplicates
         
a={"name":"jack","year":2026,"name":"jack"}
         
print(a)
         
{'name': 'jack', 'year': 2026}
b={"name":"jack","year":2026,"name":"sparrow"}
         
b
         
{'name': 'sparrow', 'year': 2026}
a={"name1":"jack","year":2026,"name2":"jack"}
         
a
         
{'name1': 'jack', 'year': 2026, 'name2': 'jack'}
# in dictionary key values must be different
         

a={"idnos":[1,2,3],"names":["jack","sparrow","alan"],"marks":[89,90,95]
   print(a)
   
SyntaxError: '{' was never closed
a={"idnos":[1,2,3],"names":["jack","sparrow","alan"],"marks":[89,90,95]}
   
print(a)
   
{'idnos': [1, 2, 3], 'names': ['jack', 'sparrow', 'alan'], 'marks': [89, 90, 95]}
a.keys()
   
dict_keys(['idnos', 'names', 'marks'])
a.values()
   
dict_values([[1, 2, 3], ['jack', 'sparrow', 'alan'], [89, 90, 95]])
a.items()
   
dict_items([('idnos', [1, 2, 3]), ('names', ['jack', 'sparrow', 'alan']), ('marks', [89, 90, 95])])

a={year":2026,"month":7}
   
SyntaxError: unterminated string literal (detected at line 1)
a={"year":2026,"month":7}
   
a.count("year")
   
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    a.count("year")
AttributeError: 'dict' object has no attribute 'count'
a.index("month")
...    
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    a.index("month")
AttributeError: 'dict' object has no attribute 'index'
>>> 
>>> 
>>> # tasks
...    
>>> a=["codegnan","python","course"]
...    
>>> #["CODEGNAN","PYTHON","COURSE"]
...    
>>> a.upper()
...    
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    a.upper()
AttributeError: 'list' object has no attribute 'upper'
>>> a.uppercase()
...    
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    a.uppercase()
AttributeError: 'list' object has no attribute 'uppercase'
>>> a.join()
...    
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    a.join()
AttributeError: 'list' object has no attribute 'join'
>>> a=["codegnan","python","course"]
...    
... #["CODEGNAN","PYTHON","COURSE"]
...    
>>> lst=a.join()
...    
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    lst=a.join()
AttributeError: 'list' object has no attribute 'join'
>>> b=str(a)
...    
>>> b.upper()
...    
"['CODEGNAN', 'PYTHON', 'COURSE']"
