
# lista de precios
# filtrar precios por rango



def filtrar_precios(precios, precio_min, precio_max):
    
    lista = []
    
    
    for precio in precios:
    
        if precio_min <= precio <= precio_max:
            
            lista.append (precio)  # append permite agregar un elemento al final de la lista
    
    return lista
        

   
precios = [20.99, 42.33, 55.50, 90.77, 36.77, 47.89]    




# parametros: lista de precios, precio minimo, precio maximo
# precios_filtrados es una lista de resultados, de precios filtrados

precios_filtrados = filtrar_precios(precios, 30, 50)
print(f'precios_filtrados{precios_filtrados}')
