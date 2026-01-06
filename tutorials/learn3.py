#adding two numbers

# a = input("enter a first integer:")
# b = input("enter a second integer:")
# c = int(a) + int(b)
# print(c)

#using function

# def add(a,b):
#   return a + b
# a=10
# b=20
# res = add(a,b)
# print(res)

#using lambda function

# x = lambda a,b : a + b
# print(x(3,5))

#max aamong them

# a = 20
# b = 30
# c = max(a,b)
# print(c)


# a = 20
# b = 30
# print(a if a>b else b)


# num = 50
# print(chr(num))

# char = "n"
# print(ord(char))

# fname = input("enter your firstname : ")
# lname = input("enter your lastname :")
# print(f"my firstname is {fname} and lastname is {lname}")

# str = "hello my name is {fname} {lname}".format(fname="nithin",lname="shetty")
# print(str)
# str = "hello my name is {0} {1}".format("nithin","shetty")

# list = [10,1010,334,65,7,777,8,466,3645,436]
# for i in range(len(list) - 1, -1, -1):
#   print(i,list[i])

# list1 = []
# for i in range(1,15):
#     list1.append(i)
# print(list1)

list2 =[i for i in range(1,15) if i % 2 == 1] 
print(list2)

