# name=int(input("): "))
# class new:
#     def __self__(self,name):
#         self.name=name
#     def new(self):
#         print(self.name)
# a=new(name)
# a.name="Aditya"
# a.__self__()

# class Student:
#     pass
# Stud_1=Student()
# Stud_1.name=input("Name: ")
# Stud_1.Branch=input("Branch")
# Stud_1.rank=input("rank: ")
# print(Stud_1.name)
# print(Stud_1.Branch)
# print(Stud_1.rank)

# class new:
#     def __init__(self,name,class_1):
#         self.name=name
#     def detail(self):
#         print(self.name,self.class_1)
# a=new("Aditya")
# a.name="Aditya"
# a.class_1=23
# a.detail()

# class Student:
#     pass
# Stud_1=Student()
# Stud_2=Student()
# Stud_1.name=input("Name: ")
# Stud_1.age=input("Age: ")
# Stud_1.degree=input("Degree: ")
# print


# class Information:
#     pass
# a=Information()
# name=input()
# a.name=name
# a.salary=input()

# class n:
#     def __init__(self,name):
#         self.name=name
#     def new(self):
#         print(self.name)
# a=n("Aditya")
# a.name="Adarsh"
# a.new()
# class Manager:
#     def __init__(self,Name,Age):
#         self.name=Name
#         self.age=Age
# Name=input()
# age=int(input())
# manager_1=Manager(Name,age)
# print(manager_1.name,manager_1.age)
# class Simple:
#     def meathod_1(self,model,ragistration):
#         self.model=model
#         self.ragistration=ragistration
#     def meathod_2(self):
#         return self.model
#     def meathod_3(self):
#         return self.ragistration
# model=input("Model: ")
# reg=input("Reg: ")
# # ragistration=input()
# a=Simple()
# a.meathod_1(model,reg)
# print(a.meathod_2(),a.meathod_3())






# 1. Write a Python program to create a class representing a Circle. Include methods to calculate its area and perimeter.


# Solution 1=
# import math
# class Circle:
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return math.pi*self.radius**2
#     def peremeter(self):
#         return 2*math.pi*self.radius
# radius = float(input("Enter Here Radius: "))
# circle_1=Circle(radius)

# area=circle_1.area()
# peremeter=circle_1.peremeter()
# print("area: ",area)
# print("perementer: ",peremeter)


# import math

# # Define a class called Circle to represent a circle
# class Circle:
#     # Initialize the Circle object with a given radius
#     def __init__(self, radius):
#         self.radius = radius
    
#     # Calculate and return the area of the circle using the formula: π * r^2
#     def calculate_circle_area(self):
#         return math.pi * self.radius**2
    
#     # Calculate and return the perimeter (circumference) of the circle using the formula: 2π * r
#     def calculate_circle_perimeter(self):
#         return 2 * math.pi * self.radius

# # Example usage
# # Prompt the user to input the radius of the circle and convert it to a floating-point number
# radius = float(input("Input the radius of the circle: "))

# # Create a Circle object with the provided radius
# circle = Circle(radius)

# # Calculate the area of the circle using the calculate_circle_area method
# area = circle.calculate_circle_area()

# # Calculate the perimeter of the circle using the calculate_circle_perimeter method
# perimeter = circle.calculate_circle_perimeter()

# # Display the calculated area and perimeter of the circle
# print("Area of the circle:", area)
# print("Perimeter of the circle:", perimeter)




# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.


# solution=2

# class Car:
#     def setdetails(self,name,model,registration):
#         self.name=name
#         self.model=model
#         self.registration=registration
#     def getdetails(self):
#         print(self.name,self.model,self.registration)
# name=input("Name of Car: ")
# model=input("MOdel of car: ")
# reg=int(input("Enter the reg. no: "))
# Hundai=Car()
# Hundai.setdetails(name,model,reg)
# Hundai.getdetails()
# class Start:
#     def __init__(self,name,Age,email):
#         self.name=name
#         self.Age=Age
#         self.email=email
#     def studentdetails(self):
#         return self.name,self.Age,self.email
# name=input("Name: ")
# Age=input("Age: ")
# email=input("Email: ")
# New=Start(name,Age,email)
# print(New.studentdetails())

# class MeathodOverloadingExample:
#     def Greeting(self,name=None,wish=None):
#         if name!=None and wish!=None:
#             print(f"Hello {name} {wish}")
#         elif name!=None and wish==None:
#             print(f"Hello {name}")
#         else:
#             print(f"Hello Mr. How are you?")
# name=input("Enter the Name: ")
# wish=input('Enter your wishing"s : ')
# Person=MeathodOverloadingExample()
# Person.Greeting(name,wish)

# class car:
#     def setenginemodel(self,engine):
#         self.engine=engine
#     def getenginemodel(self):
#         print(self.model)
# class Honda(car):
#     def setcarmodel(self,model):
#         self.model=model
#     def getcarmodel(self):
#         print(self.model)
# mycar=Honda()
# model=input("model: ")
# engine=input("ENter the Enginne: ")
# mycar.setcarmodel(model)
# mycar.setenginemodel(engine)
# mycar.getcarmodel()
# mycar.getenginemodel()

# class vehicle():
#     def __init__(self,name,price,regno):
#         self.name=name
#         self.price=price
#         self.regno=regno
# class car(vehicle):
#     def __init__(self,name,price,regno,gear):
#         self.name=name
#         self.price=price
#         self.regno=regno
#         self.gear=gear
# class boat(vehicle):
#     pass
# class hover(boat,car):
#     def __init__(self,name,price,regno,gear):
#         super().__init__(name,price,regno,gear)
# a=vehicle("Toyota",254455,"Car")
# b=boat("Maruti",4567,"Car1",)
# v=hover("Nano",987,"Car2","Manual")
# print(type(a).__name__)  
# from datetime import date      
# class Person:
#     def __init__(self,name,country,date_of_birth):
#         self.name=name
#         self.country=country
#         self.date_of_birth=date_of_birth
#     def checkage(self):
#         today=date.today()
#         age=today.year - self.date_of_birth.year
#     if today<date(today.year,self.date_of_birth.month,self.date_of_birth):
#         age-=1
#         return age
#     person1=Person("ferdi Odilia","France",date(1976,7,9))
#     print(Person1.country)

# from datetime import date

# # Define a class called Person to represent a person with a name, country, and date of birth
# class Person:
#     # Initialize the Person object with a name, country, and date of birth
#     def __init__(self, name, country, date_of_birth):
#         self.name = name
#         self.country = country
#         self.date_of_birth = date_of_birth
    
#     # Calculate the age of the person based on their date of birth
#     def calculate_age(self):
#         today = date.today()
#         age = today.year - self.date_of_birth.year
#         if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
#             age -= 1
#         return age

# # Example usage
# # Create three Person objects with different attributes
# person1 = Person("Ferdi Odilia", "France", date(1962, 7, 12))
# person2 = Person("Shweta Maddox", "Canada", date(1982, 10, 20))
# person3 = Person("Elizaveta Tilman", "USA", date(2000, 1, 1))

# # Access and print the attributes and calculated age for each person
# print("Person 1:")
# print("Name:", person1.name)
# print("Country:", person1.country)
# print("Date of Birth:", person1.date_of birth)
# print("Age:", person1.calculate_age())

# print("\nPerson 2:")
# print("Name:", person2.name)
# print("Country:", person2.country)
# print("Date of Birth:", person2.date_of birth)
# print("Age:", person2.calculate_age())


# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def sub(self):
#         return self.a-self.b
#     def mul(self):
#         return self.a+self.b
#     def devide(self):
#         if self.b!=0:
#             return self.a/self.b
#         else:
#             return ("Can Not devide by Zero")
# Calculating=Calculator(23,3)
# print(Calculating.devide())
# import math
# class Shape:
#     def __init__(self,radius):
#         self.radius=radius
#     def circlearea(self):
#         return math.pi*self.radius**2
#     def circleperimeter(self):
#         return 2*math.pi*self.radius
# class Shape2:
#     def __init__(self,side):
#         self.side=side
#     def squarearea(self):
#         return self.side**2
#     def squareperimeter(self):
#         return self.side*4
# Area=Shape2(30)
# print(Area.squarearea())
# class Vehicle:
#     def __init__(self,name,price,regno):
#         self.name=name
#         self.price=price
#         self.regno=regno
# class car(Vehicle):
#     def __init__(self,name,price,regno,gear):
#         super().__init__(name,price,regno)
#         self.gear=gear
# class boat(Vehicle):
#     pass
# class hover(car,boat):
#     def __init__(self,name,price,regno,gear):  
#         super().__init__(name,price,regno,gear)
    
# a=car(1,2,3,4)
# b=boat(5,6,7)
# c=hover(8,9,0,00)
# print(type(b).__name__,a.name,a.price,c.gear)

# class new :
#     def new1(self,name):
#         print(name)
#         self.name=name
#     def new1(self,name,Age):
#         print(name,Age)
# a=new()
# a.new1("Aditya")
# class car:
#     def setbrandname(self,name):
#         self.name=name
#         # self.model=model
#     def getbrandname(self):
#         print(self.name)
#     def setmodelname(self,model):
#         self.model=model
#     def getmodelname(self):
#         print(self.model)
# class Accord(car):
#     def setbrandname(self,name):
#         super().setbrandname(name)
#     def getbrandname(self):
#         super().getbrandname()
#     def setmodelname(self,model):
#         super().setmodelname(model)
#     def getmodelname(self):
#         super().getmodelname()
# a=Accord()
# name=input("Enter the Name: ")
# model=input("Entert the model: ")
# a.setbrandname(name)
# a.setmodelname(model)
# a.getmodelname()
# a.getbrandname()
# class Abstract(object):
#     def foo(self):
#         raise NotImplementedError("Subclass must overide the foo")

# class derived(Abstract):
#     super().foo()
#     print("hurrey")
# a=derived()
# a.foo()
# class Animal:
# import checkNegavtiveNumber:

#     def checkNegativeNUmber()
    
# class Animal:
#     def __init__(self,name="This Animal"):
#         self.name=name    
#     def eat(self,food="Grass"):
#         print(self.name,"eats",food)
# class Mammel(Animal):
#     def eat(self,food="Grass"):
#         print(self.name,"does not eat. it only drinks")
# class WingedAnimal(Animal):
#     super
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def setdetails(self,__group,__report):
#         self.__report=__report
#         self.__group=__group
#     def getdetails(self):
#         print(self.name,self.age,self.__group,self.__report)
# name=input("Name of Student:")
# Age=int(input("Age of Student: "))
# __group=input("Enter the group: ")
# __report=input("Rnter the Report: ")
# a=Student(name,Age)
# a.setdetails(__report,__group)
# a.getdetails()

# class student:
#     name=input("Enter Here: ")
#     age=input("Here: ")
#     __group=input(": ")
#     __report=input(": ")
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def setdetails(self,__group,__report):
#         self.__group=__group
#         self.__report=__report
#     def getdetails(self):
#         print(self.name,self.age,self.__report,self.__group)
# new=student("new",34)
# new.setdetails("errt","djfj")
# new.getdetails()

# def main():
#     input_list=input("Enter the number with spces: ").split()
#     original_list=[int(x) for x in input_list]
#     original_list.sort()
#     print("Original List: ",original_list)
#     print("Scending order: ",sorted(original_list))
#     print("Decending Order: ",sorted(original_list, reverse=True))
# if __name__=="__main__":
#     main()
# def right_anglr(height):
#     for i in range(1,height+1):
#         print("*"*i)
# height=int(input())
# right_anglr(height)

def triangle(n):
    for i in range(1,n+1):
        a=" "*(n-i)
        b="* "*i
        print(a+b)
c=int(input())
triangle(c)