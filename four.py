#Week 3 lecture 2
#intro to types(data structures) in python

#strings , lists, sets, tuple, dictionaries

#strings-sequence type(contents have order), use index to access specific value
#first position/index is 0, last position is -1

name = 'Cloud Strife'
print(f'The value in the first position of {name} is {name[0]}')
print(f'The value in the last position of {name} is {name[-1]}')

#strings are immutable- characters cannot be changed once the string is created
#name[2] = 'k' ----does not work

#we can update a string by changing its reference(location in memory) via the same variable

name = 'Tife Lockheart'
print(name)

#lenfunction - function used to obtain the size of a list

print(f'The name {name} has {len(name)} characters')

#lists- containers (structures that can hold different types of data)
#lists are also a sequence: contents are ordered

items = ['cheese', 'eggs', 2, 5.6, 'orange juice']
print(items)
print(items[1])#access a specific value from the list
print(items[1][3])#access a specific character from the specific value

#lists are mutable

items[-2] = 'milk' #started from the left. items[3] = items[-2]

print(items)


#useful methods for lists : append, pop, remove

items.append('bacon')
print(items)

#items.pop #remove last value in the list(default)
items.pop(2)#remove a value by specifying the position
print(items)

#remove- remove value from list
items.remove('eggs') #removes the first occurance of the value in the list
print(items)


#lists within list
nlist = [1,2,3,[4,5,6,7], 9,10]
print(nlist)
print(nlist[3][0])


#tuple- sequence and container, but immutable

somethings = (1,'A', 5.1, 9)
print(somethings[1])

#somethings[1] = 'B' #not possible

constant = (200,) #giving a comma will make it a tuple
print(constant)

#constant[0] = 300 # not possible as it is a tuple
#constant = 300 # here the whole variable data type got changed. so value will be changed



#sets - container, not a sequence. Use for storing unique values
s1 = {4,5,2, 'six', 1,3,4,2}#duplicates are removed when stored

print(s1)

#print(s1[1]) # doesnt work as sets are not sequence

s1.add(6.0)
s1.remove('six')
print(s1)
s1.pop() #removes a random element everytime
print(s1)
