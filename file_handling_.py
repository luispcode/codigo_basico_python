#Manipulación de archivos con el administrador de contexto de python.
#with open(<ruta>, <modo_apertura>) as <nombre>(f)

import os

def read():
    numbers = []
    with open('./palabras_hang.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line)) 
    print(numbers)


def write():
    names = ['Luis', 'Miguel', 'Jose', 'Christian']
    with open('./archivos/nombres.txt','w', encoding='utf-8') as f:
        #f.write(str(names))
        #f.write('\n')
        for name in names:            
            f.write(name)
            f.write('\n')


def run():
    read()


if __name__ == '__main__':
     run()