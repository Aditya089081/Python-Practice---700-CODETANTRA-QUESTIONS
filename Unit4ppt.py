# a="forrmating"
# b=['1','4',"kjdkjd"]
# # print(a[-1:-len(a)-1:-1])
# # print(a[3:2])
# # a.center(20,"***&")
# # print(a.center(20,"*"))
# print(a.join(b))

list1=['3',"3ke","new"]
list2=["oei","kijf","odo"]
# a=dict(zip(list1,list2))
# print(a)
# str1="{"
# str2="}"
# for i in range(0,len(list1)):
#     for j in range(0,len(list2)):
#         b=str1,"+",list[i],":",list2[j],"+",str2
# print(b)
# list3=list1.copy
# print(list3 is not list1)
# a=(("enter here: ").split(","))
# # b=list(map(int()))
# print(a)
data1=(input("entrer: ").split(","))
# print(data1)
# data2=data1[::-1]
# print(data2)
# data2=[int(x) for x in data1]
# sum=0
# for i in data1:
#     i=int(i)
#     sum+=i
# print(sum)

x=(1,2,5,4,34)
print(tuple(enumerate(x)))
print(max(x))
print(sorted(x))