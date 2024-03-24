#week 8 lecture 2

#arbitrary keyword arguments (section 6.15 in zybook)
def print_sandwich(meat, bread, **kwargs):
    print(f'{meat} on {bread}')
    for category, extra in kwargs.items():
        print(f'{category}:{extra}')
    print()

print_sandwich('turkey','sourdough', sauce = 'mayo')
print_sandwich('ham','wheat', sauce1 = 'mustard',veggie1='tomato',veggie2='lettuce')


#string slicing recap
name = 'Zinels void'
subname = name[5:11] #starting pos incl and ending pos is excl

#-----so far only in random module upper limit is incl

print(subname) #space is a position in string.

subname2 = name[-5:-2]
print(subname2)

subname3 = name[4:]
subname4 = name[:-3]
## so we can just have the first or last position defined and leave a blank.
print(subname3)
print(subname4)
#see section 7.3 for additional string methods

#list comprehension --- create a new list by accesing an original list

list1 = [1,2,3,4,5]
list2 = [i*10 for i in list1] #(expression) for (range variable) in (list name)
print(list1)
print(list2)

#you can use list comprehension with the tenary form
list3 =[m/2 if m>3 else m*2 for m in list1] #tenary form comes first, then loop
print(list3)

#you can use list comprehension with just an if statement
list4 = [n-1 for n in list1 if n<=2] #if statement appears last
print(list4)

#you can use list comprehension with input(but use carefully)

list5 = [(float(input('value ?'))) for p in list1]
print(list5)

#dictionary comprehension
d1 = {q:q**2 for q in range(10)}
print(d1)
print(d1[7])


#dictionary comprehension with multiple if statements
d2 = {k:v for (k,v) in d1.items() if v>4 if v%2 == 0} #2 conditions must be satisfied. it is treated as if there is an 'and' between the conditions
print(d2)