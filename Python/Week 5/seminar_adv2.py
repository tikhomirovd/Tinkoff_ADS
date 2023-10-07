import typing as tp


def add(x: tp.Union[int, str, float], y: tp.Union[int, str, float]) -> tp.Union[int, str, float]:
    return x + y


add('1', '2')  # Работает, но mypy будет ругаться. Да и PyCharm ругается

print(tp.get_type_hints(add))


def f(x: tp.Union[int, str, float]) -> tp.Union[int, str, float]:
    if isinstance(x, str):
        x.lower()
    return x


def f2(x: int | None = None) -> int | None:
    y = 0
    if x is not None:
        return x + y


a: tuple[int, ...] = (1, 2, 3)

a: tp.Sequence[int] = [1, 2, 3]
a[1] = 0  # нельзя

a: tp.MutableSequence[int] = [1, 2, 3]
a[1] = 0  # можно

a: tp.Mapping[int, str] = {1: '1'}
a[1] = 2  # нельзя

a: tp.MutableSequence[int, str] = {1: '1'}
a[1] = 2  # Можно


def foo() -> tp.NoReturn:
    while True:
        pass


def foo(x) -> int:
    if x < 0:
        return -1
    if x > 0:
        return 1
    if x == 0:
        return 0
    assert False, "Unreachable"


pi: tp.Final[float] = 3.141519 # Константа

pi = 4