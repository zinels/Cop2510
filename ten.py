#week 7 lecture1

# a = 15 #global variable (defined outside of function or block) (bad idea)

# MAX = 100 #global constant --- great idea

# def main():
#     a = 5 #local variable -- defined inside function or block
#     print(f'In main: a is {a}')
#     fun1(a)
#     fun2(a)
#     fun3()
#     print(f'In main: a is {a}')

#     #parameters can be any object
#     list1 = [1, 2, 3, 4, 'five', 6]

# def fun1(x):
#     print(f'In fun1: x is {x}')
#     print(f'In fun1: a is {a}')

# def fun2(a):
#     a += 7
#     print(f'In fun2: a is {a}')
#     return #not necessary -- can be used to exit a function

# def fun3():
#     print(f'In fun3: a is {a}')
#     print(f'In main: MAX is {MAX}')

# def printlist(I):
#     for(i,e) in enumerate(I):
#         print(f'index: {i}, Element: {e}')


# main()



#default parameters -- have value assigned in its definition 
#once a default parameter is created, all subsequent parameters must be default
def printdate(month, day, year=2024, style=1): #here 2024 and 1 is the default value for these specific things if it is not given in the input
    if style == 1:
        print(f'{month}/{day}/{year}')
    elif style == 2:
        print(f'{day}/{month}/{year}')
    elif style == 3:
        print(f'{year}/{month}/{day}')
    else:
        print('Invalid format')

def main():
    #test function with default parameters
    printdate(2,20,2024,1)# no default parameters used
    printdate(2,21)#both default parameters used
    printdate(2,23,2025) #last default parameter used

    #use keyword argument
    printdate(2,20,style=3) #kept the year default value but changing the style
    printdate(style=1,year=2025,month=2,day=20) #they dont have to be in order using keyword arguments

main()