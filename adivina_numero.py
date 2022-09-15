import random

def adivina():
    """Funcion principal del juego adivina un numero
    El numero se genera aleatoriamente en cada ejecución"""
    
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mas grande ')
            numero_elegido = int(input('Elige otro numero: '))
        else:
            print('Busca un numero mas pequeño ')
            numero_elegido = int(input('Elige otro numero: '))
    print('Ganaste!' )


if __name__ == '__main__':
    adivina()


