import math

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   2.9 LAB: Using Variables 
# Date:         27 August 2024
#

#stuff for reynolds number
print('This program calculates the Reynolds number given velocity, length, and viscosity')

print('Please enter the velocity (m/s):')
velocity_input = float(input())

print('Please enter the length (m):')
length_input = float(input())

print('Please enter the viscosity (m^2/s):')
viscosity_input = float(input())

ans = (((velocity_input) * (length_input)) / viscosity_input)

print (f'Reynolds number is {round(ans)}' )
print()

#--------------------------------------------------------------------------------------------------

#stuff for wavelength
print("This program calculates the wavelength given distance and angle")

print("Please enter the distance (nm):")
distance_input = float(input())

print("Please enter the angle (degrees):")
angle_input = (float(input()) * math.pi)/180

answer = 2 * distance_input * math.sin(angle_input)
print (f'Wavelength is {answer:.4f} nm')
print()

#--------------------------------------------------------------------------------------------------

#stuff for barrels
print("This program calculates the production rate given time, initial rate, and decline rate")

print("Please enter the time (days):")
day_input = float(input())

print("Please enter the initial rate (barrels/day):")
initial_rate_input = float(input())

print("Please enter the decline rate (1/day): ")
initial_decline_rate_input = float(input())

hc = 0.8 #hyperbolic constant

arps = (initial_rate_input/ (1 + hc * initial_decline_rate_input * day_input)**(1/hc))
print(f'Production rate is {arps:.2f} barrels/day')
print()
#--------------------------------------------------------------------------------------------------

#rocket equation stuff
print("This program calculates the change of velocity given initial mass, final mass, and exhaust velocity")

print("Please enter the initial mass (kg): ")
inital_mass_input = float(input())

print("Please enter the final mass (kg): ")
final_mass_input = float(input())

print("Please enter the exhaust velocity (m/s): ")
exhaust_velocity_input = float(input())

answer1 = exhaust_velocity_input * math.log(inital_mass_input/final_mass_input)
print(f'Change of velocity is {answer1:.1f} m/s')

