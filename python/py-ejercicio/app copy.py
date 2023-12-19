'''
Crear una lista de precios

En un bucle infinito imprimir un menú de opciones:
1 - Ver todos los precios
2 - Ver un precio por posición: introduce de 1 en adelante, le restamos 1 para que empiece en 0
3 - Crear un nuevo precio
4 - Actualizar un precio existente
5 - Borrar un precio existente
6 - Borrar todos los precios
7 - Salir

Para utilizar los métodos que están en input_utils: read_int, read_float, read_bool
'''

from input_utils import read_int, read_float, read_bool


precios = [29.99, 44.89, 64.67]

def ver_precio(precios):
    print('Ha elgido ver todos los precios')
    print(precios)

def un_precio(precios):
    print('Ha elegido ver um precio en concreto')
    posicion = read_int('Introduce la posición de precio que desea consultar: ')
    if 1 <= posicion <= len(precios):
        print(precios[ posicion - 1]) # -1 para empezar em 1
    else:
        print('posición incorrecta')

def crear_precio(precios):
    print('Ha elegido crear un precio ') 
    crear_precio = read_float('Introduce el nuevo precio: ')
    precios.append(crear_precio)

def act_precio(precios):
    print('Ha elegido actualizar un precio existente')     
    print(precios)
    posicion = read_int('Introduce la posición del precio que desea modificar: ')
    if 1 <= posicion <= len(precios):
        nuevo_precio = read_float('Introduce el nuevo precio: ')
        precios[posicion - 1] = nuevo_precio
    else:
        print('posición incorrecta')

def borrar_precio(precios):
    print('Has elegido borrar un precio existente.')
    print(precios)
    posicion = read_int('Introduce la posición del precio que desea borrar: ')
    if 1 <= posicion <= len(precios):
        precio_borrado = precios.pop(posicion - 1) # saca el elemento por posición
        print(f'Precio borrado exitosamente: {precio_borrado}')
            
    else:
        print('posición incorrecta')

def vaciar(precios):
    print('Ha decidido eliminar todos los precios')
    confirmacion = read_bool('¿Está seguro/a de vaciar el carrito (si/no): ')
    if confirmacion:
        precios.clear()
        print(f'Carrito vacío {precios}')
    else:
        print('no se eliminarán los precios.')

def max_precio(precios):
    max = read_float('Introduce el precio limite: ')
        # Opción 1:
    precios_a_borrar = [] 
    for precio in precios:
        if precio > max:
            precios_a_borrar.append(precio)
        
    for precio in precios_a_borrar:
        precios.remove(precio)

print('''
        Eligir una opción
         1 - Ver todos los precios
         2 - Ver un precio por posición
         3 - Crear un nuevo precio
         4 - Actualizar un precio existente
         5 - Borrar un precio existente
         6 - Vaciar el carrito
         7 - Filtrar el limite de precio por produto
         8 - Salir

        ''')

while True:
    
    opcion = read_int('Introce la opción (1 a 7): ')
    if opcion == 1:
        ver_precio(precios)
    elif opcion == 2:
        un_precio(precios)
    elif opcion == 3:
        crear_precio(precios)
    elif opcion == 4:
        act_precio(precios)
    elif opcion == 5:
        borrar_precio(precios)
          
    elif opcion == 6:
        vaciar(precios)

    elif opcion == 7:
        max_precio(precios)
                      
    elif opcion == 8:
        print('Hasta luego! 😉')
        break
    else:
        print('Opción incorrecta. Introduce un valor en el rango de 1 a 7.')        