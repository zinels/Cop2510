# #week5lec2
# #count controlled while loop
# i=1 #initialization
# while i<=5: #condition
#     print(f'i is {i}')
#     i=i+2 #update
#
# #while loop with walrus operator for input validation
# while (number:= int(input('Enter a positive number:')))<0:
#     print('Invalid.')
# print(f'The number is {number}')

#for loop (alternate to the counter controlled while loop)
for j in range (5):
    print(f'j is {j}')

for j in range(1,11):
    print(f'j is {j}')

for k in range(1,11,2): #starting value is 1, upper limit excl. step=2
    print(f'k is {k}')
print()
for k in range(20,1,-2): #reverse loop step=-2
    print(f'k is {k}')
print()

#create a count controlled loop with user input
n=int(input('How much to repeat?:'))
for a in range(n):
    print(f'{a}.Repeat!')
print()
names=['Jinx', 'Vi','Caitlyn', 5,11]
for b in names:
    print(f'Hi {b}!')
print()

# #wont work- careful with using range with lists- create a TypeError
# for b in range(names):
#     print(f'Hi {b}!')
# print()

#returns the values 0 to 4 based on the size of the list
for b in range(len(names)):
    print(f'Hi {b}!')
print()

#for loop with string
plan='Take a nap after class'
for p in plan:
    print(p, end='-')

#you can iterate over a substring
for p in plan[0:4]: #plan[0:4] refer to a substring 'Take' T is in 0; e is in 3,4 excl.
    print(p,end='-')
