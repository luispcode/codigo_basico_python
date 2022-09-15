#ejemplo ciclo for:

def potencial(x):
    values = []
    for i in range(2,10,2):
        exponencial = x*i
        values.append(exponencial)
    return values

#recorrer valores e indices
for indice, valor in enumerate(range(10,20)):
    print(indice, valor)


#Lista con los valores de un rango o iterable
lista = list(range(100))
print(lista)


if __name__ == '__main__':
    x = int(input('Ingrese un numero: '))
    valores = potencial(x)
    print('Los valores son: ',valores)
    
    
    
