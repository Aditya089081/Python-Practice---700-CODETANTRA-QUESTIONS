                                                                        # FUNCTIONS
# """def Hellow_World():"""
    # """ 'HEllow World'
    # 'Good Morning'
    # 'Have a Nice Day'
    # "The Function ends"
    # """
    # """return
# print(Hellow_World.__doc__)
# def new_world():
#     """"""Hello Evryone
#     Welcome to
#        my
#     Youtube
#     channel""""""
#     print("2")
    
#     return
# new_world()
# print(new_world.__doc__)"""


# """a=int(input("Enter a: "))
# b=int(input("Enter b: "))
# def addavg(a,b):
#     avg=(a+b)//2
#     return avg
# def sub(a,b):
#     substaction=a-b
#     return substaction
# def mul(a,b):
#     multiply=a*b
#     return multiply
# print(addavg(a,b))
# print(sub(a,b))
# print(mul(a,b))"""


# '''def add(a,b):
#     return a+b
# def mul(a,b):
#     print(a*b)
#     return a
# # a=int(input("ENter a: "))
# # b=int(input("Enter b: "))
# # print(add())
# print(mul(4,5))
# mul(4,5)'''



# def sayhello(username):
#     greet = 'Hello'
#     print(username,greet)
# users=['Ram','Mahesh','VAshudha','Uma','Sekhar0','John']
# for i in users:
#     sayhello(i)
    
#     user_name='Aditya'
    
# def new(User_name):
#     greet='Hii'
#     print(User_name,greet)
# user=[2,'Shayam','Sita','Geeta']
# for i in user:
#     new(i)
    
# new(user_name)

# def calculate(Salary,percent=20):
#     taxAmount=Salary*percent/100
#     print(taxAmount)
# calculate(900)
# def Astero(n,q,i=10):
#     a=q*n+i
#     return a
# Astero(12,9)




# def start(name="Pratista",age=19):
#     print(f"Happy Birthday {name} you are {age} year now")
# start("pratista",19)
# start(name="Pratistha",age=13)

# tax=lambda salary: salary*0.2
# salary=int(input("Enter:"))
# print("Tax:",tax(salary))

# doublenum=lambda a: a*2
# x=int(input("Enter:"))
# doublenum(x)
# print(doublenum(a))
# # Anonumous Function = lambda function
# tax = lambda salary:(salary*20)/100
# doublenum = lambda x:x*2
# a=4
# b=doublenum(a)
# print(b)

# def common_factor(x,y):
#     while y:
#         x=y
#         y=x%y
#     return abs(x)
# a=int(input())
# b=int(input())
# print(common_factor(a,b))
# a=int(input("j:"))
# def changeglobal():
#     global a
x=500
# def changelocal():
#     a=200
#     print("LOcak as:",a)
# print(a)
# changelocal()
# changeglobal()
# print(a)
# def function(x):
#     return x**2
# def function2(x):
#     return x*2
# print(function(function2(x)))
# x=int(input())
# def compose(*functions):
#     print(type(functions))
#     def inner(arg):
#         for i in functions:
#             arg=i(arg)
#         return inner(x)
#     return inner(x)
# print(compose(12,34))
# composeed=compose(square,)
# a=int(input())
# b=int(input())
# def new(x,y):
#     tot=0
#     if y==0:
#         return x
#     elif x>0:
#         tot=x+y
#         return tot
#     elif x<0:
#         tot=x+y
#         return tot
#     elif y>0:
#         tot=x+y
#         return tot
#     elif y<0:
#         tot=x+y
#         return tot
#     else:
#         c=tot+new(1,y-1)
#         return c
#     print(new(x=a,y=b))
# import math
# a=233
# math.gcd(a)
# print(a)
# a=[2,45,7,0]
# random.shuffle(a)
# print(a)
# a=[
#     [2,4,5,6],
#     [3,5,72,2],
#     [3,42,5,67],
#     [3,56,3,6]
# ]
# t=[
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0],
#     [0,0,0,0]
# ]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         t[j][i]=a[i][j]
# for r in t:
#     print(r)
# import math
# pi=math.pi
# n=int(input("n: "))
# for i in range(1,n+1):
#     print('{:.{}f}'.format(pi,i))
# n=int(input("n:"))
# a=0
# b=1
# c=1
# while(c<=n):
#     a=b
#     b=c
#     c=a+b
#     print(c)

# num=int(input("num:"))
# i=1
# sum=0
# temp=num
# l=len(str(num))
# while(temp):
#     a=temp%10
#     b=a**l
#     sum=sum+b
#     temp=temp//10
# if sum==num:
#     print("Amastrong Number")
# else:
#     print("Not Amastrong Number")
num=int(input("num:"))
sum=0
i=1
temp=num
# while(num):
#     a=temp%10
#     def factorial(a):
#         if a==0:
#             print(0)
#         elif a==1:
#             1
#         else:
#             a*factorial(a-1)
#     b=factorial(a)
#     sum=sum+b
#     temp=temp//10
# if sum==num:
#     print("strong Number")
# else:
#     print("not")
# while(num):
#     i+=1
#     a=num%10
#     for i in range(1,a+1):
#         b=1*i
#     sum=sum+b
#     num=num//10
# if sum==temp:
#     print("str")
# else:
#     print("not")
# n=int(input("n"))
# num=1
# for i in range(1,n+1):
#     for j in range(1,1+i):
#         print(num,end=" ")
#         num+=1
#     print()