def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors
    #divisors2 = [i for i in range(1, num +1) if num % i == 0 ]
    #return divisors2

def run():
    try:
        num = int(input('Ingreese un numero: '))
        print(divisors(num))
        print('Fin del programa')
    except ValueError:
        print('Debes ingresar un numero')  


""" solucion de alguien de la clase
<def divisor(num):
    try:
        if num < 0:
            raise ValueError("ingresa un número positvo")
        divisors =[i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False

def run():
    try: 
        num = int(input(f'Ingresa un número: '))      
        print(divisor(num))
        print("termino mi programa")
    except ValueError:
        print("ingresa un número")
    
if __name__ =='__main__':
    run()> 
"""



if __name__ == '__main__':
    run()