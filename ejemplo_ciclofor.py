def potencial(x):
    for i in range(2,100,2):
        exponencial = x**i
        print(exponencial)
        

def run():
    x = int(input('Ingrese un numero: '))
    print('Los valores son: ', )
    potencial(x)



if __name__ == '__main__':
    run()