Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
# patatypes
# list
list=[3,4.6,"jack",9+9j,True,False]
print(list)
[3, 4.6, 'jack', (9+9j), True, False]
type(list)
<class 'list'>
# list is mutable means we can change

#list methods
a=["python","java","c"]
a.append("c++")
a
['python', 'java', 'c', 'c++']
a.append("ml","ai")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a.append("ml","ai")
TypeError: list.append() takes exactly one argument (2 given)
a.append(["ml","ai"])
a
['python', 'java', 'c', 'c++', ['ml', 'ai']]

# extend
a=["java","html","css"]
a.extend(["js","bs"])
a
['java', 'html', 'css', 'js', 'bs']

# insert()
b=["apple","mango","guava"]
b.insert(1,"dragon")
b
['apple', 'dragon', 'mango', 'guava']
b
['apple', 'dragon', 'mango', 'guava']

# sort
a=["apple","mango","dragon","guava","cherry"]
a.sort()
a
['apple', 'cherry', 'dragon', 'guava', 'mango']
b=[1,90,56,78,7,54]
b.sort()
b
[1, 7, 54, 56, 78, 90]

# reverse()
a=["c","java","html","css"]
a.reverse()
a
['css', 'html', 'java', 'c']
b=[7,10,45,18,1]
b.reverse()
b
[1, 18, 45, 10, 7]
>>> 
>>> # pop()
>>> a=["white","black","navyblue","green","pink"]
>>> a.pop()
'pink'
>>> a
['white', 'black', 'navyblue', 'green']
>>> a.pop(1)
'black'
>>> a
['white', 'navyblue', 'green']
>>> a.pop("green")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    a.pop("green")
TypeError: 'str' object cannot be interpreted as an integer
>>> a.remove("green")
>>> a
['white', 'navyblue']
>>> 
>>> # copy
>>> a=["jack","alan","manoj","sweety"]
>>> a.copy()
['jack', 'alan', 'manoj', 'sweety']
>>> b=a.copy()
>>> b
['jack', 'alan', 'manoj', 'sweety']
>>> 
>>> a.clear()
>>> a
[]
>>> b=[]
>>> b.append("hi")
>>> b
['hi']
>>> 
>>> # len() and count()
>>> a=["hi","hello","how"]
>>> len(a)
3
>>> a="hello"
>>> len(a)
5
>>> a.count(a)
1
