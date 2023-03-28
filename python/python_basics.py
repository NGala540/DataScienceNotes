# Zad 0.

#name = input('Please provide your name ')
#print(f'Hello world! Your name is {name}')


# Zad 1. Napisz funkcje, ktora przyjmuje dwa argumenty, jezeli ich iloczyn bedzie wiekszy od 1000 to zwraca
# ich sume a jezeli mniejszy badz rowny to zwraca ten iloczyn

# def calculate_product_or_sum(arg1, arg2):
#     product = arg1 * arg2 #liczymy iloczyn
#     if product > 1000:
#         sum = arg1 + arg2
#         return sum
#     elif product < 1000:
#         return product
#     else:
#         return 1000
#
# x = float(input('Please provide 1st number'))
# y = float(input('Please provide 2nd number'))
# result = calculate_product_or_sum(x, y)
# print(f'Your result is: {result}')

# Zad 2.

# lista_0 = [] # deklaracja pustej listy
# lista_1 = list()
#
# lista = ["Tadeusz", "wyszedl", "na", "zakupy"]
# print(lista[0])
# print(lista[-1])
# sublista = lista[1:3] #['wyszedl', 'na']
# print(sublista[-1])
# lista_2 = [1, 2, 3, 4, 5, 6]
# sum_lista = lista + lista_2
# print(sum_lista)
# sum_lista[4] = '.'
# print(sum_lista)
# sum_lista[0] = True
# print(sum_lista)
# print(type(sum_lista[0]))
# print(sum_lista[::2])

# Zad 3.

# a = [1, 3, 6, 11, 15, 13, 21]
# b = [0, -4, 7, 2.6, 8]
#
# print(f'Max value of a list: {max(a)}, min. value of a list is: {min(a)}. The lenght is {len(a)}.')
# print(sorted(a))
#
# c = [0, 0, 0, 3.5, 1]
# a.extend(c)
# a.append(4)
# a.append([2, 5])
# print(a[-1])
# a.pop()
# print(a)
# a.pop()
# print(a)
# a.pop(0)
# print(a)
# a.pop(-1)
# print(a)
#
# print(c)
# del c[-1]
# print(c)
#
#
# list_4 = [1, 3, 4, 5]
# list_4 = list_4[:1] + list([2]) + list_4[1:]
# print(list_4)
#

#Zad 5.

# a = [1, 2]
# b = ['a', 'b', 'c']
#
# c = list(zip(a, b))
# print(c)

#Zad. 6.1

#Zwroc liste ktora zaczyna sie od elementu -10 konczy na 20 i ma krok 2
# a = list(range(-10, 21, 2))
# print(a)
#
# def check_if_in_list(x0, x1, arg):
#     lista = list(range(x0, x1))
#     print(lista)
#     if arg in lista:
#         return True
#     else:
#         return False
#
# arg = int(input('Prosze wprowadz liczbe'))
# arg2 = str(input('Prosze wprowadz imie'))
# result = check_if_in_list(-10, 21, arg)
# print(result)


# # Zad 6.2
# b = ["Kasia", "Adam", "Michal", "Stefan", "Ania"]
# c = ["Franek", "Zosia"]
# arg2 = str(input('Prosze wprowadz imie: '))
#
# def check_if_in_list(list1, arg):
#     print(list1)
#     print(arg)
#     print(type(list1))
#     print(type(arg))
#     if arg in list1:
#         return True
#     else:
#         return False
#
# result = check_if_in_list(b, arg2)
# print(result)
#
# print(arg2 in b or arg2 in c) # Mozna też zastosować skróconą formę warunku if, która zwraca True/False

# Zad. 7

# my_set = set()
# print(type(my_set))
#
# my_set.add(0)
# print(my_set)
# my_set.add(4)
# my_set.add(8)
# print(my_set)
# print(f'Min. value of my set is {min(my_set)}, max: {max(my_set)}, sum of my set is: {sum(my_set)}')
# set_1 = {5, 8, 9}
#
# my_set.update(set_1)
# print(my_set)
#
# list_with_duplicates = [1, 3, 5, 1, 8, 3, 1]
# list_without_duplicates = sorted(list(set(list_with_duplicates)))
# print(list_without_duplicates)
#
# my_set.clear()
# print(my_set)
# my_set.add("Wartosc")
# print(my_set)

#Zad. 8
# cities = {"Warszawa": 2000,
#           "Poznan": 700,
#           "Gdansk": 600}
#
# cities["Krakow"] = 767
# cities["Wroclaw"] = 638
#
# print(f'Number of citizens in Poznan is: {cities["Poznan"]}k.')
#
# del cities["Warszawa"]
# print(cities)
#
# print(cities.get('Sopot', 500))

# print(cities)
#
# if "Lodz" in cities:
#     print(True)
# else:
#     print(False)