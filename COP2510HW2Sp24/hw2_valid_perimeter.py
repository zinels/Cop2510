#Tanzeel Rahman
#U26664695

# This program takes input for the lengths of three edges of a triangle.
# It checks whether the input forms a valid triangle by ensuring that the sum
# of every pair of two edges is greater than the remaining edge.
# If the input is valid, it calculates and prints the perimeter of the triangle.
# Otherwise, it displays an error message stating that the input is invalid,
# and the perimeter cannot be calculated.


# Input from the user
edge1 = float(input("Enter length of edge1: "))
edge2 = float(input("Enter length of edge2: "))
edge3 = float(input("Enter length of edge3: "))

# Check if the input forms a valid triangle
if (edge1 + edge2 > edge3) and (edge1 + edge3 > edge2) and (edge2 + edge3 > edge1):
    # Calculate and display the perimeter
    perimeter = edge1 + edge2 + edge3
    print(f"The perimeter is {perimeter}")
else:
    # Display an error message for invalid input
    print("Perimeter cannot be calculated: the input is invalid.")


