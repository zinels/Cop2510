# #loop else
# for n in range(1,1):
#     if n == 7:
#         continue #change to break to test effects of loop else
#     print(n, end = '')
# else: #run if the loop completes all or most of its iterations
#     print('The loop has ended.')

# #nested loops- for every 1 iteration of outer loop, the inner loop completes all its iterations
# digit1 = 0
# while digit1 <= 9: #outer loop
#     digit2 = 0
#     #break # we get not output 
#     while digit2 <= 9: #inner loop
#         print(f'{digit1}----{digit2}')
#         digit2 += 1
#         #break #here inner loop is interrupted, but not outer loop. 
#         #one break statement can only effect one loop
#     digit1 += 1 
#     break #outer loop runs once, inner loop completes its iterations

#enumerate function 
# for i, j in enumerate(range(1,11)):
#     print(f'{i}---{j}')
# print()
# #enumerate function gets both the index and values from a sequence container
# values = [4, 7, 9, 12, 16]
# for p, q in enumerate(values):
#     print(f'{p} + {q} = {p + q}')


#intro to user-created function
    
def main(): #function header
    x = int(input('Enter a value:'))   # local varaiable
    print(f'In main: value of x is {x}.')
    y = tripval(x)

#avoid this- python uses the most recent function of a function defined
# def main():
#     print('Hey this is another main.')

def tripval(x):#this is not the same x that is in the other function # a variable used in oen function is only used in that functtion 
    x *= 3
    print(f'In tripval: value of x is {x}.')
    return x
    #can also use like this
    # return x*3
main()


