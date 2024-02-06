#Tanzeel Rahman
#U26664695

# This program calculates the area of a flower, where the flower is formed by a square abutted
# on all four sides by semicircles. The user is prompted to input the radius of the flower,
# and the program uses the formulas for the area of a square and a semicircle. The total area
# of the flower is then computed by adding the square's area to four times the area of a semicircle.
# The constant pi is obtained from the math module, and the result is formatted to 4 decimal places
# before being displayed to the user.


import math

# Prompt the user to enter the radius of the flower
radius1 = float(input("Enter the radius of the flower: "))
radius = radius1 / 2
# Calculate the area of the flower (square + four semicircles)
area_square = radius1**2  # Calculate the area of the square
area_semicircle = (math.pi * radius**2) / 2  # Calculate the area of a single semicircle
total_area = area_square + 4 * area_semicircle  # Calculate the total area of the flower

# Format the result to 4 decimal places
formatted_area = "{:.4f}".format(total_area)

# Display the result
print(f"The area of the flower is {formatted_area}")

