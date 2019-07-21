import random

secret = random.randint(0,30)
guess = None
while True:
    guess = int(input("Introduce un numero entre 1 y 30: "))

    if guess == secret:
        break
    elif guess > secret:
        print("Te has pasado intentalo otra vez")
    elif guess < secret:
        print("Te has quedado corto intentalo otra vez")
    else:
        print("Nop... no es intentalo otra vez ")
print("Has acertado... Mago!!!")