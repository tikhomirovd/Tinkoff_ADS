def next_even(n: int):
    """На вход подаются натуральное число.
    На выходе следующее четное число."""

    return n + (2 - n % 2)


print(next_even(4))


def del_null(array: list):
    """На вход подается массив
    На выход удалить нули из массива


    Можно реализовать ещё эффективнее и быстрее
    используя сортировку вставкой. """
    array.sort(key=lambda x: x == 0)

    while array[-1] == 0 and len(array) > 0:
        array.pop()
    return


print(del_null([1, 2, 3, 0, 0, 5]))
