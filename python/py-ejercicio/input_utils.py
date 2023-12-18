
"""
    Archivo con funciones de utilidad para leer datos por consola
    utilizando input, while, try except
"""
    
def read_int(prompt):
    while True:
        try:
            numero = int(input(prompt)) # devuelve el valor leìdo por consola
            return numero
        except Exception:
            print('No se ha podido leer el número int')
            
edad = read_int('Introduce tu edad: ')
     
     
                
def read_float(prompt):
    while True:
        try:
            numero = float(input(prompt)) # devuelve el valor leìdo por consola
            return numero
        except Exception:
            print('No se ha podido leer el número float')    

altura = read_float('Introduce tu altura: ')    


            
def read_bool(prompt):

    respuesta = input(prompt)
    booleano = respuesta.lower() in ['si', 'yes', 'sí'] # devuelve el valor leìdo por consola
    return booleano
        
            
texto =  read_bool('Eres guapa? ')
print(f'Por supuesto {texto}')
