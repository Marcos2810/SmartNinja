print("Divisibles")
print("Elige un numero entre 1 y 100")

div = int(input("Introduce tu numero: "))

for num in range(1, div+1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0:
        print("Fizz")
    else:
        print(num)
