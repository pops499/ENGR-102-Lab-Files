import math

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   Lab Topic 1 
# Date:         22 August 2024
#

fluid = 9
kv = 0.0015
cld = 0.875
print ('Reynolds number is', ((fluid * cld) / kv),)
#stuff for reynolds number

d = 0.028
a = (35 * math.pi)/180
print ('Wavelength is', (2 * d * math.sin(a)), "nm")
#stuff for wavelength

ip = 100
day = 10
id = 2
hc = 0.8
arps = (ip/ (1 + hc * id * day)**(1/hc))
print("Production rate is", arps ,"barrels/day")
#stuff for barrels




im = 11000
fm = 8300
ev = 2028
print('Change of velocity is ', ev * math.log(im/fm), 'm/s')
#rocket equation stuff
