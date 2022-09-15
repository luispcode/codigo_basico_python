# filter = [expression(i) for i in list or range if condition]
def run():
    for numeros in range(1,11): # mi solucion sin list comprehensions
        squares = numeros**2
        print(squares)   
    print(squares, 'resultado final con iteraciones')

    squares2 = [numeros2 **2 for numeros2 in range(1,11)]
    print(squares2)

    squares3 = [] #solucion de la clase
    for i in range(1, 11):
        if  i % 3 != 0:
            squares3.append(i**2)
            print(squares3)
    print(squares3, 'resultado final de iteraciones')


    squares4 = [i**2 for i in range(1,11) if i % 3 != 0] #list comprehensions
    print(squares4)

    #Ejercicio en clase

     #solucion larga
    multiple_range = list(range(1, 10000))
    multipleo_of4 = [i * 4 for i in multiple_range]
    multipleo_of6 = [i * 6 for i in multiple_range]
    multipleo_of9 = [i * 9 for i in multiple_range]
    common_multiples = [i for i in multipleo_of4 if i in multipleo_of6 and i in multipleo_of9]
    print(common_multiples)

    #solucion corta
    common_multiples = [i for i in [i * 4 for i in range(1, 10000)] if i in [i * 6 for i in range(1, 10000)] and i in [i * 9 for i in range(1, 10000)]]
    print(common_multiples )

    #solucion de alguien de la clase
    squares = [ i for i in range(1, 100000) if i % 36 == 0]
    print(squares)




if __name__ == '__main__':
    run()