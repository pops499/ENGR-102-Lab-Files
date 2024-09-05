# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   3.20 LAB: Calling functions
# Date:         4 September 2024
#

from math import *
import math
def printresult(shape, side, area):
    '''Print the result of the calculation'''
    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

# example function call:
# printresult(<string of shape name>, <float of side>, <float of area>)
# printresult('square', 2.236, 5)
# Your code goes here

print("Please enter the side length:")
side_length_input = float(input())
A1 = (math.sqrt(3)/4) * pow(side_length_input,2)

def printresult(shape, side, area):

    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

printresult("triangle", side_length_input, A1)

#------------------------------------------------------------------------


A2 = pow(side_length_input, 2)

def printresult(shape, side, area):

    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

printresult("square", side_length_input, A2)

#------------------------------------------------------------------------

A3 = (1/4) * (math.sqrt(5*(5+2 * math.sqrt(5)))) * pow(side_length_input,2)

def printresult(shape, side, area):

    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

printresult("pentagon", side_length_input, A3)

#------------------------------------------------------------------------

A4 = ((3*math.sqrt(3))/2) * pow(side_length_input,2)

def printresult(shape, side, area):

    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

printresult("hexagon", side_length_input, A4)

#------------------------------------------------------------------------


A5 = 3 * (2+math.sqrt(3)) * pow(side_length_input,2)

def printresult(shape, side, area):

    print(f'A {shape} with side {side:.2f} has area {area:.3f}')

printresult("dodecagon", side_length_input, A5)   