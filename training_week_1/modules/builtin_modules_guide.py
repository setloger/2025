"""
Наиболее часто используемые встроенные модули Python

Этот файл содержит список популярных встроенных модулей с примерами их использования.
"""

# ============================================================================
# 1. МОДУЛЬ OS - Операционная система
# ============================================================================

import os

def os_examples():
    """Примеры использования модуля os"""
    print("=== МОДУЛЬ OS ===")
    
    # Работа с путями
    current_dir = os.getcwd()  # Текущая директория
    print(f"1. Текущая директория: {current_dir}")
    
    # Создание и удаление директорий
    os.makedirs("test_folder", exist_ok=True)  # Создание директории
    print("2. Создана директория 'test_folder'")
    
    # Проверка существования файла/директории
    exists = os.path.exists("test_folder")
    print(f"3. Директория существует: {exists}")
    
    # Получение списка файлов
    files = os.listdir(".")
    print(f"4. Файлы в текущей директории: {files[:5]}...")  # Первые 5 файлов
    
    # Работа с переменными окружения
    home_dir = os.environ.get('HOME') or os.environ.get('USERPROFILE')
    print(f"5. Домашняя директория: {home_dir}")
    
    # Объединение путей
    full_path = os.path.join("folder", "subfolder", "file.txt")
    print(f"6. Полный путь: {full_path}")
    
    # Получение информации о файле
    if os.path.exists(__file__):
        file_size = os.path.getsize(__file__)
        file_time = os.path.getmtime(__file__)
        print(f"7. Размер файла: {file_size} байт")
        print(f"8. Время изменения: {file_time}")
    
    # Удаление тестовой директории
    os.rmdir("test_folder")
    print("9. Директория 'test_folder' удалена")
    print()


# ============================================================================
# 2. МОДУЛЬ SYS - Системные параметры и функции
# ============================================================================

import sys

def sys_examples():
    """Примеры использования модуля sys"""
    print("=== МОДУЛЬ SYS ===")
    
    # Версия Python
    print(f"1. Версия Python: {sys.version}")
    print(f"2. Версия Python (короткая): {sys.version_info}")
    
    # Аргументы командной строки
    print(f"3. Аргументы командной строки: {sys.argv}")
    
    # Пути поиска модулей
    print(f"4. Количество путей поиска модулей: {len(sys.path)}")
    print(f"5. Первые 3 пути: {sys.path[:3]}")
    
    # Стандартные потоки
    print(f"6. Стандартный ввод: {sys.stdin}")
    print(f"7. Стандартный вывод: {sys.stdout}")
    print(f"8. Стандартная ошибка: {sys.stderr}")
    
    # Информация о платформе
    print(f"9. Платформа: {sys.platform}")
    print(f"10. Имя системы: {sys.platform}")
    
    # Выход из программы
    # sys.exit(0)  # Закомментировано, чтобы не прерывать выполнение
    print("11. Функция sys.exit() для выхода из программы")
    print()


# ============================================================================
# 3. МОДУЛЬ DATETIME - Работа с датами и временем
# ============================================================================

from datetime import datetime, date, timedelta

def datetime_examples():
    """Примеры использования модуля datetime"""
    print("=== МОДУЛЬ DATETIME ===")
    
    # Текущая дата и время
    now = datetime.now()
    print(f"1. Текущая дата и время: {now}")
    print(f"2. Только дата: {now.date()}")
    print(f"3. Только время: {now.time()}")
    
    # Форматирование даты
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print(f"4. Отформатированная дата: {formatted}")
    
    # Создание конкретной даты
    specific_date = datetime(2024, 12, 25, 10, 30, 0)
    print(f"5. Конкретная дата: {specific_date}")
    
    # Работа с временными интервалами
    tomorrow = now + timedelta(days=1)
    print(f"6. Завтра: {tomorrow.date()}")
    
    yesterday = now - timedelta(days=1)
    print(f"7. Вчера: {yesterday.date()}")
    
    # Разность между датами
    diff = specific_date - now
    print(f"8. Дней до Рождества: {diff.days}")
    
    # Парсинг строки в дату
    date_string = "2024-01-15 14:30:00"
    parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    print(f"9. Распарсенная дата: {parsed_date}")
    
    # Текущий timestamp
    timestamp = datetime.now().timestamp()
    print(f"10. Текущий timestamp: {timestamp}")
    print()


# ============================================================================
# 4. МОДУЛЬ JSON - Работа с JSON данными
# ============================================================================

import json

def json_examples():
    """Примеры использования модуля json"""
    print("=== МОДУЛЬ JSON ===")
    
    # Создание JSON из Python объекта
    data = {
        "name": "Иван",
        "age": 25,
        "city": "Москва",
        "hobbies": ["программирование", "чтение", "спорт"],
        "active": True,
        "score": 95.5
    }
    
    # Сериализация в JSON
    json_string = json.dumps(data, ensure_ascii=False, indent=2)
    print("1. JSON строка:")
    print(json_string)
    
    # Десериализация из JSON
    parsed_data = json.loads(json_string)
    print(f"2. Распарсенные данные: {parsed_data}")
    
    # Работа с файлами JSON
    with open("test_data.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print("3. Данные сохранены в файл 'test_data.json'")
    
    # Чтение из файла JSON
    with open("test_data.json", "r", encoding="utf-8") as f:
        loaded_data = json.load(f)
    print(f"4. Данные загружены из файла: {loaded_data['name']}")
    
    # Обработка ошибок JSON
    try:
        invalid_json = json.loads('{"invalid": json}')
    except json.JSONDecodeError as e:
        print(f"5. Ошибка парсинга JSON: {e}")
    
    # Удаление тестового файла
    import os
    os.remove("test_data.json")
    print("6. Тестовый файл удален")
    print()


# ============================================================================
# 5. МОДУЛЬ COLLECTIONS - Специализированные контейнеры
# ============================================================================

from collections import Counter, defaultdict, deque, namedtuple

def collections_examples():
    """Примеры использования модуля collections"""
    print("=== МОДУЛЬ COLLECTIONS ===")
    
    # Counter - подсчет элементов
    words = ["python", "java", "python", "c++", "python", "java"]
    word_count = Counter(words)
    print(f"1. Подсчет слов: {word_count}")
    print(f"2. Самое частое слово: {word_count.most_common(1)}")
    
    # defaultdict - словарь с значением по умолчанию
    dd = defaultdict(list)
    dd["a"].append(1)
    dd["a"].append(2)
    dd["b"].append(3)
    print(f"3. defaultdict: {dict(dd)}")
    
    # deque - двусторонняя очередь
    dq = deque([1, 2, 3, 4, 5])
    dq.appendleft(0)
    dq.append(6)
    print(f"4. deque: {dq}")
    print(f"5. Первый элемент: {dq.popleft()}")
    print(f"6. Последний элемент: {dq.pop()}")
    
    # namedtuple - именованный кортеж
    Person = namedtuple("Person", ["name", "age", "city"])
    person = Person("Анна", 30, "Санкт-Петербург")
    print(f"7. Person: {person}")
    print(f"8. Имя: {person.name}, Возраст: {person.age}")
    
    # ChainMap - объединение словарей
    from collections import ChainMap
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    chain = ChainMap(dict1, dict2)
    print(f"9. ChainMap: {dict(chain)}")
    print()


# ============================================================================
# 6. МОДУЛЬ RE - Регулярные выражения
# ============================================================================

import re

def re_examples():
    """Примеры использования модуля re"""
    print("=== МОДУЛЬ RE ===")
    
    text = "Мой email: user@example.com, телефон: +7-123-456-78-90"
    
    # Поиск email
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_match = re.search(email_pattern, text)
    if email_match:
        print(f"1. Найден email: {email_match.group()}")
    
    # Поиск телефона
    phone_pattern = r'\+7-\d{3}-\d{3}-\d{2}-\d{2}'
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        print(f"2. Найден телефон: {phone_match.group()}")
    
    # Замена текста
    new_text = re.sub(r'@example\.com', '@gmail.com', text)
    print(f"3. Замененный текст: {new_text}")
    
    # Разделение строки
    words = re.split(r'[,\s]+', text)
    print(f"4. Разделенные слова: {words}")
    
    # Поиск всех совпадений
    numbers = re.findall(r'\d+', text)
    print(f"5. Все числа в тексте: {numbers}")
    
    # Проверка соответствия паттерну
    is_valid_email = re.match(email_pattern, "test@example.com")
    print(f"6. Валидный email: {bool(is_valid_email)}")
    
    # Компиляция регулярного выражения
    pattern = re.compile(r'\b\w+\b')
    matches = pattern.findall("Hello World Python")
    print(f"7. Слова: {matches}")
    print()


# ============================================================================
# 7. МОДУЛЬ MATH - Математические функции
# ============================================================================

import math

def math_examples():
    """Примеры использования модуля math"""
    print("=== МОДУЛЬ MATH ===")
    
    # Константы
    print(f"1. Pi: {math.pi}")
    print(f"2. e: {math.e}")
    print(f"3. Tau: {math.tau}")
    
    # Тригонометрические функции
    angle = math.pi / 4  # 45 градусов
    print(f"4. sin(45°): {math.sin(angle):.4f}")
    print(f"5. cos(45°): {math.cos(angle):.4f}")
    print(f"6. tan(45°): {math.tan(angle):.4f}")
    
    # Логарифмы
    print(f"7. ln(10): {math.log(10):.4f}")
    print(f"8. log10(100): {math.log10(100)}")
    print(f"9. log2(8): {math.log2(8)}")
    
    # Степени и корни
    print(f"10. 2^10: {math.pow(2, 10)}")
    print(f"11. √16: {math.sqrt(16)}")
    print(f"12. ∛27: {math.pow(27, 1/3):.4f}")
    
    # Округление
    print(f"13. ceil(3.7): {math.ceil(3.7)}")
    print(f"14. floor(3.7): {math.floor(3.7)}")
    print(f"15. round(3.7): {round(3.7)}")
    
    # Факториал
    print(f"16. 5!: {math.factorial(5)}")
    
    # НОД и НОК
    print(f"17. НОД(48, 18): {math.gcd(48, 18)}")
    
    # Проверка на бесконечность и NaN
    print(f"18. isinf(1/0): {math.isinf(float('inf'))}")
    print(f"19. isnan(float('nan')): {math.isnan(float('nan'))}")
    print()


# ============================================================================
# 8. МОДУЛЬ RANDOM - Генерация случайных чисел
# ============================================================================

import random

def random_examples():
    """Примеры использования модуля random"""
    print("=== МОДУЛЬ RANDOM ===")
    
    # Установка seed для воспроизводимости
    random.seed(42)
    
    # Случайные числа
    print(f"1. Случайное число [0, 1): {random.random()}")
    print(f"2. Случайное число [1, 10]: {random.randint(1, 10)}")
    print(f"3. Случайное число [0, 10): {random.randrange(10)}")
    print(f"4. Случайное число [1.5, 2.5]: {random.uniform(1.5, 2.5):.2f}")
    
    # Работа со списками
    items = ["яблоко", "банан", "апельсин", "груша"]
    print(f"5. Случайный выбор: {random.choice(items)}")
    print(f"6. Несколько случайных выборов: {random.choices(items, k=3)}")
    
    # Перемешивание
    numbers = list(range(1, 11))
    random.shuffle(numbers)
    print(f"7. Перемешанные числа: {numbers}")
    
    # Выборка без повторений
    sample = random.sample(range(1, 51), 6)
    print(f"8. Случайная выборка (лотерея): {sample}")
    
    # Вероятностные распределения
    print(f"9. Нормальное распределение: {random.gauss(0, 1):.3f}")
    print(f"10. Экспоненциальное распределение: {random.expovariate(1):.3f}")
    print()


# ============================================================================
# 9. МОДУЛЬ ITERTOOLS - Итераторы и комбинаторика
# ============================================================================

import itertools

def itertools_examples():
    """Примеры использования модуля itertools"""
    print("=== МОДУЛЬ ITERTOOLS ===")
    
    # Бесконечные итераторы
    counter = itertools.count(1, 2)  # Начиная с 1, шаг 2
    print(f"1. Первые 5 нечетных чисел: {list(itertools.islice(counter, 5))}")
    
    cycle = itertools.cycle(['A', 'B', 'C'])
    print(f"2. Цикл ABC (5 элементов): {list(itertools.islice(cycle, 5))}")
    
    repeat = itertools.repeat(10, 3)
    print(f"3. Повторение 10 три раза: {list(repeat)}")
    
    # Комбинаторика
    letters = ['A', 'B', 'C']
    print(f"4. Перестановки: {list(itertools.permutations(letters, 2))}")
    print(f"5. Комбинации: {list(itertools.combinations(letters, 2))}")
    print(f"6. Комбинации с повторениями: {list(itertools.combinations_with_replacement(letters, 2))}")
    
    # Объединение итераторов
    list1 = [1, 2, 3]
    list2 = ['a', 'b', 'c']
    print(f"7. Цепочка: {list(itertools.chain(list1, list2))}")
    
    # Группировка
    data = [('A', 1), ('A', 2), ('B', 3), ('B', 4)]
    grouped = itertools.groupby(data, key=lambda x: x[0])
    print("8. Группировка:")
    for key, group in grouped:
        print(f"   {key}: {list(group)}")
    
    # Фильтрация
    numbers = range(10)
    filtered = itertools.filterfalse(lambda x: x % 2 == 0, numbers)
    print(f"9. Нечетные числа: {list(filtered)}")
    
    # Накопление
    accumulated = itertools.accumulate([1, 2, 3, 4, 5])
    print(f"10. Накопленная сумма: {list(accumulated)}")
    print()


# ============================================================================
# 10. МОДУЛЬ URLLIB - Работа с URL
# ============================================================================

import urllib.request
import urllib.parse

def urllib_examples():
    """Примеры использования модуля urllib"""
    print("=== МОДУЛЬ URLLIB ===")
    
    # Парсинг URL
    url = "https://example.com/path?param1=value1&param2=value2"
    parsed = urllib.parse.urlparse(url)
    print(f"1. Схема: {parsed.scheme}")
    print(f"2. Домен: {parsed.netloc}")
    print(f"3. Путь: {parsed.path}")
    print(f"4. Параметры: {parsed.query}")
    
    # Кодирование параметров
    params = {"name": "Иван", "age": 25}
    encoded_params = urllib.parse.urlencode(params)
    print(f"5. Закодированные параметры: {encoded_params}")
    
    # Декодирование URL
    encoded_url = "https://example.com/%D0%BF%D1%83%D1%82%D1%8C"
    decoded_url = urllib.parse.unquote(encoded_url)
    print(f"6. Декодированный URL: {decoded_url}")
    
    # Создание URL
    base_url = "https://api.example.com/users"
    params = {"page": 1, "limit": 10}
    full_url = f"{base_url}?{urllib.parse.urlencode(params)}"
    print(f"7. Полный URL: {full_url}")
    
    # Примечание: urllib.request для HTTP запросов
    # (закомментировано, чтобы избежать сетевых запросов)
    print("8. urllib.request для HTTP запросов (не выполняется)")
    print()


# ============================================================================
# ЗАПУСК ВСЕХ ПРИМЕРОВ
# ============================================================================

def run_all_examples():
    """Запускает все примеры использования модулей"""
    print("НАИБОЛЕЕ ЧАСТО ИСПОЛЬЗУЕМЫЕ ВСТРОЕННЫЕ МОДУЛИ PYTHON")
    print("=" * 60)
    print()
    
    os_examples()
    sys_examples()
    datetime_examples()
    json_examples()
    collections_examples()
    re_examples()
    math_examples()
    random_examples()
    itertools_examples()
    urllib_examples()
    
    print("Все примеры завершены!")


if __name__ == "__main__":
    run_all_examples() 