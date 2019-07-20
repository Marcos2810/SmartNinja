print("\nBienvenido a la calculadora de Python\nAhora introduce los datos")

# recogemos datos
op = input ("Que cuenta quieres hacer (+ - * /):")
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
else:
    print("No son datos validos")
    exit()

# mostramos resultados
print("El resultado de la operacion es: ")
print(str(num1) + " " + op + " " + str(num2) + " " + str(resultado))
print(resultado)