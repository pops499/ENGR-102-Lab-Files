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
first_statement = a and b and c
second_statement = a or b or c

print("a and b and c:", first_statement)
print("a or b or c:", second_statement)

############ Part C ############
# Construct and evaluate Boolean expressions
thrid_statement = (a or b) and not (a and b)
fourth_statement= (a + b + c) in [1, 3]

print("XOR:", thrid_statement)
print("Odd number:", fourth_statement)
