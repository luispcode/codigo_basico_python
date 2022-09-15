
# num_1 = int(input('Escoge un entero: '))
# num_2 = int(input('Escoge otro entero: '))

# if num_1 > num_2:
#     print('El primer numero es mayor que el segundo')
# elif num_1 < num_2:
#     print('El segundo numero es mayor que el primero')
# else:
#     print('Los dos numeros son iguales')


nombre_1 = input('Jugador 1, ¿Cual es tu nombre?: ')
nombre_2 = input('Jugador 2, ¿Cual es tu nombre?: ')
edad_1 = int(input('¿Cual es tu edad, ' + nombre_1 + '?: '))
edad_2 = int(input('¿Cual es tu edad, ' + nombre_2 + '?: '))

if edad_1 < edad_2:
    print(nombre_1 + ' es menor que ' + nombre_2)
elif edad_1 > edad_2:
    print(nombre_1 + ' es mayor que ' + nombre_2)
else:
    print(nombre_1 + ' & ' + nombre_2 + 'tienen la misma edad. ')        