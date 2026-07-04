def calculate_bonus(rating, salary):
    rating  = rating
    if rating == "excellent":
        bonus =  salary * 0.20
    elif rating == "good":
        bonus =  salary * 0.10
    elif rating == "average":
        bonus =  salary * 0.50
    elif rating == "poor":
        bonus =  0
    else:
        print("invalid rating")
    return bonus
emp1_bonus = calculate_bonus("excellent",50000)
emp2_bonus = calculate_bonus("good",40000)
emp3_bonus = calculate_bonus("average",30000)

print("employee1 bonus:", emp1_bonus)
print("employee2 bonus:", emp2_bonus)
print("employee3 bonus:", emp3_bonus)