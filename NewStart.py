# # pass plays no effect 
# s="news"
# for i in s:
#     print(i)

# a=int(input("First Number:"))
# b=int(input("Second Number:"))
# list1=[]
# count=0
# while(i<num):
#     if num%i!=0:
#         list1.append("0")
#     else:
#         list1.append("1")
#     i+=1
# if '0' in list1:
#     print("prime number")
# else:
#     print("not prime")

# for i in range(a,b+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)
                                                                                        # VOWEL CONSONENT NUMBER ALNUM
# a=input("Enter: ")
# a.lower()
# if a.isalnum():
#     if a.isalpha():
#         if a in "aeiouAEIOU":
#             print("vowel")
#         else:
#             print("Consonent")
#     else:
#         print("Number")
# else:
#     print("Not an Alphabet")
                                                                               
                                                     
                                                                                              #AMSTRONG NUMBER
# sum=0
# len=len(a)
# a=int(a)
# v=a
# while(v>0):
#     v=v%10
#     x=v**len
#     sum+=x
#     v=v//10
# print(sum)
# if sum==a:
#     print("Amstrong")
# else:
#     print("not amstrong")
# sum=0
# for i in a:
#     i=int(i) 
#     sum+=i
# print(sum)
# sum=0
# for i in a:
#     i=int(i)
#     for j in range(1,i):
#         b=i*j
#         sum=sum+b
# print(sum)
# if sum==int(a):
#     print("strong number")
# else:
#     print("not strong number")
# num=int(a)
# temp=int(a)
# i=1
# sum=0
# while(num):
#     temp1=num%10
#     while(i<=temp1):
#         fact=1*i
#         i+=1
#     sum=sum+fact
#     num=num//10
# print(sum)
        
    
# class person:
#     def __init__(self,name):
#         self.name=name
#     def develop(self):
#         print(f"Hellow Iam {self.name}")
        
# a=person("Model")

# b=person("Heloow")
# a.develop()

# class Area:

#     pi=3.14
#     def __init__(self,r):
#         self.radius=r
                        
                        
                        
                        
class rectangle():
    length=10
    def __init__(self,length,width):
        self.len=length
        self.wid=width
    def area(self):
        return self.length*self.wid
a=rectangle(10,10)
print(a.area())