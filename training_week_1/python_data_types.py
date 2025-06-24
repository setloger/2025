#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Примеры основных типов данных в Python
"""

# 1. Числовые типы данных (Numeric Types)
# =====================================

# Целые числа (integers - int)
integer_number = 42
negative_integer = -17
big_integer = 1_000_000  # можно использовать _ для удобства чтения больших чисел

print("Целые числа:")
print(f"Обычное целое число: {integer_number}")
print(f"Отрицательное число: {negative_integer}")
print(f"Большое число: {big_integer}")
print(f"Тип данных: {type(integer_number)}")
print()

# Числа с плавающей точкой (float)
float_number = 3.14
scientific_notation = 2.5e-3  # 2.5 × 10^(-3) = 0.0025

print("Числа с плавающей точкой:")
print(f"Обычное float число: {float_number}")
print(f"Научная нотация: {scientific_notation}")
print(f"Тип данных: {type(float_number)}")
print()

# Комплексные числа (complex)
complex_number = 3 + 4j
print("Комплексные числа:")
print(f"Комплексное число: {complex_number}")
print(f"Действительная часть: {complex_number.real}")
print(f"Мнимая часть: {complex_number.imag}")
print(f"Тип данных: {type(complex_number)}")
print()

# 2. Последовательности (Sequence Types)
# ==================================

# Строки (str)
simple_string = "Привет, мир!"
multiline_string = """Это
многострочная
строка"""

print("Строки:")
print(f"Простая строка: {simple_string}")
print(f"Многострочная строка:\n{multiline_string}")
print(f"Тип данных: {type(simple_string)}")
print()

# Списки (list) - изменяемый тип данных
my_list = [1, "два", 3.0, [4, 5]]
print("Списки:")
print(f"Список: {my_list}")
print(f"Первый элемент: {my_list[0]}")
print(f"Вложенный список: {my_list[3]}")
print(f"Тип данных: {type(my_list)}")
print()

# Кортежи (tuple) - неизменяемый тип данных
my_tuple = (1, "два", 3.0)
print("Кортежи:")
print(f"Кортеж: {my_tuple}")
print(f"Второй элемент: {my_tuple[1]}")
print(f"Тип данных: {type(my_tuple)}")
print()

# 3. Отображения (Mapping Types)
# ===========================

# Словари (dict)
my_dict = {
    "name": "Иван",
    "age": 25,
    "city": "Москва"
}
print("Словари:")
print(f"Словарь: {my_dict}")
print(f"Значение по ключу 'name': {my_dict['name']}")
print(f"Тип данных: {type(my_dict)}")
print()

# 4. Множества (Set Types)
# =====================

# Множество (set) - изменяемое, неупорядоченное собрание уникальных элементов
my_set = {1, 2, 3, 3, 2, 1}  # дубликаты будут удалены
print("Множества:")
print(f"Множество: {my_set}")
print(f"Тип данных: {type(my_set)}")
print()

# Неизменяемое множество (frozenset)
my_frozenset = frozenset([1, 2, 3, 3, 2, 1])
print("Неизменяемые множества:")
print(f"Неизменяемое множество: {my_frozenset}")
print(f"Тип данных: {type(my_frozenset)}")
print()

# 5. Логический тип (Boolean Type)
# =============================

# Bool
is_true = True
is_false = False
print("Логический тип:")
print(f"Истина: {is_true}")
print(f"Ложь: {is_false}")
print(f"Тип данных: {type(is_true)}")
print()

# 6. Специальный тип None
# ====================

# None - представляет отсутствие значения
nothing = None
print("Тип None:")
print(f"Значение: {nothing}")
print(f"Тип данных: {type(nothing)}")
print()

# Примеры преобразования типов
print("Преобразование типов:")
print(f"str в int: {int('42')}")
print(f"float в int: {int(3.14)}")
print(f"int в float: {float(42)}")
print(f"int в str: {str(42)}")
print(f"list в set: {set([1, 2, 2, 3, 3])}") 