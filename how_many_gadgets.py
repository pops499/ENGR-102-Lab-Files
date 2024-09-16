# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   4.20 LAB: How many gadgets
# Date:         15 September 2024
#




day_input = int(input("Please enter a positive value for day: " ))


#Process for range of gadgets between 0 and 10
if day_input <= 10 and day_input >= 0:
    gadgets = day_input * 10
    print(f'The sum total number of gadgets produced on day {day_input} is {gadgets:.0f}')

#Process for range of gadgets between 10 and 50
elif day_input > 10 and day_input < 50:
    gadgets = 100 + ((11 + day_input)*(day_input - 11 +1))/2
    print(f'The sum total number of gadgets produced on day {day_input} is {gadgets:.0f}')

#Process for range of gadgets between 50 and 100
elif day_input >= 50 and day_input <= 100:
    gadgets = 1270 + ((day_input - 49)*50)
    print(f'The sum total number of gadgets produced on day {day_input} is {gadgets:.0f}')

#Process for just day 102
elif day_input == 102:
    gadgets = 1170 + ((day_input - 49)*50)
    print(f'The sum total number of gadgets produced on day {day_input} is {gadgets:.0f}')


#Process for invalid numbers
elif day_input < 0:
    print("You entered an invalid number!")