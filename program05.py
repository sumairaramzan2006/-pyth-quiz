principal = float(input("enter principal: "))
rate = float(input("enter annula intrst rate(%): "))
time = float(input("entr   time in year: "))
# simple intrest
simple_intrest = (principal * rate * time) / 100
n = int(input("entr number of time compound per year:"))
amount = principal * (1 + rate / (100 * n) ** (n * time))
compound_intrest = amount - principal
print("final amount=", round(amount))
print("comound_intrest =", round(compound_intrest))
if compound_intrest > simple_intrest:
    print("compound intresst earnr more by:", round( compound_intrest-simple_intrest))
    print("simple intrest earn more by:", round(simple_intrest - compound_intrest))
else:
    print("both are equal")      