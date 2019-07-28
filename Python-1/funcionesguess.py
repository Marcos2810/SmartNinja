import random
import datetime


def play_game():
    secret = random.randint(1, 30)
    attempts = 0
    nombre = input("Introduce tu nombre: ")
    wrong = []
    score_list = get_score_list()
    while True:
        guess = int(input("Introduce un numero entre 0 y 30: "))
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


# Get a list of all scores
def get_score_list():
    with open("score_list.txt", "r") as score_file:
        score_list = json.loads(score_file.read())
        return score_list


# Return top 3 scores
def get_top_scores():
    score_list = get_score_list()
    top_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
    return top_score_list
