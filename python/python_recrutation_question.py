"""
Question 1
Level 1

Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
Consider use range(#begin, #end) method
"""

# i % 2 == 0 sprawdzenie czy liczba jest parzysta (podzielna przez 2)
# i % 10 == 0 sprawdzenie czy liczba jest wielokrotnoscia 10

# Opcja 1
# for i in range(2000, 3201):
#     if (i % 7 == 0) and (i % 5 != 0):
#         print(i, end=',')
#
# # Opcja 2
# l = []  # utworzenie pustej listy
# for i in range(2000, 3201):
#     if (i % 7 == 0) and (i % 5 != 0):
#         l.append(str(i))
#
# print(','.join(l))  # laczymy wszyskie elementy listy za pomoca spojnika string w tym przypadku przecinka: ','


"""
Question 2
Level 1

With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
Suppose the following input is supplied to the program:
8
Then, the output should be:
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
"""
# numbers = {}  # utworzenie pustego slownika
# n = int(input("Podaj liczbę całkowitą: "))  # wprowadzenie liczby i zrzucenie jej na inta (liczbe calkowita)
#
# for i in range(1, n+1):  # iterowanie po wartosciach od 1 do n
#     numbers[i] = i * i   # tworzenie slownika gdzie klucze sa od 1 do n, a wartosci to druga potega klucza (klucz to i)
#
# print(f'Moj slownik dla liczby calkowitej {n} to {numbers}')
# print('Moj slownik dla liczby calkowitej ' + str(n) + ' to ' + str(numbers))
#
# # Bardziej zaawansowana metoda za pomoca dict comprehension:
# n = int(input("Podaj liczbę całkowitą: "))
# numbers = {i: i * i for i in range(1, n+1)}  # potegi: i*i == i**2,   k*k*k == k**3,

# kiedy jaki nawias?
# 1. {} - deklaracja slownika oraz seta lub f-print
# pusty slownik: {}, set: {2, 3, 4}, lista: [2, 3]
# 2. [] - poruszanie sie po listach za pomoca indeksu, oraz dostawanie sie do slownika po kluczu
# 3. () - przy funkcjach, metodach

"""
Question 3:
Level 2:

Write a program that accepts a sequence of whitespace separated words as input and
prints the words after removing all duplicate words and sorting them alphanumerically.

Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again

Then, the output should be:
again and hello makes perfect practice world
"""
# words = input("Wprowadź sekwencje słów i spacji: ")
#
# list_of_words = words.split()  # podzielenie zdanie za pomoca spacji (domyslnie)
# set_of_words = set(list_of_words)  # usuniecie duplikatow za pomoca setu
# list_of_sorted_words = sorted(list(set_of_words))  # set przerzucilismy na liste w celu posortowania
# output = ' '.join(list_of_sorted_words)  # laczy slowa z listy posortowanych slow
# # bez duplikatow za pomoca wskazanego stringa
# # w tym przypadku spacji
# print(output)


"""
Question 4:
Level 2

Write a program that accepts a sentence and calculate the number of letters and digits.

Suppose the following input is supplied to the program:
hello world! 123

Then, the output should be:
LETTERS 10
DIGITS 3

hint:
sprawdzenie czy string jest liczba: <str>.isdigit() -> i.isdigit()
sprawdzenie czy string jest litera: <str>.isalpha() -> i.isalpha()
"""
# sentence = input("Write a sentence with numbers: ")
#
# digit_counter = 0
# letter_counter = 0
# others_counter = 0
#
# for i in sentence:  # iterowanie po elementach (cyfrach/literach) zdania
#     if i.isdigit() == True:  # sprawdzenie czy element jest liczba
#         digit_counter += 1  # zwiekszenie licznika liczb o 1
#     elif i.isalpha() == True:  # sprawdzenie czy element jest litera
#         letter_counter += 1  # zwiekszenie licznika liter o 1
#     else:   # jezeli nie jest litera ani liczba to nie robi nic: pass
#         others_counter += 1  # zliczanie pozostalych znakow
#
# print(f'Number of letters in sentence is: {letter_counter}, number of numbers is: {digit_counter}')

"""
Question 5:
Level 2:

The list is input by a sequence of comma-separated numbers.
Use a list comprehension to square each odd number in a list.

Suppose the following input is supplied to the program:
1,2,3,4,5,6,7,8,9,
Then, the output should be:
1,9,25,49,81
"""
# [x for x in range(..)] - list comprehension
# [i for i in list(..)]
#
# numbers = input("Podaj sekfencje liczb całkowitych odzieloną przecinkami: ")  # podanie sekwencji liczb i przecinkow
# print(numbers.strip(',').split(','))  # strip pozwala usunac znaki z brzegu zdania
# list_comp = [str(int(x) ** 2) for x in numbers.strip(',').split(',') if int(x) % 2 != 0]  # list comprehension, ktore podnosi do kwadratu
# # wszystkie nieparzyste liczby z zmiennej numbers - numbers.split(',') tworzy liste z sekwencji liczb i przecinkow
# print(list_comp)  # ['1', '9', '25', '49', '81']
# print(','.join(list_comp))
#
# # list comprehension w formie zwyklej petli for:
# list_comp = []
# for x in numbers.strip(',').split(','):
#     if int(x) % 2 != 0:
#         list_comp.append(int(x) ** 2)

"""
Question 6:
Level 2

Question:
Write a program that computes the net amount of a bank account based a transaction log from console input.
The transaction log format is shown as following:
D 100
W 200

D means deposit while W means withdrawal.
Suppose the following input is supplied to the program:
D 300
D 300
W 200
D 100
Then, the output should be:
500
"""
# Opcja pierwsza z z gory podana liczba transakcji

# balance = 0  # poczatkowy stan konta
# number_transaction = input('Prosze podaj liczbe transakcji ktora bedziesz chcial wykonac: ')
#
# for transaction in range(int(number_transaction)):
#     user_input = input('Prosze podaj operacje do wykonania przez bankomat:')
#     values = user_input.split()  # lista stworzona z rozdzielenia inputu za pomoca spacji ['OPERACJA', 'KWOTA']
#     operation_name = values[0]
#     operation_value = values[1]
#     if operation_name == 'D':  # depozyt zwieksza balans
#         balance += int(operation_value)
#     elif operation_name == 'W':  # wyjecie pieniedzy zmniejsza balans
#         balance -= int(operation_value)
#     else:
#         pass  # nie rob nic jezeli operacja nie jest ani D ani W
#
# print(f'''
# #############################
# # Your balance: {balance}        #
# #############################
# ''')

# Opcja druga z liczba transakcji nieznana
# balance = 0  # poczatkowy stan konta
#
# while True:
#     user_input = input('Prosze podaj operacje do wykonania przez bankomat:')
#     if user_input == 'exit':
#         break
#     values = user_input.split()  # lista stworzona z rozdzielenia inputu za pomoca spacji ['OPERACJA', 'KWOTA']
#     operation_name = values[0]
#     operation_value = values[1]
#     if operation_name == 'D':  # depozyt zwieksza balans
#         balance += int(operation_value)
#     elif operation_name == 'W':  # wyjecie pieniedzy zmniejsza balans
#         balance -= int(operation_value)
#     else:
#         break
#       #  pass  # nie rob nic jezeli operacja nie jest ani D ani W
#
# print(f'''
# #############################
# # Your balance: {balance}        #
# #############################
# ''')

# trzecia opcja

# Opcja druga z liczba transakcji nieznana
# balance = 0  # poczatkowy stan konta
# if_continue = 'y'
# while if_continue == 'y':
#     user_input = input('Prosze podaj operacje do wykonania przez bankomat:')
#     values = user_input.split()  # lista stworzona z rozdzielenia inputu za pomoca spacji ['OPERACJA', 'KWOTA']
#     operation_name = values[0]
#     operation_value = values[1]
#     if operation_name == 'D':  # depozyt zwieksza balans
#         balance += int(operation_value)
#     elif operation_name == 'W':  # wyjecie pieniedzy zmniejsza balans
#         balance -= int(operation_value)
#     else:
#         pass  # nie rob nic jezeli operacja nie jest ani D ani W
#     if_continue = input('Czy chcesz kontynuowac (y/n): ')
#     # if if_continue == 'y':
#     #     pass
#     # elif if_continue == 'n':
#     #     break
#
# print(f'''
# #############################
# # Your balance: {balance}        #
# #############################
# ''')

"""
Bank Account class

1.  Create a Python class called BankAccount which represents a bank account,
having as attributes:accountNumber(numeric type), name(name of the account owner as string type), balance.
2.  Create a constructor with parameters: accountNumber, name, balance. hint: (__init__)
3.  Create a Deposit() method which manages the deposit actions. hint: (adding amounts to balance)
4.  Create a Withdrawal() method which manages withdrawals actions. hint: (subtracting amounts from balance)
5.  Create an bankFees() method to apply the bank fees with a percentage of 5% of the balance account.
6.  Create a display() method to display account details.

"""
class BankAccount:
    bank_fee = 0.05  # zmienna klasowa
    def __init__(self, account_number: int, name: str, balance: int):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def Deposit(self, amount: int):
        self.balance += amount
        print(f'You have just deposed {amount}.')

    def Withdrawal(self, amount: int):
        if amount > self.balance:  # to to samo co: self.balance - amount < 0
            print('Your account balance is insufficient.')
        else:
            self.balance -= amount
            print(f'You have just withdrawn {amount}.')

    def bankFees(self):
        old_balance = self.balance
        #self.balance -= 0.05 * self.balance
        self.balance *= 1 - self.bank_fee
        print(f'Bank fees is: {old_balance * self.bank_fee}.')

    def display(self):
        print(f'Hello {self.name}, on your account number {self.account_number} is {self.balance}')

moje_konto_bankowe = BankAccount(7813456, 'Max Max', 0)
moje_konto_bankowe.Deposit(200)
moje_konto_bankowe.Deposit(100)
moje_konto_bankowe.Withdrawal(50)
moje_konto_bankowe.display()

moje_konto_bankowe.Withdrawal(200)
moje_konto_bankowe.bankFees()
moje_konto_bankowe.Withdrawal(50)