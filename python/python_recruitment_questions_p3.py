"""Question:
Define a function that can accept two strings as input and print the string with maximum length in console.
If two strings have the same length, then the function should print al l strings line by line.
"""
#
# def two_strings(string1, string2):
#     try:
#         string1_len = len(string1)
#         string2_len = len(string2)
#         if string1_len > string2_len:
#             print(f'Najdluzszy string to: {string1} jego dlugosc to {string1_len}')
#         elif string1_len < string2_len:
#             print(f'Najdluzszy string to: {string2} jego dlugosc to {string2_len}')
#         else:
#             print(f'{string1} oraz {string2} maja rowna dlugosc o wartosci {string1_len}')
#     except TypeError:
#         print('Podales/as zle argumenty funkcji')
#     finally:
#         print('Funkcja zakonczyla dzialanie czy znalazla blad czy nie')
#
# two_strings(123, 'wiertarka')
#
# """
# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
# """
#
# sentence = input('Please provide any sentence: ')
# upper_counter = 0
# lower_counter = 0
#
# for i in sentence:  # zdanie jest sekwencja mozna przez nie iterowac
#     if i.isupper():  # if i.isupper() == True
#         upper_counter += 1
#     elif i.islower():
#         lower_counter += 1
#     else:
#         pass
#
# print(f'UPPER CASE {upper_counter}\nLOWER CASE {lower_counter}')  # znacznik \n pozwala przejsc do nowej linii w princie

"""
Question:

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its
input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
"""
# funkcja int pozwala zamienic liczby z systemu dwojkowego (binarnego) na system dziesietny: int(p, 2)
# print(int('0100', 2)) #0100 = 4
# print(int('0011', 2)) #0011 = 2 + 1 = 3
# print(int('1010', 2)) #1010 = 10 <---- jest podzielna przez 5
# print(int('1001', 2)) #1001 = 9

# raw_binary_numbers = input('Prosze wprowadz dowolna sekwencje 4-cyfrowych liczb binarnych oddzielonych przecinkami: ')
# binary_numbers = raw_binary_numbers.split(',')
# binary_numbers_4_dig_only = [x for x in binary_numbers if len(x) == 4]  # odfiltrowuje lcizby nie 4 cyfrowe
# results = []  # pusta lista na lapanie wynikow
# for i in binary_numbers:
#     try:
#         num = int(i, 2)  # przypisanie wartosci dziesietnej mojej liczby
#         #print(f'{i}: {num}')  # wyswietlenie wartosci liczb w formacie binarnym (i) oraz w formacie dziesietnym (num)
#         if num % 5 == 0:  # sprawdzamy podzielnosc przez 5 (np. 7 nie jest podzielne przez 5, bo 7 / 5  = 1 reszty 2 wiec reszta 2 != 0)
#             results.append(i)  # chcemy pokazywac w konsoli liczby binarne a nie dziesietne wiec printujemy i a nie num
#     except ValueError as e:
#         print(f'{i} nie jest liczba binarna, szczegoly bledu - nazwa: {e}, argumenty: {e.args}, typ: {type(e)}')
# print(','.join(results))

# """
# Question 12
# Level 2
#
# Question:
# Write a program, which will find all such numbers between 1000 and 10000 (both included) such that each digit of
# the number is an even number.
# The numbers obtained should be printed in a whitespace-separated sequence on a single line.
# """
# results = []
#
# for i in range(1000, 80001):  # 10001 bo chcemy zeby 10000 bylo zawarte w przedziale
#     s = str(i)  #  "1001"
#     try:
#         if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and \
#                 int(s[3]) % 2 == 0 and int(s[4]) % 2 == 0:  # sprawdzenie podzielnosci
#             results.append(s)
#     except IndexError:
#         if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
#             results.append(s)
#
# print(' '.join(results))
#

"""
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with
a given steps. The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after the direction are steps.
Please write a program to compute the distance from current position after a sequence of movement and original point.
If the distance is a float, then just print the nearest integer.
Example:
If the following tuples are given as input to the program:
Starting from (0,0)
UP 5 (0,5)
DOWN 3 (0,2)
LEFT 3 (-3,2)
RIGHT 2 (-1, 2)
"""
# import math
#
# position = [0, 0]  #[x-owa wspolrzedna, y-owa wspolrzedna]
# # position[0] - x-owa wspl.
# # position[1] - y-owa wspl.
#
# while True:
#     command = input('Prosze wprowadz komende dla robota: ')
#     if command == 'exit' or 'EXIT':
#     # if command in ['exit', 'EXIT']  # to samo dzialanie
#     # if command.upper() == 'EXIT':
#         break
#     try:
#         direction = command.split()[0].upper()
#         n_steps = int(command.split()[1])
#         print(f'Robot porusza sie w kierunku {direction} o liczbe krokow: {n_steps}')
#         if direction == 'UP':
#             position[1] += n_steps  # poruszamy sie w gore, czyli po wspl. Y czyli position[1], dodajemy liczbe krokow
#         elif direction == 'DOWN':
#             position[1] -= n_steps
#         elif direction == 'LEFT':
#             position[0] -= n_steps  # poruszamy sie w lewo, czyli po wspl. X czyli position[0], odejmujemy liczbe krokow
#         elif direction == 'RIGHT':
#             position[0] += n_steps
#         else:
#             pass
#     except IndexError:  # lub except (IndexError, ValueError)
#         print('Dostepne komendy to UP, DOWN, LEFT, RIGHT podane ze spacja i liczba krokow')
#     except ValueError:
#         print('Blednie podana liczba krokow')
# try:
#     distance = int(math.sqrt(position[0] ** 2 + position[1] ** 2))
# except NameError:
#     print('Biblioteka, z ktorej chcesz skorzystac nie jest zaimportowana')
#     distance = int((position[0] ** 2 + position[1] ** 2) ** (1/2))
# print(f'Dystans od punktu (0,0) to w przyblizeniu: {distance}')

"""
Write a Python class Restaurant with attributes like menu_items, book_table, and customer_orders,
and methods like add_item_to_menu, book_tables, and customer_order.

Perform the following tasks now:
Now add items to the menu.
Make table reservations.
Take customer orders.
Print the menu.
Print table reservations.
Print customer orders.
"""
class Restaurant:
    def __init__(self, menu_items: dict, book_table: list, customer_orders: dict):
        self.menu_items = menu_items
        self.book_table = book_table
        self.customer_orders = customer_orders

    def add_item_to_menu(self, item: str, price: int):
        self.menu_items[item] = price
        print(f'You have just added new item to menu: {item} with price {price}')

    def book_tables(self, tables: list):
        for table in tables:  # unikanie duplikatow w zarezerwowanych stolikach
            if table in self.book_table:
                pass
            else:
                self.book_table.append(table)
                print(f'You have just booked new tables to the list: {table}')

    def customer_order(self, table_number: int, ordered_items: list):
        self.customer_orders[table_number] = ordered_items
        print(f'Table number {table_number} ordered {ordered_items}')

    def print_menu(self):
        print('######## MENU ########')
        for idx, (k, v) in enumerate(self.menu_items.items(), 1):
            print(f'{idx}. {k}: {v} [PLN]')

    def print_reserved_tables(self):
        print(f'Reserved tables for now are: {self.book_table}')

try:
    san_giovani = Restaurant({'spaghetti bolenese': 35, 'pizza marinara': 20}, [3, 5], {})
    san_giovani.print_menu()
    san_giovani.add_item_to_menu('foccacia', 17)
    san_giovani.print_menu()
    san_giovani.book_tables([7])
    san_giovani.print_reserved_tables()
    san_giovani.customer_order(7, ['foccaci', 'ice cream'])
    print(san_giovani.customer_orders)
    san_giovani.book_tables([7])
    san_giovani.print_reserved_tables()
    san_giovani.add_item_to_menu('pizza blanca')
except TypeError:
    print('Wrong arguments have been provided')