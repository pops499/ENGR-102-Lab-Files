# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   4.18 LAB: Largest number
# Date:         11 September 2024
#
# inputs
print("Enter number 1:")
input_1 = float(input())
print("Enter number 2:")
input_2 = float(input())
print("Enter number 3:")
input_3 = float(input())

# Stuff to check if input 1 is the largest number
if (input_1 > input_2) and (input_1 > input_3):
    print(f'The largest number is {input_1}')

# Stuff to check if input 2 is the largest number
elif (input_2 > input_1) and (input_2 > input_3):
    print(f'The largest number is {input_2}')

#If input 1 or 2 were not the largest numbers, then input 3 must be the largest and there for does not need to be checked
else:
    print(f'The largest number is {input_3}')

