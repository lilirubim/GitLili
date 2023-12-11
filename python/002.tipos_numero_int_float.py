edad = 30 # nùmero entero

peso = 80.34 #número con decimales

print(edad + 2)

print(peso - 5)

#utilizando constructor
edad2 = int(40)
peso2 = float(90.55)
print(edad2 + 2)
print(peso2 - 5)

# convertir de texto a número
edad3 = "70"
peso3 = "100.21"

#print(edad3 + 2) # error
#print(peso3 - 5) # error - TypeError: can only concatenate str (not "int") to str

edad3_num = int(edad3) # convierte el texto "70" a número 70
print(edad3_num + 2)

peso3_num = float(peso3) # convierte el texto "100.21" a úmero 100.21
print(peso3_num - 5)


# convertir de número a texto
codigo_postal = str(28000) #convierte de int a str
print(codigo_postal)
