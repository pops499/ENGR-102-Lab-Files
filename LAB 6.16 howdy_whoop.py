# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   6.16 LAB: Howdy Whoop
# Date:         4 September 2024
#

input_1 = int(input("Enter an integer: "))
input_2 = int(input("Enter another integer: "))
print()
for i in range(1,101):
    if (i % input_1 != 0) and (i % input_2 != 0):
        print(i)
    elif (i % input_1 == 0) and (i % input_2 != 0):
        print('Howdy')
    elif (i % input_2 == 0) and (i % input_1 != 0):
        print('Whoop')
    elif (i % input_1 == 0) and (i % input_2 == 0):
        print('Howdy Whoop')

#comment
