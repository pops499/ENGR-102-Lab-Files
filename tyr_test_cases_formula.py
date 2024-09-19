# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Jon Schiflett
# Section:      536
# Assignment:   Lab 3
# Date:         19/9/2024
#

#
gen = str(input())
old = int(input())
cholesterol = int(input())
smoke = str(input())
hdl = int(input())
systolic_bp = int(input())
medication = str(input())

if gen == 'M' or gen == 'Male':
    sex = 'M'
elif gen == 'F' or gen == 'Female':
    sex = 'F'
#Sex value

if old >= 20 and old <= 34:
    if sex == 'M':
        age = -9
    elif sex == 'F':
        age = -7
#Age 20-34 value

if old >= 35 and old <= 39:
    if gen == 'M' or gen == 'Male':
        age = -4
    elif gen == 'F' or gen == 'Female':
        age = -3
#Age 35-39 value

if old >= 40 and old <= 44:
    if gen == 'M' or gen == 'Male':
        age = 0
    elif gen == 'F' or gen == 'Female':
        age = 0
#Age 40-44 value

if old >= 45 and old <= 49:
    if gen == 'M' or gen == 'Male':
        age = 3
    elif gen == 'F' or gen == 'Female':
        age = 3
#Age 45-49 value

if old >= 50 and old <= 54:
    if gen == 'M' or gen == 'Male':
        age = 6
    elif gen == 'F' or gen == 'Female':
        age = 6
#Age 50-54 value

if old >= 55 and old <= 59:
    if gen == 'M' or gen == 'Male':
        age = 8
    elif gen == 'F' or gen == 'Female':
        age = 8
#Age 55-59 value

if old >= 60 and old <= 64:
    if gen == 'M' or gen == 'Male':
        age = 10
    elif gen == 'F' or gen == 'Female':
        age = 10
#Age 60-64 value

if old >= 65 and old <= 69:
    if gen == 'M' or gen == 'Male':
        age = 11
    elif gen == 'F' or gen == 'Female':
        age = 12
#Age 65-69 value

if old >= 70 and old <= 74:
    if gen == 'M' or gen == 'Male':
        age = 12
    elif gen == 'F' or gen == 'Female':
        age = 14
#Age 70-74 value

if old >= 75 and old <= 79:
    if gen == 'M' or gen == 'Male':
        age = 13
    elif gen == 'F' or gen == 'Female':
        age = 16
#Age 75-79 value

if cholesterol < 160:
    if gen == 'M' or gen == 'Male':
        if old >= 20 and old <= 39:
            cho = 0
        elif old >= 40 and old <= 49:
            cho = 0
        elif old >= 50 and old <= 59:
            cho = 0
        elif old >= 60 and old <= 69:
            cho = 0
        elif old >= 70 and old <= 79:
            cho = 0
    if gen == 'F' or gen == 'Female':
        if old >= 20 and old <= 39:
            cho = 0
        elif old >= 40 and old <= 49:
            cho = 0
        elif old >= 50 and old <= 59:
            cho = 0
        elif old >= 60 and old <= 69:
            cho = 0
        elif old >= 70 and old <= 79:
            cho = 0

if cholesterol >= 160 and cholesterol <= 199:
    if gen == 'M' or gen == 'Male':
        if old >= 20 and old <= 39:
            cho = 4
        elif old >= 40 and old <= 49:
            cho = 3
        elif old >= 50 and old <= 59:
            cho = 2
        elif old >= 60 and old <= 69:
            cho = 1
        elif old >= 70 and old <= 79:
            cho = 0
    if gen == 'F' or gen == 'Female':
        if old >= 20 and old <= 39:
            cho = 4
        elif old >= 40 and old <= 49:
            cho = 3
        elif old >= 50 and old <= 59:
            cho = 2
        elif old >= 60 and old <= 69:
            cho = 1
        elif old >= 70 and old <= 79:
            cho = 1

if cholesterol >= 200 and cholesterol <= 239:
    if gen == 'M' or gen == 'Male':
        if old >= 20 and old <= 39:
            cho = 7
        elif old >= 40 and old <= 49:
            cho = 5
        elif old >= 50 and old <= 59:
            cho = 3
        elif old >= 60 and old <= 69:
            cho = 1
        elif old >= 70 and old <= 79:
            cho = 0
    if gen == 'F' or gen == 'Female':
        if old >= 20 and old <= 39:
            cho = 8
        elif old >= 40 and old <= 49:
            cho = 6
        elif old >= 50 and old <= 59:
            cho = 4
        elif old >= 60 and old <= 69:
            cho = 2
        elif old >= 70 and old <= 79:
            cho = 1

if cholesterol >= 240 and cholesterol <= 279:
    if gen == 'M' or gen == 'Male':
        if old >= 20 and old <= 39:
            cho = 9
        elif old >= 40 and old <= 49:
            cho = 6
        elif old >= 50 and old <= 59:
            cho = 4
        elif old >= 60 and old <= 69:
            cho = 2
        elif old >= 70 and old <= 79:
            cho = 1
    if gen == 'F' or gen == 'Female':
        if old >= 20 and old <= 39:
            cho = 11
        elif old >= 40 and old <= 49:
            cho = 8
        elif old >= 50 and old <= 59:
            cho = 5
        elif old >= 60 and old <= 69:
            cho = 3
        elif old >= 70 and old <= 79:
            cho = 2

if cholesterol >= 280:
    if gen == 'M' or gen == 'Male':
        if old >= 20 and old <= 39:
            cho = 11
        elif old >= 40 and old <= 49:
            cho = 8
        elif old >= 50 and old <= 59:
            cho = 5
        elif old >= 60 and old <= 69:
            cho = 3
        elif old >= 70 and old <= 79:
            cho = 2
    if gen == 'F' or gen == 'Female':
        if old >= 20 and old <= 39:
            cho = 13
        elif old >= 40 and old <= 49:
            cho = 10
        elif old >= 50 and old <= 59:
            cho = 7
        elif old >= 60 and old <= 69:
            cho = 4
        elif old >= 70 and old <= 79:
            cho = 2

if smoke == 'N' or smoke == 'No':
    if gen == 'M' or gen == 'Male':
        if old >= 20 and old <= 39:
            smo = 0
        elif old >= 40 and old <= 49:
            smo = 0
        elif old >= 50 and old <= 59:
            smo = 0
        elif old >= 60 and old <= 69:
            smo = 0
        elif old >= 70 and old <= 79:
            smo = 0
    if gen == 'F' or gen == 'Female':
        if old >= 20 and old <= 39:
            smo = 0
        elif old >= 40 and old <= 49:
            smo = 0
        elif old >= 50 and old <= 59:
            smo = 0
        elif old >= 60 and old <= 69:
            smo = 0
        elif old >= 70 and old <= 79:
            smo = 0

if smoke == 'Y' or smoke == 'Yes':
    if gen == 'M' or gen == 'Male':
        if old >= 20 and old <= 39:
            smo = 8
        elif old >= 40 and old <= 49:
            smo = 5
        elif old >= 50 and old <= 59:
            smo = 3
        elif old >= 60 and old <= 69:
            smo = 1
        elif old >= 70 and old <= 79:
            smo = 1
    if gen == 'F' or gen == 'Female':
        if old >= 20 and old <= 39:
            smo = 9
        elif old >= 40 and old <= 49:
            smo = 7
        elif old >= 50 and old <= 59:
            smo = 4
        elif old >= 60 and old <= 69:
            smo = 2
        elif old >= 70 and old <= 79:
            smo = 1

if hdl >= 60:
    if gen == 'M' or gen == 'Male':
        hdl_v = -1
    elif gen == 'F' or gen == 'Female':
        hdl_v = -1

if hdl >= 50 and hdl <= 59:
    if gen == 'M' or gen == 'Male':
        hdl_v = 0
    elif gen == 'F' or gen == 'Female':
        hdl_v = 0

if hdl >= 40 and hdl <= 49:
    if gen == 'M' or gen == 'Male':
        hdl_v = 1
    elif gen == 'F' or gen == 'Female':
        hdl_v = 1

if hdl < 40:
    if gen == 'M' or gen == 'Male':
        hdl_v = 2
    elif gen == 'F' or gen == 'Female':
        hdl_v = 2

if systolic_bp < 120:
    if gen == 'M' or gen == 'Male':
        if medication == 'N' or medication == 'No':
            sbd = 0
        elif medication == 'Y' or medication == 'Yes':
            sbd = 0
    if gen == 'F' or gen == 'Female':
        if medication == 'N' or medication == 'No':
            sbd = 0
        elif medication == 'Y' or medication == 'Yes':
            sbd = 0

if systolic_bp >= 120 and systolic_bp <= 129:
    if gen == 'M' or gen == 'Male':
        if medication == 'N' or medication == 'No':
            sbd = 0
        elif medication == 'Y' or medication == 'Yes':
            sbd = 1
    if gen == 'F' or gen == 'Female':
        if medication == 'N' or medication == 'No':
            sbd = 1
        elif medication == 'Y' or medication == 'Yes':
            sbd = 3

if systolic_bp >= 130 and systolic_bp <= 139:
    if gen == 'M' or gen == 'Male':
        if medication == 'N' or medication == 'No':
            sbd = 1
        elif medication == 'Y' or medication == 'Yes':
            sbd = 2
    if gen == 'F' or gen == 'Female':
        if medication == 'N' or medication == 'No':
            sbd = 2
        elif medication == 'Y' or medication == 'Yes':
            sbd = 4

if systolic_bp >= 140 and systolic_bp <= 159:
    if gen == 'M' or gen == 'Male':
        if medication == 'N' or medication == 'No':
            sbd = 1
        elif medication == 'Y' or medication == 'Yes':
            sbd = 2
    if gen == 'F' or gen == 'Female':
        if medication == 'N' or medication == 'No':
            sbd = 3
        elif medication == 'Y' or medication == 'Yes':
            sbd = 5

if systolic_bp >= 160:
    if gen == 'M' or gen == 'Male':
        if medication == 'N' or medication == 'No':
            sbd = 2
        elif medication == 'Y' or medication == 'Yes':
            sbd = 3
    if gen == 'F' or gen == 'Female':
        if medication == 'N' or medication == 'No':
            sbd = 4
        elif medication == 'Y' or medication == 'Yes':
            sbd = 6

out = age + cho + smo + hdl_v + sbd

if gen == 'M' or gen == 'Male':
    if out <0:
        output = '<1'
    elif out >=0 and out <= 4:
        output = '1'
    elif out >=5 and out <= 6:
        output = '2'
    elif out == 7:
        output = '3'
    elif out == 8:
        output = '4'
    elif out == 9:
        output = '5'
    elif out == 10:
        output = '6'
    elif out == 11:
        output = '8'
    elif out == 12:
        output = '10'
    elif out == 13:
        output = '12'
    elif out == 14:
        output = '16'
    elif out == 15:
        output = '20'
    elif out == 16:
        output = '25'
    elif out >= 17:
        output = '>30'

if gen == 'F' or gen == 'Female':
    if out <9:
        output = '<1'
    elif out >=9 and out <= 12:
        output = '1'
    elif out >=13 and out <= 14:
        output = '2'
    elif out == 15:
        output = '3'
    elif out == 16:
        output = '4'
    elif out == 17:
        output = '5'
    elif out == 18:
        output = '6'
    elif out == 19:
        output = '8'
    elif out == 20:
        output = '11'
    elif out == 21:
        output = '14'
    elif out == 22:
        output = '17'
    elif out == 23:
        output = '22'
    elif out == 24:
        output = '27'
    elif out >= 25:
        output = '>30'

print(f'sex:{str(sex)} age:{old} cho:{cholesterol} smo:{str(smoke)} hdl:{hdl} sbp:{systolic_bp} med:{str(medication)} out:{str(output)}')