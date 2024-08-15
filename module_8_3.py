"""
module_8_3
"""
class Car:
    def __init__(self, model, vin_number, numbers):
        """
        Атрибут объекта model - название автомобиля (строка).
        Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
        """
        self.model = model
        if self.__is_valid_vin(vin_number):
            self.__vin = vin_number
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers

    def __is_valid_vin(self, vin_number):
        """
        принимает vin_number и проверяет его на корректность. Возвращает True, если корректный,
        в других случаях выбрасывает исключение
        Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер',
        если передано не целое число. (тип данных можно проверить функцией isinstance).
        Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера',
        если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
        Возвращает True, если исключения не были выброшены.
        Уровень доступа private.

        :param vin_number:
        :return: True or Raised exception
        """
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_numbers(self, numbers):
        """
        принимает numbers и проверяет его на корректность. Возвращает True, если корректный,
        в других случаях выбрасывает исключение.
        Уровень доступа private.
        Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров',
        если передана не строка. (тип данных можно проверить функцией isinstance).
        Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера',
        переданная строка должна состоять ровно из 6 символов.
        Возвращает True, если исключения не были выброшены.

        :param numbers:
        :return: True or Raised exception
        """
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    first = Car('Model3', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model4', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model5', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')

"""
Model1 успешно создан
Неверный диапазон для vin номера
Неверная длина номера

module_8_3.py
"""