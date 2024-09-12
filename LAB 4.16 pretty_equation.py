import math
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   4.16 LAB: Pretty equation
# Date:         11 September 2024
#
a = int(input("Please enter the coefficient A: "))
b = int(input("Please enter the coefficient B: "))
c = int(input("Please enter the coefficient C: "))
#comments
stringA = ""
stringB = ""
stringC = ""

if abs(a) == 1:
    if a > 0:
        stringA = " x^2"
    else:
        stringA = " - x^2"
elif a>0:
    stringA = f" {a}x^2"
elif a<0:
    stringA = f" - {abs(a)}x^2"

if abs(b) == 1:
    if b > 0:
        if a == 0:
            stringB = " x"
        else:
            stringB = " + x"
    else:
        stringB = " - x"
elif b > 0:
    if a == 0:
        stringB =f' {b}x'
    else:
        stringB = f' + {abs(b)}x'
elif b < 0:
    stringB = f' - {abs(b)}x'
if c > 0:
    stringC = f' + {c}'
if c < 0:
    stringC = f' - {abs(c)}'

print(f'The quadratic equation is{stringA}{stringB}{stringC} = 0')
