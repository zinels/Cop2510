#Tanzeel Rahman
#U26664695
'''
This program asks the user to enter coordinates for two points and calculates the slope of the line connecting these points without relying on the math module. 
The calculated slope is formatted to 3 decimal places and presented in a user-friendly output.
'''

# Exercise 3: Slope of a Line
x1 = float(input("Enter the x-coordinate for point1: "))
y1 = float(input("Enter the y-coordinate for point1: "))
x2 = float(input("Enter the x-coordinate for point2: "))
y2 = float(input("Enter the y-coordinate for point2: "))
slope = (y2 - y1) / (x2 - x1)
formatted_slope = "{:.3f}".format(slope)
print(f"The slope for the line that connects two points ({x1}, {y1}) and ({x2}, {y2}) is {formatted_slope}")
