import math
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   4.21 LAB:Calculate roots
# Date:         15 September 2024
#




input_A = int(input("Please enter the coefficient A: " ))
input_B = int(input("Please enter the coefficient B: " ))
input_C = int(input("Please enter the coefficient C: " ))



#stuff to see if its invalid
if input_A == 0 and input_B == 0:
    print("You entered an invalid combination of coefficients!")


if input_A == 0:
    root = (-1)*(input_C/input_B)
    print(f'The root is x = {root}')

stuff_under = math.pow(input_B, 2) - 4 * (input_A) * (input_C)

#stuff to determine if the result contains imaginary numbers
if stuff_under < 0:
    stuff_under = stuff_under * -1
    positive_quadratic = ((-1 * (input_B)) + math.sqrt(stuff_under)) / (2 * input_A)
    stuff_under = math.sqrt(stuff_under) * -1
    positive_quadratic = positive_quadratic * -1
    print(f'The roots  are x = {stuff_under} + {positive_quadratic}i and x = {stuff_under} - {positive_quadratic}i')


#stuff to calculate for the positive quadratic formula
elif input_A != 0 or input_B != 0:
    stuff_under = math.pow(input_B, 2) - 4 * (input_A) * (input_C)
    positive_quadratic = ((-1 * (input_B)) + math.sqrt(stuff_under)) / (2 * input_A)

#stuff to calculate for the negative quadratic formula
    stuff_under = math.pow(input_B, 2) - 4 * (input_A) * (input_C)
    negative_quadratic = ((-1 * (input_B)) - math.sqrt(stuff_under)) / (2 * input_A)

    #stuff to see if there is only one root
    if positive_quadratic == negative_quadratic:
        print(f'The root is x = {positive_quadratic}')
        
    elif positive_quadratic != negative_quadratic:
        print(f'The roots are x = {positive_quadratic} and x = {negative_quadratic}')
