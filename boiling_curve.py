import math
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   5.5 LAB: Boiling Curve
# Date:         19 September 2024
#

#print statement
print("Enter the excess temperature: ")
x = float(input())

slope_1=(math.log(7000/1000)) / (math.log(5/1.3))

#stuff to see if its less than 1.3 and not available
if x < 1.3 or x > 1200:
    print("Surface heat flux is not available")

#slope for range between 1.3 and 5
if x >= 1.3 and x <=5:
    evaluate = 1000 * (x/1.3)**slope_1
    print( f'The surface heat flux is approximately {evaluate:.0f} W/m^2')

#slope for range between 5 and 30
slope_2=(math.log(1500000/7000)) / (math.log(30/5))
if x >= 5 and x <= 30:
    evaluate = 7000 * (x/5)**slope_2
    print(f'The surface heat flux is approximately {evaluate:.0f} W/m^2')

#slope for range between 30 and 120
slope_3=(math.log((25000)/(1500000))) / (math.log(120/30))
if x >= 30 and x <= 120:
    evaluate =  1500000 * (x/30)**slope_3
    print(f'The surface heat flux is approximately {evaluate:.0f} W/m^2')

#slope for range between 120 and 1200
slope_4=(math.log((1500000)/(25000))) / (math.log(1200/120))
if x >= 120 and x <= 1200:
    evaluate = 25000 * (x/120)**slope_4
    print(f'The surface heat flux is approximately {evaluate:.0f} W/m^2')


# comment
# commenefae
# comeefefef
# odfmadsofmads
#nosdfnadsjnf