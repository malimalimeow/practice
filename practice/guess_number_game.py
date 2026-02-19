import random
x = random.randint(1, 100)
count = 0

while True:
    try:
        num = int(input("Guess a number from 1-100: "))
    except ValueError:
        print("This is not a number!")
        continue

    count += 1
    if num > x:
        print("too much")
    elif num < x:
        print("too less")
    else:
        print("yeah, you got it!")
        print("you guessed", count, "times")
        break

    if count == 10:
        print("Oh no, you guessed", count, "times")
        break