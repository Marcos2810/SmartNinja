import random

secret = random.randint(0, 30)
attempts = 0

with open("record.txt", "r") as record:
    best_record = int(record.read())
    print("Top score (intentos): " + str(best_record))

while True:
    guess = float(input("Introduce un numero entre 0 y 30: ").replace(",", "."))
    attempts += 1
    if guess == secret:
        print("Has acertado... Mago!!!")
        print("Intentos: " + str(attempts))
        if attempts < best_record:
            with open("record.txt", "w") as record:
                record.write(str(attempts))
        break
    elif guess > secret:
        print("Te has pasado intentalo otra vez")
    elif guess < secret:
        print("Te has quedado corto intentalo otra vez")


