import functions as f

f.hello_name("Ulises")
f.hello()
f.bye()
text = f.say_hello(name="Matt")
print(text)

sum2 = f.sum(5, 6)
print(str(sum2))

sum1 = f.sum(n1=int(input("ingrese n1: ")), n2=int(input("ingres n2: ")))
print(str(sum1))