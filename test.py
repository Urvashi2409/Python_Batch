# print("Hello world!")

# print statement is something which can be used to display on screen 

# data types 

# naming conventions of varible 

# ray mond 
# case sensitive 
# cannot start with number 
# no keyword 
# symbols are not allowed 
# _ is allowed 

# arithematic operators = +, -, *, /, %, **, // 

# print(3**2)
# print(8/3)
# print(8//2)

# assignment operators 
# =, +=, 
# x = 23

# x = 2;
# x += 3
# x = x + 3
# print(x)

# x -= 3

# x *= 3

# x /= 3

# x %= 3

# x //=3

# x **= 3

# relational operators  
# <, >, !=, ==, >=, <= 
# conditional statements 
# age = 18 
# if age < 18: 
#     print("You are not eligible to vote")
# elif age > 18:
#     print("You are eligible to vote")
# else:
#     print("I am going to apply for voter id")


# logical operators 

# if: 

# if : 

# if: 

# if: 

# elif: 

# elif: 

# else: 
# | 

# x = 12
# y = 3
# z = 11
# if (x == 2 and x < 3):
#     print(x)
# if x != 5:
#     print("whatever")
# if x != 5 and y >= 5 and z <= 13:
#     print("its gonna happen")
# if z != 0 or x == 2:
#     print("you say")
# if (not(y < 10)):
#     print(y)
# elif(x < 10 or x < 5):
#     print("okkkkkkk")
# elif(y < 10 or y <= 0):
#     print("pikachu")
# elif(z == 0 or y ==5):
#     print("Pikaboo")
# else:
#     print("Default value")


# Data types: 
# int = integer 
# float = decimal point numbers ex: 8.4567 
# double = decimal point number ex: 23.443746482384648234783284362384632843874436832
# complex = :  x = 1j 

# x = 23

# print(type(1j))
# print(type(23))
# print(type(23.45))
# print(type(23.45227462874628428424624412462147816418424821642146242428734434623463248267846))
# print(type("Apurv hiiii"))
# print(type(True))

# print(len(mylist))
# print(mylist)
# print(mylist[5])
# print(mylist[-4])
# slicing in list 
# print(mylist[4:6])

# 4, apurv, 45.6 
# 2 = start 
# 9 = end 
# 3 = steps 
# by default steps = 1
# print(mylist[2:9:3])
# print(mylist[-7:9:3])
# print(mylist[-7::3])

# print(mylist[-2::])
# print(mylist[::])


# print(mylist[-2:-7:])
# print(mylist[-2:-7:-1])

# print(mylist[-3::-2])
# print(mylist[::-2])
# print(mylist[::3])
# True, person, 3 

# print(mylist[-2::-3])


# for i in range(0, len(mylist)):
#     print(mylist[i], end=" || ")

# startpoint, endpoint, steps 
# for i in range(2, len(mylist), 2):
#     print(mylist[i], end=" ")

# for i in range(len(mylist)-1, 2, -1):
#     print(mylist[i], end=" ")

# for i in mylist[2::]:
#     print(i, end=" ")

# new line character 
# print('\n')

# print(mylist[2::])

# mylist[5] = "New Zealand"
# print(mylist)

# lists are mutable 

# how to add things in a list 
# mylist.append("Hii")
# print(mylist)

# mylist.insert(8, "900")
# print(mylist)

# how to remove things from a list

# remove = deletes a particular element 
# mylist.remove("apurv")
# print(mylist)

# pop = deletes a particular element according to the index 
# mylist.pop(7)
# print(mylist)

# mylist.pop()
# print(mylist)

# del mylist[5]

# print(mylist)

# list2 = [0, 23, 45, 12]

# mylist.extend(list2)
# print(mylist)

# mylist = mylist + list2 
# print(mylist)

# for i in list2: 
#     mylist.append(i)

# print(mylist)

# mylist = ['aarav', 'urshita', 'person', "apurv", '''urvashi''']

# for i in range(len(mylist)):
#     if 'u' in mylist[i]:
#         print(mylist[i])

# for i in mylist: 
#     if 'u' in i:
#         print(i)

# list comprehension  
# newlist = [mylist[i] for i in range(len(mylist)) if 'u' in mylist[i]]
# print(newlist)
# list2 = [1, 2, 3, 4]
# mylist = [12, 34, '90', 'piyush', '''yash''', """tushar""", "tarun", [9, 3, 56, 235], list2, True]
# print(mylist[7][2])
# print(mylist[-3][-2])
# print(mylist[7][-2])
# print(mylist[-3][2])

# mylist[3:6] = [34, 45, 60]
# print(mylist)

# mylist[7][1:3] = [11, 111]
# print(mylist)

# mylist = [23, 12, 4, 34, 5, 50]

# it sorts the uppercase first and then lowercase 
# Yash apurv 

# list2 = [90, 34.5, 45.6]
# mylist.sort()
# print(mylist)

# mylist.sort(reverse=True)
# list2.sort(reverse=True)
# print(mylist)
# print(list2)

# print(mylist.index("piyush"))

# print(mylist.count("yash"))

# for i in mylist: 
#     if 'u' in i:
#         print(i)

# a = 0
# for i in range(len(mylist)):
#     if mylist[i] == "yash":
#         a += 1
# print(a)

# mylist = ["yash", "kunal", "piyush", "manish", "Urshita", "Riya", "yash", "yash"]

# its just giving the reference of the same list 
# list1 = mylist 
# list1[2:4] = [0, 1]
# print(mylist)
# print(list1)


# list1 = mylist.copy()
# list1[2:4] = [0, 1]
# print(list1)
# print(mylist)

# list1 = []
# for i in mylist: 
#     list1.append(i)

# list1[2:4] = [0, 1]
# print(mylist)
# print(list1)

# mylist.clear()
# print(mylist)

# del mylist 
# print(mylist)

# strings, tuples, dictionaries 

# operators: 
# Arithematic: +, -, /, *, %, ** 
# Assignment: =, +=, -=, *=, %=, **= 
# Relational: ==, !=, >=, <=, >, < 
# Logical: and, or, not 
# Identity operator: is, is not 
# in, not in  

# x = "yash"
# y = "yash"
# if y is x: 
#     print("True")

# if y is not x: 
#     print("False")

# for i in mylist: 
#     if i == "yash":
#         print(i)
#     elif i not in "yash":
#         print("false")


# 4.56  
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 
# 4343746327824
# decimal = made of 10 digits 
# 9 
# binary = only 2 digits (0, 1)
# 01011010101 

# print(4/2)
# print(4 >> 1)


# tuples  

# mytuple = (1, 2, 3, "riya", True, 0.7)
# print(mytuple)
# print(mytuple[2])
# print(mytuple[-3])

# list() = list constructor  

# mylist = [0, 0, 0]
# mylist = mylist + list(mytuple)
# print(mylist)

# newtuple = tuple(mylist)
# print(newtuple)

# tuples are faster than lists because those are not editable  

# mylist = [1]
# print(type(mylist))
# newtuple = (1,)
# print(type(newtuple))


# mytuple.count(1)

# function method 

# mylist.sort() = methods are class based 
# sorted(mytuple) = functions based 

# mytuple.index("riya")

# mytuple = reversed(mytuple)
# print(mytuple)

# mytuple[-2] = 34 
# to change tuple element, convert it into list then change and convert it back 


# unpacking tuples 
# (x, y, z, w, p, m) = mytuple 
# print(x, y, z, w, p, m)

# *z is used to pack to a list and unpack from a list into elements 

# (x, y, *z) = mytuple 
# print(x, y, z)
# mylist = [1, 2, 3]
# mylist = [x, y, *z]
# print(mylist)

# mytuple = (1, 2, 3, "riya", True, 0.7)

# mylist = [1, 2, 3, "riya", True, 0.7]

# [x, y, z, a, b, c] = mylist 
# print(x, y, z, a, b, c)

# dictionary 

# key value pair 
# first_name = fgskhfgkfkgffk 

# print(mydict)
# print(mydict['riya'])

# print(mydict['esha'][1])
# print(mydict['esha'][1:])

# nested dictionary 
# mydict = {
#     "1" : {
#         1 : 3,
#         4: 6,
#         5: 7,
#     },
#     "4" : {
#         11 : 13,
#         41: 64,
#         15: 71,
#     }
# }

# print(mydict["4"][41])

# lists, dict are mutable, tuples are immutable 
# keys are unique 


# mydict["piya"] = 70 

# it adds new when we dont have that key but it updates if we have it 
# ordered 

# mydict.update({
#     "ya" : 70
# })

# print(mydict)

# print(mydict["piya"])
# print(mydict.get("piya"))


# mydict.pop("piya")
# mydict.popitem()
# del mydict["piya"]
# del mydict 
# mydict.clear()
# print(mydict)

# for loops  
# mydict = {
#     "priya" : 20,
#     "tiya" : 90,
#     "piya" : 0,
#     "esha" : [0, 1, 2]
# }

# for i in mydict: 
#     print(i)

# for i in mydict.values():
#     print(i)

# for i in mydict.keys():
#     print(i)

# for i, j in mydict.items():
#     print(i, j)

# print(mydict.values())
# print(mydict.keys())
# print(mydict.items())

# functions 
# inbuilt 
# module functions 
# custom functions 

# parameters = parantheses when we are defining the function 
# def greeting(name, message):
#     print("Hi", name)
#     print(message)
#     print("dskfskdjfkjsfgksfdkjf")
#     print("ajhkskdkadadkasdadadkakdj")
#     print("sjkdjkaskjdgaksdgksadgsagd")

# function call 
# arguments = function call 
# greeting("Riya", "You are good")
# greeting("Urvashi")
# greeting("Apurv")

# def add(a, b):
#     c = a + b
    # return c 
#     print(c)

# add(1, 2)
# ans = add(3, 4)
# print(ans)
# print(ans)

# scopes 
# 3, 3, 2, 10, 11, 
# global scope , function scope, local scope  
# x = 3 
# print(x)
# def func(x):
#     print(x)
#     x = 10 
#     print(x)
#     x += 1 
#     print(x)
#     if x <= 9:
#         x = 23
#         print("cool ", x)
#     elif x == 11:
#         x = 45
#         print("not cool ", x)
#     else:
#         x = 90
#         print("yes ", x)
#     return x 

# print(x)
# x = func(2)
# print(x)


# child can access parent everytime but there is some condition for parent to access the child 
# def sub(a, b):
#     c = a - b 
#     if 3 > 4: 
#         y = 34 
#         print(c)
#     elif 5 > 3:
#         y = 45 
#         print(c)
#     else:
#         y = 4 
#         print(c)
#     print(y)

# sub(1, 2)

# break, continue 
# 0, default, u 
# break will stop the current iteration after executing that if/else and the whole for loop 
# for i in range(5):
#     if i == 0:
#         print(i)
#     if i >= 1: 
#         print("u")
#         break 
#     elif i > 2:
#         print("no")
#     else:
#         print("default")
    
# 0, default, u 
# continue = skips the current iteration after executing the particular if/else statement 

# for i in range(5):
#     if i == 0:
#         print(i)
#     if i >= 1: 
#         print("u")
#         continue 
#     if i > 0:
#         print("something")
#     elif i > 2:
#         print("no")
#     else:
#         print("default")

# paramaters in functions 

# default parameter 
# def func(a = 10, b = 2):
#     return a + b 

# argument 
# print(func(3, 4))

# by default first parameter takes the value 

# keyword arguments and positional arguments 

# positional arguments 

# def func(b, a = 10):
#     return a + b 

# print(func(10, 5))

# arbitrary arguments 
# *args = it is packing all the arguments inside a tuple 
# if we don't know the number of arguments then use args 
# def func(*args):
#     res = 0 
#     for i in range(len(args)):
#         res += args[i]
    
    # args[2] = 3
    # print(args)
#     print(type(args))
#     return res 


# res = func(2, 3, 4, 5, 9, 12, 3, 4, 5, 5, 6, 7)
# print(res)

# positional arguments //  keyword arguments
# def func(a, c, b):
#     res = 0
#     res += (a + b + c)
#     return res 


# res = func(a = 3, b = 4, c = 5)
# print(res)


# arbitrary keyword arguments 

# def func(**kwargs):
#     res = 0
    # print(type(kwargs))
    # res += (kwargs.get('a') + kwargs.get('b'))
    # res += (kwargs['a'] + kwargs['b'])
    # return res 

# res = func(a = 3, b = 8, c = 9, r = 0)
# print(res)


# sets 
# s = {1, 2, 3, 4, 5, 5, 5, 5, 5}
# print(type(s))

# empty {} is a dictionary 
# s = {}
# print(type(s))

# s = set(["rsdfhsdflfdhfsl", "skjhsjhsdjfgsdjfdf"])
# print(s)

# s = set()
# print(type(s))

# if we want empty set we can use set()
# if i want to put values inside set() then put it as an iterable(list, tuple, strings, dictionary)

# s = set({
#     1 : 2,
#     2 : 3,
#     4 : 5,
# })

# print(s)
# print(type(s))

# for i in "food":
#     print(i)

# strings are immutable 
# s = "food"
# s[0] = "p"
# print(s)

# dict['r'] = 'foof'

# sets are mutable 
# s = {1, 2, 3, 4}
# s.add('food')
# print(s)

# sets are unordered 
# s[0] = "p"
# print(s)

# s.update({10, 2, 3, 4, 50, 6})
# print(s)

# s.remove(1)
# print(s)

# s.clear()
# del s 

# del s[1]
# print(s)

# s = s1.union(s2)
# s = s1 | s2 
# s = s2 | s1 
# s1.update(s2)
# print(s1)

# s = s1.intersection(s2)
# s1.intersection_update(s2)
# s = s1 & s2 
# s = s2 & s1 

# not commutative 
# s = s1 - s2 
# s = s2 - s1 
# s = s1.difference(s2)
# s1.difference_update(s2)
# print(s1)

# s1 = {1, 2, 3, 4}
# s2 = {20, 3, 4, 5, 6}

# s = s1 ^ s2 
# s = s1.symmetric_difference(s2)
# s1.symmetric_difference_update(s2)
# print(s1)

# print(s1)

# cardinality = 
# print(len(s))
