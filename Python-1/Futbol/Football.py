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

with open("foot.txt", "r") as player_foot:
    player_list = json.loads(player_foot.read())
    print(player_list)

print("tu jugador")

name = input("Nombre: ")
lastname = input("Apellido: ")
height = float (input("Altura: "))
weight=float(input("Kilos: "))
goals=int(input("Goles: "))
y_cards=int(input("Tarjetas amarillas: "))
r_cards=int(input("Tarjetas rojas: "))

new_player = FootballPlayer(first_name=name, last_name=lastname, height_cm=float(height), weight_kg=float(weight),
                            goals=int(goals), yellow_cards=int(y_cards), red_cards=int(r_cards))

jugadores = (new_player.__dict__)

with open("foot.txt", "w") as player_foot:
    player_foot.write(json.dumps(jugadores))
    print(jugadores)