list =[]
list1 =[[1,2,[3,4]],"hola",None]
list1.append("adios")#introduzco un valor a la list1

for i in list1:
    print(i)

print(list1)

capitales = ["madrid", "lisboa", "roma", "berlin"]
capitales.append("buenos aires")
print(capitales)

for cap in capitales:
    print("Estuve en {0}".format(cap))

some_list = [1, 34, 12, 17, 87]
some_list.sort() #ordenar la lista
print(some_list)

another_list = ["tesla", "toyota", "nissan", "ford"]
another_list.sort()
print(another_list)

mixed_list = [22, "elon", True, "SmartNinja", 3.14, 28]
print(mixed_list)

