# class Employee:
#     raise_amount = 1.04
#     seniorities = ['Junior', 'Mid', 'Senior']
#     total_employee_number = 0  # licznik pracownikow
#
#     def __init__(self, first_name, last_name, pay):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.pay = pay
#         self.email = f'{first_name}.{last_name}@xyz.com'
#         self.seniority = 0
#         self.dev_seniority = self.seniorities[0]
#         Employee.total_employee_number += 1
#         self.id = Employee.total_employee_number
#         print(f'Dodales nowego pracownika: {self.first_name} {self.last_name}.')
#
#     def give_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#         print(f'Brawo! Po podwyzce Twoja pensja wynosi: {self.pay}')
#
#     def give_promotion(self):
#         self.seniority += 1
#         self.pay = int(self.pay * 1.2 * self.raise_amount)
#         print(f'Hurra! You have got a promotion, your pay is now: {self.pay} and your new level is: {self.seniority}')
#
#     def give_developers_promotion(self):
#         self.dev_seniority = self.seniorities[1]
#
#     @classmethod
#     def set_new_raise_amount(cls, new_value):
#         cls.raise_amount = new_value
#
#     @classmethod
#     def new_total_empl_number(cls, new_number):
#         cls.total_employee_number = new_number
#
#     @staticmethod
#     def welcome_function(company_name):
#         return f'#### Welcome to {company_name}!!! ####'
#
# pracownik_1 = Employee('Jan', 'Kowalski', 6000)
# pracownik_1.give_promotion()
#
# pracownik_2 = Employee('Danuta', 'Nowak', 7000)
# pracownik_2.give_promotion()  # metoda
#
# print(pracownik_2.email)  # atrybut
# print(pracownik_1.pay)
#
# print(format(pracownik_2.id, "03d"))  # wyswietlanie liczby w formacie 3 cyfrowym
#
# print(f'Podwyzka bazowa w 2022 roku wynosi: {Employee.raise_amount}.')
# # Firma wprowadza zwiekszenie podwyzki
# Employee.set_new_raise_amount(1.10)
# print(f'Podwyzka bazowa w 2023 roku wynosi: {Employee.raise_amount}.')
#
# print(f'Liczba pracownikow w 2022 roku: {Employee.total_employee_number}')
# Employee.new_total_empl_number(200)
# print(f'Liczba pracownikow w 2023 roku: {Employee.total_employee_number}')
#
# print(Employee.welcome_function('My new brand company sp. z o.o.'))

# Zad 1.
"""
Wymysl klase ktora przyjmuje min. trzy argumenty w trakcie inicjalizacj, tworzy atrybuty oraz posiada dwie metody, ktore
modyfikuja te atrybuty.
"""

# Zad 1A
# Dopisz metode klasowa ktora zamienie wartosc mileage, ktora domyslnie jest w milach na kilometry.
# 1 mila to 1.6 km w przyblizeniu

# class Jetpack:
#     mileage = 0
#
#     def __init__(self, series, model):
#         self.series = series
#         self.model = model
#         self.ignition = False
#         self.movement_up = False
#         self.movement_forward = False
#
#     def ignite(self):
#         self.ignition = True
#
#     def go_up(self):
#         self.movement_up = True
#         Jetpack.mileage += 1
#
#     def go_forward(self):
#         self.movement_forward = True
#         Jetpack.mileage += 1
#
#     @classmethod
#     def convert_miles_to_km(cls):
#         cls.mileage = cls.mileage * 1.6  # cls.mileage *= 1.6
#
#
# my_little_jetpack = Jetpack('series_1', 'model_small')
# print(f'My current jetpack status: {my_little_jetpack.ignition}')
# my_little_jetpack.ignite()
# print(f'My current jetpack status: {my_little_jetpack.ignition}')
# for i in range(100):
#     my_little_jetpack.go_forward()
#
# print(Jetpack.mileage)

# Zad 2
class Animals:
    rok = 2023

    def __init__(self, imie, waga, rok_urodzenia, gatunek=None):  # argument=None to opcjonalny argument, nie trzeba go definiowac
        self.imie = imie
        self.waga = waga
        self.rok_urodzenia = rok_urodzenia
        self.gatunek = gatunek

    def wiek(self):
        self.wiek = self.rok - self.rok_urodzenia
        return self.wiek

    def zmiana_wagi(self):
        self.waga += self.wiek
        return self.waga

pies = Animals('Burek', 50, 2015)

wiek = pies.wiek()
waga = pies.zmiana_wagi()
print(f'Wiek zwierzaka {pies.imie} wynosi: {wiek} a jego waga: {waga}')

kot = Animals('Stefan', 7, 2020, 'kot')
print(f'{kot.gatunek} o imieniu {kot.imie} wazy aż {kot.waga} kg.')
