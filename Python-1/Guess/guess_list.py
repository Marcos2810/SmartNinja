
import random
import json
import datetime
import mimodulo.func_guess_list as f
"""
top3 = f.get_score_list()

for t in top3:
    print(t)"""
with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    for score in score_list:
        print(score)
    print("Top scores: " + str(score_list[:5]))

"""
with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())#json como lee lista Python - lee en formato lista

"""

secret = random.randint(1, 30)
attempts = 0
nombre = input("Introduce tu nombre: ")
wrong = []
score_list = f.get_score_list()
while True:
    try:# capturar errores / try - except
        guess = int(input("Introduce un numero entre 0 y 30: "))
    except:
        print("Escribe solo numeros")
        continue# continue no rompe y vuelve a ejecutar
    attempts += 1

    if guess == secret:
        print(nombre +" " + "Has acertado... Mago!!! Este es tu numero " + str(secret).format(nombre, secret))
        print("{0} Has acertado eres un Mago!!! Este es tu numero {1}".format(nombre, secret))
        print("Numero de intentos: " + str(attempts))

        score_list.append({"usuario": nombre, "attempts": attempts, "fecha": str (datetime.datetime.now()), "secret": secret, "errores": wrong})

        with open("score_list.txt", "w") as score_file:
            score_file.write(json.dumps(score_list)) #json como lee lista Python - lee en formato lista
        break
    elif guess > secret:
        print("Tu numero es incorrecto... intenta uno mas pequeño")
    elif guess < secret:
        print("Tu numero es incorrecto... intenta uno mas grande")
    wrong.append(guess)
