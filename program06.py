present = 0
absent = 0
print("enter prensent and absent for 10 days:")
for daay in range(1, 11):
    status =  input("Day {day}:")
    if status == "P" or status == "P":
        present = present + 1
    else:
        absent = absent + 1
percentage = (present / 10) * 100
print("\n=====REESUULT=======")
print("total present days:", present)
print("total absent days:", absent)
print("attendance perentage:", percentage)
if percentage < 75:
    print("warning: attendance below 75%")

