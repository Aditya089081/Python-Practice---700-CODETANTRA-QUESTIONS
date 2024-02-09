"""# print('Hellow print("World")')
# # Its my Replet
# I = [")*(",")(&*())"]
# print(I[1] + I[0])
# print(I)
# a = 7
# print(type(a))
# print(0B10)
# print("Hellow's "World"")
# print(type(len("2343400")))
# print(len("10"))
# a,b = 9428,777
# b = 8987
# print(int(a))
# first_number = input("Enter the first No. :")
# second_number = input("Enter the Second No. : ")
# sum = first_number + second_number
# print((sum))
# print("a"[2])
# print(a + b)
# print(a - b)
# print(a * b)
# print(a % b)
# print(a ** b)
# b += 9

# print(not(b>9 and a>8))
# print((b<9 and a>8))
# print(not(b>9 or a>8))
# print(not(b<9 or a>8))
# str_1 = "Bhudsyhudw"
# str_2 = "s"
# print(str_2, "in", str_1, ":", str_2 in str_1)
# a = 3
# b = 3.0
# print(a == b)
# print(id(a))
# print(id(b))


#                         ''' BMI CALCULATOR '''
# Weight = int(input("Enter Your Weight in Kg: "))
# height = float(input("Enter Your Height in meter: "))
# BMI = (Weight/(height**2))
# print(("BMI: ", BMI))





# alphabet = 999898996.5333
# alphabet_4 = 999898999.5333
# alphabet_7 = 9998989934.5333
# alphabet8 = 99989890.5333
# print(round(alphabet, -1))
# print(round(alphabet_4, -10))
# print(round(alphabet_7, -1))
# print(round(alphabet8, -1))
# name = "Krishna"
# age = 12 
# Height = 3.4
# print("MY name is : ", name, "iam ", age, "Years Old","I was ", Height,"meter Long")
# print(f"My name is {name} . Iam {age} years old . Iam {Height} meter long")



#                  AGE CALCULATOR

# age = int(input("Enter Your Age: "))
# years_left = 100 - age
# days_left = years_left*365
# month_left = years_left*12
# weeks_left = years_left*53

# print(f"I am {age} years old . I have still {years_left} years , {days_left} dayds , {month_left} months and {weeks_left} weeks in my Whole Life")





# a = int(input("Enter Some Value Here: "))
# if(a % 2 == 0):
#   print("Its a Even Number")
# elif(a % 2 == 1):
#   print("its a Odd Number")
    
# else:
#   print("Nothing"




#                     Performance of STUDENT CHECK


# marks = int(input("Enter Your Marks: "))
# if (marks<=33):
#   print("Pass")
# elif(marks>33):
#   if (marks>33)and(marks<50):
#     print("WorkHard")
#   elif(marks>=50)and(marks<=70):
#     print("Focus and Complete Your Classwork")
#   elif(marks>70)and(marks<80):
#     print("Try to learn How to presrent Answer In Answer Sheet")
#   elif(marks>=80)and(marks<=90):
#     print("Litle bit Unfocuced")
# else:
#   print("Topper")







#                    Leap Year CALCULATOR 



# year = int(input("Enter Year, You wants to check: "))
# if(year % 4 == 0):
#   if (year % 100 == 0):
#     if (year % 400 == 0):
#       print("Leap Year")
#     else:
#       print("Not Leap Year")
#   else:
#     print("Leap Year")
# else:
#   print("Not Leap Year")


#        PIZZA ORDER SHOP
# size = input("What Size of Pizza You Wants to Buy (S/M/L): ")
# bill = 0
# if (size == "S")or(size == "s"):
#   bill += 99
# elif (size == "M")or(size == "m"):
#   bill += 149
# elif (size == "L")or(size == "l"):
#   bill += 199
# add_pepperoni = input("Do You Want Pepperoni (Y/N): ")
# if(add_pepperoni == "Y")or(add_pepperoni == "y"):
#   if (size == "s")or(size == "S"):
#     bill+=20
#     print("prize ofExtra Pepperoni is 20Rs ")
#   else:
#     bill+=50
#     print("Prize of Extra Pepperoni Is 50Rs")
# else:
#  bill  += 0

# print(bill)


#                     LOVE CALCULATOR
# male_friend = input("Enter Boyfriend Name: ")
# female_friend = input("Enter Girlfriend Name: ")
# Malefriend = male_friend.lower()
# Femalefriend = female_friend.lower()
# combined_name = Malefriend+Femalefriend

# t = combined_name.count('t')
# r = combined_name.count('r')
# u = combined_name.count('u')
# e = combined_name.count('e')
# true = t + r + u + e

# l = combined_name.count('l')
# o = combined_name.count('o')
# v = combined_name.count('v')
# e = combined_name.count('e')
# love = l + o + v + e

# love_score = int(str(true) + str(love))
# print(love_score)

# if(love_score <= 10):
#   print("Just BE Friend")
# elif(love_score > 10)and(love_score<=50):
#   print("Recent Relationsip")
# elif(love_score>50)and(love_score<=80):
#   print("Made for Each Other")
# else:
#   ("Couples")


# List Is Mutable = changeable
# Tuple is not mutable = not changeable

# roll_number = [1,2,3,4,5,6,7,9,8,8]
# name = ["Aditya", "Harsh", "Aman", "Anurag", "Anshika", "Anuj", "Yashveer", "Ankit"]
# # Roll_number=tuple(roll_number)
# # Name=tuple(name)
# # print(zip(roll_number,name))
# print(name[0:-1:2])           #Slicing
# roll_number.sort()
# print(roll_number)
# roll_number.reverse()
# # roll_number.end("0")
# # print(roll_number.get(00))
# print(roll_number)
# roll_number.append('New')
# print(roll_number)
# roll_number[1:4]=["newe",65,56]
# print(roll_number)
# roll_number.insert(2,89)
# print(roll_number)
# roll_number.extend([2,89,00])
# print(roll_number)
# # print(name.count("name"))
# name.remove("Aditya")
# roll_number.pop(5)
# print(name)
# # print(roll_number.count("8"))
# print(name)

# import random
# a=random.randint(1,9)
# print("a: ",a)
# b=random.randrange(1,9)
# print("b: ",b)
# print(a+b)
# c=random.random()        #float number between 0 and 1
# print("c: ",c)
# d = random.uniform(1,9)     #float number between given range
# print("d: ",d)
# l = [1,32,3,4,49,44]

# e = random.choice(l)               #random Value from LIst
# print("e: ",e)
# p = [1,32,3,4,49,44]
# f = random.shuffle(p)  
# print("f: ",f)



#                        TOSS PROGRAM 
# import random


# a = random.randint(0,1)
# print("a:",a)
# if (a == 1):
#   print("Head")
# else:
#   print("Tail")



#                         Bill PAYMENT CHOICE

# import random
# name = input("Enter name seperated by comma: ")
# Each_name = name.split(",")
# length = len(Each_name)
# choose = random.randint(0,length-1)
# print(f"{Each_name[choose]} Will Pay the Bill")



# list_1 = [1,2,4,5,[3,34,3,4],6,87]
# print(list_1[4][2])
# print(list_1[len(list_1)-3])




#                        STORE ROOM
# import random
# Amount = input("Enter the value you wants to Store: ")
# List_1 = [1,2,3]
# List_2 = [4,5,6]
# List_3 = [7,8,9]
# a = random.choice(List_1)
# b = random.choice(List_2)
# z = random.choice(List_3)
# c = [a, b, z]
# d = random.choice(c)
# s = c.insert(d,Amount)
# print(s)
# print(List_1)
# print(List_2)
# print(List_3)





#                                      Rock, Paper , Seasor GAME

# import random
# List_1 = [Rock,Paper,Seasor]
# Sum_1= 0
# List_2 = [Rock,Paper,seasor]
# Sum_2 = 0
# Chosen_1 = random.choice(List_1)
# Chosen_2 = random.choice(List_2)
# print("chosen_1",Chosen_1)
# print("chosen_2",Chosen_2)
# if (Chosen_1="Rock")or(Chosen_2="Rock"):
#   print("No Point")
# elif (Chosen_1 = "Rock")or(Chosen_2="Paper"):
#   print("Friend Won")
#   Sum_2 + 1
# elif (Chosen_1 = "Rock")or(Chosen_2="Seasor"):
#   print("You Won")
#   Sum_1+1
# elif (Chosen_1 = "Paper")or(Chosen_2="Paper"):
#   print("No Wins")
# elif (Chosen_1 = "Paper")or(Chosen_2="Rock"):
#   print("You Won")
#   Sum_1+1
# elif (Chosen_1 = "Paper")or(Chosen_2="Seasor"):
#   print("Friend Wins")
#   Sum_2+1
# elif (Chosen_1 = "Seasor")or(chosen_2="Paper"):
#   print("You Win")
#   Sum_1+1
# elif (Chosen_1 = "Seasor")or(Chosen_2="Rock"):
#   Sum_2+1
#   print("Friend Won")
# else:
#   print("No One WInns")


# tup_1 = ("New", 2, "How", 0, 8.98)
# tup_2 = (90)
# print(type(tup_2))
# tup = ()
# print(type(tup))
# # tup_1[1]=23
# tup.append("Once")
# print(tup)
# # print(tup_1)

# set_4 = ("New", "World", 30,50,90)
# set_3 = {"New", "World", 3,5,9}
# set_1 = {1,3,4,1,"5","New"}
# set_1.add((13,34,45))     # we cannot add List Because of Mutable
# print(set_1)
# set_1.remove("5")
# print(set_1)
# set_2= {1,2,3,4,5,6,7,8}
# print(type(set_2))
# print(len(set_1))
# # print(set_1.get("New"))
# set_1.discard("New")
# print(set_1)
# # set_1.pop("True")
# print(set_1.pop())


# print(set_1.union(set_2))
# print(set_1.union(set_2,set_3,set_4)) # Not Necessary That It is A set It may BE Tuple Also
# print(set_1 |set_2 |set_3)
# set_1.update(set_3)
# set_1.update([5, 6, 7,800 ,800,900 ])
# print(set_1)
# print(set_1.intersection(set_2,set_3))
# print(set_1&set_2)
# set_2.intersection_update(set_3)
# print(set_2)
# set_1.symmetric_difference(set_2)
# print(set_1)
# # print(set_1&set_2)
# set_a = {"f",8,"k"}
# set_b = {"h","u","g"}
# set_c = {"b","u","f"}
# print(set_c.difference(set_b,set_a))
# set_a.difference_update(set_b)
# print(set_a)
# print(set_a^set_b)
# set_a.symmetric_difference_update(set_b)
# print(set_a)
# set_1 = {29}
# print(type(set_1))
# set_2 = {1,2,3,4,5}
# print(set_1.isdisjoint(set_2))
# print(set_1.issubset(set_2))
# print(set_1<=set_1)
# print(set_1.issuperset(set_2))
# print(set_1>=set_2)
# set_1.clear()
# print(set_1)
# del set_1
# print(set_1)



#                               LOOPS
# Two Type + for Loop, While Loop
# squares = []
# lists = [1,4,5,20,7,8,0]
# for list in lists:
#     print(list)
#     square = list ** 2
#     squares.append(square)
#     print(squares)
#   # print("New "*list)
  
# for Variable_name in sequence
  
# a = [1,1,1,2,1,1,1,1]
# for i in a:
#   i=i+1
#   print(i)
# list = "Aditya"
# New= []
# for i in list:
#   # print(i)
#   New.append(i)
#   # print(New)
# print(New)
# sum=list[1]+list[2]+list[3]
# print(sum)


# ##########################         For - Else
# for i in a:
#   print(i)
#   if(i == "2"):
#     print('fgxxdhf')
#     break
# else:
# #   print('Completed')
# num = input("Enter the number: ")
# s= []
# l =0
# for e in num:
#   i = input("Enter: ")
#   i=int(i)
#   s.append(i)
#   l=l+i
# print(s)
# d =int(len(s))
# c = l/d
# print(c)


# ############################## While Loop ##########################################
# # list = [22,3,34,4,5,0]
# num=98
# while num<1000:
#   # print(list)
#   # list.pop()
#   num=num/2
#   i=i+1
#   # if list%5==0:
#     # break
# else:
# #   print("Compleated")
# num = int(input('Enter the vslue'))
# num1=0
# while num>0:
#   if(num%2==0):
#     num=num+1
#     print(num)
#     num=int(input("Enter Again"))


# (Loop Control Statement: break,pass,continue)===Only for 'for' and 'While' Loop

# list=['ankit','niket']
# list1= ['aman','anurag']
# for i in list:
#   for k in list1:
#     print(i,k)
#     if i=='ankit' and k == 'aman':
#       print("Nothing")
#       break
#     if i=='niket'and k=='anurag':
#       continue
#   print("Out fronm loop")
# print("New line")


# for i in range(100):
#   # print(i)
#   if i %30==0 :
#     break
#   if i %14==0 :
#     continue
#   if i%5==0:
#     pass
#   print(i)


# def function():
#   pass


# ##################     HANGMAN GAME  == Not Completed
# import random
# Name_List=["apple",'word','new']
# name=random.choice(Name_List)
# print(name)
# guess = []
# life=5
# for i in name:
#   guess.append("_ ")
#   guess.reverse
# print(guess)
# word = input('Enter Word: ')
# for k in name:
#   if k is word:
#     print("Correct")
#   else:
#     print('Not Pass')
    
# while name:
#   if word in name:
#     print(life)
#     print("pass")
#     print('Entered words: ',guess)
#     word = input('Enter Again')
#   else:
#     life.pop()


# def add(a,b):
#   c=a+b
#   print(f"Sum is {c}")
# add(5,7)
# add(90,0)

# def greet(name,dept,clas1="1"):
#   print(f"hii {name}")
#   print(f"Are you from {dept} department {clas1}")
# greet("jenny","CS","--")
# greet("Aditya","Civil","--")


# greet(name="Niket","fainance")
# import math
# def paint_Calaculation(Length,width,cover):
#   area=Length*width
#   no_of_cans=math.ceil(area/cover)
#   print("no of canns needed:", no_of_cans)
  
# Length=int(input("Height:"))
# width=int(input("Width:"))
# cover=3
# paint_Calaculation(Length,width,cover)

# is_prime="True"
# def prime_checker(number):
#   for i in range(2,number):
#     if number%i==0:
#       is_prime=False
# if is_prime==True:
#       print("It is a prme n umber")
# number=int(input("Enter the value"))




# ###############################Caesar Cipher

#        Encryption and Decryption
# alphabet=['a','b','c','d','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# Student_marks={
#   "niket":92,
#   "ankit":80,
#   "prince":78,
#   "parsh":67,

# }
# student_grade={}
# for i in Student_marks():
#   marks=Student_marks["i"]
#   if marks>90:
#       student_grade[i]="A+"
#   elif marks>80:
#       student_grade[i]="A"
#   elif marks>70:
#       student_grade[i]="B+"
#   elif marks>60:
#       student_grade[i]="B"
#   else:
#       student_grade[i]="fail"






# num=int(input("Enter the Number:"))                                                                                    
# i=1
# Store=[]
# while(i<=(num//2)):
#     if num%i==0:
#         Store.append(i)
#     print(Store)"""

# ment help in Decision making and itration
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
# elif num<0:
    
#     print('negative')
# else:
#     print("Sum:",0)
#     print("Zero")

# print(sum(list))
# print(list)

# list=[]
# i=0
# cout=0
# num=int(input("Entert the value: "))
# while(i<=num):
#   list.append(i)
#   i+=1
# su=sum(list)
# if num<0:
#   su=-(su)
# print(su)


# i=0
# num=-12
# while(i<=num):
#     print(i)
# for n in range(0,-12):
#     print(n)


# num=int(input("ENter the number to find its Highest factor:"))
# num2=int(input("Enter tyhe second"))
# i=1
# list=[]
# while(i<num):
#     if num%i==0:
#         list.append(i)
#     i+=1
# print(max(list))
# list=set(list)
# list2=[]
# while(i<num2):
#     if num2%i==0:
#         list2.append(i)
#     i+=1
# print(list2)
# list2=set(list2)
# print(list2)
# list.intersection(list2)

