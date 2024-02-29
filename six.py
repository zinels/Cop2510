#there is 23 lines before it. Came to clas late
#it is about while loop and if else


#multiple selection
#standard nested if else structure

score = int(input('Enter your score:'))
if score >=90:
    grade = 'A'
else:
    if score >= 80:
        grade = 'B'
    else:
        if score >= 65:
            grade = 'C'
        else:
            if score >= 50:
                grade = 'D'
            else: #trailing else
                grade = 'F'
print(f'The grade is {grade}')

#if-elif-else structure (preferred)
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 65:
    grade = 'C'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'
print(f'The grade is {grade}')

#if elif is more efficient as it doesnt need to check every condition if it gets one right it stops.

#series of if statements
if score in range(90,101): #upper limit is exclusive in range function
    grade = 'A'
if 80 <= score <= 89:
    grade = 'B'
if score in range(65,80):
    grade = 'C'
if score in range(50,65):
    grade = 'D'
if score in range(0,50):
    grade = 'F'
print(f'The grade is {grade}')

#match case can be used for multiple selection

'''match expression:
    case pattern1:
        # Code block to execute if expression matches pattern1
    case pattern2:
        # Code block to execute if expression matches pattern2
    ...
    case patternN:
        # Code block to execute if expression matches patternN
    case _:
        # Code block to execute if expression doesn't match any of the above patterns
'''

match score // 10:
    case 10|9:
        print('The grade is A.')
    case 8:
        print('The grade is B.')
    case 7:
        print('The grade us C.')
    case 6: 
        print('The grade is D.')
    case _:#default case (same as trailing else)
        print('The grade is F.')