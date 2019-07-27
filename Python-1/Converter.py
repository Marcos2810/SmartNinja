print("Nuestro primer conversor")
print("Conversor de KM a Millas")

while True:
  km = float(input("Introduce el valor en KM: ").replace(",",".")) #antigua linea mia - mejorada
  #se puede definir la variable despues de pedir su valor

  #km = input("Introduce el valor de KM: ")convierte comas en punto
  #km = float(km.replace(",", ".")) convierte comas en punto

  miles = km * 0.6215

  print("Estos KM" + " " + str(km) + " " +"equivalen a" + " " + str(miles)+" "+"Millas")
  print("{0} kilometers is {1} miles.".format(km, miles)) #formato mas corto
  print("%s kilometros igual a %s" % (km, miles)) #formato mas corto
  
  yes = input("Quieres repetir y/n: ")
  if yes.lower() != "y" and yes.lower() !="si" and yes.lower() !="yes":
    break
print("Hasta pronto!")
