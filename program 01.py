# program 01

print("\n==========================")
units = int(input("enter units: "))
bill = 0
# slab 1 = 100 * $5 = $500
if units > 100:
    bill = bill +  100 * 5
    units = units  - 100
else:
    bill = bill + units * 5
    units = 0
# slab  2 = (101-300) * 8 = 200 * 8 = $1600
if units > 0:
    if units >  200:
        bill =  bill + 200 * 8
        units = units - 200
    else:
        bill = bill + units * 8
        units = 0
# slab 3 = (350 - 100 - 200) * 12 = 50 * $12 $600
if units > 0:
        bill = bill + 50 * 12
print("total bill=", bill)

