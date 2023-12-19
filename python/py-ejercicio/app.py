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

while True:
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
    opcion = read_int('Introce la opción (1 a 7): ')
    if opcion == 1:
        print('Ha elgido ver todos los precios')
        print(precios)
    elif opcion == 2:
        print('Ha elegido ver um precio en concreto')
        posicion = read_int('Introduce la posición de precio que desea consultar: ')
        if 1 <= posicion <= len(precios):
            print(precios[ posicion - 1]) # -1 para empezar em 1
        else:
            print('posición incorrecta')
    elif opcion == 3:
        print('Ha elegido crear un precio ') 
        crear_precio = read_float('Introduce el nuevo precio: ')
        precios.append(crear_precio)
    elif opcion == 4:
        print('Ha elegido actualizar un precio existente')     
        print(precios)
        posicion = read_int('Introduce la posición del precio que desea modificar: ')
        if 1 <= posicion <= len(precios):
            nuevo_precio = read_float('Introduce el nuevo precio: ')
            precios[posicion - 1] = precio_modificado
        else:
            print('posición incorrecta')
    elif opcion == 5:
        print('Has elegido borrar un precio existente.')
        print(precios)
        posicion = read_int('Introduce la posición del precio que desea borrar: ')
        if 1 <= posicion <= len(precios):
            precio_borrado = precios.pop(posicion - 1) # saca el elemento por posición
            print(f'Precio borrado exitosamente: {precio_borrado}')
            
            #Otra manera:
            #precio_borrado = precios[posicion -1]
            #precios.remove(precio_borrado) 
            
            # Otra manera 2:
            # del precios[posicion -1]
        else:
            print('posición incorrecta')
            
    elif opcion == 6:
        print('Ha decidido eliminar todos los precios')
        confirmacion = read_bool('¿Está seguro/a de vaciar el carrito (si/no): ')
        if confirmacion:
            precios.clear()
            print(f'Carrito vacío {precios}')
        else:
            print('no se eliminarán los precios.')

    elif opcion == 7:
        max = read_float('Introduce el precio limite: ')
        # Opción 1:
        #precios_a_borrar = [] 
        #for precio in precios:
        #    if precio > max:
        #        precios_a_borrar.append(precio)
        
        #for precio in precios_a_borrar:
        #    precios.remove(precio)
        
        #  Opción 2:
        precios = [precio for precio in precios if precio <= max]
         
                    
    elif opcion == 8:
        print('Hasta luego! 😉')
        break
    
    else:
        print('Opción incorrecta. Introduce un valor en el rango de 1 a 7.')        