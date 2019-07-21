import random
secret = random.randint(0,30)
mago = None
guess = None
while mago != "q":
    # recogemos datos
    print("Para salir escribe q")
    mago = input ("Quieres empezar?: ")
    if mago != "q":
        guess = int(input("Introduce primer valor: "))

    if guess == secret:
        print("Has acertado... Mago!!!")
        exit()
    elif guess > secret:
        print("Te has pasado intentalo otra vez")
    elif guess < secret:
        print("Te has quedado corto intentalo otra vez")
    elif guess == mago:
        break
    else:
        print("Nop... no es intentalo otra vez ")
print("bye")