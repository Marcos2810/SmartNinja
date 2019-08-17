import json

class FootballPlayer():
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.goals = goals
        self.yellow_cards = yellow_cards
        self.red_cards = red_cards

try:
    with open("foot.txt", "r") as f:
        player_list = json.loads(f.read())
except:
    player_list=[]

for jugadores in player_list:
    print(jugadores)
    print(jugadores['first_name'])#solo imprimo nombre - porque estan en diccionario

print(player_list[:2])

print(player_list)

print("Tu jugador")

name = input("Nombre: ")
lastname = input("Apellido: ")
height = float (input("Altura: "))
weight=float(input("Kilos: "))
goals=int(input("Goles: "))
y_cards=int(input("Tarjetas amarillas: "))
r_cards=int(input("Tarjetas rojas: "))

new_player = FootballPlayer(first_name=name, last_name=lastname, height_cm=(height), weight_kg=(weight),
                            goals=int(goals), yellow_cards=(y_cards), red_cards=int(r_cards))
player_list.append(new_player.__dict__)
with open("foot.txt", "w") as f:
    f.write(json.dumps(player_list))
