print("\nBienvenido a la calculadora de Python\nAhora introduce los datos")

op = None
while op != "q":
    # recogemos datos
    print("Para salir escribe q")
    op = input ("Que cuenta quieres hacer (+ - * / q):")
    if op != "q":
        num1 = float(input("Introduce primer valor: "))
        num2 = float(input("Introduce segundo valor: "))
    resultado = None

    # proceso de daatos
    if op == "+":
        resultado = num1 + num2
    elif op == "-":
        resultado = num1 - num2
    elif op == "*":
        resultado = num1 * num2
    elif op == "/":
        resultado = num1 / num2
    elif op == "q":
        break
    else:
        print("No son datos validos!!!")
        exit()
    print("El resultado de la operacion es: ")
    print(resultado)

    # mostramos resultados
print("Bye, bye!!!")
