# Функция для вычисления периметра куба.
def calc_cube_perimeter(side):
    return side * 12

# Функция для вычисления площади куба.
def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area

# Основная функция, которая принимает длину ребра куба
def calc_cube(side):
    # Вызываем функцию, рассчитывающую периметр
    # и передаём в неё размер куба
    one_cube_perimeter = calc_cube_perimeter(side)
    full_length = one_cube_perimeter * 8

    # Вызываем функцию, рассчитывающую площадь стекла
    # и передаём в неё размер куба
    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * 8

    print('Для 8 кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)

# В результате остался лишь один вызов "основной" функции,
# а она уже вызовет две вспомогательные
calc_cube(3)

# --------------------

import datetime as dt

DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_count_friends(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city in UTC_OFFSET:
                what_time(city)
                return f'Там сейчас {dt.datetime.utcnow()}'
            else:
                return f'<не могу определить время в городе {city}>'

        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?'
    ]
    for query in queries:
        print(query, '-', process_query(query))

runner()





#  Как бы база данных
#  name (англ. 'имя') - название мороженого
#  description (англ. 'описание') - описание мороженого

icecream_db = [
    {
    'name': 'Золотое мороженое',
    'description': ('Шарики таитянского ванильного мороженого, шоколад '
                    '"Amedei Porcelana" и груда экзотических фруктов.'
                    'Всё это покрыто золотой фольгой, '
                    'её тоже полагается съесть.'),
    },    
    {
    'name': 'Готическое мороженое',
    'description': ('Чёрное мороженое в чёрном вафельном рожке для '
                    'true black goths. Состав: сливочное мороженое, '
                    'миндаль, активированный уголь, чернота, мрак, '
                    'отрицание.'),
    },
    {
    'name': 'Мороженое паста карбонара',
    'description': ('Порция макарон под тёмным соусом. '
                    'Паста — из ванильного мороженого, '
                    'продавленного через пресс с дырочками, '
                    'соус — ликёр с орехами. Buon appetito!'),
    },
    {
    'name': 'Фруктово-ягодное мороженое ГОСТ 119-52',
    'description': ('Сырьё: сливки, пахта, фрукты и ягоды в свежем виде, '
                    'яичный порошок из куриных яиц, патока карамельная. '
                    'Общее количество микробов в 1 мл мороженого: '
                    'не более 250 тыс.'),
    },
    {
    'name': 'Люминесцентное мороженое',
    'description': ('Сливочное мороженое с белками, '
                    'активированными кальцием. '
                    'Светится, если облизнуть. '
                    'Можно подавать в тыкве на Хэллоуин '
                    'или кормить собаку Баскервилей.'),
    },
    {
    'name': 'Жареное мороженое',
    'description': ('Шарики мороженого обваливают в яйце и в панировке, '
                    'сильно замораживают и быстро обжаривают '
                    'в растительном масле. Едят быстро.'),
    },
]

# информацию из списков получают по индексу, 
# а информацию из словаря — по ключу. 
# Проверим
print(icecream_db[0])
# будет напечатано: 
# {'name': 'Золотое мороженое', 'description': 'Шарики таитянского ... съесть.'}

print(icecream_db[1]['description'])
# будет напечатано: Чёрное мороженое ... мрак, отрицание.