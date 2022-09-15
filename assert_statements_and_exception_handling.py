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
        num = input('Ingreese un numero: ')
        if num.isspace or num == '':
            raise ValueError
        assert num.isnumeric and int(num) > 0, 'Debe ingresar un numero positivo entero'
        print(divisors(int(num)))
        print('Fin del programa')
    except ValueError as ve:
        print('debe ingresar al menos un numero') 


if __name__ == '__main__':
    run()