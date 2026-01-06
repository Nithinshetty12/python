                         #INTERMEDIATE


# string = "roronoa, zoro"
# strings = string.split()
# mmy_string = '   '.join(string)
# print(strings)
# print(mmy_string)
# list = [1,2,3,4,5,6]
# print(list)

# string = "roronoa"
# new_string = "you are %s" % string # old version format
# print(new_string)


# string = "roronoa"
# new_string = "you are {}".format(string)
# print(new_string)


# string = "roronoa"
# bounty = 40000
# new_string = (f"you are {string} and you hava bounty on your head is {bounty*2:.2f}")
# print(new_string)



#     collections

# counter
# from collections import Counter

# string = "aaaabbbcccdddggvknsnv"
# strings = Counter(string)
# # print(strings)
# print(set(strings.elements()))


# namecounter
# from collections import namedtuple
# tuple = namedtuple('tuple','x,y,z')
# pt = tuple(1,2,3)
# print(pt.x,pt.y,pt.z)

# from collections import namedtuple
# point =  namedtuple('point','x,y,z')
# pt = point(1,2,3)
# print(pt)

# OrderdDict

# defaultDict
# from collections import deque
# new = deque()

# new.append(1)
# new.append(3)
# new.appendleft(2)
# new.append(4)
# new.rotate(5)
# new.rotate(-6)
# new.extend([1,2,3])
# new.append(190)
# # new.clear()
# print(new)


# itertools

# from itertools import product

# a = [1,2]
# b = [5,6]
# prod = product(a,b, repeat=2)
# print(list(prod)) 


# from itertools import permutations

# a = [1,2,3]
# perm = permutations(a,3)

# for i in perm:
#     print(i)



# from itertools import combinations, combinations_with_replacement

# a = [1,2,3,4]
# comb = combinations(a,2)
# print(list(comb))
# comb_wr = combinations_with_replacement(a,2)
# print(list(comb_wr))


# accumulate

# from itertools import accumulate

# a = [1,2,3,4]
# acc = accumulate(a)
# print(list(acc))

# from itertools import accumulate

# a = [1,5,2,3,4]
# acc = accumulate(a, func=max)
# print(a)
# print(list(acc))



# groupby 

# from itertools import groupby
 
# def smaller_than_3(x):
#     return x < 3

# a = [1,2,3,4]
# group = groupby(a, key=smaller_than_3)

# for key, value in group:
#     print(key, list(value))


# from itertools import count,cycle,repeat


# for i in count(10):
#     print(i)
#     if i == 15:
#         break
    
# a = [1,2,3]
# for i in cycle(a):
#     print(i)

    
# a = [1,2,3]
# for i in repeat(a):
#     print(i)



# lambda

# def add_fun(x):
#     return x + 10
# print(add_fun(2))


# exp = lambda x: x + 15
# print(exp(10))


# mul = lambda  x: x * 10
# print(mul(3))


# a = [1,2,3]
# print(a * 2)


# a = [(59,22),(26,85),(76,34),(49,54)]
# a_lmdb = sorted(a,key=lambda x : x[1])
# print(a_lmdb)


# a = [(59,22),(26,85),(76,34),(49,54)]
# def sort_by_y(x):
#     return x[0]
# a_lmdb = sorted(a,key=sort_by_y)
# print(a_lmdb)


# a = [(59,22),(26,85),(76,34),(49,54)]
# a_lmdb = sorted(a,key=lambda x :x[0] + x[1])
# print(a)
# print(a_lmdb)

# a = [1,2,3,4]
# b = list(map(lambda x: x * 2,a))
# print(b)

# #list comprehension

# c = [i*2 for i in a ]
# print(c)

# a = [1,2,3,4]
# b = list(filter(lambda x: x % 2 !=0,a))
# print(b)


# exceptions

# x = 98
# if x < 100:
#     raise Exception("x should be within the range 100")

# try:
#     a = 5/4
#     b = 5 + "2"
# except TypeError as e:
#     print(e)
# except ZeroDivisionError as e:
#     print(e)
# else:
#     print("everything is fine")
# finally:
#     print("cleaning up...")


# logging

# import logging
# logger = logging.getLogger(__name__)
# logger.info("this is my module")


# import module


# json
# import json

# op = { "firstname" :"Monkey", 
#      "middlename" :"D",
#      "lastname" : "Luffy", 
#      "age" : "21", 
#      "crewname" :"strawhats"}

# op_json = json.dumps(op,indent=4,sort_keys=True)
# print(op_json)

# with open('op.json','w') as file:
#     json.dump(op,file,indent=4)

# json to array

# op_json = json.dumps(op,indent=4,sort_keys=True)
# # print(op_json)


# with open('op.json','r') as file:
#     json.load(file)
# op = json.loads(op_json)
# print(op)

# import json

# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         pass
    
# user = User('luffy',21)

# def encode_user(o):
#     if isinstance(o, User):
#         return {'name':o.name , 'age':o.age, o.__class__.__name__:True}
#     else:
#         raise TypeError
    
# from json import JSONEncoder

# class UserEncoder(JSONEncoder):
#     def default(self, o):
#         if isinstance(o, User):
#             return  {'name':o.name , 'age':o.age, o.__class__.__name__:True}
#         return JSONEncoder.default(self,0)
        
    
# userjson =UserEncoder().encode(user)
# print(userjson)


# random numbers

# import random

# a = random.normalvariate(0,1)
# print(a)

# import random
# mylist = list("ABCDEFG")
# a = random.sample(mylist,k = 4)
# print(a) #gives a list contains random elements in mylist


# random.shuffle(mylist)
# print(mylist)  #shuffle mylist

# import secrets
# mylist = list("ABCDEFG")
# a = secrets.choice(mylist)
# print(a)


# import numpy as np
# # a = np.random.randint(0,10,(3,3))
# # print(a)

# arr = np.array([[1,2,3],[2,3,4],[3,4,5]])
# np.random.shuffle(arr)
# print(arr)


# decorators
#         function that takes another function as input and extends or modifies its behavior without changing its code.


#     function decorators
    
    
# def decorator(func):
#     def wrapper():
#         print("start")
#         func()
#         print("end")
#     return wrapper
# @decorator
# def print_name():
#     print("alex")
# # print_name = decorator(print_name) >-- this line i == to the @decorator 
# print_name() # without arguments



# def decorator(func):
    
#     def wrapper(*args,**kwargs):
#         print("start")
#         result = func(*args,**kwargs)
#         print("end")
#         return result
#     return wrapper

# @decorator
# def mults(x):
#     return x * 5

# result = mults(10)
# print(result)

# import functools

# def repeat(num_times):
#     def  decorator_repeat(fun):
        
#         @functools.wraps(fun)
#         def wrapper(*args,**kwargs):
#             for _ in range(num_times):
#                 result = fun(*args,**kwargs)
#             return result
#         return wrapper
#     return decorator_repeat
            
# @repeat(num_times=3)
# def greet(name):
#     print(f'hello {name}')
    
# greet('nithin')


#     class decorators

# class countCalls:
#     def __init__(self,func):
#         self.func = func
#         self.num_calls = 0
        
#     def __call__(self, *args, **kwargs):
#         self.num_calls += 1
#         print(f'this is executed {self.num_calls} times')
#         return self.func(*args, **kwargs)




# @countCalls
# def say_hello():
#     print('hello')
    
# say_hello()
# # this is executed 1 times
# # hello
# say_hello()
# # this is executed 2 times
# # hello


# generators

# >>>- A generator is a special kind of function that allows you to generate values one at a time, instead of returning them all at once.

# def mygenerator():
#     yield 3
#     yield 1
#     yield 2
    
# g = mygenerator()

# value = next(g)
# print(value)
# value = next(g)
# print(value)
# value = next(g)
# print(value)

# print(sum(g))
# print(sorted(g))


# def countdown(num):
#     print("starting")
#     while num > 0:
#         yield num
#         num -= 1
        
# cd = countdown(4)
# value = next(cd)
# print(value)

# print(next(cd))
# print(next(cd))
# print(next(cd))


# import sys

# def firstn(n):
#     nums = []
#     num = 0
#     while num < n:
#         nums.append(num)
#         num += 1
#     return nums

# def mygenerator(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
# print(sys.getsizeof(mygenerator(10)))    
# print(sys.getsizeof(firstn(10)))

# def firstn(n):
#     return list(range(n))
# # print(sum(firstn(10)))


# def fibonacci(limit):
#     a , b = 0,1
#     while a < limit:
#         yield a
#         a, b = b ,a +b
#     return a,b

# fb = fibonacci(30)
# for i in fb:
#     print(i)


# # mygenerators = (i for i in range(10) if i % 2 == 0)
# # for x in mygenerators:
# #     print(x)

# age = int(input("enter you age:"))

# if age >= 18:
#     print("You are an adult")
# elif age <= 13:
#     print("You are a teenager")
# else:
#     print("You are a child")


# multiprocessing and threading

# from multiprocessing import Process
# import os
# import time


# def squ_num():
#     for i in range(100):
#         i*i
#         time.sleep(0.1)

# process = []
# num_process = os.cpu_count()

# #create a processess
# for i in range(num_process):
#     p = Process(target=squ_num)
#     process.append(p)

# #start
# for p in process:
#     p.start()

# #join
# for p in process:
#     p.join()

# print('end main')


#function arguments and parameters

# def fool(a,b,c):
#     print(a)
#     print(b)
#     print(c)
# fool(6,2,3)


# def fool(a,b,*args,**kwargs):
#   print(a,b)
#   for arg in args:
#     print(arg)
#   for key in kwargs:
#         print(key,kwargs[key])
  
# fool(1,2,3,4,5,six=6,seven=7)

# def fool():
#   global number
#   x = number
#   number = 3
#   print("number inside function:",x)

# number = 0
# fool()
# print(number)



# class Counter:
#     def __init__(self):
#         self.value = 1

#     def count_up(self):
#         self.value += 1

#     def count_down(self):
#         self.value -= 1

#     def __str__(self):
#         return f"Count={self.value}"

#     def __add__(self,other):
#         if isinstance(other,Counter):
#             return self.value + other.value
#         raise Exception("invalid type")

# count1 = Counter()
# count2 = Counter()

# count1.count_up()
# count2.count_up()

# print(count1 , count2)
# print(count1 + count2)



# class Car:
#     def __init__(self,make,model,year):
#         self,make = make
#         self,model = model
#         self,year = year

#     def __str__(self):
#         return f"{self.year} {self.make} {self.model}"
    
#     def __repr__(self):
#         return f"Car(make='{self.make}',model='{self.model}', year={self.year})"
    
# my_car = Car('bmw','m5',2025)

# print(str(my_car))
# print(repr(my_car))


# item = [1, 2, 3, 4, 5, 6]
# target = 4

# for n in item:
#     if n == target:
#         print(f"number {target} is found")
#         break


