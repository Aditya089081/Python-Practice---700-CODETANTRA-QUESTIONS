# str1 = "The JUpcoming Project Is Given"
# str2 = "The"
# print(str2,"in",str1,str2 in str1)
# str3 = input()
# str4 = input()
# print(str4,"in",str3,str4 in str3)put("kg: "))
# lb=2.2*mass= int(inmass
# print("lb:", lb)

# a=int(input())
# b=int(input())
# print("a: ",a)
# print("b: ",b)
# print(a ," + ",b,"= ",a + b)
# print(a ," - ",b ,"= ",a - b)
# print(a ," * ",b ,"= ",a * b)
# print(a ," / ",b ,"= ",a / b)
# print(a ," ** ",b ,"= ",a ** b)
# print(a ," % ",b ,"= ",a % b)
# print(a ," // ",b-1 ,"= ",a // b-1)

# distinction = int(input())
# marks = int(input())
# if (marks> distinction):
#   print("Distinction" )
# #   elif(a != b):
# # print(Wrong)
# else:
#   print("Work Hard")
# print("program ended")

# a = int(input("Enter the Balance: "))
# if (a >= 1000):
#   print("Sufficient Value")
#   if(a >= 1000)or(a <=1500):
#     print ("lower Middle Class")
#   if(a >= 1500)or(a <= 2000):
#     print("Still You are in lower Middle Class")
#   if(a > 2000)or(a >= 1000000000):
#     print("Ambani nhi ban Jayegaa Jaidaa mat pAISAA Collect Kr")
# else:
#   print("Balance is low")



# ch = input("ch:m ")
# if ((ch >= 'a' and ch >= 'z')or(ch >= 'A' and ch <= 'Z')):
#   print(al-phabet)

# ch = input("ch: ")
# if (ch.isalpha()):
#   print("Alphabet")
# elif(ch.isnumeric()):
#   print("Number")
# else:
#   print("it is not Nummeric nor Alphabet")
# num = int(input("number Enter: "))
# sum = 0
# i = 1
# while (i <= num):
#   if (i % 2 == 0):
#     sum = sum + 1
#   i = i + 1
# print("sum: ", sum)

# k = int(input("k: "))
# i = 0
# while (i <= k):
#   if(i % 2 == 0):
#     print(f"{i} : Even Number")
#   else:
#     print(f"{i} : Odd Number")
#   i=i+1
# range = "Python"
# # india = 0
# for a in range(10,100,10):
#   print(a+10)
# print(a+100)
  # print(india, range)
  # india += 1



# while True:
#     a = input("Enter Value: ")
#     if a.lower() in 'aeiou':
#         print(a,"vowel")
#     elif a.isdigit() and a!=9:
#         print(a,"Number entered")
#     elif(a == 9):
#         break
#     else:
#         print(a,"Consonent")    

# while (i<=5):
#   if (i == 3):
#     continue
#     i=i+1
#     print(i)

# for num in range(0,100):
#   if (num % 10 ==1):
#     continue
#   print(num)
# Number = [ 1, 32, 3, 4, 567, 6, 5,4 ,500]
# for a in Number:
#   if(a%2==1):
#     pass
# else:
  # print(a+1)



# str= "1010"
# num=int(str,2)
# print(num)

# print("x:", 0B63)
# print()

# n = int(input("Enter value"))
# Binary = bin(n)
# Octal = oct(n)
# hexa = hex(n)
# print("binary",Binary)
# print("octal",Octal)
# print("Hexa",hexa)
# num = int(input("Enter Value"))
# print("num: ",num.ceil(num))
# print("num: ",a.trunc(num))

# import random
# for i in range(3):
#   print(random.seed(77))
#   print(random.randint(1,100))
#   print(random.randrange(88,129,8))
  # a = (3,45,6)
  # print(random.shuffle(a))




# # Fibonacci Sequence
# a = 0
# b = 1
# n = int(input("n:"))
# c = a
# while (c <= n):
#   print(c)
#   a =b
#   b = c
#   c = a+b


# Vowels = ["a","e","i","o","u"]
# a = input("Enter:")
# a.lower()
# if (a.isalpha()):
#   print("Alphabet")
#   if(a in Vowels):
#     print("Vowels")
#   else:
#     print("Consonent")
# else:
#   print("Not ALphabet")


# num = int(input("ENter Value: "))
# sum = 0
# temp = num
# while (num):
#   sum = sum + (num%10)
#   num//10
# print(sum,": sum")


# rows = int(input("rows: "))
# for index in range(0, rows):
#   for index in range (rows,index, -1):
#       print(" ", end='')
# number = 1
# for col in range(0, index+1):
#     print("%d "% number,end ='')
#     number = number*(index - col)/(col+1)
# print()


# a,b,c = (input("a,b,c: ").split(','))
# a,b,c = [int(a),int(b),int(c)]
# if (a>b and a>c):
#   print(b)
# elif(b>c)and (b>a):
#   print(a)
# else:
#   print(c)

                  # Prime Number Finder
# num = int(input("Enter the Value: "))
# if (num%(num/2)):
#   print("Not Prime")
# else:
#   print("Prime")


# count = 0
# i = 2
# num = int(input("num: "))
# while (i <= (num/2)):
#   if((num%i)==0):
#     count = count + 1
#     break
#   i = i+1
# if((count==0) and (num != 1)):
#   print("prime number")
# else:
  # print("not a prime Number")



# a,b,c= (input("Enter a,b,c,.. ").split(","))
# a,b,c = [int(a),int(b),int(c)]
# num2 = a^3+b^3+c^3
# print(num2)




##############################AAMASTRONG NUMBER
# 1

# x = int(input("ENter thye Value: "))
# sum = 0
# y = x
# while(y>0):
#   digit=y%10
#   sum=sum+digit**3
#   y=y//10
# if(x==sum):
#   print(sum,"Amastrong Number")
# else:
#   print(sum,"Not Amastrong")



# a=98
# b=99
# print(sum((a,b)))


# num= str(input("Enter the Number: "))
# sum=0
# temp=num
# b=len(num)
# for i in num:
#   a = i**b
#   sum = sum +a
# print(sum,"sum")
# # a = num[-1]**b



# digit =[]
# sum = 0
# temp = 0
# number = int(input("n: "))
# temp = number
# while(temp!=0):



  # 2
# n= int(input("ENter the value"))
# length = len(str(n))
# s = 0
# temp = n
# while(temp>0):
#   dig=temp%10
#   s+=dig**length
#   temp = temp//10
#   print("Sum of powers",s)
#   if s==n:
#     print("amastrong Number")
#   else:
#     print("No amastrong Number")


# x = 1010
# n=2
# a,b=x<<2,x>>2
# print(a)
# print(b)

# num = input("ENter: ")#
# sum =0
# temp = num
# while(temp>="0"):
#   num_8=num%10
#   num_9= num_8//10
#   num_9.factorial()
#   sum = sum+num_9
#   if (sum==num):
#     print("Strong Number")
#   else:
#     print("Not Strong Number")#
                                  # Strong Nunmber
# a = 0
# num = int(input())
# temp = num
# while(num):
#   i = 1
#   fact = 1
#   digit = num%10
#   while(i<=digit):
#     fact = fact**2
# Perfect Number = Sum Of their factor is equal to That Number
# Aboundant Number = Sum Of their factor is more than  to That Number
# Deficient Number = Sum Of their factor is less than to That Number

# num = int(input("ENter the VAlue: "))
# sum =0
# i=1
# while(i<=num):
#   if (num%i==0):
#     sum=sum+i
#     i=i+1
# print("sum: ",sum)
# x=int(input(""))
# y=int(input(""))
# def addition(x,y):
#   a = x+y
#   return a
# def substraction(x,y):
#   b = x-y
#   return b
# s=addition(x,y)
# print(s)


# list1=[2,2,33,4,5]
# def squares(x):
#     return x**2
# print(list(map(squares, list1)))
# print(list(map(lambda x:x**2,list1)))
# print([x**2 for x in list1])

# a=[2,3,4,4]
# b= [2,4,6,7,9,3,3,87]
# print(list(filter(lambda x : x in a,b)))
# print([x for x in a if x in b])
# ############################################local and global variable
a=3
b=44
def test1():
  
  print(a,b)
def test2():
  global a
  a=4
  
  print(a,b)
def test3():
  
  print(a,b)
test1()
test2()
test3()
