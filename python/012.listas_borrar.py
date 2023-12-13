
# borrar elementos de una lista existente

phones = ['890988', '998766', '765789', '997659']

# remove () borra un elemento que pasemos por parámetro

phones.remove('998766')
print(phones)

# pop() elimina y devuelve el último elemento de la lista o por su índice
pendientes_calificacion = ['Aitor', 'Yessi', 'judith', 'Noemi', 'Silvia']
alumno_a_calificar = pendientes_calificacion.pop() # vacio es el último de la lista
print(f"alumno_a_calificar {alumno_a_calificar}")

alumno_a_calificar = pendientes_calificacion.pop(2) # borra el 3
print(f"alumno_a_calificar {alumno_a_calificar}")





