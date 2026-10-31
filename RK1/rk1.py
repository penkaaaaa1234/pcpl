from operator import itemgetter



class OS:
    """
    Операционная система.
    Поля:
    - id      : ID записи об операционной системе
    - name    : Название операционной системы
    - version : Номер версии ОС (количественный признак)
    - comp_id : ID компьютера (для связи один-ко-многим)
    """
    def __init__(self, id, name, version, comp_id):
        self.id = id
        self.name = name
        self.version = version
        self.comp_id = comp_id



    """
    Компьютер.
    Поля:
    - id   : ID записи о компьютере
    - name : Название компьютера
    """
    def __init__(self, id, name):
        self.id = id
        self.name = name



class OSComp:
    """
    Операционная система компьютера.
    Реализует связь многие-ко-многим.
    Поля:
    - comp_id : ID компьютера
    - os_id   : ID операционной системы
    """
    def __init__(self, comp_id, os_id):
        self.comp_id = comp_id
        self.os_id = os_id



computers = [
    Computer(1, 'Acer Aspire 5'),
    Computer(2, 'Dell Latitude 5540'),
    Computer(3, 'HP ProBook 450'),
]


os_list = [
    OS(1, 'Android 14',     14.0,   1),
    OS(2, 'Arch Linux',     2024.0, 2),
    OS(3, 'Windows 11',     11.0,   1),
    OS(4, 'Ubuntu 22.04',   22.04,  3),
    OS(5, 'Astra Linux 1.7', 1.7,   3),
]


os_comps = [
    OSComp(1, 1),   # Acer Aspire 5    — Android 14
    OSComp(2, 2),   # Dell Latitude    — Arch Linux
    OSComp(1, 3),   # Acer Aspire 5    — Windows 11
    OSComp(3, 4),   # HP ProBook 450   — Ubuntu 22.04
    OSComp(3, 5),   # HP ProBook 450   — Astra Linux 1.7
]


def main():

    one_to_many = [
        (os.name, os.version, c.name)
        for c in computers
        for os in os_list
        if os.comp_id == c.id
    ]
    print('Таблица один-ко-многим (название ОС, версия, компьютер):')
    print(one_to_many)


    res_1 = sorted(
        [(os_name, comp_name)
         for os_name, version, comp_name in one_to_many
         if os_name.startswith('A')],
        key=itemgetter(0)
    )
    print('\nЗапрос 1 — ОС с названием на "A" и их компьютеры:')
    print(res_1)

    #
    res_2_unsorted = []
    for c in computers:

        c_os = list(filter(lambda i: i[2] == c.name, one_to_many))
        if len(c_os) > 0:

            c_versions = [version for _, version, _ in c_os]

            c_min_version = min(c_versions)
            res_2_unsorted.append((c.name, c_min_version))

    res_2 = sorted(res_2_unsorted, key=itemgetter(1))
    print('\nЗапрос 2 — Компьютеры с мин. версией ОС (сортировка по версии):')
    print(res_2)


    many_to_many_temp = [
        (c.name, oc.comp_id, oc.os_id)
        for c in computers
        for oc in os_comps
        if oc.comp_id == c.id
    ]

    many_to_many = [
        (os.name, os.version, comp_name)
        for comp_name, comp_id, os_id in many_to_many_temp
        for os in os_list
        if os.id == os_id
    ]

    res_3 = sorted(many_to_many, key=itemgetter(0))
    print('\nЗапрос 3 — Все связанные ОС и компьютеры (мн-ко-мн, сортировка по ОС):')
    print(res_3)


if __name__ == '__main__':
    main()
