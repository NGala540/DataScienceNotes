# Powtorka z 28.02.2023

# Zad powtorkowe 1
# Napisz funkcje liczaca bmi oraz pobierz od uzytkownika wzrost i wage oraz wyswietl wynik.
# def compute_bmi(weight, height):
#     bmi = weight / height ** 2
#     print(f'Weight: {weight}, height: {height}, bmi: {bmi}')
#     if bmi < 18.5:
#         result = 'underweight'
#     elif bmi > 25:
#         result = 'overweight'
#     else:
#         result = 'normal'
#     return result
#
#
# waga = float(input('Podaj prosze wage: '))
# wzrost = float(input('Podaj swoj wzrost: ')) #prosze podawac w metrach
#
# wynik = compute_bmi(waga, wzrost)
# print(f'Your result is: {wynik}')


# Zad powtorkowe 2
# Wyswietl wartosc liczby mieszkancow dla Gdanska na podstawie ponizszego slownika.
# cities = {"Warszawa": 2000, "Poznan": 700, "Gdansk": 600, "Krakow": 767, "Wroclaw": 638}
#
# print(f'Liczba mieszkancow w Gdansku: {cities["Gdansk"]}')
# print(cities.get("Sopot", 1000))
# print(f"ladne zdanie {cities['Gdansk']}")
# print(f'Liczba mieszkańców Gdańska to: {cities["Gdansk"]}k.')


# Zad powtorkowe 3
# Wyswietl liste ktora sklada sie z elementow od -100 do 100 co 25.
# print(list(range(-100, 101, 25)))
# # Przypisz liste do zmiennej moja_lista oraz 3 element tej listy do zmiennej a i wyswietl go.
# moja_lista = list(range(-100, 100, 25))
# a = moja_lista[2]
# print(a)
# # Do moja_lista dodaj recznie liczby 125 oraz 150 (do konca listy).
# # Opcja 1
# moja_lista.append(125)
# moja_lista.append(150)
# # # Opcja 2
# moja_lista = moja_lista + [125, 150]
# # # Opcja 3
# moja_lista.extend([125, 150])
# #Odwrot liste tyl na przod.
# list(reversed(moja_lista))
# moja_lista = moja_lista[::-1]
# moja_lista.reverse()
# print(moja_lista)

# Zadania 01.03.2023
# Zad 1 List comprehension (wyrażenia listowe)
# moja_lista = [150, 125, 75, 50, 25, 0, -25, -50, -75, -100]
# # Dodaj 10 do kazdego elementu listy
# nowa_lista = [x + 10 for x in moja_lista]
# # Pomnoz dwukrotnie kazdy element wiekszy od 0
# nowa_lista_1 = [x * 2 for x in moja_lista if x > 0]
# print(nowa_lista_1)
# # Utworz liste na podstawie moja_lista, ktora wszystkie elementy mniejsze od zera podniesie do kwadratu
# nowa_lista_2 = [x ** 2 for x in moja_lista if x < 0]
# print(nowa_lista_2)
# # Jakbyśmy chcieli liste zlożoną np, z kwwadratów liczb ujemnych i niezmienionych dodatnich?
# niezmienione_dodatnie = [x for x in moja_lista if x > 0]
# lista_norberta = nowa_lista_2 + niezmienione_dodatnie
# print(sorted(lista_norberta))
# # Jak dzialo modulo? if x % 2 == 0 to wszystkie liczby parzyste, if x % 3 == 0
# # Utworz liste na podstawie moja_lista liczb ktore sa podzielne przez 50 i te liczby podzielic przez 3
# # bez wartosci dziesietnych
# nowa_lista = [x for x in moja_lista if not x % 50]
# print(nowa_lista)

# Zad 2
# cities = {"Warszawa": 2000, "Poznan": 700, "Gdansk": 600, "Krakow": 767, "Wroclaw": 638}
# # Odwroc slownik tak zeby klucz byl slownikiem a slownik kluczem
# reversed_cities_dict = {v: k for k, v in cities.items()}
# print(cities.items())
# print(reversed_cities_dict)
# # Stworz nowy slownik w ktorym zostana miasta ponizej 1000 mieszkancow
# small_cities = {k: v for k, v in cities.items() if v < 1000}
# print(small_cities)
#
# cities_3 = {k * 2: v * 2 for k, v in cities.items() if v < 1000}
# # Wstawka liryczna
# print(cities_3)
# a = 'Miasto'
# print(3*a)
# # Dla miast ponizej 1000 mieszkancow pomnoz wartosc (liczbe mieszkancow) dwukrotnie
# cities_3 = {k: v * 2 for k, v in cities.items() if v < 1000}
# # Dla miast powyzej 601k mieszkancow podnies wartosc do potegi 3 i zamienic na typ float
# new_dict_2 = {k: float(v ** 3) for k, v in cities.items() if v > 601}
# print(new_dict_2)

#Zad 3
#Wyswietl liczby od 1 do 10
# for element in range(1, 11):
#     print(f'Nowy element: {element}')
#
# #Wyswietl zdanie z nazwa miasta i liczba mieszkancow
# cities = {"Warszawa": 2000, "Poznan": 700, "Gdansk": 600, "Krakow": 767, "Wroclaw": 638}
# for klucz, wartosc in cities.items():
#     print(f'Liczba mieszkancow dla miasta {klucz} wynosi: {wartosc}')
#
# # Przeiteruj ponizsze elementy a i b
# a = ["Ala", "ma", "psa"]
# for word in a:
#     print(word)
#
# b = "Onomatopeja"
# for x in b:
#     print(x)

#Zad 4
# Napisz funkcje ktora wylicza od podanej liczby do 100
# def count_from_x_to_100(x):
#     while x <= 100:
#         print(x, end=" ") #print pozwalajacy na wypisanie liczb w rzedzie print(... , end=" ")
#         x = x + 1

# count_from_x_to_100(80)

# Zad 5 - izogram (slowo bez powtarzajacych sie liter)
# print('ASDASDSAD'.lower())
# print('asdsadasd'.upper())
# def is_isogram(word):
#     letters = set() #Utworzenie pustego zbioru do zbierania liter ze slowa
#     for l in word.lower(): #Iterowanie po kolejnych literach slowa z malych liter
#         print("Nowe wykonanie petli")
#         print(l)
#         if l in letters:
#             return False
#         letters.add(l)
#         print(letters)
#     return True
#
# print(is_isogram("zamek"))

# Zad. 1
# Napisz program, który zamieni wprowadzony przez użytkownika ciąg cyfr na formę tekstową, np.:
# 112 - > „jeden jeden dwa”
# 9973 -> „dziewięć dziewięć siedem trzy”
# Podpowiedź: potrzebujesz funkcji input(), słownika oraz pętli.

# number = str(input('Prosze wprowadz liczbe: '))
#
# letters_dict = {'0': 'zero', '1':'jeden', '2':'dwa', '3':'trzy', '4':'cztery', '5':'pięć',
#             '6':'sześć', '7':'siedem', '8':'osiem', '9':'dziewięć'}
#
# new_word = '' # zadeklarowanie pustego stringa
# for num in number:  # iterowanie po wprowdzonym slowie
#     new_word = new_word + letters_dict[num]  # dodawanie nowego slowa ze slownika
#     new_word += " "  # dodawanie spacji miedzy slowami
#
# new_word = new_word.strip()  # usuniecie whitespaceow czyli spacji z poczatka i konca stringa
#
# print(new_word)

# Zad. 2
# Stwórz funkcję przyjmującą listę liczb całkowitych, a zwracającą informację, na której pozycji znajduje się najmniejsza liczba.
# Nie korzystaj z wbudowanych funkcji.
# np. dla listy [42, 13, 56, 7, 12, 3, 85] funkcja powinna zwrócić 5, ponieważ pod tym indeksem w tej liście znajduje się element najmniejszy.
# def find_index_of_smallest(my_list):
#     min_value = min(my_list)
#     output = my_list.index(min_value)
#     return output
#
# result = find_index_of_smallest([42, 13, 56, 7, 12, 0, 2, -1, 3, 85])
# print(result)