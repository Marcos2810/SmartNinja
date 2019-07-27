import random

secret = random.randint(1, 30)
attempts = 0
try:
    with open("score.txt", "r") as score_file:
        best_score = int(score_file.read())
        print("Top score (attempts): " + str(best_score))
except:
    print("no se ha podido guardar")

while True:
    # capturar errores / try - except
    # continue no rompe y vuelve a ejecutar
    try:
        guess = int(input("Guess the secret number (between 1 and 30): "))
    except:
        print("Escribe solo numeros")
        continue
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        if attempts < best_score:
            with open("score.txt", "w") as score_file:
                score_file.write(str(attempts))
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")