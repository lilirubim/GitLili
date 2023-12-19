 while True:
        try:
            resultado = input(prompt).lower()
            if resultado == 'si':
                return True
            elif resultado == 'no':
                return False
            else:
                print('Valor incorrecto')
                #no te saca del bucle, repite otra interación hasta que escriba si
        
        except Exception:
            print('No se ha podido leer')
            