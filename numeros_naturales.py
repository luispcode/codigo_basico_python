def run():
    for numeros in range(1,100):
        squares = numeros**2
        print(squares)

    squares2 = [numeros **2 for numero in range(1,100)]
    squares2


if __name__ == '__main__':
    run()