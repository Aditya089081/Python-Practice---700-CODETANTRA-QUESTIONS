# user=['Ram','Mahesh','UMA']
# username="Aditya"
# def sayhello(username):
#     greet = "Hello "
#     print(greet + username)
# for i in user:
#     sayhello(username)
#     # print(greet,i)
# for i in range(100):
#   # print(i)
#   if i %30==0 :
#     break
#   if i %14==0 :
#     continue
#   if i%5==0:
#     pass
#   print(i)
# simplicable(a,)
# Lemda Argument : Expression
# tax=lamda salary:
# salary=int(input("Pleease enter the value: "))
# print("Tax to be pAid is",tax(salary))
# doublenum=lambda a:a*2
# a=input("Enter the value: ")
# print(doublenum(a))

# tax = lambda salary: salary*1.3
# salary=int(input("Enter your Salary"))
# print(tax(salary))


# doublenum= lambda x: x*2
# x=int(input("Enter the value"))
# print(doublenum(x))


# list=[2,2,33,4,5]
# def squares(x):
#     return x**2
# print(list(map(squares, list)))
# num=int(input("Enter the value"))
# def square(num):
#     return num*num
# def double(num):
#     return 2*num
# square(double(num))
# print(square(double(num)))

# Student_marks={
#     "niket":92,
#     "ankit":80,
#     "prince":78,
#     "parsh":67,
# }
# student_grade={}
# for i in Student_marks():
#     marks=Student_marks["i"]
#     if marks>90:
#         student_grade[i]="A+"
#     elif marks>80:
#         student_grade[i]="A"
#     elif marks>70:
#         student_grade[i]="B+"
#     elif marks>60:
#         student_grade[i]="B"
#     else:
#         student_grade[i]="fail"

new = { 
       "start":{"Mon":99,"Tue":787},
       "How":00,
       "You":[9,98,977,{"m":"n","L":"k"}],
       "List1":('How you',"iuiu")}
# print(new)
# new["How"]={"How's":"New","Hows":67}
# print(new["How"]["How's"])
# print(type(new["List1"]))
# new["start"]["Tstart"]={'New Life'}
# print(new)
# del new["start"]["Tstart"]
# print(new)
# print(new["start"].pop("Tstart"))


# print(new["You"]["m"])
# i=[9,8,7,6,5,0]
# for n in i():
#        print(n)

# sum=0
# num = int(input("ENter:"))
# cout=1
# while cout<=num:
#        if cout%2==0:
#               sum=sum+cout
#        cout+=1
# print(sum)


# import math
# num=float(input("Enetr:")) 
# if num-float(num)>=0.5:
#        print(math.ceil(num))
#        print(math.trunc(num))

# a=int(input("Enter the Number: "))
# def checkNegativeNumber(a):
#        if a>0:
#               print("positve")
#        if(a==0):
#               print("Zero")
#        else:
#               print("Negative number")
# checkNegativeNumber()


# import CheckNegative
# x=int(input("Enter the valuwe:"))
# CheckNegative.CheckNegativeNumber(x)

# a='This is my first string'
# print(a)
# b=a.count("f")
# print(b)
# print(a(b,b+1))



# a= "pyhton is a high level language"
# b=a.capitalize()
# print(b)
# c=a.upper()
# print(c)
# d=a.title()
# print(d)
# e=a.split(" ")
# print(e)




# a=input()
# b=input()
# print(a*3+b)

# data=(input("Enter number with , between them ").split(","))
# list1=[]
# list1=list(data)
# print(list1)
# for i in list1:
#        i=i**2
#       int(list1.append(i))
# print(list1)
      

# list1=(input("ch: ").split(","))
# list2=(input("ch: ").split(","))
# if len(list1)!=len(list2):
#        print("list of different length")
# else:
#        outstr="{"
#        for i in range(len(list1)):
#               outstr+=f"{list1[i]} : {list2[i]},"
#        outstr=outstr[:-2]
#        outstr+="}"
#        print(outstr)


# list1=(input("list1: ").split(','))
# list2=(input("list1: ").split(','))
# list3=[]
# if len(list1)!=len(list2):
#        print("list are different length")
# else:
#        for i in range(len(list1)):
#               a=int(list1[i])-int(list2[i])
#               list3.append(a)
# # print(list3)
# x=(input().split(","))
# y=(input().split(","))
# # x.append(y)
# # print(x)
# x.extend(y)
# print(x)

# x=(input("x: ").split(","))
# y=(input("y: ").split(","))
# y.reverse()
# print(y)
# num=(input("num: ").split(','))
# sum=0
# for i in num:
#        i=int(i)
#        sum=sum+i
# print(sum)


# list=[]
# size=int(input("size:"))
# for i in range(1,size+1):
#        element=int(input("elements:"))
#        list.append(element)
# print(list)

# data=input("data: ").split(",")
# print(data)
# print(tuple(data))


# list1=[]
# data=(input("data:").split(","))
# for i in data:
#        i=int()
#        list1.append(i)
# print(sum(list1))
# # print(data)
# # tuple1=tuple(data)
# # print(tuple1)
# print("tuple:",tuple(data))


                                                        #      strong Number
# num=int(input("num: "))
# sum=0
# temp=num
# while(num):
#      number=temp%10
#      i=1
#      while(i<=number):
#             a=1*i
#             i+=1
#      sum=sum+a
#      num=num//10
# if temp==sum:
#        print("strong number")
# else:
#        print("not strong number")

# num=int(input("Bhanu Betichod enter: "))
# i=1
# temp=num
# sum=0
# while(num):
#        number=num%10
#        while(i<=number):
#               new=1*i
#               i+=1
#        sum=sum+new
#        num=num//10
# if sum==temp:
#        print('strong number')
# else:
#        print("not strong number")

# num=int(input("num:"))                                #Floyds Triangle
# n=1
# for i in range(1,num+1):
#        for j in range(1,i+1):
#               print(n,end=" ")
#               n+=1
#        print()
# num=int(input("inter"))
# list1=[]
# i=1
# while(i<num):
#        if num%i==0:
#               list1.append(i)
#        i+=1
# print(list1)
# print(sum(list1))
# if sum(list1)>num:
#        print("Aboundant")
# else:
#        print("deficient")


# num=int(input("Give the value:"))
# n=1
# for i in range(1,num+1):
#        for i in range(1,i+1):
#               print(n,end=" ")
#               n+=1
#        print()
# data1=(input("Enter").split(","))                           #gamma.app
# data2=(input("Enter").split(","))                           #gamma.app
# data3=(input("Enter").split(","))                           #gamma.app
# data4=(input("Enter").split(","))     #gamma.app
# dict1=dict(zip(data1,data2))
# dict2=dict(zip(data3,data4))
# key=input("key:")
# if key in dict1 and key not in dict2:
#        print("it is in dict1")
# elif key in dict2 and key not in dict1:
#        print("key is in dict2")
# else:
#        print("key is in both")

# list1=[1,3,2,5]
# list2=[1,3,5]
# # a=[x+y for x,y in list1,list2]
# # print(a)

# print(tuple(filter(lambda x:x%2,list1)))

# data=[1,2,4,6]
# data2=[4,6,7,9]
# dict1=dict(zip(data,data2))
# print(dict1)



# a=[4,4,4,4,4,43,33,5,0]
# for i in a:
#        i+=1
#        print(i)
# i=1
# while(i<87):
#        print(i)
#        i+=1









# from collections import defaultdict, deque

# def min_clicks(start, end, links):
#     graph = defaultdict(list)

#     # Create a graph from the given links
#     for link in links:
#         graph[link[0]].append(link[1])
#         graph[link[1]].append(link[0])

#     # BFS to find the shortest path
#     queue = deque([(start, 0)])
#     visited = set()

#     while queue:
#         current, clicks = queue.popleft()

#         if current == end:
#             return clicks

#         if current not in visited:
#             visited.add(current)
#             for neighbor in graph[current]:
#                 queue.append((neighbor, clicks + 1))

#     # If end page cannot be reached
#     return -1
# z=min_clicks(1,12,2)
# print(z)




































# # 1st ppt 
# write tags and world3school related to property
# mcq
# lecture

