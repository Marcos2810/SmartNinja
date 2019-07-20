
mood = None
while mood != "exit":
    print("Escribe exit para salir")
    mood = input("Como te sientes hoy? (feliz, nervioso, excitado):")
    if mood == "feliz":
        print("Que bueno verte feliz!")
    elif mood == "nervioso":
        print("Toma aire 3 veces!!!")
    elif mood == "excitado":
        print("Relaja observando el amanecer")
    elif mood == "exit":
        break
    else:
        print("No entiendo ese sentimiento")

print("A vivir!!!")

