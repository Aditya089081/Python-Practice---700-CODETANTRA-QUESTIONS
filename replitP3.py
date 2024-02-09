# a = 3
# b = 3.0
# if (a == b):
#   print("Equal")
# else:
#   print("Not Equal")

# value = input("Enter the value:")
# if value.isnumeric():
#   print("it is a Number")
# elif value.isalpha():
#   print("it is a alphabet")
# else:
#   print("it is a charecter")
# if (value>='a' and value<='z'):
#   print("alphabet")
# elif value>='0' and value<='9':
#   print('number')
# else:
#   print('Nothing')

# num = int(input("Enter the value"))
# sum = 0
# i=1
# while(i<=num):
#   if i%2==0:
#     # print("Even Number:",num)
#     sum=sum+i
#   i=i+1
# print("sum:",sum)


# num = int(input("Enter the Value:"))
# i=0
# while (i<=num):
#   if(i%2==0):
#     print("Even Number",i)
#   elif(i%2==1):
#     print("Odd NUmber",i)
#   i=i+1
# item = "Python"
# index = 0
# for i in item:
#   print(index,item)
#   index=index+1
# sum=0
# index=0
# for i in range(1,21,2):
#   if(i%2==0):
#     sum+=i
#     index+=1
#   else:
#     sum+=0
# print(sum)
# print(index)
# 
# a.alphabet()
# for i in range(a,z):
#   if (i==a==e==i==o==u):
#     print(i,"Vowel")
#   else:
#     print(i,"consonent")
# a = input()

# if (a.isalpha()):
#   print("Alphabet")
#   if(a=="a"=='e'=='i'=='o'=='u'):
#     print("Vowel")
#     b = input("Enter: ")
#     if(b==9):
#       print("Wrong")
#     elif(b>="0"and b<="8"):
#       print("Right")
#   else:
#     print('consonent')
# else:
#   print("Number")
  
  # #######################35 ppt
# i = [2,3,5,6,6,7,7,6]
# for a in i:
#   if a%2==0:
#     print("Divisible")
#     pass
#   else:
#     print(a)
# i = "1234"
# iu = int(i,8)
# print(iu)

# num= input("Enter the Value")
# if(num.isdigit()):
#   print("digit")
# elif(num.isalpha()):
#   print("Alphabet")
# else:
#   print("No None")

# num=int(input("Enter the Value: "))
# i=0
# sum = 0
# while(i<=num):
#   if(i%2==0):
#     sum=sum+i
#   i+=1
# print(sum)
# num=int(input("Enter: "))
# i=0
# while(i<=num):
#   if(i%2==0):
#     print(i,"Even number")
#   else:
#     print(i,"Odd NUmber")
#   i+=1

# value = input("Enter:")#
# index=0/
# for i in value:
#   print(index,i)
#   index+=1
# i=1
# while(i<=value):
#   print(index,i)
#   index+=1
#   if(i%5==0):
#     pass
# #   i+=1
# if(value>="a")and(value<='z'):
#   print("Vowel")
#   b = int(input("Number: "))
#   if(b==9):
#     print("Wrong")
#   else:
#     print("Correct")
# else:
#   print("Consonent")

# for i in range(1,10):
#   if(i%4==0):
#     continue
#   elif(i%6==0):
#     break
#   elif(i%3==0):
#     pass
#   print(i)
# num = int(input("Enter: "))
# print(bin(num))
# print(oct(num))
# print(hex(num))
# import math
# value= float(input("E: "))
# a=math.ceil(value)
# print(a)
# n=math.trunc(value)
# print(n)


#  #Fibbonacci Series
# a=0
# b=1
# c=a
# num = int(input("E: "))
# while(c<=num):
#   print(c)
#   a=b
#   b=c
#   c=a+b
# A=["a",'e','i','o','u']
# value = input("Enter: ")
# if(value.isalpha()):
#   if(value in A):
#     print("Vowel")
#   else:
#     print('consonent')
# else:
#   print('Not A;p')


# num = int(input("E:"))
# sum=0
# for i in num:
#   sum=sum+i
# print(sum)

# temp = num
# while(num):
#   sum=sum+(num%10)
#   num//=10
# print(sum)

# a,b,c=(input("a,b,c").split(","))
# a,b,c=[int(a),int(b),int(c)]
# if(a>b and a>c):
#   print(a)
# elif(c>b and c>a):
#   print(c)
# elif(b>c and b>a):
#   print(b)
# else:
#   print("New Ndnd")

# num = int(input("N: "))
# for i in range(2,num):
#   if(num%i==0):
#     print('not prime')
#     break
#   else:
#     print('prime')

# cout= 0
# i=2
# num = int(input("Enter the value: "))
# while(i<=(num/2)):
#   if((num%i)==0):
#     cout+=1
#     break
#   i=i+1
# if ((cout==0)and(num!=1)):
#     print("Prime Number")
# else:
#   print("Not Prime Number")
    

rows = int(input("rows: "))
for index in range(0,rows):
  for spaces in range(rows,index,-1):
    print(" ",end=' ')
  number=1
  for col in range (0,index+1):
    print('%d ' %number,end =' ')
    number = number*(index - col)/(col +1)
print()

# def generate_pascals_triangle(rows):
#     triangle = []

#     for i in range(rows):
#         row = []
#         for j in range(i + 1):
#             if j == 0 or j == i:
#                 row.append('*')
#             else:
#                 # Calculate the value between '*' using binomial coefficient formula
#                 value = triangle[i - 1][j - 1] + triangle[i - 1][j]
#                 row.append('*')
#         triangle.append(row)

#     return triangle

# n=5
# for i in range(n):
#   for j in range (n-i-1):
#     print(' ',end='')
#   for k in range(2*i+1):
#     print('*',end="")
#   print()

num = int(input("r:"))
temp = 1
for i in range(num):
  for j in range(1,num-i+1):
    print(" ",end='')
  for j in range(i+1):
    if(j==0 or i==0):
      temp=1
    else:
      temp=temp*(i-j+1)//j
      print(temp,end=' ')
  print()