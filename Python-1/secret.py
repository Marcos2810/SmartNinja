secret = 22
guess = 0

while guess != secret:

    guess = int(input("Introduce un numero entre 1 y 30: "))

    if guess == secret:
        print("Has acertado... Mago!!!")
    else:
        print("Nop... no es " + str(guess) + " intentalo otra vez ")