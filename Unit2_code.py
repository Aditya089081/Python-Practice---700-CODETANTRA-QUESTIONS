#  selection and itterative statement help in Decision making and itration
# list=[]
# list2=[]
# num=int(input("Enter the value: "))
# i=0
# cout=0
# if num>0:
#     while(i<=num):
#         list.append(i)
#         i+=1
#     print('positive')
# if num<0:
#     while cout<=num :
#         list2.append(cout)
#         i+=1
#     print('negative')
# else:
#     print("Sum:",0)
#     print("Zero")

# print(sum(list))
# print(list)
# num=int(input("Enter the value:"))
# i=0
# sum=0
# while(num>=i):
#     sum=sum+i
#     i+=1
# else:
#     i=0
#     while num<i:
#         i=i-1
#         sum+=i
# print(sum)

# a=-12
# b=12
# print(abs(a))
# print(abs(b))

# num=int(input("ENter the number to find its Highest factor:"))
# i=1
# list=[]
# while(i<=num):
#     if num%i==0:
#         list.append(i)
#     i+=1
# print(list)
# sum=0
num=int(input("num: "))
# for i in range(1,num+1):
    
#         sum+=i
# print(sum)
# x=int(input("x: "))
# y=int(input("y: "))
# list1=[]
# if x==0 or y==0:
#     print("Value must be non zero")
# else:
#     if x>y:
#         for i in range(1,y):
#             if x%i==0 and y%i==0:
#                 list1.append(i)
#     elif x<y:
#         for i in range(1,x):
#             if x%i==0 and y%i==0:
#                 list1.append(i)
#     else:
#         for i in range(1,x):
#             if x%i==0:
#                 list1.append(i)
# print(list1)
"""a=0
b=1
i=0
c=0
sum=0
while(c<num):
    i+=1
    if i%2!=0:                                                                                    #Fibnocci Series Extended Form
        sum+=i
    a=b
    b=c
    c=a+b
    print(c)
print("c",c)"""

# state_capital_dictionary=dict()
# while True:
#     capital=input("Capital:").strip()
#     if capital.lower()=='end':
#         break
#     state=input("state: ").strip()
#     state_capital_dictionary[capital]=state
# for capital,state in state_capital_dictionary.items():
#     print("{%d}:{%d}"%(capital,state))
# x=int(input("x: "))
# y=int(input("y: "))
# i=1
# while(i<=y):
#     if i<=20:
#         print(f"{x} * {i} = {x*y}")
#     else:
#         break
#     i+=1

matrix=[
    [1,3,6],
    [4,6,2],
    [9,0,5]
]
transpose=[
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[1])):
        transpose[i][j]=matrix[j][i]
print(transpose)
    