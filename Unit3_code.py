# def add(x,y):
#     a=x+y
#     print(a)
# def sub(x,y):
#     a=x-y
#     print(a)
# def mul(x,y):
#     print(x*y)
# add(20,20)
# sub(20,20)
# mul(20,20)
#                                                                        #25.1.4
# def simplecalc(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
# a=int(input("a:"))
# b=int(input("b:"))
# c=input("c:")
# simplecalc(a,b)
# simplecalc(b,a)
# def saysomething(name,message):
#     a=f"Good {name}"
#     print(a)
# name=input()
# message=input()
# saysomething(name,message)
# saysomething(message,name)
# def simple(a,b):
#     print(a+b)
# a=int(input("a:"))
# b=int(input("b:"))
# simple(a,b)
# def calculateTax(salary,percent=20):
#     taxAmount=salary*percent/100
#     print(taxAmount)
# sal=int(input("salary:"))
# per=int(input("percent:"))
# calculateTax(sal,per)
# def fun1(name="ankit",age=12):
#     print(name,"in",age,"year old")
# name=input("name:")
# age=int(input("age:"))
# fun1(name,age)
# fun1(age=age)
# fun1(age=28,name=name)
# fun1()

# def num(*n):
#     print(type(n))
# print(num())
#     sum=0
#     for i in n:
#         i=int(i)
        
#         sum=sum+i
#     return sum
# # print(num(12,45,78))
# doublenum=lambda x:x*2
# a=int(input("inter: "))
# r=doublenum(a)
# print(r)
# list1=(input().split(","))
# new=list(map(int,list1))
# # print(tuple(map(lambda x:x**2,new)))
# list2=[1,3,4,5]
# print(list(filter(lambda x:x in new,list2)))
                                                                                          #28.1.3
# def largestinthree(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#         return b
#     else:
#         return c
# print(largestinthree(12,34,3))

# def test1():
#     a=34
#     b=23
#     return a,b
# def test2():
#     global a
#     a=23
#     global b
#     b=45
#     print(a,b)
# def test3():
#     print(a,b)
# print(test1())
# test2()
# test3()
# a=input("a: ")
# def changeglobal():
#     global a
#     a=200
# def changelocal():
#     a=500
#     print(a)
# # changeglobal()
# # changelocal()
# print(a)
# print(a)
# print(a)
# x=int(input("x: "))
# def square(x):
#     return x*x
# def double(x):
#     return x*2
# print(square(double(x)))
                                                                             #29.2.2
# def factorial(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# n=int(input("Enter Number:"))
# if n<0:
#     print("for factorial enter +ve number please",factorial(n))
# b=factorial(n)
# print(b)
                                                                        # 30.1.4
                                                                        #30.1.5
# def add(a,b):
#     tot=0
#     if b==0:
#         return a
#     elif a<0:
#         tot=a+b
#         return tot
#     elif b<0:
#         tot=a+b
#         return tot
#     elif a>0 and b>0:
#         tot=a+b
#         return tot
#     else:
#         return tot+add(1,b-1)
# print(add(0,1))
# import math
# num=int(input("Enter Here:"))
# n=math.gcd(num)
# print(n)
# import random
# list1=[1,3,5,6]
# a=random.choice(list1)
# print(a)
import math
print(type(math.pi))
print(type(math.inf))     # it represent positive infinity.it's a special floating point numberthat represent a quantity greater then any finite positive number
print(type(math.e))       #euler's number
print(type(math.tau))
print(type(math.nan))
