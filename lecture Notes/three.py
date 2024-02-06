#-----multiplpe input------
#option 1: use multiple input statementa
print('Enter 2 values(seperated by enter):') # have to press enter after entering each value
a = int(input())
b = float(input())
f = a*b
print(f'The product of the two numbers is: {f}')

#option 2: read all the iputs as strings, then convert as needed

c,d = input('Enter another 2 values(seperated by spaces) : ').split() #input takes strings as input as default
#.split() is a built in fucntion that sepeates the entries after a space
c = int(c)
d = float(d)
j = c*d
#could have done this in one line
####j = int(c) * float(d)####
#but doing so c and d is still a string for the whole code and it just got changed in the line for assigning value to j
print(f'The product of the new two numbers is : {j}')
#walrus operator with input
print('h is', h := int(input('Enter an integer(walrus operator):')))

print(f'k is {(k := int(input("Enter the integer(another way for walrus operator):")))}') 
# you can do this but it is very messy and you wouldnt want to do this


#-----importing modules------
import math, random
num = float(input('Enter a positive number:'))
sq = math.sqrt(num)
print(f'The squareroot of {num} is {sq:.7f}')#formatting it to 7 decimal places

#option 2 - import the specific method
from math import ceil, trunc
ce = ceil(sq) # dont need to use math. as i only imported the specific one i need
t = trunc(sq)
print(f'{sq} truncated is {t}')
print(f'{sq} rounded up is {ce}')

#option 3 - import all the methods using wildcard (*)
from math import *
fnum = fabs(sq)
print(f'The absolute value of {sq} is {fnum}')

p, l = map(int, input('Enter the numbers you want the random number inside of:').split())
r = random.randint(p,l)
print(f'Here is a random integer between {p} and {l} : {r}')


#python allows you to rename your modules within your files aka alias

#like this 
#from random import random as rand
# from the point forward where I gave it an alias I have to use the alias name