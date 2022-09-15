
def run():
    my_list = [1, "Hello", True, 4.5, [1, 2, 'a']]
    my_dict = {"firstname": "Facundo", "lastname": "García"}

    listan = [
        ['a', 'b', 'c', 'd', 'e', 'f'],
        [1, 2, 3, 4, 5, 6],
        ['!','"','%','&','/', '¿'],
        ['<', '>', '=<', '=>', '!=', '==']
        
    ]

    super_list = [ #dictionaries inside a list.
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martinez"},
        {"firstname": "José", "lastname": "García"}

    ]

    super_dict = { #lists inside a dictionary.
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]

    }

    for key, value in super_dict.items():
         print(key, "-", value)

    for i in super_list:
        for key, value in i.items():
            print(key, "-", value)

    for i in super_list:
         print(i.items())


if __name__ == '__main__':
    run()