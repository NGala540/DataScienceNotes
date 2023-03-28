# Zad 1.
"""
Zaimplementuj klase dotyczaca podrozy wakacyjnych z metodami liczacymi koszt podrozy oraz czas podrozy.
"""

# import math  # importujemy biblioteke wbudowana math w celu skorzystania z funkcji matematycznych, w szczegolnosci math.ceil()
#
# class VacationDestination:
#     gdynia = 0
#     koszt_za_kilometr = 0.7
#
#     def __init__(self, city, distance, travel_time):
#         self.city = city
#         self.distance = distance
#         self.travel_time = travel_time
#
#     def distance_cost(self):
#         #self.distance = int(self.distance * self.koszt_za_kilometr)
#         self.distance = math.ceil(self.distance * self.koszt_za_kilometr)  # math.ceil pozwala zaokraglic w gore (math.floor w dol)
#         print(f"Koszt dojazdu do {self.city} wynosi: {self.distance} zł")
#
#     def travel_t(self):
#         self.travel_time = int(self.travel_time + self.gdynia)
#         print(f"Hurra! Dojedziesz tam za {self.travel_time} godziny.")
#
# dest1 = VacationDestination('Zakopane', 718, 8)  # inicjalizacja obiektu z argumentami wejsciowymi
# dest1.distance_cost()
# print(dest1.distance)
# print(dest1.travel_time)
#
# dest2 = VacationDestination('Świnoujście', 351, 5)
# dest2.travel_t()
# dest2.distance_cost()



# Zad 2.
"""
Utworz klase bazowa rower, ktora przyjmuje trzy atrybuty: wielkosc kola (int), wielkosc ramy (float),
kolor (str).
Zaimplementuj dwie metody ktore pozwalaja na:
- zmiana wielkosci opon na rozmiar podany w metodzie (int)
- przemalowanie roweru na nowy kolor (str)
"""
# sprawdzenie czy string da sie przerzucic na liczbe: print('572'.isnumeric())
# zeby dopytywac w metodzie o dobry rozmiar kola do skutku trzeba uzyc petli while not str.isnumeric(): input(...)

class Bike:

    def __init__(self, wheel_size, frame_size, color):
        self.wheel_size = wheel_size
        self.frame_size = frame_size
        self.color = color

    def change_wheel_size(self):
        new_wheel_size = int(input('Please provide new wheel size: '))
        self.wheel_size = new_wheel_size

    def change_color(self):
        new_color = input('Please provide new color: ')
        if new_color in ['pink', 'red', 'green', 'blue']:
            self.color = new_color
        else:
            print('Your color is not available!')

# Dodatkowe dwie metody od Marcina zeby zmieniac rozmiar opon o 1 w dol i gore
    def change_wheel_size_up(self):
        self.wheel_size += 1

    def change_wheel_size_down(self):
        self.wheel_size -= 1

# mój_rower = Bike('20', '5', 'black')
# print(f'My bike is {mój_rower.color}, its wheel is {mój_rower.wheel_size} and the frame is {mój_rower.frame_size}.')
# mój_rower.change_wheel_size()
# mój_rower.change_color()
# print('Update!')
# print(f'My bike is {mój_rower.color}, its wheel is {mój_rower.wheel_size} and the frame is {mój_rower.frame_size}.')
# print('Oh no! This wheel is too big! I need a smaller one')
# mój_rower.change_wheel_size_down()
# print(f'My bike is {mój_rower.color}, its wheel is {mój_rower.wheel_size} and the frame is {mój_rower.frame_size}.')
#

# Zad.3
# """
# Opisz klase dziedziczaca po klasie Bike. Dodaj nowy atrybut suspension.
# """
# class MountainBike(Bike):
#     """
#     Mountain bike class.
#     """
#     def __init__(self, wheel_size, frame_size, color, suspension):
#         super().__init__(wheel_size, frame_size, color)  # zaimportowanie atrybutow z klasy bazowej
#         self.suspension = suspension  # nowy atrubut mowiacy o zawieszeniu: True/False
#
#     # Zad 3. Dopisz metode klasy MountainBike, ktora wylacza zawieszenie (zmienia wartosc atrybutu suspension na False)
#     def remove_suspension(self):
#         self.suspension = False
#
#     # Zad 4. Nadpisz metode/metody klasy bazowej
#     def change_wheel_size_up(self):  # nadpisanie metod klasy bazowej, rozmiary kol gorskich zmieniaja sie co 2
#         self.wheel_size += 2
#
#     def change_wheel_size_down(self):
#         self.wheel_size -= 2
#
# moj_rower_gorski = MountainBike(26, 7, 'green', True)
# print(f'My mountain bike is {moj_rower_gorski.color}, its wheel is {moj_rower_gorski.wheel_size} and '
#       f'the frame is {moj_rower_gorski.frame_size} and suspension status: {moj_rower_gorski.suspension}.')
# moj_rower_gorski.remove_suspension()
# print(f'My mountain bike is {moj_rower_gorski.color}, its wheel is {moj_rower_gorski.wheel_size} and '
#       f'the frame is {moj_rower_gorski.frame_size} and suspension status: {moj_rower_gorski.suspension}.')
# print('My wheel size is too big')
# moj_rower_gorski.change_wheel_size()  # skorzystanie z metody klasy bazowej w celu zmiany rozmiaru kola
# print(f'My new wheel size: {moj_rower_gorski.wheel_size}')
# moj_rower_gorski.change_color()
# print(f'My new color: {moj_rower_gorski.color}')
# print('I need bigger wheel anyway')
# moj_rower_gorski.change_wheel_size_up()
# print(f'New wheel size is {moj_rower_gorski.wheel_size}')
#

# Zad. 4
"""
Stwórz klasę Prostokąt, której atrybutami będą wysokość i szerokość figury. Zaimplementuj metody do mierzenia obwodu i pola prostokąta.
Następnie stwórz klasę Kwadrat pamiętając, że każdy kwadrat jest prostokątem, ale nie każdy prostokąt jest kwadratem.
"""
import math

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def calculate_perimieter(self):
        self.parimieter = 2 * (self.width + self.height)

    def calculate_field(self):
        self.field = self.width * self.height


class Square(Rectangle):
    def __init__(self, height):
        super().__init__(self, height)
        self.height = height

    def calculate_perimieter(self):
        self.parimieter = 4 * self.height

    def calculate_field(self):
        self.field = self.height ** 2

    # Zad 4.1 Dopisz metode, ktora pozwala policzyc przekatna kwadratu d = a * sqrt(2)
    def calculate_diagonal(self):
        self.diagonal = self.height * math.sqrt(2)

sample_square = Square(5)
print(f'My square side: {sample_square.height}')
sample_square.calculate_field()
print(f'My square area: {sample_square.field}')
sample_square.calculate_diagonal()
print(f'My square diagonal equals: {sample_square.diagonal}')

sample_square = Square(26)  # nadpisanie obiektu
sample_square.calculate_diagonal()
print(f'My square diagonal equals: {sample_square.diagonal}')