# import os 
# if os.path.exists("text.txt"):
#     os.remove("text.txt")
# else:
#     print("this file does not exists")




# with open("text.txt") as f:
#     print(f.read())
 
    
# n = int(input("Enter an integer: "))

# if n % 2 != 0:
#     print("Weird")
# elif n % 2 == 0 and 2 <= n <= 5:
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")



# x = int(input("enter an interer:"))

# if x % 2 == 0:
#     print("it is odd")
    
# else:
#     print("it is even")




# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(num, "is Even")
# else:
#     print(num, "is Odd")



# num = int(input("enter a number:"))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")
    
# num = int(input("enter a number:"))
# for i in range(1,21):
#     print(f"{num}*{i} = {num*i}")

# 1.
# num = int(input("enter a number:"))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
    
# print("factorial of number of",num, "is",fact)
    
    
# 2.
# num = int(input("enter a number:"))
# fact = 1
# for i in range(1, num + 1):
#     fact *= i
    
#     print("factorial of number of",num, "is",fact)
    



# text = input("enter a word:")
# if text == text[::-1]:
#     print("this is polindrome")
# else:
#     print("this is not a polindrome")




# import random

# def get_choices():
#     player_choice = input("enter your choice (rock,paper,scissors):")
#     list = ["rock", "paper" ,"scissors"]
#     computer_choice = random.choice(list)
#     choices = {"player" : player_choice, "computer" : computer_choice}
#     return choices

# choices = get_choices()
# print(choices)



# #rock paper scissors

# import random

# def get_choices():
#     player_choice = input("enter your choice (rock,paper,scissors):")
#     list = ["rock", "paper" ,"scissors"]
#     computer_choice = random.choice(list)
#     choices = {"player" : player_choice, "computer" : computer_choice}
#     return choices

# def check_win(player,computer):
#     print(f"you choose {player}, computer choose {computer}".upper())
#     if player == computer:
#         return "it's a tie"
#     elif player == "rock":
#         if computer == "paper":
#             return "paper covers , you lose!"
#         else:
#             return "you wwwin"
#     elif player == "paper":
#         if computer == "scissors":
#             return "rock smashes , you win!"
#         else:
#             return "you lose"
    
# choices = get_choices()
# result = check_win(choices["player"], choices["computer"])
# print(result)





# a = 5 
# b = 2
# c = "10"
# print(a+b+int(c))



# p = "10"
# q = "20"
# print(int(p+q)-int(q+p))


# age = 23
# print(isinstance(age,float))

# print(10//2)


# num1 = 2 + 3j
# num = complex(2,3.032)
# print(num.real, num.imag)


#enumeration

# marks = [20, 24, 90, 45]
# for index, i in enumerate(marks,start=1):
#     print(i)
#     if (index == 2):
#         print("nithin")



# marks = ["nithi", "nithin", "shetty","nithinshetty"]
# for index, i in enumerate(marks):
#     print(f"{index + 1} : {i}")



# names = ["Alice", "Bob", "Charlie"]
# for index, name in enumerate(names):
#     print(index, name)



# from enum import Enum

# class state(Enum):
#     inactive = 0
#     active = 1
#     none = 3
#     inactive1 = 88
#     active1 = 17
#     none1 = 37
#     inactive2 = 876
#     active2 = 143
#     none2 = 3234
#     inactive3 = 765
#     active3 = 145
#     none3 = 33
# print(len(state))


# print("what is ur age")
# age = input()
# print(f"your age is",age)


#control statement

# Condition = False

# if Condition == True :
#     print("yes, it is")
# else:
#     print("no, its not") #inside the block {when if condition does't works}
# print("hello") # outside the block so its value print no matter what


# list
#(modifiable, ordered , allow dupes)

# dog = ["puppy","charlie","kitty"]
# dog[0] = "charly"
# dog.insert(3,"penny")
# print(dog)


# dog = ["Puppy","charlie","Kitty","bob", "Bonny"]
# dog.sort(key = str.lower)
# print(dog)


#tuple
# (not modifiable,ordered,alllow dupes)

# name = ("nithin", "raj", "charan")
# names = list(name)
# names.sort()
# print(names) #changing tuple to list ( b'cause it is immutable{not modify})


#dictinaries(key : value)
# (ordered, changeable, do not allow dupes)

# dog = {"name" : "luffy",
#        "crew name" : "strawhats",
#        "as" : "nika"
#        }

# print(list(dog.items()))


        #append
# dog = {"name" : "luffy",
#        "crew name" : "strawhats",
#        "as" : "nika"
#        }
# dog["ship name"] = "thousand sunny"
# print(dog)

        #deletion
# dog = {"name" : "luffy",
#        "crew name" : "strawhats",
#        "as" : "nika"
#        }
# del dog["as"]
# print(dog)


#sets
# (not order, mutable,no dupes allow)

# name = {"luffy", "nami", "sanji", "zoro", "ussop"}
# name2 = {"chopper", "robin","brook", "jimbe","zoro"}
# intersect = name.union(name2) #adding two sets
# intersect2 = name & name2 #intesect(common i both sets)
# intersect3 = name | name2 #combining 2 sets
# intersect4 = name - name2 #difference in 2 sets
# print(intersect)
# print(intersect2)
# print(intersect3)
# print(intersect4)


#functions

# def greet():
#     user_name = input("enter your name:")
#     user_age = input("enter your age:")
#     print(f"hello, i am  {user_name}, and i am {user_age} year old")
# greet()


# def change(value):
#     value["name"] = "luffy"
# val = {"name":"nami"} #dict is mutable
# change(val)
# print(val)

# def change(value):
#     value= "luffy"
# val = "nami" #val outside the function remains unchanged.
# change(val)
# print(val)

# def greet(name):
#     print("hello" , " " + name)
#     return
# greet("nithin")


# def greet(name):
#     return "hello " + name # return - sends a value back to where the function was called
# print(greet("nithin"))
    

#variable scope
    #depending the declaration i can decide is it local or global variable
# strength = 20
# def test():
#     print(f"total is {strength} ")
# print(test)


# age = 20
# def test():
#     print(age)
# print(age)
# test()


#nested functions 
    #(fun in fun)


# def talk(phrase):
#         def say(word):
#                 print(word)
        
#         words = phrase.split(" ")
#         for word in words:
#                 say(word)
                
# talk(" i am going to buy the milk product")



# def count():
#         count = 0
#         def increment():
#                 nonlocal count
#                 count = count + 1
#                 print(count)
#         increment()
# count()




#closures in nested functions

# def counter():
#         count = 0
#         def increment():
#                 nonlocal count
#                 count = count + 1
#                 return count
#         return increment  #increment fun is returning itself not the value
# increment = counter()
# print(counter()) #1
# print(counter()) #2
# print(counter()) #3
# print(counter()) #4



# def counter():
#         count = 0
#         def increment():
#                 nonlocal count
#                 count = count + 1
#                 return count
#         return increment()  #here increment function is returning fun val
# increment = counter()
# print(counter()) #1
# print(counter()) #1
# print(counter()) #1
# print(counter()) #1


#loops
  
# count = 0
# while count < 10:
#         print("the condition is true")   #while
#         count += 1

# items =[1,2,3,4]
# for index, i in enumerate(items):
#         print(index,i)


#break and continue

# items =[1,2,3,4]
# for i in items:
#         if i == 2:
#                 continue  #skip and continue to iterate
#         print(i) # 1,3,4



# items =[1,2,3,4]
# for i in items:
#         if i == 2:
#                 break #stops loop iteration
#         print(i)



# #classes
# class animal: #inheritance  (parent calss)
#         def animals(self):
#                 print("walking")
# class dog(animal):#inherited class (child class)
#         def __init__(self,name,age):
#                 self.name = name
#                 self.age = age
        
#         def bark(self):
#                 print("bow")
                
# yeah = dog("puppy",7)
# print(yeah.name)#puppy
# print(yeah.age)#age
# yeah.bark()#bow
# yeah.animals()#walking


#modules

# import module
# module.classic() #hello world

# from module import classic
# classic()#hello world

# from math import sqrt
# print(sqrt(16))#4.0



#arguments and command line

# import argparse

# parser = argparse.ArgumentParser(description='This program will print the name of my dog')
# parser.add_argument("-c", "--color", metavar="color", required=False, help="The color to search for")

# args = parser.parse_args()

# print(args.color)


# import sys 
# print(sys.argv)



#lambda functions

# number = lambda num: num * 2
# print(number(4))


#map(),filters() and reduce() - {global functions}

     # 1.map()

# num = [1, 2, 3]
# double = lambda a : a * 2
# result = map(double,num)
# print(tuple(result)) #(2,4,6)


# num = [1,2,3]
# def double(a):
#     return a * 2
# result = map(double,num)
# print(tuple(result)) #(2,4,6)

    #2.filter()
# treats 0 as False, and any non-zero number as True.

# num = [1, 2, 3,4,5,6]
# double = lambda a : a % 2 == 0
# result = filter(double,num)
# print(tuple(result)) #(2,4,6)


# num = [1, 2, 3,4,5,6]
# def double(n):
#     return n % 2 == 0
# result = filter(double,num)
# print(list(result)) #(2,4,6)

    #3.reduce()
# calculate the value of a sequence

# from functools import reduce

# expense = [ ("dinner", 1800),("lunch",2200)]
# sum = reduce(lambda a,b: a[1] + b[1], expense)

# print(sum)


#recursion
#calling a function in function

# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(6))


#decorators
#A decorator is a function that adds extra behavior to another function — without changing its actual code.

# def logtime(func):
#     def wrapper():
#         print("before")
#         val = func()
#         print("after")
#         return val
#     return wrapper
# @logtime
# def hello():
#     print("hello")
# hello()

# or

# def logtime(func):
#     def wrapper():
#         print("before")
#         val = func()
#         print("after")
#         return val
#     return wrapper
# def hello():
#     print("hello")
# logtime(hello)()


#docstring (used to documrnt in python)
#(special string used to document a function, class, or module in Python.)

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print(f"Hello, my name is {self.name}.")

#     def update_name(self, new_name):
#         self.name = new_name
    
# p = Person("Luffy")

# p.greet()
# p.update_name("zoro")
# p.greet()



# def greet(name):
#     """This function greets the user by their name."""
#     return f"Hello, {name}!"
# print(greet("chopper"))


#annotation
#let u specify expt otp data types of fun arg and return values


# def increment(n : int) -> int:
#     return n + 1

# print(increment(5)) #6


#exceptions

# try:
#     num = int(input("enter an integer :"))
#     result = num * 6
#     print(result)
# except :
#     print("invalid input")


# try:
#     result =  2 / 0
# except ZeroDivisionError:
#     print("cannot divisible by 0")
# finally:
#     result = 1
# print(result)


#list compression

# num = [1,2,3,4,5]

# num2 = [ n**2 for n in num]

# print(num2)


#polymorphism
# allows objects of different classes to be treated through the same interface

# class Animal:
#     def speak(self):
#         return "Some sound"

# class Dog(Animal):
#     def speak(self):
#         return "Woof!"

# class Cat(Animal):
#     def speak(self):
#         return "Meow!"

# animals = [Dog(), Cat(), Animal()]

# for animal in animals:
#     print(animal.speak())


#operator overloading

# class dog:
    
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def __gt__(self,other):
#         return True if self.age > other.age else False
    
# puppy = dog("puppy", 8)
# kitty = dog("kitty",7)

# print(puppy > kitty)
    