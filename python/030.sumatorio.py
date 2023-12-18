
def sumatorio(numeros):
    """_summary_

    Args:
        numeros (_type_): _description_
    
    Returns:
        float: suma total de los elementos de la lista
    """
    suma = 0
    for num in numeros:
        suma += num
    return suma
        



resultado1 = sumatorio([2, 5, 10, 10])
print(f'resultado1 {resultado1}')

resultado2 = sumatorio([100, 200, 300, 400, 500, 600])
print(f'resultado2 {resultado2}')

    
