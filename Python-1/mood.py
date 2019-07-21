
mood = None
while mood != "exit":
    print("Escribe exit para salir")
    mood = input("Como te sientes hoy? (feliz, nervioso, excitado, triste):")
    if mood == "feliz":
        print("Que bueno verte feliz!")
    elif mood == "nervioso":
        print("Toma aire 3 veces!!!")
    elif mood == "excitado":
        print("Relajate observando el amanecer")
    elif mood == "triste":
        print("Arriba el animo")
    elif mood == "exit":
        break
    else:
        print("No entiendo este sentimiento")

print("A vivir!!!")

