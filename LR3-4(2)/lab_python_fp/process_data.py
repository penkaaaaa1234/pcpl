import json
import sys

from print_result import print_result
from cm_timer import cm_timer_1
from unique import Unique
from gen_random import gen_random

# Путь к файлу передаётся как аргумент командной строки
path = sys.argv[1] if len(sys.argv) > 1 else 'data_light.json'

with open(path, encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(arg):
    # Отсортированный список профессий без повторений (игнорируем регистр при сравнении)
    return list(Unique(sorted(field(arg, 'job-name'), key=str.lower), ignore_case=True))


@print_result
def f2(arg):
    # Только те профессии, которые начинаются со слова "программист"
    return list(filter(lambda x: x.lower().startswith('программист'), arg))


@print_result
def f3(arg):
    # Добавляем "с опытом Python" к каждой специальности
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    # Генерируем зарплаты и присоединяем к названию специальности
    salaries = gen_random(len(arg), 100_000, 200_000)
    return [f'{job}, зарплата {salary} руб.' for job, salary in zip(arg, salaries)]


def field(items, *args):
    """Генератор значений ключей из списка словарей (переиспользуем логику из field.py)"""
    assert len(args) > 0
    if len(args) == 1:
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value
    else:
        for item in items:
            result = {key: item[key] for key in args if item.get(key) is not None}
            if result:
                yield result


if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
