
import json
import funcionesguess as f


with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())#json como lee lista Python - lee en formato lista
    print("Top" + str(score_list))
    print("Top score (attempts): " + str(score_list[:5])) #[ 5 ] cantidad de numeros que mostrara
    print("Top score (attempts): {0}".format(score_list[:1]))  # [ 5 ] cantidad de numeros que mostrara
    #for score_dict in score_list:
    #   print(str(score_dict["attempts"])+" attempts, date " + score_dict.get("date"))


while True:
    f.play_game()
    f.get_score_list()
    break
