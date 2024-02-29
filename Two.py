'''a,b = 5,4
c = a * b
print("the ans is", c)
#this is a comment

'''

rate = 0.6532434
print(f'Your new rate is {rate:%}') #format as a %
print(f'Your new rate is {rate:.3%}')#format as a % with 3 decimal places

#-------operator precedence-------
#()
#** 
#this symbolizes exponent
#* / // % # // operator divides then rounds down to the nearest integer
#+ - 

'''(), [], {} |Grouping operators
** |Power operator
*, /, % |Multiplication, division, and modulo operators
+, - |Addition and subtraction operators
<<, >> |Shift operators
<, <=, >, >=, ==, != |Comparison operators
&, |, ^ |Bitwise AND, OR, and XOR operators
and, or, not |Logical operators
in, not in, is, is not |Membership operators
-> |Lambda arrow
yield |Yield operator
'''


#-----update variables------
var = 10 #initialization or declaring a variable
var = var + 9 # update statement ; var = 10+9 = 19
print(f'var is {var}')

#------compound assignment operators----
#var += 8 # var = var + (8)
y = 3
##var *= y + 2
#var = var*(y+2)# var = var * y + 2

var += 8
print(f'var is {var}')
var -= 10
print(f'var is {var}')
var /= 0.2
print(f'var is {var}')
var //= 8 
print(f'var is {var}')
var %= 4
print(f'var is {var}')
var **= 2
print(f'var is {var}')



#-------input-------
####var2 = input()#no readable promt####
#default value of string is a string

name = input('Enter your name:')
print(f'Hello {name} !')


num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

ans = num1 + num2 # just adding or joining two strings

print(f'Your answer is {ans}')