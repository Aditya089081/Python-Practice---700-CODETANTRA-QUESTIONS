# a="New"
# if a==12:
#     print("Equals to 12")
#     print("End Programe")
# elif a=="Rosee":
#     print("True")
# else:
#     print("FAlse")
# marks=12
# distinction=3
# if marks-distinction>0:
#     print("Distinction Marks")
# elif marks-distinction==0:
#     print("Zero Distinction Marks Obtained")
# else:
#     print("Distinction marks not obtained")
# if marks >distinction:
#     print("Distinction Marks Obatained")
# else:
#     print("No Distinction Maks Obatined")
# price=1200
# BAnk_Amount=1900000000
# if BAnk_Amount>price:
#     print("I can Buy the Shirt")
# else:
#     print("I Can't")
# income=21000000
# incomeTax=0
# if income<=500000:
#     print("Not Tax")
# if (income>500000) and (income<1000000):
#     incomeTax=25000+(income-incomeTax)*2
# if (income>1000000):
#     incomeTax=75000+(income-10000000)*3
# print(incomeTax)
# check=int(input("Enter:"))
# if check.isalpha():
#     print(check,"Alphabet")
# else:
#     check=int()
#     print(check,"Numeric")
#     if check>0:
#         print("Positive")
#     if check==0:
#         print("Zero")
#     else:
#         print("Negative")
# if check>0:
#     print("positive")
# elif check<0:
#     print("Negative")
# else:
#     print("zerro")
# year=int(input("Enter Year:"))
# if year%4==0:
#     if year%100==0:
#         if year%400==0:
#             print("Leap year")
#         else:
#             print("Not a Leap year")
#     else:
#         print("Leap year")
# else:
#     print("Not a Leap year")
# num=int(input("num:"))
# i=1
# sum=0
# while(i<=num):
#     sum+=i
#     i+=1
# print(sum,"sum")
# list=[]
# x=int(input("num:"))
# y=12
# if (y==0)or (x==0):
#     print("it's Zero")
# else:
#     i=1
#     if x<y:
#         while(i<=x):
#             if x%i==0 and y%i==0:
#                 list.append(i)
#             i+=1
#     elif x>y:
#         while(i<=y):
#             if x%i==0 and y%i==0:
#                 list.append(i)
#             i+=1
# print(max(list))
# num=int(input("num:"))
# a=0
# b=1
# c=a
# i=0
# sum=0
# while(c<num):
#     print(c)
#     i+=1
#     if i%2!=0:
#         sum+=c
#     a=b
#     b=c
#     c=a+b
# print("sum",c)
# print(sum)
                                                                #   Fibnocci series with even Question
                                                                #   multiplication table
# dict={
#     "state":"Capital"
# }
# capital=input("capital:")
# dict["state"]=capital
# state=input("state:")
# print(dict)

# num=int(input("num: "))
# a=0
# b=1
# c=a
# sum=0
# while(c<=num):
#     print(c)
#     c+=1
#     if c%2!=0:
#         sum=sum+c
#     a=b
#     b=c
#     c=a+b
# print(c,":sum")
# print(sum)


# dic={
#     "name":"New",
#     "class":"Btech"
# }
# for key in dic.values():
#     print(f"its {key}")


# for key,value in dic.items():
#     print(f"{key} = {value}")
# print(dic.items())

# dic={
#     "state":"capital",
#     "city":'famous'
# }
# dic["state"]=input("Entr state: ")

# A='python'
# for  i in A:
#     print(i)

# x=int(input("x: "))
# y=int(input("y: "))
# for i in range(1,x):
#     if i<20:
#         print(f"{y} * {i} = {y*i}")
#     elif i>=20:                                                          #dictionary
                                                                         #matrix transpose
                                                                        #decimal increasement
                                                                         #sum of all number
#         break
#     else:
#         print(f"{y} * {i} = 0")
# list=[]
# num=int(input("num:"))
# i=1
# while(i<=num):
#     if num%i==0:
#         list.append(i)
#     i+=1
# print(list)

# t=input("enter:")
# a=t.count("(")
# b=t.count(")")
# if b==a:
#     print("Valid and depth",a)
# elif b!=a:
#     if a>b:
#         print("not valid and errors",a-b)
#     elif b>a:
#         print("not valid and errors",b-a)

# a=12
# for i in range(1,a):
#     # if i%2==0:
#     print(i)
#         # continue
#     if i%5==0:
#         break
# s=0
# for i in range(1,23):
#     if i%2==0:
#         s+=i
#     elif i%3==0:
#         pass
#     print(i,s)

# num=int(input("num: "))
# a=0
# b=1
# c=a
# while(c<=num):
#     print(c)
#     a=b
#     b=c
#     c=a+b
# list=[]
# x=int(input("x: "))
# y=int(input("y: "))
# for i in range(x,y):
#     for a in range(2,i):
#         if i%a==0:
#             break
#     else:
#         print(i)
# ch=input("ch: ")
# if ch.isalpha():
#     if ch in "aeiou":
#         print("vowel")
#     else:
#         print("consonent")
# else:
#     print("not an alphabet")

# num=int(input("num: "))
# temp=num
# l=len(str(num))
# sum=0
# while(temp):
#     temp1=temp%10
#     temp2=temp1**l
#     sum=temp2+sum
#     temp=temp//10
# if sum==num:
#     print("Amstrong Number")
# else:
#     print("not an Amastrong Number")


# num=int(input("num: "))
# temp=num
# sum=0
# length=len(str(num))
# while(temp):
#     a=temp%10
#     b=a**length
#     sum+=b    
#     temp=temp//10
# if num==sum:
#     print("Amastrong Number")
# else:
#     print("Not an Amastrong Number")
# num=int(input("num: "))
# temp=num
# sum=0
# while temp:
#     a=temp%10
#     sum+=a
#     temp//10
# if num==sum:
#     print("Done")
# else:
#     print("Nothing")
# num=input("num: ")
# sum=0
# for i in range(1,len(num)):
#     sum=int(num[i])+sum
# print(sum)

# num=int(input('num: '))
# list=[]
# temp=num
# while(temp):
#     a=temp%10
#     list.append(a)
#     temp//10
# print(sum(list))
# def add(a=3,b=4):
#     print(a+b)
# # add(b=8,4)
# add()
# def avg(**numbers):# it will be tuple now
#     print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum+=i
#     print(sum/len(numbers))
# avg(10,10)

# def add(*args):                #mainly used for loops 
#     print(list(args))
#     sum1=[]
#     for i in args:
#         sum1.append(i)
#     print(sum1)
# a=209,13098,"90"
# add(a)
# def add(*num):
#     num=list(num)
#     num_power1=num[0]
#     return num_power1
# a=input("Enter: ")
# b=add(a)
# print(b)
# def special(**num):         # mainly used for dectionaries
#     print(type(num))
#     for key,value in num.items():
#         print(f"{key} is {value}")
# n={"num":"1","num1":"2"}
# special(n)
# def sq(a):
#     return a*a
# num=[2,3,4,5]
# square=list(map(int,num))
# print(square)
# b=[2,34,5]
# def new(a):
#     return a>2
# print(list(filter(new,b)))
# for functools import reduce

# num=[2,3,4,5]
# new=list(reduce(lambda x,y:x+y,num))
# # print(new)
# def fun1(name="Padma",age="12"):
#     print(name,"is",age,"years old")
# fun1(name="Aditya",age="17")
# fun1()
# tax=lambda salary:salary*20/100
# salary=int(input("salary: "))
# print("Total tax you have to pay",tax(salary))
# doublenum=lambda x:x*2
# a=int(input("a: "))
# result=doublenum(a)
# print(result)
# def sq(x):
#     return x%2==0
# list1=[1,2,4,5]
# new=list(filter(lambda x:x%2==0 , list1))
# print(new)

# list1=[2,3,7,9]
# list2=[2,3,7,9]

# new=list(filter(lambda x:x in list1,list2))
# print(new)
# new1=[x for x in list1 if list1 in list2]
# print(new1)

# globvar="Hello Everyone"
# def test1():
#     global globvar
#     globvar="Good Morning"
# def test2():
#     globvar="Good After Noon"
# print(globvar)
# test1()
# test2()
# print(globvar)
# num=int(input("num: "))    #function composition
# def square(x):
#     return x*x
# def double(num):
#     return num*2
# print(square(double(num)))
# num=int(input("input: "))
# def factorial(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(num))
# def checkNegativeNumber(num):
#     if num>=0:
#         print("negative")
#     else:
#         print("positive")
# import CheckNegative
# x=int(input("x: "))
# CheckNegative.CheckNegativeNumber(x)