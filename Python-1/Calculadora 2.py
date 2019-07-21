print("\nBienvenido a la calculadora de Python\nAhora introduce los datos")

op = None
while op != "q":
    # recogemos datos
    print("Para salir escribe q")
    op = input ("Que cuenta quieres hacer (+ - * / q):")
    if op != "q":
        n1 = float(input("Introduce primer valor: "))
        n2 = float(input("Introduce segundo valor: "))

    # proceso de daatos
    if op == "+":
        print("Resultado" + " " + str(n1) + str(n2))
    elif op == "-":
        print("Resultado" + " " + str(n1) - str(n2))
    elif op == "*":
        print("Resultado" + " " + str(n1) * str(n2))
    elif op == "/":
        print("Resultado" + " " + str(n1) / str(n2))
    elif op == "q":
        break
    else:
        print("No son datos validos!!!")


    # mostramos resultados

print("Bye, bye!!!")
