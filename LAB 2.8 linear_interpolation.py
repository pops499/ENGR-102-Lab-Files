import math
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   2.8 LAB: Linear Interpolation
# Date:         22 August 2024
#

x = 10
x1 = 55
y = 2028
y1 = 23028
slope = (y1 - y) / (x1 - x)

#part 1
x = 25
linear_interpolation = (slope) * (x - x1) + y1
print("Part 1:")
print("For t = 25 minutes, the position p =", linear_interpolation, "kilometers" )

x = 27.556597091188028
linear_interpolation = (slope) * (x - x1) + y1
print("Part 2:")
print("For t = 300 minutes, the position p =", linear_interpolation, "kilometers" )


#part 2


