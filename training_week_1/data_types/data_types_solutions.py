"""
Решения упражнений: Типы данных в Python

Этот файл содержит решения всех упражнений для проверки.
"""

import math

# ============================================================================
# РЕШЕНИЕ УПРАЖНЕНИЯ 1: Работа с числами
# ============================================================================

def solution_1_numbers():
    """Решение: Работа с числами"""
    print("=== Решение 1: Работа с числами ===")
    
    a = 10
    b = 3
    
    print(f"a = {a}, b = {b}")
    print(f"1. Сумма: {a + b}")
    print(f"2. Разность: {a - b}")
    print(f"3. Произведение: {a * b}")
    print(f"4. Частное: {a / b}")
    print(f"5. Остаток от деления: {a % b}")
    print(f"6. Целочисленное деление: {a // b}")
    print()


# ============================================================================
# РЕШЕНИЕ УПРАЖНЕНИЯ 2: Работа со строками
# ============================================================================

def solution_2_strings():
    """Решение: Работа со строками"""
    print("=== Решение 2: Работа со строками ===")
    
    text = "Hello World Python"
    
    print(f"Исходная строка: '{text}'")
    print(f"1. Количество символов: {len(text)}")
    print(f"2. Количество слов: {len(text.split())}")
    print(f"3. Верхний регистр: '{text.upper()}'")
    print(f"4. Нижний регистр: '{text.lower()}'")
    print(f"5. Замена пробелов: '{text.replace(' ', '_')}'")
    print(f"6. Начинается с 'H': {text.startswith('H')}")
    print(f"7. Заканчивается на 'n': {text.endswith('n')}")
    print()


# ============================================================================
# РЕШЕНИЕ УПРАЖНЕНИЯ 3: Работа со списками
# ============================================================================

def solution_3_lists():
    """Решение: Работа со списками"""
    print("=== Решение 3: Работа со списками ===")
    
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    
    print(f"Исходный список: {numbers}")
    print(f"1. Максимальное значение: {max(numbers)}")
    print(f"2. Минимальное значение: {min(numbers)}")
    print(f"3. Среднее арифметическое: {sum(numbers) / len(numbers):.2f}")
    print(f"4. Сортировка по возрастанию: {sorted(numbers)}")
    print(f"5. Сортировка по убыванию: {sorted(numbers, reverse=True)}")
    print(f"6. Сумма элементов: {sum(numbers)}")
    
    even_numbers = [x for x in numbers if x % 2 == 0]
    odd_numbers = [x for x in numbers if x % 2 != 0]
    print(f"7. Четные числа: {even_numbers}")
    print(f"8. Нечетные числа: {odd_numbers}")
    print()


# ============================================================================
# РЕШЕНИЕ УПРАЖНЕНИЯ 4: Работа со словарями
# ============================================================================

def solution_4_dictionaries():
    """Решение: Работа со словарями"""
    print("=== Решение 4: Работа со словарями ===")
    
    students = {'Алиса': 85, 'Боб': 92, 'Карл': 78}
    
    print(f"Исходный словарь: {students}")
    
    # 1. Добавляем студента
    students['Дина'] = 88
    print(f"1. После добавления: {students}")
    
    # 2. Удаляем студента
    del students['Дина']
    print(f"2. После удаления: {students}")
    
    # 3. Изменяем оценку
    students['Алиса'] = 90
    print(f"3. После изменения: {students}")
    
    # 4. Находим лучшего студента
    best_student = max(students, key=students.get)
    print(f"4. Лучший студент: {best_student} ({students[best_student]})")
    
    # 5. Находим худшего студента
    worst_student = min(students, key=students.get)
    print(f"5. Худший студент: {worst_student} ({students[worst_student]})")
    
    # 6. Средняя оценка
    average_grade = sum(students.values()) / len(students)
    print(f"6. Средняя оценка: {average_grade:.2f}")
    
    # 7. Студенты выше среднего
    above_average = [name for name, grade in students.items() if grade > average_grade]
    print(f"7. Студенты выше среднего: {above_average}")
    print()


# ============================================================================
# РЕШЕНИЕ УПРАЖНЕНИЯ 5: Работа с кортежами
# ============================================================================

def solution_5_tuples():
    """Решение: Работа с кортежами"""
    print("=== Решение 5: Работа с кортежами ===")
    
    # 1. Создаем точки
    point1 = (0, 0)
    point2 = (3, 4)
    print(f"1. Точка 1: {point1}")
    print(f"2. Точка 2: {point2}")
    
    # 3. Вычисляем расстояние
    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)
    print(f"3. Расстояние между точками: {distance}")
    
    # 4. Создаем информацию о студенте
    student_info = ("Алиса", 20, 85)
    print(f"4. Информация о студенте: {student_info}")
    
    # 5. Список кортежей студентов
    students = [
        ("Алиса", 20, 85),
        ("Боб", 22, 92),
        ("Карл", 19, 78)
    ]
    print(f"5. Список студентов: {students}")
    
    # 6. Самый старший студент
    oldest_student = max(students, key=lambda x: x[1])
    print(f"6. Самый старший: {oldest_student[0]} ({oldest_student[1]} лет)")
    print()


# ============================================================================
# РЕШЕНИЕ УПРАЖНЕНИЯ 6: Работа с множествами
# ============================================================================

def solution_6_sets():
    """Решение: Работа с множествами"""
    print("=== Решение 6: Работа с множествами ===")
    
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"Множество A: {set_a}")
    print(f"Множество B: {set_b}")
    
    print(f"1. Объединение: {set_a | set_b}")
    print(f"2. Пересечение: {set_a & set_b}")
    print(f"3. Разность A - B: {set_a - set_b}")
    print(f"4. Разность B - A: {set_b - set_a}")
    print(f"5. Симметричная разность: {set_a ^ set_b}")
    print(f"6. A является подмножеством B: {set_a.issubset(set_b)}")
    
    # 7. Удаляем дубликаты
    numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
    unique_numbers = set(numbers_with_duplicates)
    print(f"7. Уникальные числа: {unique_numbers}")
    print()


# ============================================================================
# РЕШЕНИЕ УПРАЖНЕНИЯ 7: Преобразование типов
# ============================================================================

def solution_7_conversions():
    """Решение: Преобразование типов"""
    print("=== Решение 7: Преобразование типов ===")
    
    # 1. Строка в число
    number_from_string = int("123")
    print(f"1. Строка '123' в число: {number_from_string} (тип: {type(number_from_string)})")
    
    # 2. Число в строку
    string_from_number = str(456)
    print(f"2. Число 456 в строку: '{string_from_number}' (тип: {type(string_from_number)})")
    
    # 3. Строка в список символов
    char_list = list("Python")
    print(f"3. Строка 'Python' в список: {char_list}")
    
    # 4. Список в кортеж
    original_list = [1, 2, 3]
    tuple_from_list = tuple(original_list)
    print(f"4. Список {original_list} в кортеж: {tuple_from_list}")
    
    # 5. Кортеж в список
    original_tuple = (1, 2, 3)
    list_from_tuple = list(original_tuple)
    print(f"5. Кортеж {original_tuple} в список: {list_from_tuple}")
    
    # 6. Список в множество
    list_with_duplicates = [1, 2, 2, 3]
    set_from_list = set(list_with_duplicates)
    print(f"6. Список {list_with_duplicates} в множество: {set_from_list}")
    
    # 7. Словарь из списков
    keys = ['a', 'b', 'c']
    values = [1, 2, 3]
    dictionary = dict(zip(keys, values))
    print(f"7. Словарь из списков: {dictionary}")
    print()


# ============================================================================
# РЕШЕНИЕ УПРАЖНЕНИЯ 8: Проверка типов
# ============================================================================

def solution_8_type_checking():
    """Решение: Проверка типов"""
    print("=== Решение 8: Проверка типов ===")
    
    # Проверяем типы
    print(f"1. 42 является числом: {isinstance(42, (int, float))}")
    print(f"2. 'hello' является строкой: {isinstance('hello', str)}")
    print(f"3. [1, 2, 3] является списком: {isinstance([1, 2, 3], list)}")
    print(f"4. {{'a': 1}} является словарем: {isinstance({'a': 1}, dict)}")
    
    def process_data(data):
        """Обрабатывает разные типы данных"""
        if isinstance(data, (int, float)):
            print(f"Это число: {data}")
        elif isinstance(data, str):
            print(f"Это строка: {data}")
        elif isinstance(data, list):
            print(f"Это список с {len(data)} элементами")
        elif isinstance(data, dict):
            print(f"Это словарь с {len(data)} ключами")
        elif isinstance(data, tuple):
            print(f"Это кортеж с {len(data)} элементами")
        elif isinstance(data, set):
            print(f"Это множество с {len(data)} элементами")
        else:
            print(f"Неизвестный тип: {type(data)}")
    
    print("\nТестирование функции process_data:")
    process_data(42)
    process_data("hello")
    process_data([1, 2, 3])
    process_data({'a': 1, 'b': 2})
    process_data((1, 2, 3))
    process_data({1, 2, 3})
    print()


# ============================================================================
# ЗАПУСК ВСЕХ РЕШЕНИЙ
# ============================================================================

def run_all_solutions():
    """Запускает все решения"""
    print("РЕШЕНИЯ УПРАЖНЕНИЙ: ТИПЫ ДАННЫХ В PYTHON")
    print("=" * 50)
    print()
    
    solution_1_numbers()
    solution_2_strings()
    solution_3_lists()
    solution_4_dictionaries()
    solution_5_tuples()
    solution_6_sets()
    solution_7_conversions()
    solution_8_type_checking()
    
    print("Все решения показаны!")


if __name__ == "__main__":
    run_all_solutions() 