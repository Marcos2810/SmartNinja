
import random
import json
import datetime

try:
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())#json como lee lista Python - lee en formato lista
        print("Top score (attempts): " + str(score_list[:5])) #[ 3 ] cantidad de numeros que mostrara
except:
    print("no hay scores")
    score_list = []

secret = random.randint(1, 30)
attempts = 0
nombre = input("Introduce tu nombre: ")
wrong = []
intento = []
while True:
    try:# capturar errores / try - except
        guess = int(input("Guess the secret number (between 1 and 30): "))
    except:
        print("Escribe solo numeros")
        continue# continue no rompe y vuelve a ejecutar
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        score_data = {"attempts": attempts, "date": str (datetime.datetime.now()),"intentos": intento, "usuario": nombre, "secret": secret, "wrong": wrong}
        score_list.append(score_data)
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list)) #json como lee lista Python - lee en formato lista
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
    wrong.append(guess)
    intento.append(attempts)
