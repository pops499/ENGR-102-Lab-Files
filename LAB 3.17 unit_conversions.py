# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   3.17 LAB CONVERSIONS
# Date:         3 September 2024
#
print (f'Please enter the quantity to be converted:')
userinput = float(input())

#Conversion pounds to newtons
poundforce = (userinput) * 4.44822
print (f'{userinput:.2f} pounds force is equivalent to {poundforce:.2f} newtons')

#Conversion for Meters to Feet
meters = userinput * 3.28084
print (f'{userinput:.2f} meters is equivalent to {meters:.2f} feet')

#Conversion for Atmosphere to Kilopascals
atmosphere = userinput * 101.325
print (f'{userinput:.2f} atmospheres is equivalent to {atmosphere:.2f} kilopascals')

#Conversion for watts to BTU
watts = userinput * 3.412141633
print (f'{userinput:.2f} watts is equivalent to {watts:.2f} BTU per hour')

#Conversion for liters to gallons
liters = userinput * 15.850323140625
print (f'{userinput:.2f} liters per second is equivalent to {liters:.2f} US gallons per minute')

#Conversion for liters to gallons
Celcius = userinput * 9/5 + 32
print (f'{userinput:.2f} degrees Celsius is equivalent to {Celcius:.2f} degrees Fahrenheit')
