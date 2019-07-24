print("Nuestro primer conversor")
print("Conversor de KM a Millas")

while True:
  km = float(input("Introduce el valor en KM: "))
  miles = km * 0.6215

  print("Estos KM" + " " + str(km) + " " +"equivalen a" + " " + str(miles))
  
  yes = input("Quieres repetir y/n: ")
  if yes != "y" and yes != "yes":
    break
print("bye...")
