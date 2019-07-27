import random
from functions import bye #funciones

secret = random.randint(0, 30)
attempts = 0


while True:
    guess = float(input("Introduce un numero entre 0 y 30: ").replace(",","."))
    attempts += 1
    if guess == secret:
        print("Has acertado... Mago!!!")
        print("Intentos: " + str(attempts))
        yes = input("Quieres intentarlo de nuevo? y/n: ")
        if yes.lower() != "y" and yes.lower() != "yes" and yes.lower() !="si":
            break
    elif guess > secret:
        print("Te has pasado intentalo otra vez")
    elif guess < secret:
        print("Te has quedado corto intentalo otra vez")
    else:
        print("No hagas trampa")
        exit()
bye()

