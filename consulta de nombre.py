def saludo(nombre):
    mensaje_saludo = 'Bienvenido al sistema'
    mensaje_final = mensaje_saludo + ' ' + nombre
    longitud_cadena = mensaje_final + ', ' + '\n' +  'la longitud de la cadena es : ' + str(len(mensaje_final))
    return longitud_cadena


def run():
    usuario = input('Cual es su nombre?: ')
    ingreso = saludo(usuario)
    print(ingreso)


if __name__ == '__main__':
    run()