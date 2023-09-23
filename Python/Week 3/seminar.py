from functools import cmp_to_key


def task2_1(array):
    """Вход: n последовательностей цифр
    Выход: наибольшее число которое можно составить из этих последовательностей """

    sorted_array = sorted(array, reverse=True)
    return "".join(sorted_array)


array = ['2', '20', '004', '66']
print(task2_1(array))  # ошибка


# Пишем свой компаратор
def cpm(a, b):
    """return 1 if a is greater than b
    return - 1 if b is greater than a
    return 0 if equals"""
    x1 = a + b
    x2 = b + a
    if x1 > x2:
        return 1
    elif x1 < x2:
        return -1
    else:
        return 0


def task2_2(array):
    sorted_array = sorted(array, key=cmp_to_key(cpm), reverse=True)
    return "".join(sorted_array)


array = ['2', '20', '004', '66']
print(task2_2(array))  # ошибка
