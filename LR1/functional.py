"""
Решение биквадратного уравнения ax^4 + bx^2 + c = 0
Функциональная парадигма (сопоставление с образцом — match/case, Python 3.10+)
"""

import sys
import math


def get_coefficient(name, value=None):
    """Считывает коэффициент из значения или с клавиатуры."""
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


def classify_discriminant(d):
    """Классифицирует дискриминант в виде строки-образца."""
    if d < 0:
        return "negative"
    elif d == 0:
        return "zero"
    else:
        return "positive"


def roots_from_t(t):
    """
    Возвращает действительные корни x из значения t = x^2.
    Использует сопоставление с образцом.
    """
    match t:
        case t if t > 0:
            return [math.sqrt(t), -math.sqrt(t)]
        case 0.0 | 0:
            return [0.0]
        case _:             # t < 0 — корней нет
            return []


def solve_biquadratic(a, b, c):
    """
    Решает ax^4 + bx^2 + c = 0 функциональным стилем.
    Замена t = x^2: at^2 + bt + c = 0.
    """
    d = b * b - 4 * a * c

    # Сопоставление с образцом по знаку дискриминанта
    match classify_discriminant(d):
        case "negative":
            t_values = []
        case "zero":
            t_values = [-b / (2 * a)]
        case "positive":
            sqrt_d = math.sqrt(d)
            t_values = [(-b + sqrt_d) / (2 * a),
                        (-b - sqrt_d) / (2 * a)]

    # Применяем roots_from_t к каждому t и объединяем списки
    all_roots = [x for t in t_values for x in roots_from_t(t)]

    return sorted(set(all_roots))


def format_roots(roots):
    """Форматирует результат с помощью сопоставления с образцом."""
    match roots:
        case []:
            return "Действительных корней нет."
        case [single]:
            return f"Один корень: {round(single, 6)}"
        case _:
            return f"Корни уравнения: {', '.join(str(round(r, 6)) for r in roots)}"


def main():
    args = sys.argv[1:]

    a = get_coefficient("A", args[0] if len(args) > 0 else None)
    b = get_coefficient("B", args[1] if len(args) > 1 else None)
    c = get_coefficient("C", args[2] if len(args) > 2 else None)

    print(f"\nУравнение: ({a})x^4 + ({b})x^2 + ({c}) = 0")

    roots = solve_biquadratic(a, b, c)
    print(format_roots(roots))


if __name__ == "__main__":
    main()
