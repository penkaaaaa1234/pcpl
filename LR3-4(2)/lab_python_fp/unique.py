# Итератор для удаления дубликатов
from gen_random import gen_random


class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.iterator = iter(items)
        self.seen = set()

    def __next__(self):
        while True:
            value = next(self.iterator)  # бросит StopIteration когда данные закончатся
            # Ключ для проверки дубликатов
            key = value.lower() if self.ignore_case and isinstance(value, str) else value
            if key not in self.seen:
                self.seen.add(key)
                return value  # возвращаем оригинальное значение (без модификации)

    def __iter__(self):
        return self


if __name__ == '__main__':
    print("=== Unique([1,1,1,2,2,2]) ===")
    data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    print(list(Unique(data)))

    print("\n=== Unique(gen_random(10, 1, 3)) ===")
    data = gen_random(10, 1, 3)
    print(list(Unique(data)))

    print("\n=== Unique(['a','A','b','B','a','A','b','B']) ===")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data)))

    print("\n=== Unique(['a','A','b','B'], ignore_case=True) ===")
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    print(list(Unique(data, ignore_case=True)))
