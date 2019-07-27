import random

secret = random.randint(0, 30)
attempts = 0

while True:
    guess = float(input("Introduce un numero entre 0 y 30: ").replace(",","."))
    attempts += 1
    if guess == secret:
        print("Has acertado... Mago!!!")
        print("Intentos: " + str(attempts))
        yes = input("Quieres intentarlo de nuevo? y/n: ")
        if yes != "y":
            break
    elif guess > secret:
        print("Te has pasado intentalo otra vez")
    elif guess < secret:
        print("Te has quedado corto intentalo otra vez")
    elif guess == "q":
        break
    else:
        print("No hagas trampa")
        exit()
print("Bye, bye...")

