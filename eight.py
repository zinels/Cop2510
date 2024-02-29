# #application of loops

# import random
# for i in range(3):
#     print(random.randint(1,6)) #integers: #both end points included
# print()
# for i in range(3):
#     print(random.randrange(1,7))#integers: #upper limit is excluded
# print()
# for i in range(3):
#     print(random.random())#floating point in range 0 (incl) to 1 (excl)
# print()
# for i in range(3):
#     print(random.uniform(2.5,4.0)) #random.uniform(a, b) is a function commonly found in programming libraries for generating a random floating-point number between two specified values a and b. The function is part of the random module in Python.

# import turtle
# #draw a square
# for j in range(4):
#     turtle.fd(100)
#     turtle.dot(5, 'blue')
#     turtle.left(90)

# turtle.clearscreen()

# turtle.shape('turtle')
# for c in range(36):
#     turtle.circle(75)
#     turtle.rt(10)
#     turtle.speed(50)

# turtle.clearscreen()

# #draw a series of circles
# turtle.shape('turtle')
# #turtle.speed(50)
# x,y = -300, 0
# turtle.setpos(x,y)
# for c in range(5):
#     turtle.pendown()
#     turtle.circle(50)
#     x += 100
#     turtle.penup()
#     turtle.setpos(x,y)
# turtle.done()


#break and continue loop 
for a in range(1,11):
    if a == 4:
        break #interrupted loop
print(a, end = '')

print()

for a in range(1,11):
    if a == 4:
        continue #skip iteration
    print(a, end = '')

# while True:
#     print('frolic!')
#     break
# #avoid this type of loop

# i = 1
# while True:
#     print('Hello.')
#     i = i +1
#     if i > 7:
#         break
# print()

#do this instead
i = 1
while i <= 7:
    print('Hello.')
    i += 1


# try: This block of code is used to wrap the code that might raise an exception. Python will attempt to execute the code inside the try block. If an exception occurs during the execution of this code, Python will immediately jump to the except block.

# except: This block of code is used to handle the exception that occurred within the try block. You specify the type of exception you want to catch after the except keyword. If the type of exception matches the one that occurred, the code inside the except block will be executed. If you don't specify a particular exception type, it will catch any type of exception.