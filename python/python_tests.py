# import unittest
#
# class MyTest(unittest.TestCase):
#
#     def setUp(self) -> None:
#         print('Wlaczam sie przed kazdym testem')
#
#     def test_01(self):
#         self.assertEqual(2, 2)
#
#     def test_02(self):
#         self.assertEqual(2, int('2'))
#
#     def test_03(self):
#         print('Test czy 3 i 5 sa rowne')
#         self.assertEqual(3, 5)
#
#     def test_04(self):
#         print('test 04')
#         self.assertIn('pies', ['zaba', 'kot', 'pies'])
#
#
#     def test_05(self):
#         with self.assertRaises(ValueError):
#             int('XXXXXXXXX')
#
#     def test_06(self):
#         with self.assertRaises(KeyError):
#             int('XXXXXXXXX')
#
#     def tearDown(self) -> None:
#         print('wykonuje sie po kazdym tescie')
#
# if __name__ == '__main__':
#     unittest.main()

# """
# Napisz klase Calculator(), ktora bedzie posiadala 4 metody do dodawania, odejmowania, mnozenia i dzielenia dwoch liczb.
# Nastepnie napisz klase testujaca kalkulator.
# """
# import unittest
#
# class Calculator:
#     def __init__(self):
#         print('Welcome to my calculator')
#
#     def add(self, a, b):
#         return a + b
#
#     def substract(self, a, b):
#         return a - b
#
#     def multiply(self, a, b):
#         return a * b
#
#     def divide(self, a, b):
#         return a / b
#
#
# class TestCalculator(unittest.TestCase):
#
#     def setUp(self) -> None:
#         self.calculator = Calculator()  # utworzenie instancji kalkulatora za pomoca klasy Calculator()
#                                         # przypisanie jej do atrybutu klasy TestCalculator: self.calculator
#     def tearDown(self) -> None:
#         print('I"ve just finished a test')
#
#     def test_add_01(self):
#         x = int(input('podaj liczbe'))
#         y = int(input('podaj druga liczbe'))
#         expected_result = int(input('podaj oczekiwany wynik'))
#         result = self.calculator.add(x, y)
#         self.assertEqual(result, expected_result)
#
#     def test_add_02(self):
#         result = float(self.calculator.add(10.0, -5))
#         self.assertIs(result, 5)
#
#     def test_add_03(self):
#         result = self.calculator.add(10.0, -5)
#         self.assertEqual(result, 5)
#
#     def test_add_04(self):
#         result = self.calculator.add(0, 81)
#         self.assertIn(result, [81, 93])
#
#     def test_substract_01(self):
#         result = self.calculator.substract(9, 3)
#         self.assertEqual(result, 6)
#
#     def test_substract_02(self):
#         result = self.calculator.substract(float(51), int(30))
#         self.assertEqual(result, 21)
#
#     def test_multiply_01(self):
#         result = self.calculator.multiply(13, 9)
#         self.assertNotIn(result, [13, 9])
#
#     def test_divide_01(self):
#         result = self.calculator.divide(30, 6)
#         self.assertGreater(result, 4, msg='Błąd')  # atrybut opcjonalny msg pozwala na dodanie komunikatu przy failure testu
#
# if __name__ == "__main__":
#     unittest.main()

class Car:
    def __init__(self, brand: str, color: str, tire_size: int, damaged: bool):
        self.brand = brand
        self.color = color
        self.tire_size = tire_size
        self.damaged = damaged
        self.show_details()

    def change_color(self, new_color):
        self.color = new_color
        print(f'Color of your car is now: {new_color}')

    def change_tire_size(self, new_tire_size):
        self.tire_size = new_tire_size
        print(f'New tire size is applied: {new_tire_size}')

    def repair(self):
        if self.damaged == False:
            return
        else:
            self.damaged = False
            print(f'Your car is now brand new! :)')

    def show_details(self):
        print(f'Your car details: {self.brand}, {self.color}, tire size: {self.tire_size}, damaged = {self.damaged}')



import unittest

class MyCarsTests(unittest.TestCase):

    def setUp(self) -> None:
        self.my_car = Car('BMW', 'black', 21, True)  # tworzymy obiekt klasy Car, ktora w __init__ ma wywolanie metody
        # show details, ktora printuje wartosci atrybutow obiektu
        self.my_friends_car = Car('Porsche', 'yellow', '20', False)

    def tearDown(self) -> None:
        self.my_friends_car.damaged = True
        print(f'My friends car status if damaged: {self.my_friends_car.damaged}')

    def test_if_bmw(self):
        self.assertEqual(self.my_car.brand, 'BMW')

    def test_change_color(self):
        self.my_car.change_color('blue')
        self.assertEqual(self.my_car.color, 'blue')

    def test_repair(self):
        self.my_car.repair()
        self.assertEqual(self.my_car.damaged, False)

    def test_change_tire_size(self):
        self.my_car.change_tire_size(20)
        self.my_friends_car.change_tire_size(19)
        self.assertNotEqual(self.my_car.tire_size, 21)
        self.assertNotEqual(self.my_friends_car.tire_size, 30)


