# a="mYYkk"
# print(a)
# print(a.capitalize())
# print(a)
# print(a.upper())
# print(a.startswith("mj"))
# print(a.split("k"))
# print(a.replace("Y","o"))
# print(a.strip("Y"))
# print(a.count("k"))

# def poem():
#     """Hellow everey ome hii  my  self Adi IamLEarning Python in mmmmm CLass O"""
# print(poem())




# a=[3,4,5,6,7]
# print(sum(a))
# print(sorted(a))


                                                                  # Fibnocci Series
"""a=0
b=1
c=a
num=int(input("Enter the Number:"))
while (c<=num):
    print(c)
    a=b
    b=c
    c=a+b"""
    
                                                            #    Sumation
"""
sum=0
num=int(input("ENter the VALUE:"))
temp=num
while num :
    remainder = num%10
    sum=sum+remainder
    num=num//10
print(sum)
"""
                                                                #   Prime Number FInder
"""
sum=0
i=2
num=int(input("ENter the Value:"))
while (i<=(num/2)):
    if num%i==0 :
        sum+=1
    i+=1
if sum==0 and num!=0:
    print("Prime Number")
else:
    print("Not Prime Number")
"""
                                                                        #   Armstrong Number
"""sum=0
num=int(input("Enter the Value:;"))
temp=num
length=len(str(num))
while (temp):
    a=temp%10
    b=a**length
    sum+=b
    temp=temp//10
print(sum)
if sum==num and :
    print("Armstrong Number")
else:
    print("Not a Armstrong Number")"""
    
                                                            #    Maximum Number
"""
a=input("Enter value of a")
b=input("Enter value of b")
c=input("Enter value of c")
List=[a,b,c]
print(max(List))
"""


                                                                                    # Prime NUmber
"""i=2
sum=0
num=int(input("Enter the VAlue:"))
while(i<=(num//2)):
    if num%i==0:
        sum+=1
    i+=1
if sum==0 and num!=0:
    print("Prime NUmber")
else:
    print("Not prime")
"""
                                                                            #  Left_shift and Right_Shift BASICS
"""a=int(input("Enter number to do shifting:"))
b=int(input("Enter value for shifts:"))
print("Right shift:",a>>b)
print("Left shift:",a<<b)
"""
                                                                                            #   Strong Number
"""sum=0
num=int(input("Enter The calue to check it:"))
new=num
while(num):
    i=1
    temp=1
    number=num%10
    while(i<=num):
        temp=temp*i
        i=i+1
    sum=sum+temp
    num//10
if sum==new:
    print("Strong Number")
else:
    print("Not a Strong Number")
    """
    
                                                                                    #  Perfect Number
"""num=int(input("Enter the Number:"))                                                                                    
i=1
Store=[]
while(i<=(num//2)):
    if num%i==0:
        Store.append(i)
    i+=1
print(Store)
if sum(Store)==num :
    print("Perfect Number")
elif sum(Store)>num :
    print("Abundant Number")
else:
    print("Defeciant Number")"""
# i=0
# num=-12
# while(i<=num):
#     print(i)
# for n in range(0,-12):
#     print(n)

# num=int(input("ENter:"))
# n=abs(num)
# i=1
# sum=0
# while(i<=n):
#     if i%2==0:
#         sum+=i
#     i+=1
# if num>0:
#     print(sum)
# else:
# #     print(-sum)
# list=[]
# x=int(input("Enter:"))
# y=int(input("Enter:"))
# i=1
# sum=0
# if x==0 or y==0:
#     print("Sum:",0)
# else:
#     if x>y:
#         while(i<=y):
#             if x%i==0 and y%i==0 :
#                 list.append(i)
#             i+=1
#     elif (y>x):
#         while(i<=x):
#             if x%i==0 and y%i==0 :
#                 list.append(i)
#             i+=1
#     else:
#         print("Sum:",0)
# print(max(list))
# num=int(input("Enter:"))
# a=0
# b=1
# c=a
# for i in range(1,num):
#     a=b
#     b=c
#     c=a+b
#     print(c)
#     if c>=num:
#         break

# a=int(input("Enter:"))
# b=int(input("ENter:"))
# i=1
# while(i<=b):
#     print(a,"*",i,"=",a*i)
#     i+=1
#     if b<10:
#         pass
#     else:
#         break
# matrix=[
#     [1,2,5],
#     [4,7,40],
#     [89,67,34]
# ]

# transpose=[
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transpose[j][i]=matrix[i][j]
# for t in transpose:
#     print(t)

# a=[
#     [1,3,5],
#     [4,6,9],
#     [0,6,3]
# ]
# result=[
#     [0,0,0],
#     [0,0,0],
#     [0,0,0]
# ]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         result[i][j]=a[j][i]
# for n in result:
#     print(n)

# a=float(input("enter float number:"))
# j=1
# b=0
# while(j<a):
#     b+=j
#     c=f"{a:{j}f}"
#     print(c)
#     j+=1
# x=int(input("x:"))
# y=int(input("y:"))
# b=0
# for i in range(x,y):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
num=int(input('num:'))

temp=num
i=1
sum=0
# while(temp):
#     temp=temp%10
#     def factorial(temp):
#         if temp==0:
#             return 0
#         elif temp==1:
#             return 1
#         else:
#             return temp*factorial(temp-1)
    
#     b=factorial(temp)
#     sum+=b
#     temp=temp//10
# print(b)
# if sum!=num:
#     print("not strog number")
# else:
#     print("strong")

# count=1
# while(temp):
#     temp=temp%10
#     while(i<=temp):
#         i+=1
#         b=count*i
#     sum+=b
#     temp//10
# if temp==sum:
#     print(sum)
# else:
#     print("not strong number")
    
num=5
n=1
for i in range(num+1):
    for j in range(i+1):
        print(n,end=" ")
        n+=1
    print()






