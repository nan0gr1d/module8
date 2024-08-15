"""
module_8_2
"""
def personal_sum(numbers):
    """
    Должна принимать коллекцию numbers.
    Подсчитывать сумму чисел в numbers путём перебора и увеличивать переменную result.
    Если же при переборе встречается данное типа отличного от числового,
    то обработать исключение TypeError, увеличив счётчик incorrect_data на 1.
    В конечном итоге функция возвращает кортеж из двух значений:
    result - сумма чисел,
    incorrect_data - кол-во некорректных данных.
    :param numbers: collection
    :return: (result, incorrect_data)
    """
    result = 0
    incorrect_data = 0
    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
            print(f"Некорректный тип данных для подсчёта суммы - {item}")

    return result, incorrect_data

def calculate_average(numbers):
    """
    Среднее арифметическое - сумма всех данных делённая на их количество.
    Должна принимать коллекцию numbers и возвращать: среднее арифметическое всех чисел.
    Внутри для подсчёта суммы используйте функцию personal_sum написанную ранее.
    Т.к. коллекция numbers может оказаться пустой, то обработайте исключение ZeroDivisionError
    при делении на 0 и верните 0.
    Также в numbers может быть записана не коллекция, а другие типы данных, например числа.
    Обработайте исключение TypeError выводя строку 'В numbers записан некорректный тип данных'.
    В таком случае функция просто вернёт None.

    :param numbers:
    :return: average of numbers
    """
    if isinstance(numbers, list) or isinstance(numbers, tuple) or isinstance(numbers, str):
        n_items = len(numbers)
        summa, errors = personal_sum(numbers)
        try:
            return summa / (n_items - errors)
        except ZeroDivisionError:
            return 0
    else:
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

"""
eof-module_8_2
"""