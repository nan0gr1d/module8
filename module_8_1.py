"""
module_8_1
"""
def add_everything_up(a, b):
    """
    принимает a и b, которые могут быть как числами(int, float), так и строками(str).
    TypeError - когда a и b окажутся разными типами (числом и строкой), то возвращать строковое представление этих
    двух данных вместе (в том же порядке). Во всех остальных случаях выполнять стандартные действия.

    :param a: int, float, str
    :param b: int, float, str
    :return: summa, a + b
    """
    try:
        result = a + b
    except TypeError as exc:      # exc указан для общности, для будущего использования
        result = str(a) + str(b)
    except Exception as exc:
        result = f"Exception raised: {exc} - {exc.args}"  # просто для примера
    return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
