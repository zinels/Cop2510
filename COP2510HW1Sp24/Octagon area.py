#Tanzeel Rahman
#U26664695
# Exercise 1: Area of an Octagon
'''
This program prompts the user to input the side length of an octagon, 
calculates the area of the octagon using a formula that avoids using the math module, and then
formats and displays the result to 5 decimal places.
'''

side_length = float(input("Enter the side length of the octagon: "))
area = 2 * (1 + (2 ** 0.5)) * side_length ** 2
formatted_area = "{:.5f}".format(area)
print(f"The area of an octagon with side length {side_length} is {formatted_area}")
