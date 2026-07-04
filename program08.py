import random
number = random . randint(1,  50)
print("guess the number between 1 and 50. you have 7 attemps.")
for attempt in range(1, 8):
    guess = int(input(f"attempt {attempt}: enter your guess:"))
    if guess == number:
        print(f"congratulation : you won in {attempt} attempt")
    elif guess > number:
        print("too hight! try again")
    else:
        print("too low! try gain")
else:
    print("game over!")
        