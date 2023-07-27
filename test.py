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

list2 = [0, 23, 45, 12]

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