from math import sqrt

message = (f'Добро пожаловать в самую лучшую программу для вычисления '
           f'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Проверяет что число больше нуля."""
    if your_number <= 0:
        return

    root = 0
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f'Это будет : {calculate_square_root(your_number)}')


calc(25.5)
