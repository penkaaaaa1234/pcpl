# Пример:
# goods = [
#   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
#   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
# ]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        # Один ключ — выдаём только значение, пропускаем None
        key = args[0]
        for item in items:
            value = item.get(key)
            if value is not None:
                yield value
    else:
        # Несколько ключей — выдаём словарь без None-значений
        for item in items:
            result = {key: item[key] for key in args if item.get(key) is not None}
            if result:  # пропускаем если все значения были None
                yield result


if __name__ == '__main__':
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': 500, 'color': 'red'},
    ]

    print("=== field(goods, 'title') ===")
    for val in field(goods, 'title'):
        print(val)

    print("\n=== field(goods, 'title', 'price') ===")
    for val in field(goods, 'title', 'price'):
        print(val)
