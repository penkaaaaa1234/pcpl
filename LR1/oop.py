"""
Решение биквадратного уравнения ax^4 + bx^2 + c = 0
Объектно-ориентированная парадигма (класс)
"""

import sys
import math


class BiquadraticEquation:
    """Класс для решения биквадратного уравнения ax^4 + bx^2 + c = 0."""

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def discriminant(self):
        """Вычисляет дискриминант вспомогательного квадратного уравнения."""
        return self.b ** 2 - 4 * self.a * self.c

    def solve(self):
        """
        Решает уравнение и возвращает список действительных корней x.
        Замена t = x^2: at^2 + bt + c = 0.
        """
        d = self.discriminant()

        if d < 0:
            return []

        if d == 0:
            t_values = [-self.b / (2 * self.a)]
        else:
            sqrt_d = math.sqrt(d)
            t_values = [(-self.b + sqrt_d) / (2 * self.a),
                        (-self.b - sqrt_d) / (2 * self.a)]

        roots = []
        for t in t_values:
            if t > 0:
                roots.extend([math.sqrt(t), -math.sqrt(t)])
            elif t == 0:
                roots.append(0.0)

        return sorted(set(roots))

    def __str__(self):
        return f"({self.a})x^4 + ({self.b})x^2 + ({self.c}) = 0"


class InputHandler:
    """Класс для получения коэффициентов от пользователя."""

    @staticmethod
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

    @staticmethod
    def get_from_args_or_input(args):
        """Получает три коэффициента из аргументов или с клавиатуры."""
        a = InputHandler.get_coefficient("A", args[0] if len(args) > 0 else None)
        b = InputHandler.get_coefficient("B", args[1] if len(args) > 1 else None)
        c = InputHandler.get_coefficient("C", args[2] if len(args) > 2 else None)
        return a, b, c


def main():
    args = sys.argv[1:]

    a, b, c = InputHandler.get_from_args_or_input(args)

    equation = BiquadraticEquation(a, b, c)
    print(f"\nУравнение: {equation}")

    roots = equation.solve()

    if not roots:
        print("Действительных корней нет.")
    else:
        print(f"Корни уравнения: {', '.join(str(round(r, 6)) for r in roots)}")


if __name__ == "__main__":
    main()
