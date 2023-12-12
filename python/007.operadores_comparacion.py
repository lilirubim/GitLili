# Todos estos operadores devuelven boolean True o False

# = es para asgnación de un valor a una variable

# Igual ==

password = input('Introduce contraseña: ')
password_correct = 'admin'
print(password == password_correct)

email = input('Introduce tu email: ').lower()
email_correct = 'alan@gmail.com'
print(email == email_correct)


# Distinto que !=
# INVERSA DE ==

password = input('Introduce contraseña: ')
password_correct = 'admin'
if password != password_correct:
    print("Credenciales incorrectas")


respuesta_correcta = 'Madrid'
capital = input('Introduce capital de España: ').lower().replace(" ","")

if capital != respuesta_correcta:
    print('Respuesta incorrecta')
else:
    print('Has acertado, toma un pin.')
    
    
    
# > mayor que (Greater than, GT)
# >= mayor o igual que (Greater than or equals, GTE)
print(50 > 20) # True
print(50 > 50) # False
print(50 >= 50) # True
print(50 > 100) # False

# < menor que (Less than, LT)
# <= menor o igual que (Less than or equals, LTE)
print(50 < 20) # False
print(50 < 50) # False
print(50 <= 50) # True
print(50 < 100) # True

