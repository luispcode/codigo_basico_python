
def divide_elementos_de_lista(lista, divisor):
    try:
        return [i / divisor for i in lista]
    except ZeroDivisionError as e:
        print(e)
        return lista    


lista = list(range(10))
divisor = 0


print(divide_elementos_de_lista(lista, divisor))

# ejemplo EAFP (easier to ask for forgiveness than permission)
# # Python

# def busca_pais(paises, pais):
#     &quot;&quot;&quot;
#     Paises es un diccionario. Pais es la llave.
#     Codigo con el principio EAFP.
#     &quot;&quot;&quot;
    
#     try:
#         return paises[pais]
#     except KeyError:
#         return None

# ejemplo LBYL (look before you leap, revisa antes de saltar)

# // Javascript

# /**
# * Paises es un objeto. Pais es la llave.
# * Codigo con el principio LBYL.
# */
# function buscaPais(paises, pais) {
#   if(!Object.keys(paises).includes(pais)) {
#     return null;
#   }

#   return paises[pais];
# }
