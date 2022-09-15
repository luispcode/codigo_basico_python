from functools import reduce

def main():

    #Filter, filtra elementos y se reducen los outputs
    myList = [1,4,5,7,9,13,19,21]

    odd = list(filter(lambda x: x % 2 != 0, myList))
    print(odd)

    #Map #se ejecuta una operacion con los mismos outputs
    myList2 = [1, 2, 3, 4, 5]

    squares = list(map(lambda x: x**2, myList2))
    print(squares)

    #reduce lambda toma 2 argumentos y se utilizan los 2 primeros elementos de la lista 
    myList3 = [2, 2, 2, 2, 2]
    
    allMultiplied = reduce(lambda a, b: a * b, myList3)
    print(allMultiplied)

if __name__ == '__main__':
    main()