# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   4.17 LAB: Boolean expressions
# Date:         15 September 2024
#
############ Part A ############
# Input Boolean values from the keyboard
a_input = input("Enter True or False for a: ")
b_input = input("Enter True or False for b: ")
c_input = input("Enter True or False for c: ")

# Convert user input to Boolean values
a = a_input.lower() in ['true', 't']
b = b_input.lower() in ['true', 't']
c = c_input.lower() in ['true', 't']

############ Part B ############
# Evaluate Boolean expressions
expr1 = a and b and c
expr2 = a or b or c

print("a and b and c:", expr1)
print("a or b or c:", expr2)

############ Part C ############
# Construct and evaluate Boolean expressions
expr3 = (a or b) and not (a and b)
expr4 = (a + b + c) in [1, 3]

print("XOR:", expr3)
print("Odd number:", expr4)