# Конструкция match/case с кортежами и списками

Конструкция `match/case` в Python 3.10+ особенно эффективна при работе с последовательностями — кортежами (tuples) и списками (lists). Эта функциональность называется **сопоставлением последовательностей** (sequence pattern matching) и позволяет элегантно обрабатывать данные различной структуры.

## Основы работы с последовательностями

### Принцип работы

`match/case` может сопоставлять любые последовательности, которые являются экземплярами `collections.abc.Sequence`, включая списки и кортежи[^1][^2]. При этом **все формы записи эквивалентны**:

```python
# Эти формы записи одинаковы:
case [action, obj]:      # список
case (action, obj):      # кортеж
case action, obj:        # без скобок

# Все они сопоставляют любую последовательность из двух элементов
```


## Работа с кортежами

### Базовое сопоставление кортежей

Кортежи отлично подходят для представления координат, точек и других структурированных данных:

```python
def analyze_point(point):
    match point:
        case (0, 0):
            return "Точка в начале координат"
        case (0, y):
            return f"Точка на оси Y в позиции y={y}"
        case (x, 0):
            return f"Точка на оси X в позиции x={x}"
        case (x, y) if x == y:
            return f"Точка на диагонали x=y={x}"
        case (x, y):
            return f"Точка с координатами ({x}, {y})"
        case _:
            return "Не является валидной точкой"

# Примеры использования
print(analyze_point((0, 0)))      # Точка в начале координат
print(analyze_point((0, 5)))      # Точка на оси Y в позиции y=5
print(analyze_point((3, 0)))      # Точка на оси X в позиции x=3
print(analyze_point((4, 4)))      # Точка на диагонали x=y=4
print(analyze_point((2, 7)))      # Точка с координатами (2, 7)
```


### Работа с кортежами разной длины

```python
def process_data(data):
    match data:
        case ():
            return "Пустой кортеж"
        case (value,):  # Важно: запятая для кортежа из одного элемента
            return f"Одно значение: {value}"
        case (x, y):
            return f"Пара значений: {x}, {y}"
        case (x, y, z):
            return f"Три значения: {x}, {y}, {z}"
        case (first, *middle, last):
            return f"Много значений: начало={first}, конец={last}, всего={len(middle)+2}"
        case _:
            return "Неопознанная структура"

# Тестирование
print(process_data(()))                    # Пустой кортеж
print(process_data((42,)))                 # Одно значение: 42
print(process_data((1, 2)))                # Пара значений: 1, 2
print(process_data((1, 2, 3)))             # Три значения: 1, 2, 3
print(process_data((1, 2, 3, 4, 5)))       # Много значений: начало=1, конец=5, всего=5
```


### Практический пример: обработка команд

```python
def process_command(cmd):
    match cmd:
        case ("move", direction, distance):
            return f"Двигаемся {direction} на {distance} единиц"
        case ("rotate", angle):
            return f"Поворачиваем на {angle} градусов"
        case ("stop",):
            return "Останавливаемся"
        case ("info", "position"):
            return "Запрос текущей позиции"
        case ("info", "status"):
            return "Запрос статуса системы"
        case _:
            return "Неизвестная команда"

# Примеры
commands = [
    ("move", "forward", 10),
    ("rotate", 90),
    ("stop",),
    ("info", "position"),
    ("unknown", "command")
]

for cmd in commands:
    print(f"{cmd} -> {process_command(cmd)}")
```


## Работа со списками

### Базовое сопоставление списков

Списки используются для данных переменной длины, и `match/case` отлично подходит для их анализа[^3]:

```python
def describe_list(items):
    match items:
        case []:
            return "Пустой список"
        case [x]:
            return f"Список с одним элементом: {x}"
        case [x, y]:
            return f"Список с двумя элементами: {x} и {y}"
        case [x, y, z]:
            return f"Список с тремя элементами: {x}, {y}, {z}"
        case [first, *rest]:
            return f"Список из {len(rest)+1} элементов, начинается с {first}"
        case _:
            return "Не является списком"

# Примеры
lists = [
    [],
    [^42],
    ["apple", "banana"],
    [1, 2, 3],
    [1, 2, 3, 4, 5, 6]
]

for lst in lists:
    print(f"{lst} -> {describe_list(lst)}")
```


### Продвинутые паттерны со списками

```python
def analyze_data(data):
    match data:
        case []:
            return "Нет данных"
        case [single] if isinstance(single, str):
            return f"Одна строка: '{single}'"
        case [single] if isinstance(single, (int, float)):
            return f"Одно число: {single}"
        case [*numbers] if all(isinstance(x, (int, float)) for x in numbers):
            return f"Числовой массив: сумма = {sum(numbers)}, среднее = {sum(numbers)/len(numbers):.2f}"
        case [first, *middle, last] if len(middle) > 0:
            return f"Последовательность: '{first}' ... '{last}' (всего {len(middle)+2} элементов)"
        case [head, tail]:
            return f"Пара: голова='{head}', хвост='{tail}'"
        case _:
            return "Неизвестный формат данных"

# Тестирование
test_data = [
    [],
    ["hello"],
    [^42],
    [1, 2, 3, 4, 5],
    ["start", "middle1", "middle2", "end"],
    ["first", "second"],
    [1, "mixed", 3.14]
]

for data in test_data:
    print(f"{data} -> {analyze_data(data)}")
```


### Извлечение элементов из списков

```python
def extract_elements(data):
    match data:
        case [first, *_]:  # Берем только первый элемент
            return f"Первый элемент: {first}"
        case [_, second, *_]:  # Берем только второй элемент
            return f"Второй элемент: {second}"
        case [*_, last]:  # Берем только последний элемент
            return f"Последний элемент: {last}"
        case []:
            return "Список пуст"

# Более сложный пример
def parse_csv_row(row):
    match row:
        case [name, age, city] if age.isdigit():
            return {"name": name, "age": int(age), "city": city}
        case [name, age, city, country] if age.isdigit():
            return {"name": name, "age": int(age), "city": city, "country": country}
        case [name, *contact_info]:
            return {"name": name, "contacts": contact_info}
        case _:
            return {"error": "Неверный формат строки"}

# Тестирование
csv_data = [
    ["Анна", "25", "Москва"],
    ["Петр", "30", "СПб", "Россия"],
    ["Мария", "контакт1", "контакт2", "контакт3"],
    ["invalid"]
]

for row in csv_data:
    print(f"{row} -> {parse_csv_row(row)}")
```


## Различение типов последовательностей

Хотя паттерны `[...]` и `(...)` работают одинаково, можно явно проверять типы[^4]:

```python
def check_sequence_type(seq):
    match seq:
        case list(items):
            return f"Это список с элементами: {items}"
        case tuple(items):
            return f"Это кортеж с элементами: {items}"
        case set(items):
            return f"Это множество с элементами: {items}"
        case str(text):
            return f"Это строка: '{text}'"
        case _:
            return "Неизвестный тип последовательности"

# Примеры
sequences = [
    [1, 2, 3],
    (4, 5, 6),
    {7, 8, 9},
    "hello",
    range(3)
]

for seq in sequences:
    print(f"{seq} ({type(seq).__name__}) -> {check_sequence_type(seq)}")
```


## Комбинированные паттерны

### Вложенные структуры

```python
def analyze_nested_data(data):
    match data:
        case []:
            return "Пустой список"
        case [[x, y], [a, b]]:
            return f"Список из двух пар: ({x},{y}) и ({a},{b})"
        case [(name, age), *rest] if isinstance(age, int):
            return f"Первая запись: {name} ({age} лет), остальных записей: {len(rest)}"
        case [first, *middle, last] if isinstance(first, (list, tuple)):
            return f"Список структур: начало={first}, конец={last}, всего={len(middle)+2}"
        case _:
            return "Сложная структура данных"

# Тестирование
nested_data = [
    [],
    [[1, 2], [3, 4]],
    [("Анна", 25), ("Петр", 30), ("Мария", 28)],
    [(1, 2), (3, 4), (5, 6), (7, 8)]
]

for data in nested_data:
    print(f"{data} -> {analyze_nested_data(data)}")
```


### Паттерны с условиями (guards)

```python
def validate_coordinates(coords):
    match coords:
        case (x, y) if x >= 0 and y >= 0:
            return f"Первый квадрант: ({x}, {y})"
        case (x, y) if x < 0 and y >= 0:
            return f"Второй квадрант: ({x}, {y})"
        case (x, y) if x < 0 and y < 0:
            return f"Третий квадрант: ({x}, {y})"
        case (x, y) if x >= 0 and y < 0:
            return f"Четвертый квадрант: ({x}, {y})"
        case (x, y, z) if all(isinstance(i, (int, float)) for i in [x, y, z]):
            return f"3D координаты: ({x}, {y}, {z})"
        case _:
            return "Неверный формат координат"

# Примеры
coordinates = [
    (3, 4),      # первый квадрант
    (-2, 5),     # второй квадрант
    (-1, -3),    # третий квадрант
    (2, -1),     # четвертый квадрант
    (1, 2, 3),   # 3D
    "invalid"
]

for coord in coordinates:
    print(f"{coord} -> {validate_coordinates(coord)}")
```


## Практический пример: парсер конфигурации

```python
def parse_config_entry(entry):
    """
    Парсит записи конфигурации различных форматов:
    - ["key", "value"]
    - ["section", "key", "value"]  
    - ["key", "value", "comment"]
    - ["section", "key", "value", "comment"]
    """
    match entry:
        case []:
            return {"error": "Пустая запись"}
        case [key, value] if isinstance(key, str) and isinstance(value, str):
            return {"key": key, "value": value, "section": "default"}
        case [section, key, value] if all(isinstance(x, str) for x in [section, key, value]):
            return {"key": key, "value": value, "section": section}
        case [key, value, comment] if all(isinstance(x, str) for x in [key, value, comment]):
            return {"key": key, "value": value, "section": "default", "comment": comment}
        case [section, key, value, comment] if all(isinstance(x, str) for x in [section, key, value, comment]):
            return {"key": key, "value": value, "section": section, "comment": comment}
        case [key, *values] if len(values) > 0:
            return {"key": key, "values": values, "type": "multi-value"}
        case _:
            return {"error": f"Неверный формат записи: {entry}"}

# Тестовые данные
config_entries = [
    ["debug", "true"],
    ["database", "host", "localhost"],
    ["port", "8080", "server port"],
    ["logging", "level", "INFO", "log level setting"],
    ["servers", "web1", "web2", "web3"],
    [],
    [123, "invalid"],
    ["single"]
]

print("=== Парсинг конфигурации ===")
for entry in config_entries:
    result = parse_config_entry(entry)
    print(f"{entry} -> {result}")
```


## Ключевые особенности и советы

### Важные моменты

**Универсальность паттернов**: Паттерны `[a, b]`, `(a, b)` и `a, b` **идентичны** и сопоставляют любую последовательность из двух элементов[^1].

**Захват остальных элементов**: Используйте `*rest` для захвата произвольного количества элементов[^2]:

```python
case [first, *middle, last]:  # первый, последний + все средние
case [head, *tail]:           # первый + все остальные
case [*init, last]:           # все кроме последнего + последний
```

**Ограничения**: В одном паттерне может быть максимум один оператор `*`[^2].

### Преимущества использования

- **Читаемость**: код становится более декларативным
- **Безопасность**: автоматическая проверка структуры данных
- **Гибкость**: легко добавлять новые случаи
- **Производительность**: часто быстрее множественных `if/elif`

Конструкция `match/case` с кортежами и списками предоставляет мощный и элегантный способ работы с последовательностями, делая код более выразительным и менее подверженным ошибкам.

<div style="text-align: center">⁂</div>

[^1]: https://peps.python.org/pep-0636/

[^2]: https://buddy.works/tutorials/structural-pattern-matching-In-python

[^3]: https://betterstack.com/community/guides/scaling-python/python-pattern-matching/

[^4]: https://pc-python.readthedocs.io/en/latest/python_advanced/match_case.html

[^5]: https://www.semanticscholar.org/paper/b0b5c2f479466f9152c9d35c9382038ce747ee59

[^6]: https://iopscience.iop.org/article/10.1088/1361-6420/ad22e8

[^7]: https://onepetro.org/SPEHFTC/proceedings/25HFTC/25HFTC/D021S003R003/633710

[^8]: https://ieeexplore.ieee.org/document/10408399/

[^9]: https://dl.acm.org/doi/10.1145/3448016.3452818

[^10]: https://www.semanticscholar.org/paper/a064f697e71b0660d868f932ae97936d9bbcf08d

[^11]: https://www.ijrte.org/portfolio-item/B3024078219/

[^12]: https://www.econometricsociety.org/doi/10.3982/QE2475

[^13]: https://benhoyt.com/writings/python-pattern-matching/

[^14]: https://stackoverflow.com/questions/70077422/why-python-matches-a-list-as-a-tuple

[^15]: https://habr.com/ru/articles/585216/

[^16]: https://www.datamentor.io/python/match-case

[^17]: https://guicommits.com/python-match-case-examples/

[^18]: https://www.geeksforgeeks.org/python/python-match-case-statement/

[^19]: https://stackoverflow.com/questions/75062113/how-to-check-if-list-includes-an-element-using-match-case

[^20]: https://peps.python.org/pep-0622/

[^21]: https://www.reddit.com/r/learnpython/comments/sq1xdm/python_310_matching_against_lists/

[^22]: https://proproprogs.ru/python_base/python3-konstrukciya-matchcase-s-kortezhami-i-spiskami

[^23]: https://highload.tech/prymery-match-case-v-python-3-10-s-obyasnenyem/

[^24]: https://habr.com/ru/companies/yandex_praktikum/articles/547902/

[^25]: https://ijarsct.co.in/Paper24928.pdf

[^26]: https://journals.sagepub.com/doi/full/10.3233/JIFS-231039

[^27]: https://joss.theoj.org/papers/10.21105/joss.00670.pdf

[^28]: http://arxiv.org/pdf/1403.2769.pdf

[^29]: http://arxiv.org/pdf/2403.01631.pdf

[^30]: https://arxiv.org/html/2312.11873v1

[^31]: https://arxiv.org/pdf/2206.01503.pdf

[^32]: https://arxiv.org/pdf/1710.06915v1.pdf

[^33]: https://arxiv.org/pdf/2106.10821.pdf

[^34]: http://conference.scipy.org/proceedings/scipy2017/pdfs/manuel_krebber.pdf

[^35]: https://arxiv.org/pdf/2401.07576.pdf

[^36]: http://arxiv.org/pdf/2206.04157.pdf

[^37]: https://docs-python.ru/tutorial/tsikly-upravlenie-vetvleniem-python/konstruktsija-match-case/

[^38]: https://proproprogs.ru/python_base/python3-konstrukciya-matchcase-so-slovaryami-i-mnozhestvami

[^39]: https://stackoverflow.com/questions/73594044/structural-pattern-matching-python-match-at-any-position-in-sequence

[^40]: https://realpython.com/structural-pattern-matching/

