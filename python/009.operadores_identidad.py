
# Operadores de identidad

email = None

email_user = input('Introduce tu email: ')

if email_user.endswith('gmail.com'):
    email = email_user


# is
if email is None:
    print('No se ha podido completar el registro.')
    

# is not

if email is not None: # comprueba que el email no sea nulo o vacío
    print('El email es correcto, registro completado.')

# Operadores de membresía
# Comprueban si un valor es miembro de una secuencia string o estructura de datos 

# in
# con textos
print("java" in "curso avanzado de java con spring") # True
print("java" in "curso avanzado de java con Flask") # False

# in en listas
students = ['Yessi','Judith', 'Silvia', 'Noemi']
name = input('Introduce tu nombre ')

if name in students:
    print('Tienes acceso al curso Java')
else:
    print('No eres VIP.')

