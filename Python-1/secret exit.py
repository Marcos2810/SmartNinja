import random

secret = random.randint(0, 30)

while True:
    guess = int(input("Introduce un numero entre 0 y 30: "))

    if guess == secret:
        break
    elif guess > secret:
        print("Te has pasado intentalo otra vez")
    elif guess < secret:
        print("Te has quedado corto intentalo otra vez")
    else:
        print("No hagas trampa")
    yes = input("Quieres intentarlo de nuevo? y/n: ")
    if yes != "y":
        break
print("Has acertado... Mago!!!")