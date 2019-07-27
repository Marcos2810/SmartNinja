
import random
import json
import datetime


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())#json como lee lista Python - lee en formato lista
    print("Top score (attempts): " + str(score_list[:5])) #[ 5 ] cantidad de numeros que mostrara


secret = random.randint(1, 30)
attempts = 0
nombre = input("Introduce tu nombre: ")
wrong = []
while True:
    try:# capturar errores / try - except
        guess = int(input("Introduce un numero entre 0 y 30: "))
    except:
        print("Escribe solo numeros")
        continue# continue no rompe y vuelve a ejecutar
    attempts += 1

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        score_data = {
            "Usuario": nombre,
            "Intentos": attempts,
            "date": str (datetime.datetime.now()),
            "secret": secret,
            "wrong": wrong}
        score_list.append(score_data)
        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list)) #json como lee lista Python - lee en formato lista
        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")
    wrong.append(guess)
