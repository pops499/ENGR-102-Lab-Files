# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   3.18 LAB: Still More Linear Interpolation
# Date:         4 September 2024
#

print('Enter time 1:')
#time variable
time_input1 = float(input())

#first position variables
print ('Enter the x position of the object at time 1:')
location_input_1x = float(input())
print ('Enter the y position of the object at time 1:')
location_input_1y = float(input())
print ('Enter the z position of the object at time 1:')
location_input_1z = float(input())


print('Enter time 2:')
#time variable
time_input2 = float(input())

#second position variables
print ('Enter the x position of the object at time 2:')
location_input_2x = float(input())
print ('Enter the y position of the object at time 2:')
location_input_2y = float(input())
print ('Enter the z position of the object at time 2:')
location_input_2z = float(input())


#time for 1st line
print(f'At time {time_input1:.2f} seconds the object is at ({location_input_1x:.3f}, {location_input_1y:.3f}, {location_input_1z:.3f})')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#time for x for 2nd line
slope1x = ((location_input_2x - location_input_1x) / (time_input2 - time_input1))
second_x =  (slope1x * ((time_input2-time_input1) / 4) + location_input_1x)

#time for y for 2nd line
slope1x = ((location_input_2y - location_input_1y) / (time_input2 - time_input1))
second_y =  (slope1x * ((time_input2-time_input1) / 4) + location_input_1y)

#time for z for 2nd line
slope1x = ((location_input_2z - location_input_1z) / (time_input2 - time_input1))
second_z =  (slope1x * ((time_input2-time_input1) / 4)   + location_input_1z)

#print statment for 2nd line
print (f'At time {((time_input2-time_input1) / 4) + (time_input1):.2f} seconds the object is at ({second_x:.3f}, {second_y:.3f}, {second_z:.3f})')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#time for x for 3rd line
slope1x = ((location_input_2x - location_input_1x) / (time_input2 - time_input1))
second_x =  (slope1x * (2*((time_input2-time_input1)) / 4) + location_input_1x)

#time for y for 3rd line
slope1x = ((location_input_2y - location_input_1y) / (time_input2 - time_input1))
second_y =  (slope1x * (2*((time_input2-time_input1)) / 4) + location_input_1y)

#time for z for 3rd line
slope1x = ((location_input_2z - location_input_1z) / (time_input2 - time_input1))
second_z =  (slope1x * (2*((time_input2-time_input1)) / 4)   + location_input_1z)

#print statment for 3rd line
print (f'At time {2 *((time_input2-time_input1) / 4) + (time_input1):.2f} seconds the object is at ({second_x:.3f}, {second_y:.3f}, {second_z:.3f})')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#time for x for 4th line
slope1x = ((location_input_2x - location_input_1x) / (time_input2 - time_input1))
second_x =  (slope1x * (3*((time_input2-time_input1)) / 4) + location_input_1x)

#time for y for 4th line
slope1x = ((location_input_2y - location_input_1y) / (time_input2 - time_input1))
second_y =  (slope1x * (3*((time_input2-time_input1)) / 4) + location_input_1y)

#time for z for 4th line
slope1x = ((location_input_2z - location_input_1z) / (time_input2 - time_input1))
second_z =  (slope1x * (3*((time_input2-time_input1)) / 4)   + location_input_1z)

#print statment for 4th line
print (f'At time {3 *((time_input2-time_input1) / 4) + (time_input1):.2f} seconds the object is at ({second_x:.3f}, {second_y:.3f}, {second_z:.3f})')

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

#print statement for 5th line
print(f'At time {time_input2:.2f} seconds the object is at ({location_input_2x:.3f}, {location_input_2y:.3f}, {location_input_2z:.3f})')






