Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #tuple()
... a=(6,7.6,"vaishu",5+6j,True,False)
... print(a)
... (6, 7.6, 'vaishu', (5+6j), True, False)
... type(a)
... <class 'tuple'>
... len(a)
... 6
... a.index(True)
... 4
... a.count("vaishu")
... 1
... 
... 
... #sets{}
... a={3,6.7,"vaishu",8+9j,True,False}
... print(a)
... {False, True, 3, (8+9j), 6.7, 'vaishu'}
... type(a)
... <class 'set'>
... b=
... SyntaxError: invalid syntax
... b={6,3,7,21,6,3,56}
... print(b)
... {3, 21, 6, 7, 56}
... 
... a={3,5,6,7,4,1}
... b={7,3,1}
... b.issubset(a)
... True
... a.issubset(b)
... False
... 
... a={4,5,6,7,8,9}
... b={6,7,8,9}
... a.issuperset(b)
... True
... b.issuperset(a)
... False
... 
... #union
... a={1,2,3,4,5}
... b={4,5,6,7,8,9}
... a.union(b)
... {1, 2, 3, 4, 5, 6, 7, 8, 9}

#intersection
a={3,4,5,6,7,8,9}
b={6,7,8,9,2,3,4}
a.intersection(b)
{3, 4, 6, 7, 8, 9}

#difference
a={12,13,14,15,16,17,18}
b={15,16,22,23,24,21}
a.difference(b)
{12, 13, 14, 17, 18}

b.difference(a)
{24, 21, 22, 23}

#symmetric difference
a={1,2,3,4,5,6,7,8}
b={6,7,8,9,10,11,12}
a.symmetric_difference(b)
{1, 2, 3, 4, 5, 9, 10, 11, 12}

#it will delete the same values and print the remaining values.
b.symmetric_difference(a)
{1, 2, 3, 4, 5, 9, 10, 11, 12}

#update
a={1,2,3,4,5}
b={4,5,6,7,8}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8}
a
{1, 2, 3, 4, 5, 6, 7, 8}
b
{1, 2, 3, 4, 5, 6, 7, 8}
#it will remove the given values and store the updated values..

a={1,3,5,7,8,9,10}
b={2,4,6,7,10,11,12}
a
{1, 3, 5, 7, 8, 9, 10}
a.intersection_update(b)
a
{10, 7}
b.intersection_update(a)
b
{10, 7}
a
{10, 7}
b
{10, 7}

a={1,3,5,7,8,9,10}b={2,4,6,7,10,11,12}
SyntaxError: invalid syntax
a={1,3,5,7,8,9,10}b={2,4,6,7,10,11,12}
SyntaxError: invalid syntax
a={2,3,4,5,6,7,8}
b={1,5,6,7,8,9}
a.difference_update(b)
a
{2, 3, 4}
b.difference_update(a)
b
{1, 5, 6, 7, 8, 9}
a
{2, 3, 4}
b
{1, 5, 6, 7, 8, 9}

a={2,3,4,5,6,7,8,9}
b={5,6,7,8,9,10,11}
a.symmetric_difference_update(b)
a
{2, 3, 4, 10, 11}
b.symmetric_difference_update(a)
b
{2, 3, 4, 5, 6, 7, 8, 9}

a={3,4,5,6,7,8}
a.add(10)
a
{3, 4, 5, 6, 7, 8, 10}
a.copy()
{3, 4, 5, 6, 7, 8, 10}
b=a.copy()
b
{3, 4, 5, 6, 7, 8, 10}
a.clear()
a
set()
c=set()
c.add(30)
c
{30}

a={5,6,7,8,9}
a.pop()
5
7
7
a.remove(7)
a
{6, 8, 9}

a={2,3,4,5,6}
a.discard(4)
a
{2, 3, 5, 6}
b={4,5,6,7}
c={8,9,10,11}
b.isdisjoint(a)
False
b.isdisjoint(c)
True
>>> #disjoint means all different elements should be present.
>>> 
>>> a={4,5,6,7,8}
>>> len(a)
5
>>> a.count(7)
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    a.count(7)
AttributeError: 'set' object has no attribute 'count'
>>> 
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> #[7,6,4,3,0,9,8,5,2,1]
>>> a[0:5]
[9, 1, 5, 2, 8]
>>> a.sort()
>>> a
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> a[5:10]
[5, 6, 7, 8, 9]
>>> 
>>> 
>>> a=[9,1,5,2,8,4,6,3,7,0]
>>> a[0:5]
[9, 1, 5, 2, 8]
>>> a[5:10]
[4, 6, 3, 7, 0]
>>> c=a[:5]
>>> c
[9, 1, 5, 2, 8]
>>> c.sort()
>>> c
[1, 2, 5, 8, 9]
>>> c.reverse()
>>> c
[9, 8, 5, 2, 1]
>>> b=a[5:]
>>> b
[4, 6, 3, 7, 0]
>>> b.sort()
>>> b
[0, 3, 4, 6, 7]
>>> b.reverse()
>>> b
[7, 6, 4, 3, 0]
>>> d=b+c
>>> d
