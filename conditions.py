# coditions
# if-condition by using comparision operators
# <,>,<=,>=,!=,==

'''a=2
b=4
if a<b:
    print("true")'''

'''a=2
b=4
if a>b:
    print("true")'''

'''a=12
b=14
if a<=b:
    print("true")'''

'''a=20
b=40
if a>=b:
    print("true")'''

'''a=7
b=9
if a!=b:
    print("not equal")'''

'''a=2
b=4
if a==b:
    print("true")'''

'''a=20
b=20
if a==b:
    print("true")'''

# use case by taking input
'''a=int(input("a value"))
b=int(input("b value"))
if a<b:
    print("lesser")'''

'''a=int(input("a value"))

if a<10:
    print("lesser") '''

'''a="pyhton"
if a=="java":
    print("true")'''

'''a=int(input("a value"))
if a=="java":
    print("lesser")'''

# if-condition by using logical operators

'''a=4
b=9
if a<b and b>a:
    print("less")'''

    
'''a=4
b=9
if a<=b and b>=a:
    print("less")  '''

'''a=10
b=20
if a!=b and a==b:
    print("jack")'''

'''a=10
b=20
if a<b or b>a:
    print("jack")'''

'''a=10
b=20
if a<=b or b>=a:
    print("jack") '''
'''a=10
b=20
if a!=b or b==a:
    print("jack")'''

'''a=20
b=40
if not a<b and b>a:
    print("jack")'''
'''a=20
b=40
if not a<b or b>a:
    print("jack")'''

'''a=int(input())
b=int(input())
if a<b and b>a:
    print("jack")'''

'''a=int(input())
b=int(input())
if a<=b or b>=a:
    print("jack") '''

'''a=int(input())
b=int(input())
if not a==b:
    print("jack")'''

# if-condition by using identify operators
# is,is not

'''a=5
if type(a) is int:
    print("it is int")'''

'''a=8
if type(a) is not int:
    print("it is int")'''
'''a=int(input())
if type(a) is int:
    print("it is int")'''

'''a=50.5
if type(a) is float:
    print("jack")'''

'''a=7.7
if type(a) is not int:
    print("jack")'''

'''a=float(input())
if type(a) is float:
    print("jack")'''

'''a="jack"
if type(a) is str:
    print("jack")'''

'''a="jack"
if type(a) is not str:
    print("jack") '''   
    
'''a=str(input())
if type(a) is str:
    print("jack") '''

# if-condition by using membership
# in,not in
'''a=2,3,4,5,6,7,8,9,10
if 10 in a:
    print("jack")'''

'''a=2,3,4,5,6,7,8,9,10
if 20 not in a:
    print("jack")'''

'''a=int(input(" enter a value"))
if 30 in a:
    print("jack")// error//'''
'''a=2,3,4,5,6,7,8,9,10
b=int(input(" enter a value"))
if b in a:
    print("jack")'''
    
      
      

# if=else conditions by using comparision operators
'''a=3
b=6
if a<b:
    print("true")
else:
    print("false")'''
          
    
'''a=3
b=6
if a>b:
    print("true")
else:
    print("false")'''
          
'''a=12
b=14
if a!=b:
    print("not equal")
else:
    print("equal")'''

#if-else conditions by using logical operators

'''a=5
b=10
if a<b and b>a:
    print("less")
else:
    print("more")'''

'''a=10
b=7
if a>b or b<a:
    print("less")
else:
    print("more")'''
'''a=7
b=14
if a!=b:
    print("less")
else:
    print("more")'''
# if-else conditions by using identify operator

'''a=7
if type(a) is int:
    print("correct")
else:
    print("in correct")'''

'''a=7
if type(a) is not int:
    print("correct")
else:
    print("in correct")'''
    
              
# if-else condition by using membership operators
'''a=2,3,4,5,6,7,8,9,10
if 7 in a:
    print("jack")
else:
    print("sparrow")'''

'''a=2,3,4,5,6,7,8,9,10
if 7 not in a:
    print("jack")
else:
    print("sparrow")'''

# if-elif-else conditions by using comparision operators
'''a=8
b=10
if a<b:
    print("less")
elif b>a:
    print("greater")
else:
    print("false")'''

'''a=8
b=10
if a==b:
    print("less")
elif b>a:
    print("greater")
else:
    print("false")'''

'''a=8
b=10
if a>b:
    print("less")
elif b<a:
    print("greater")
else:
    print("false")'''
# we can use multiple times elifs 

'''a=13
b=18
if a>b:
    print("less")
elif b<a:
    print("greater")
elif a!=b:
    print("jack")
else:
    print("false")'''


#   if-elif-else conditions by using logical operators        

'''a=10
b=20
if a<b and b>a:
    print("jack")
elif a>b and b<a:
    print("sparrow")
else:
    print("alan")'''

'''a=20
b=10
if a<b or b>a:
    print("jack")
elif a>b or b<a:
    print("sparrow")
else:
    print("alan")'''

# identify operator by using if-else
'''a=10
if type(a) is int:
    print("jack")
elif type(a) is not int:
    print("sparrow")
else:
    print("alan")'''

'''a=10
if type(a) is not int:
    print("jack")
elif type(a) is int:
    print("sparrow")
else:
    print("alan")  '''

# membership by using if-else
'''a=2,3,4,5,6,7,8,9,10
if 7 in a:
    print("jack")
elif 7 not in a:
    print("sparrow")
else:
    print("alan")'''


# multiple-if conditions
'''a=20
b=40
if a<b:
     print("jack")
if b>a:
    print("sparrow")
if a!=b:
    print("alan")'''

'''a=20
b=40
if a>b:
     print("jack")
if b>a:
    print("sparrow")
if a!=b:
    print("alan")'''

# multiple-if conditions by using logical
'''a=10
b=20
if a<b and b>a:
    print("jack")
if a!=b and b!=a:
    print("sparrow")
if a<=b and b>=a:
    print("alan")'''

# nested-if
'''a=4
b=6
if a<b:
    print("less")
    if b>a:
        print("greater")'''
# first if condition is false it can't enter into next if condition

'''a=4
b=6
if a>b:
    print("less")
    if b>a:
        print("greater")'''
'''a=7
b=12
if a<b:
    print("less")
    if a==b:
        print("greater")'''
'''a=12
b=13
if a<b:
    print("less")
    if a==b:
        print("greater")
    else:
        print("true")'''

'''a=15
b=17
if a>b:
    print("less")
    if b>a:
        print("greater")
else:
        print("true")'''
# we can take two elses 

'''a=9
b=11
if a<b:
    print("less")
    if b>a:
        print("greater")
    else:
        print("true")
else:
    print("false")'''

'''a=4
b=6
if a<b:
    print("less")
    if b==a:
        print("greater")
    elif a!=b:
         print("not equal")'''

a=4
b=6
if a<b:
    print("less")
    if b==a:
        print("greater")
    elif a>=b:
         print("not equal")
    else:
        print("equal")
              

