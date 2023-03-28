# """
# Zad 3.
# Stwórz funkcję, która sprawdzi, czy liczba podana w argumencie jest pierwsza.
# Funkcja powinna przyjmować wartość numeryczną, a zwracać powinna wartość logiczną True/False.
# Np.
# Dla 11 funkcja zwróci True, natomiast dla 12 -> False.
# """
#
# def is_prime_number(num):
#     """
#     Checks if number is prime.
#     It must: n % 1 == 0 and n % n == 0, there is no other dividers.
#     :param n: sample number from user
#     :return: True/False
#     """
#     if num <= 1:
#         return False
#     else:
#         for i in range(2, num):
#             if num % i == 0:
#                 print(f'{i} is divider, so {num} is not a prime number')
#                 return False
#     print(f"We couldn't find any dividers for {num} so {num} is a prime number.")
#     return True
#
# output = int(input('Please provide any number: '))
# print(is_prime_number(output))

# Zad. 4
# """
# Stwórz funkcję, która sprawdzi,
# czy podany jako argument napis jest palindromem
# (tj. czytany od przodu i wspak jest dokładnie taki sam, np. „kajak”, „Madam”).
# """
#
# def is_palindrom(word):
#     word = word.lower()
#     word_reversed = word[::-1]
#     if word == word_reversed:
#         return True
#     else:
#         return False
#
# word = input('Please provide any word: ')
# print(is_palindrom(word))

# # Zad. 5
# """
# Stwórz funkcję, która obliczy liczbę małych i wielkich liter w ciągu.
# np. dla : “The quick Brown Fox”
# oczekiwany wynik :
# LIczba wielkich liter : 3, liczba małych liter : 13
# Podpowiedź: wykorzystaj pętlę, instrukcję warunkową i odpowiednie metody dla stringa.
# """
# # Sample isupper() method usage:
# # print('A'.isupper())
# # print('asd'.isupper())
# # print('ASA'.isupper())
#
# def counting(sent):
#     low_letters = 0
#     upper_letters = 0
#     for i in sent:
#         if i.isupper():
#             upper_letters += 1
#         elif i.islower():
#             low_letters += 1
#     return low_letters, upper_letters
#
# #sent = 'The quick Brown Fox in The Wood'
# sent = input('Please provide any sentence: ')
# low_letters, upper_letters = counting(sent)  # wywolanie funkcji, ktora zwraca 2 wartosci
# print(f"There are {low_letters} low letters and {upper_letters} upper letters in sentence: {sent}")
#
# # Zad. 6
# """
# Napisz funkcję, która przyjmuje dwa stringi i sprawdza, czy są swoimi anagramami. Na przykład:
# „army” i „Mary”,
# „dzielenia” i „niedziela”,
# „Quid est veritas?” i „Vir est qui adest”,
# „Jim Morrison” i „Mr Mojo Risin”
# „Tom Marvolo Riddle” i „I am Lord Voldemort”
# """
#
# def is_anagram(sent1, sent2):
#     """
#     Definiacja anagramu:
#         wyraz, wyrażenie lub całe zdanie powstałe przez przestawienie
#         liter bądź sylab innego wyrazu lub zdania,
#         wykorzystujące wszystkie litery (głoski bądź sylaby) materiału wyjściowego
#     """
#     sent1 = sent1.replace(' ', '').lower()  # replace wyszukuje dany substring i zamienia go na inny
#     sent1 = sorted(sent1)
#
#     sent2 = sent2.replace(' ', '').lower()
#     sent2 = sorted(sent2)
#
#     if sent1 == sent2:
#         return True
#     else:
#         return False
#
# print(is_anagram('Jim Morrison', 'Mr Mojo Risin'))

# # Zad 1.
# """
# Utworz plik o nazwie "testowy_plik_1.txt" i wpisz do niego:
#  "Czesc,
#
#  jak sie masz?
#
#  Pozdrawiam"
# """
# with open('testowy_plik_1.txt', 'w') as f:
#     f.write('Czesc,\n\njak sie masz?\n\nPozdrawiam')
#
# with open('testowy_plik_1.txt', 'w') as f:
#     f.write('Czesc\n\n')
#     f.write('jak sie masz\n\n')
#     f.write('Pozdrawiam\n')
#
# with open('testowy_plik_1.txt', 'w') as f:
#     f.write("""
#      Czesc,
#
#      jak sie masz?
#
#      Pozdrawiam"
#     """)
#
#     print(len(f.readlines())) # pozwala na sprawdzenie dlugosci tekstu (liczy linijki)

# Zad. 2
"""
Odczytaj tresc pliku tekstowy_plik_1.txt po modyfikacji recznej oraz wypisz numer kazdej linijki.
"""

# with open("testowy_plik_1.txt", "r") as f:
#     for index, line in enumerate(f):
#         print(f'{index}: {line}')

# Co to jest enumerate i jak tego uzywac?
# for index, i in enumerate(['a', 'b', 'c']):
#     print(f'Indeks {index}: {i}')

# Zad 7.
"""
Napisz funkcję, która zwróci 5 najczęstszych słów z dzieła Mickiewicza.
https://pastebin.com/raw/aAHeW5Pt (przekopiuj i zapisz do pliku tekstowego to, co znajdziesz pod tym linkiem).
Podpowiedź: skorzystaj z funkcji open(), metody split(), słownika oraz pętli.
"""
#print("ala.ma.kota".split('.'))  # jak dziala split?
#
# with open('mickiewicz.txt', 'r', encoding='utf8') as f: # otwieramy kontekst managera z naszym plikiem tekstowyn
#     mickiewicz_dict = {}  # deklarujemy pusty slownik do zliczania slow
#     for line in f:
#         #print(line.split())
#         line_words = [x.lower() for x in line.split()]  # dzielenie zdania na slowa w ramach listy i rzutowanie slow na male litery
#         #print(line_words)
#         for word in line_words:
#             if word not in mickiewicz_dict:
#                 mickiewicz_dict[word] = 1
#             else:
#                 mickiewicz_dict[word] += 1
#
# print(mickiewicz_dict)
# print(mickiewicz_dict['martwym'])
#
# top_5_words_from_mickiewicz = sorted(mickiewicz_dict, key=mickiewicz_dict.get, reverse=True)[:5]
#
# print(10 * '#' + ' Mickiewicz ' + 10 * '#')
#
# for i in top_5_words_from_mickiewicz:
#     value = mickiewicz_dict[i]  # pobranie wartosci z slownika glownego
#     print(f'Slowo: {i} wystapilo {value} razy')
#

with open("mickiewicz.txt", "r") as f:
    mickiewicz_dict = {}
    for line in f:
        line_words = [x.lower() for x in line.split()]
        for word in line_words:
            if word not in mickiewicz_dict:
                mickiewicz_dict[word] = 1
            else:
                mickiewicz_dict[word] += 1

top_5 = sorted(mickiewicz_dict, key=mickiewicz_dict.get, reverse=True)[:5]  # sorted sortuje slownik uzywajac klucza key,
# klucz key musimy okreslic za pomoca dict.get co oznacza sortowanie po wartosciach, domsylnie sortowanie jest od najmniejszej do najwiekszej,
# a my chcemy najwieksze wiec dodajemy slowo kluczowe reverse=True, nastepnie pobieramy 5 wartosci z przodu listy za pomoca [:5]

print(mickiewicz_dict['a'])
for i in top_5:
    print(f"Słowo: {i} wystąpiło {mickiewicz_dict[i]} razy")

