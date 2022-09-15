import math

def run():

#     my_dict = {} #sin list comprehensions

#     for i in range(1, 101):
#         if i % 3 != 0 :
#             my_dict[i] = i**3

#     print(my_dict)      


#my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0 } #con list comprehensions
#print(my_dict)

    natural_numbers =  {i: math.sqrt(i) for i in range(1,101)} #reto clase
    print(natural_numbers)

    








if __name__ == '__main__':
    run()