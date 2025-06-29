# Справочник: Наиболее часто используемые встроенные модули Python

## Содержание
1. [os](#os---операционная-система)
2. [sys](#sys---системные-параметры)
3. [datetime](#datetime---даты-и-время)
4. [json](#json---работа-с-json)
5. [collections](#collections---специализированные-контейнеры)
6. [re](#re---регулярные-выражения)
7. [math](#math---математические-функции)
8. [random](#random---случайные-числа)
9. [itertools](#itertools---итераторы)
10. [urllib](#urllib---работа-с-url)

---

## os - Операционная система

**Назначение**: Работа с операционной системой, файловой системой, путями.

### Основные функции:

```python
import os

# Работа с путями
os.getcwd()                    # Текущая директория
os.chdir(path)                 # Смена директории
os.path.join(path1, path2)     # Объединение путей
os.path.exists(path)           # Проверка существования
os.path.isfile(path)           # Проверка файла
os.path.isdir(path)            # Проверка директории

# Работа с файлами и директориями
os.listdir(path)               # Список файлов
os.makedirs(path)              # Создание директорий
os.remove(path)                # Удаление файла
os.rmdir(path)                 # Удаление директории
os.rename(old, new)            # Переименование

# Информация о файлах
os.path.getsize(path)          # Размер файла
os.path.getmtime(path)         # Время изменения
os.path.abspath(path)          # Абсолютный путь

# Переменные окружения
os.environ                     # Словарь переменных окружения
os.environ.get('VAR')          # Получение переменной
os.putenv('VAR', 'value')      # Установка переменной
```

---

## sys - Системные параметры

**Назначение**: Доступ к системным параметрам и функциям интерпретатора.

### Основные функции:

```python
import sys

# Информация о системе
sys.version                    # Версия Python
sys.version_info              # Кортеж с версией
sys.platform                  # Платформа
sys.executable                # Путь к интерпретатору

# Аргументы командной строки
sys.argv                      # Список аргументов
sys.argv[0]                   # Имя скрипта

# Пути поиска модулей
sys.path                      # Список путей поиска
sys.path.append(path)         # Добавление пути

# Стандартные потоки
sys.stdin                     # Стандартный ввод
sys.stdout                    # Стандартный вывод
sys.stderr                    # Стандартная ошибка

# Выход из программы
sys.exit(code)                # Выход с кодом
sys.exit()                    # Выход с кодом 0
```

---

## datetime - Даты и время

**Назначение**: Работа с датами, временем и временными интервалами.

### Основные классы:

```python
from datetime import datetime, date, timedelta

# Текущее время
now = datetime.now()
today = date.today()

# Создание объектов
dt = datetime(2024, 12, 25, 10, 30, 0)
d = date(2024, 12, 25)

# Форматирование
dt.strftime("%Y-%m-%d %H:%M:%S")  # В строку
datetime.strptime("2024-12-25", "%Y-%m-%d")  # Из строки

# Временные интервалы
delta = timedelta(days=7, hours=3)
tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)

# Разность дат
diff = dt1 - dt2
diff.days                      # Количество дней
diff.seconds                   # Количество секунд

# Timestamp
timestamp = dt.timestamp()     # В timestamp
dt.fromtimestamp(timestamp)    # Из timestamp
```

---

## json - Работа с JSON

**Назначение**: Сериализация и десериализация JSON данных.

### Основные функции:

```python
import json

# Сериализация
json.dumps(obj)               # В строку
json.dump(obj, file)          # В файл

# Десериализация
json.loads(string)            # Из строки
json.load(file)               # Из файла

# Параметры
json.dumps(obj, indent=2)     # С отступами
json.dumps(obj, ensure_ascii=False)  # Поддержка Unicode
json.dumps(obj, sort_keys=True)      # Сортировка ключей

# Обработка ошибок
try:
    data = json.loads(string)
except json.JSONDecodeError as e:
    print(f"Ошибка: {e}")
```

---

## collections - Специализированные контейнеры

**Назначение**: Альтернативные реализации встроенных типов данных.

### Основные классы:

```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter - подсчет элементов
counter = Counter(['a', 'b', 'a', 'c'])
counter['a']                   # Количество 'a'
counter.most_common(3)         # Топ-3 элемента

# defaultdict - словарь с значением по умолчанию
dd = defaultdict(list)
dd['key'].append(1)           # Не нужно проверять существование

# deque - двусторонняя очередь
dq = deque([1, 2, 3])
dq.appendleft(0)              # Добавить слева
dq.popleft()                  # Удалить слева
dq.rotate(1)                  # Сдвиг

# namedtuple - именованный кортеж
Person = namedtuple('Person', ['name', 'age'])
person = Person('Иван', 25)
person.name                   # Доступ по имени
```

---

## re - Регулярные выражения

**Назначение**: Работа с регулярными выражениями для поиска и замены текста.

### Основные функции:

```python
import re

# Поиск
re.search(pattern, string)    # Первое совпадение
re.match(pattern, string)     # Совпадение в начале
re.findall(pattern, string)   # Все совпадения
re.finditer(pattern, string)  # Итератор совпадений

# Замена
re.sub(pattern, repl, string) # Замена всех совпадений
re.subn(pattern, repl, string) # Замена с подсчетом

# Разделение
re.split(pattern, string)     # Разделение по паттерну

# Компиляция
pattern = re.compile(r'\d+')
pattern.search(string)        # Использование скомпилированного паттерна

# Флаги
re.IGNORECASE                 # Игнорировать регистр
re.MULTILINE                  # Многострочный режим
re.DOTALL                     # Точка включает перенос строки
```

---

## math - Математические функции

**Назначение**: Математические функции и константы.

### Основные функции:

```python
import math

# Константы
math.pi                       # π
math.e                        # e
math.tau                      # 2π
math.inf                      # Бесконечность
math.nan                      # NaN

# Тригонометрия
math.sin(x), math.cos(x), math.tan(x)
math.asin(x), math.acos(x), math.atan(x)
math.degrees(x)               # Радианы в градусы
math.radians(x)               # Градусы в радианы

# Логарифмы
math.log(x)                   # Натуральный логарифм
math.log10(x)                 # Логарифм по основанию 10
math.log2(x)                  # Логарифм по основанию 2

# Степени и корни
math.pow(x, y)                # x^y
math.sqrt(x)                  # √x
math.exp(x)                   # e^x

# Округление
math.ceil(x)                  # Вверх
math.floor(x)                 # Вниз
math.trunc(x)                 # К нулю

# Другие функции
math.factorial(n)             # n!
math.gcd(a, b)                # НОД
math.lcm(a, b)                # НОК (Python 3.9+)
```

---

## random - Случайные числа

**Назначение**: Генерация случайных чисел и выборка.

### Основные функции:

```python
import random

# Случайные числа
random.random()               # [0.0, 1.0)
random.uniform(a, b)          # [a, b]
random.randint(a, b)          # [a, b] (целые)
random.randrange(stop)        # [0, stop)
random.randrange(start, stop, step)

# Выборка
random.choice(seq)            # Один элемент
random.choices(seq, k=n)      # n элементов с повторениями
random.sample(seq, k=n)       # n элементов без повторений

# Перемешивание
random.shuffle(seq)           # Перемешать на месте
random.sample(seq, len(seq))  # Перемешать с копированием

# Установка seed
random.seed(x)                # Для воспроизводимости

# Распределения
random.gauss(mu, sigma)       # Нормальное распределение
random.expovariate(lambd)     # Экспоненциальное
random.triangular(low, high, mode)  # Треугольное
```

---

## itertools - Итераторы

**Назначение**: Функции для создания итераторов.

### Основные функции:

```python
import itertools

# Бесконечные итераторы
itertools.count(start, step)  # Счетчик
itertools.cycle(iterable)     # Циклический
itertools.repeat(elem, n)     # Повторение

# Комбинаторика
itertools.permutations(iterable, r)      # Перестановки
itertools.combinations(iterable, r)      # Комбинации
itertools.combinations_with_replacement(iterable, r)  # С повторениями

# Объединение
itertools.chain(*iterables)   # Цепочка итераторов
itertools.chain.from_iterable(iterables)

# Группировка
itertools.groupby(iterable, key)  # Группировка по ключу

# Фильтрация
itertools.filterfalse(pred, iterable)  # Элементы, где pred=False
itertools.dropwhile(pred, iterable)     # Пропустить пока pred=True
itertools.takewhile(pred, iterable)     # Взять пока pred=True

# Накопление
itertools.accumulate(iterable, func)    # Накопление значений
```

---

## urllib - Работа с URL

**Назначение**: Работа с URL и HTTP запросами.

### Основные функции:

```python
import urllib.request
import urllib.parse

# Парсинг URL
urllib.parse.urlparse(url)    # Разбор URL
urllib.parse.urlunparse(parts)  # Сборка URL

# Кодирование/декодирование
urllib.parse.quote(string)    # Кодирование
urllib.parse.unquote(string)  # Декодирование
urllib.parse.urlencode(dict)  # Кодирование параметров

# HTTP запросы
urllib.request.urlopen(url)   # Открыть URL
urllib.request.Request(url)   # Создать запрос

# Пример HTTP запроса
with urllib.request.urlopen('https://api.example.com/data') as response:
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
```

---

## Дополнительные полезные модули

### logging - Логирование
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Сообщение")
logging.error("Ошибка")
```

### pathlib - Современная работа с путями
```python
from pathlib import Path
path = Path("folder/file.txt")
path.exists()
path.read_text()
path.write_text("content")
```

### argparse - Парсинг аргументов командной строки
```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--name", default="World")
args = parser.parse_args()
```

### configparser - Работа с конфигурационными файлами
```python
import configparser
config = configparser.ConfigParser()
config.read('config.ini')
value = config['section']['key']
```

---

## Заключение

Эти модули покрывают большинство повседневных задач в Python. Рекомендуется:

1. **Изучить основы** каждого модуля
2. **Практиковаться** с реальными примерами
3. **Использовать документацию** для детального изучения
4. **Комбинировать модули** для решения сложных задач

Помните: встроенные модули Python - это мощные инструменты, которые могут значительно упростить вашу работу! 