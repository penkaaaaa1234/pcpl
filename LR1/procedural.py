"""
Решение биквадратного уравнения ax^4 + bx^2 + c = 0
Процедурная парадигма (функции)
"""

import sys
import math


def get_coefficient(name, value=None):
    """Считывает коэффициент из значения или с клавиатуры, пока не получит число."""
    if value is not None:
        try:
            return float(value)
        except ValueError:
            print(f"Некорректное значение параметра {name}, введите вручную.")

    while True:
        raw = input(f"Введите коэффициент {name}: ")
        try:
            return float(raw)
        except ValueError:
            print("Ошибка: введите действительное число.")


def solve_biquadratic(a, b, c):
    """
    Решает биквадратное уравнение ax^4 + bx^2 + c = 0.
    Замена t = x^2, затем решается at^2 + bt + c = 0.
    Возвращает список действительных корней x.
    """
    discriminant = b * b - 4 * a * c

    if discriminant < 0:
        return []                   # нет действительных корней

    roots_x = []

    t_values = []
    if discriminant == 0:
        t_values = [-b / (2 * a)]
    else:
        sqrt_d = math.sqrt(discriminant)
        t_values = [(-b + sqrt_d) / (2 * a),
                    (-b - sqrt_d) / (2 * a)]

    for t in t_values:
        if t > 0:
            roots_x.extend([math.sqrt(t), -math.sqrt(t)])
        elif t == 0:
            roots_x.append(0.0)
        # t < 0 — корней нет

    return sorted(set(roots_x))


def print_results(roots):
    """Выводит корни уравнения."""
    if not roots:
        print("Действительных корней нет.")
    else:
        print(f"Корни уравнения: {', '.join(str(round(r, 6)) for r in roots)}")


def main():
    # Разбор параметров командной строки: python procedural.py A B C
    args = sys.argv[1:]

    a = get_coefficient("A", args[0] if len(args) > 0 else None)
    b = get_coefficient("B", args[1] if len(args) > 1 else None)
    c = get_coefficient("C", args[2] if len(args) > 2 else None)

    print(f"\nУравнение: ({a})x^4 + ({b})x^2 + ({c}) = 0")

    roots = solve_biquadratic(a, b, c)
    print_results(roots)


if __name__ == "__main__":
    main()
