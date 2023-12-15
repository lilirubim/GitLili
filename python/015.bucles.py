
# While Input = Mientras

# Pedir datos al usuario en bucle hasta que los escriba bien

password = 'admin'
password_user= ''

while password_user != password:
    password_user = input('Introduce tu contraseña: ')
    
print('fin')


# EJEMPLO 2: Lo mismo pero con un máximo de 3 reintentos. Utilizando break

password = 'admin'
password_user = ''
intento = 1 #contador para el número de intentos
max_intentos = 3

while intento <= 3:
    password_user = input('Introduce tu contraseña: ')
    if password_user == password:
        print('Credenciales correctas.')
        # ... invocar una función que realice la acción deseada ...
        break # sale del bucle
    intento += 1
    
print('fin')


