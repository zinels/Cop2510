#week 4 lecutre 1

#intro to dictionaries(mapping  type)
#use key value pair

cutenames = {'cat':'floof', 'sanke' :'danger noodle'}

#use the key to access the value
print(f"A cute name for a cat is {cutenames['cat']}")
#print the full dictionary
print(cutenames)

#add or change key/value pair
cutenames['dog'] = 'pupper'
print(cutenames)
cutenames['dog'] = 'doggo'
print(cutenames)

#delete entry
del cutenames['dog']
print(cutenames)


#dictionaries can include other containers
scores = {'Annie':[89, 92, 97], 'Brad': [88,91,98]}
print(scores['Annie'])

#add another square bracket to get the specific value
print(scores['Annie'][2])

#to get the keys from a dictionary, use keys method
print(scores.keys())

scores['Annie'].append(87)
print(scores)

#you can convert containers using built in functions

#list() <---- convert another container to a list ; use [] to create an empty list
#tuple() <---- convert another container to a tuple; use () to create an empty tuple / but thats kinda meaningless
#set() <---- convert another container to a set ; use set() to create an empty set


#dict() <----- create an empty dictionary ir initialze a new dictionary

#membership operators

#in, not in # <----- used for containers.

char = input('Enter a letter number of symbol:')
name = 'Zinels'

#python is very strict with indentations

if char in name:
    print(f"The character '{char}' is in the {name}")
else:
    print(f"The character '{char}' is not in {name}")

#identity operators : is, is not(used to check if two variables refere to the smae object)
w = 500
x = 1000
y = w+w
z = x

if z is x:
    print('Z and X are bound to the same object')
if z is not y:
    print('Z and Y are not bound to same obejct')
   
#value of z and y are same but not bound to same object in memory


#comparison operators 
#<,<=,>,>=,==,!=

#logical operators <---- not and or
temp, rain = input('Enter the temperature:'), input('Is it raining? (yes/no):')
temp = float(temp)

if rain == 'yes':
    raining = True
else:
    raining = False

if temp > 70 and not raining: 
    print('Go hiking.')
else:
    print('Stay inside.')