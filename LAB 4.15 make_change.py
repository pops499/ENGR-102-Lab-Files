# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Daniel Garcia
# Section:      544
# Assignment:   4.15 LAB: Make change
# Date:         11 September 2024
#

print("How much did you pay?")
pay = float(input())

print("How much did it cost?")
cost = float(input())

change = pay - cost
ch = round(change,2)
print(f'You received ${ch:.2f} in change. That is...')

chpr = ch * 100
quarter = (chpr - (chpr % 25)) / 25
chpr2 = chpr % 25
dime = (chpr2 - chpr2 % 10) / 10
chpr3 = chpr2 % 10
nickel = (chpr3 - (chpr3 % 5))/5
chpr4 = chpr % 5
penny = (chpr4 - (chpr4 % 1))

#quarters
if quarter > 1:
    q = "quarters"
    print(f'{quarter:.0f} {q}')
elif quarter == 1:
    q = 'quarter'
    print(f'{quarter:.0f} {q}')

if dime > 1:
    d = "dimes"
    print(f'{dime:.0f} {d}')
elif dime == 1:
    d = 'dime'
    print(f'{dime:.0f} {d}')

if nickel > 1:
    n = "nickels"
    print(f'{nickel:.0f} {n}')
elif dime == 1:
    n = 'nickel'
    print(f'{nickel:.0f} {n}')

if penny > 1:
    p = "pennies"
    print(f'{penny:.0f} {p}')
elif penny == 1:
    p = 'penny'
    print(f'{penny:.0f} {p}')





            

        


            


    

    

    







