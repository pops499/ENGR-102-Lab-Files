import math
# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   6.19 LAB: Juggler sequence
# Date:         4 September 2024
#
input = int(input('Enter a positive integer: '))
print(f'The Juggler sequence starting at {input} is:')

#counter
counter = 0

while input > 1:
    counter +=1
    if input % 2 == 0:
        print(input, end=', ')
        input = math.floor(math.sqrt(input))
        
        
        
    elif input % 2 != 0:
        print(input, end=', ')
        input = math.floor(input **(3/2))
        if input % 2 == 0:
            print(input, end=', ')
            input = math.floor(math.sqrt(input))
            counter += 1
    

print('1')
print(f'It took {counter} iterations to reach 1')





