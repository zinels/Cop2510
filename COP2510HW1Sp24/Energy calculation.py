#Tanzeel Rahman
#U26664695
'''
The energy calculation program prompts the user to input the weight of water in kilograms, 
along with the initial and final temperatures. 
It computes the energy needed to heat the water using a specific formula, 
formats the result with commas for readability, and then outputs the energy value in joules.
'''
# Exercise 2: Calculating Energy
water_weight = float(input("Enter the amount of water (in kg): "))
initial_temp = float(input("Enter the initial temperature: "))
final_temp = float(input("Enter the final temperature: "))
energy = water_weight * (final_temp - initial_temp) * 4184
formatted_energy = "{:,}".format(int(energy))
print(f"The energy needed is {formatted_energy} Joules")
