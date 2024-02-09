"""Indexing
    Slicing
    Concatination
    Repitation
    Membership
    
    """
a="This is my first string"
# print(a)
# print(a[0])
#                     #  Slicing not Possible
# print(a.count(" "))
# print("Upper",a.upper())
# print("Capitalize",a.capitalize())
# print("title",a.istitle())
# print("lower:",a.lower())
# print("swapcase:",a.swapcase())
# print("center",a.center(40,"%"))
# print(a.split(" "))
# print(a.replace("my","our"))
# b=a.split(" ")
# print(b)
# c="."
# print(c.join(b))
# print(a.isalpha())
# print(a.isalnum())
# b="123c"
# print(b.isnumeric())
# print(a.isspace())
# print("new \"\\is\tworld \' ")
# num=(input("num: ").split(","))
# print("num:",num)
# a=list(map(int,num))
# print(a)
# sum=0
# for i in a:
#     sum+=i
# print(sum)
# b=list(map(lambda x:x*x,a))
# print(b)
# count=0
# for i in b:
#     count+=i
# print(count)
# a="{"
# b=[2,345,6]
# c=['dd','sd','er']
# for i in a:
#     for n in b:
#         d=f"{j}:{i},"
                                                                            #dictionary making layout
# print(a,d,a)
a=[10,20,30]
b=[5,10,15]
d=[]
# if len(a)!=len(b):
#     print("Enter list of equal length")
# else:
#     for i in range(1,len(a)):
#         c=a[i]-b[i]
#         d.append(c)
# print(d)
# def list_call():
#     if len(a)!=len(b):
#         print("please enter list of equal length")
#     else:
#         c=[abs(a-b) for a,b in zip(a,b)]
#     print(c)
# print(list_call())
# a.extend(b)
# print(a)
# a.insert(3,"new")
# print(a)
# a.remove("new")
# print(a)
# a.pop(3)
# print(a)
# a.sort()
# print(a)
# a.reverse()
# print(a)
# z=a.copy()
# print(z)
# print(a==z)
# list=[]
# size=int(input("inter:"))
# for i in range(size):
#     element=int(input("Element:"))
#     list.append(element)
# print(list)
# m=(2,56,676,[False,6,7]) # all read only element of tuple not nested list
# m[3][1]=1223344
# print(m)
# print(any(m))
# print(tuple(enumerate(m)))  #enumerate #enumerate
# k=tuple()
# print(all(k))
# print(any(k))

# m=(3,5,789,9)
# print(sorted(m))
# print(tuple("2345"))
# # print(min('e','y','a',' 4'))
# list=[]
# x=("357635")
# print(tuple(x))
# for i in x:
#     i=int(i)
#     list.append(i)
# print(sum(tuple(list)))
# m=tuple("33546")
# print(m)
# print(tuple(map(int,m)))
# data=tuple(map(int,input("Enter the value").split(",")))
# a="39"
# print(a.center(20,'*'))
# print(a.count("3"))
# a=(input("jj:"))
# print(a)
# a=[int(x) for x in a.split(",")]
# print(a)
# sum=[x**2 for x in a]
# print(sum)
list1=[3,45,6,9]
list2=[3,5,2,3]
# str=int(input("Key:"))
# a=dict(zip(list1,list2))
# print(a)
# for key in list1:
#     for value in list2:
#         b=f'{key}:{value},'
#     dic1= f'{str} {b}'
# dic1[-1]="}"
# print(dic1)

# if len(list1)!=len(list2):
#     print("enter equal length list")
# else:
#     for i in range(len(list1)):
#         str+=f"'{list1[i]}':'{list2[i]}',"
#     str=str[:-2]
#     str+="}"
#     print(str)
# a=[x-y for x,y in zip(list1,list2)]
# print(a)
# print(all((2,4,5,False)))
# print(any((2,3,68,False)))
# list3=[2,34,67,8,0]
# list4=[00,99,88,77]
# dict1=dict(zip(list1,list2))
# dict2=dict(zip(list3,list4))
# print(dict1)
# print(dict2)
# if str in dict1:
#     print("in dict 1")
# else:
#     print("dict2")
# data=['asd','asdf','ll']
# data1=['qqw','ldpe','ppr']
# data2=['Aasd','Sasdf','Dll']
# data3=['Eqqw','Gldpe','Fppr']
# dict1=dict(zip(data,data1))
# a=sorted(dict1)
# print(dict1)
# # a=dict1.keys()
# print(a)
# dict2=dict(zip(data2,data3))
# b=sorted(dict2)
# print(b)
# s=sorted(dict1.items())
# print(s)
# s=sorted(dict1.items(),key=lambda x:x[0])
# print(s)
# a={x**2 for x in range(1,90) if x!=89}
# a={x**2 if x%2==0 else x**3 for x in range(1,11)}
# print(a)
# print(sorted(a))
# def cd():
#     cod={}
#     ocd={}
#     col=[(65,'A'),(66,'B'),(67,'C')]
#     for ov,char in col:
#         cod[ov]=char
#         ocd[char]=ov
#     return cod,ocd
# cod,ocd=cd()
# print(sorted(cod.items()))
# print(sorted(ocd.items()))
# set1=set(list1)
# set2=set(list2)
# # element=int(input("Element:"))
# # set2.discard(element)
# # print(set2)
# set1.difference(set2)
# print("difference:",sorted(set1))
# set1.difference_update(set2)
# print("Difference_update:",sorted(set1))

# num=int(input("Write:"))
# for i in range(num):
#     for j in range(num-i+1):
#         print("",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()
# from math import factorial

# num=int(input("Write:"))
# for i in range(num):
#     for j in range(num-i+1):
#         print(end="")
#     for j in range(j+1):
#         print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
#     print()

# n=5
# for i in range(n):
#     print(""*(n-1),end=" ")
#     print((" ".join(map(str,str(11**i)))))
# i=0
# for q in range(num):
#     for w in range(num-q+1):
#         print(end=" ")
#     for e in range(q+1):
#         if w==0 or q==0:
#             i=1
#         else:
#             i=i*(q-w+1)//w
#             print(i,end=" ")
#     print()


