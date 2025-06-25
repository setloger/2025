#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Полная информация о функциях в Python с примерами
"""

# 1. Базовые функции
# ================

def simple_function():
    """Простая функция без параметров"""
    print("Привет из простой функции!")

def function_with_params(name, age):
    """Функция с параметрами"""
    print(f"Привет, {name}! Тебе {age} лет.")

def function_with_return(x, y):
    """Функция с возвращаемым значением"""
    return x + y

print("=== БАЗОВЫЕ ФУНКЦИИ ===")
simple_function()
function_with_params("Анна", 25)
result = function_with_return(5, 3)
print(f"Результат сложения: {result}")
print()

# 2. Параметры функций
# ===================

def function_with_default_params(name="Гость", age=18):
    """Функция с параметрами по умолчанию"""
    print(f"Привет, {name}! Тебе {age} лет.")

def function_with_args(*args):
    """Функция с произвольным количеством позиционных аргументов"""
    print(f"Получены аргументы: {args}")
    return sum(args)

def function_with_kwargs(**kwargs):
    """Функция с произвольным количеством именованных аргументов"""
    print(f"Получены именованные аргументы: {kwargs}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def function_with_mixed_params(name, age=25, *args, **kwargs):
    """Функция со всеми типами параметров"""
    print(f"Имя: {name}, Возраст: {age}")
    if args:
        print(f"Дополнительные позиционные аргументы: {args}")
    if kwargs:
        print(f"Дополнительные именованные аргументы: {kwargs}")

print("=== ПАРАМЕТРЫ ФУНКЦИЙ ===")
function_with_default_params()
function_with_default_params("Петр", 30)
function_with_default_params(age=35, name="Мария")

print("\nАргументы *args:")
result = function_with_args(1, 2, 3, 4, 5)
print(f"Сумма: {result}")

print("\nАргументы **kwargs:")
function_with_kwargs(name="Иван", city="Москва", job="Программист")

print("\nСмешанные параметры:")
function_with_mixed_params("Алексей", 28, "дополнительный", "аргумент", city="СПб", hobby="спорт")
print()

# 3. Типы функций
# ==============

# 3.1 Лямбда-функции (анонимные функции)
lambda_square = lambda x: x ** 2
lambda_add = lambda x, y: x + y

print("=== ЛЯМБДА-ФУНКЦИИ ===")
print(f"Квадрат числа 5: {lambda_square(5)}")
print(f"Сумма 3 и 7: {lambda_add(3, 7)}")

# Использование lambda с функциями высшего порядка
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
filtered = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Исходный список: {numbers}")
print(f"Квадраты: {squared}")
print(f"Четные числа: {filtered}")
print()

# 3.2 Вложенные функции
def outer_function(x):
    """Внешняя функция"""
    def inner_function(y):
        """Внутренняя функция"""
        return x + y
    return inner_function

print("=== ВЛОЖЕННЫЕ ФУНКЦИИ ===")
add_five = outer_function(5)
result = add_five(3)
print(f"Результат: {result}")
print()

# 3.3 Рекурсивные функции
def factorial(n):
    """Рекурсивная функция для вычисления факториала"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Рекурсивная функция для вычисления чисел Фибоначчи"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("=== РЕКУРСИВНЫЕ ФУНКЦИИ ===")
print(f"Факториал 5: {factorial(5)}")
print(f"Число Фибоначчи F(7): {fibonacci(7)}")
print()

# 4. Области видимости (Scope)
# ===========================

global_var = "Глобальная переменная"

def scope_example():
    """Пример работы с областями видимости"""
    local_var = "Локальная переменная"
    print(f"Внутри функции: {local_var}")
    print(f"Глобальная переменная: {global_var}")
    
    def nested_function():
        nested_var = "Переменная вложенной функции"
        print(f"Вложенная функция: {nested_var}")
        print(f"Локальная переменная внешней функции: {local_var}")
    
    nested_function()

def modify_global():
    """Функция для изменения глобальной переменной"""
    global global_var
    global_var = "Измененная глобальная переменная"
    print(f"Глобальная переменная изменена: {global_var}")

print("=== ОБЛАСТИ ВИДИМОСТИ ===")
print(f"Глобальная переменная: {global_var}")
scope_example()
modify_global()
print()

# 5. Декораторы
# ============

def timer_decorator(func):
    """Декоратор для измерения времени выполнения функции"""
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Функция {func.__name__} выполнилась за {end_time - start_time:.4f} секунд")
        return result
    return wrapper

def cache_decorator(func):
    """Простой декоратор-кэш"""
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@timer_decorator
def slow_function():
    """Медленная функция для демонстрации декоратора"""
    import time
    time.sleep(1)
    return "Функция завершена"

@cache_decorator
def expensive_calculation(n):
    """Дорогая операция для демонстрации кэширования"""
    import time
    time.sleep(0.5)
    return n * n

print("=== ДЕКОРАТОРЫ ===")
result = slow_function()
print(f"Результат: {result}")

print("\nКэширование:")
print(f"Первый вызов: {expensive_calculation(5)}")
print(f"Второй вызов (из кэша): {expensive_calculation(5)}")
print()

# 6. Генераторы
# ============

def number_generator(n):
    """Генератор чисел от 1 до n"""
    for i in range(1, n + 1):
        yield i

def fibonacci_generator():
    """Генератор чисел Фибоначчи"""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("=== ГЕНЕРАТОРЫ ===")
print("Генератор чисел:")
for num in number_generator(5):
    print(num, end=" ")
print()

print("\nГенератор Фибоначчи (первые 10 чисел):")
fib_gen = fibonacci_generator()
for _ in range(10):
    print(next(fib_gen), end=" ")
print()

# Генераторные выражения
squares = (x**2 for x in range(5))
print(f"\nГенераторное выражение: {list(squares)}")
print()

# 7. Функции высшего порядка
# =========================

def apply_operation(func, *args):
    """Функция высшего порядка - принимает функцию как аргумент"""
    return func(*args)

def multiply(x, y):
    return x * y

def power(base, exponent):
    return base ** exponent

print("=== ФУНКЦИИ ВЫСШЕГО ПОРЯДКА ===")
result1 = apply_operation(multiply, 4, 5)
result2 = apply_operation(power, 2, 3)
print(f"Умножение: {result1}")
print(f"Возведение в степень: {result2}")

# Функция, возвращающая функцию
def create_multiplier(factor):
    """Создает функцию-умножитель"""
    def multiplier(x):
        return x * factor
    return multiplier

double = create_multiplier(2)
triple = create_multiplier(3)
print(f"Удвоение 5: {double(5)}")
print(f"Утроение 5: {triple(5)}")
print()

# 8. Аннотации типов
# =================

def typed_function(name: str, age: int) -> str:
    """Функция с аннотациями типов"""
    return f"{name} имеет возраст {age} лет"

def complex_typed_function(numbers: list[int], operation: str = "sum") -> float:
    """Функция с более сложными аннотациями типов"""
    if operation == "sum":
        return sum(numbers)
    elif operation == "average":
        return sum(numbers) / len(numbers)
    else:
        raise ValueError("Неизвестная операция")

print("=== АННОТАЦИИ ТИПОВ ===")
result = typed_function("Анна", 25)
print(result)

numbers_list = [1, 2, 3, 4, 5]
print(f"Сумма: {complex_typed_function(numbers_list)}")
print(f"Среднее: {complex_typed_function(numbers_list, 'average')}")
print()

# 9. Обработка исключений в функциях
# =================================

def safe_division(a, b):
    """Функция с обработкой исключений"""
    try:
        return a / b
    except ZeroDivisionError:
        print("Ошибка: деление на ноль!")
        return None
    except TypeError:
        print("Ошибка: неверный тип данных!")
        return None

def validate_age(age):
    """Функция с пользовательскими исключениями"""
    if not isinstance(age, int):
        raise TypeError("Возраст должен быть целым числом")
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным")
    if age > 150:
        raise ValueError("Возраст слишком большой")
    return age

print("=== ОБРАБОТКА ИСКЛЮЧЕНИЙ ===")
print(f"10 / 2 = {safe_division(10, 2)}")
print(f"10 / 0 = {safe_division(10, 0)}")

try:
    validate_age(25)
    print("Возраст 25 корректен")
    validate_age(-5)
except (TypeError, ValueError) as e:
    print(f"Ошибка валидации: {e}")
print()

# 10. Документирование функций
# ===========================

def documented_function(param1: str, param2: int = 10) -> str:
    """
    Подробно документированная функция.
    
    Args:
        param1 (str): Первый параметр - строка
        param2 (int, optional): Второй параметр - целое число. По умолчанию 10.
    
    Returns:
        str: Строка с результатом обработки параметров
    
    Raises:
        ValueError: Если param1 пустая строка
        TypeError: Если param2 не является числом
    
    Examples:
        >>> documented_function("hello", 5)
        'hello: 5'
        >>> documented_function("test")
        'test: 10'
    """
    if not param1:
        raise ValueError("param1 не может быть пустой строкой")
    
    return f"{param1}: {param2}"

print("=== ДОКУМЕНТИРОВАНИЕ ===")
print(documented_function("test", 15))
print(f"Документация функции:\n{documented_function.__doc__}")
print()

# 11. Замыкания (Closures)
# =======================

def create_counter():
    """Создает счетчик с замыканием"""
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

def create_multiplier_with_state(factor):
    """Создает умножитель с состоянием"""
    calls = 0
    
    def multiplier(x):
        nonlocal calls
        calls += 1
        print(f"Функция вызвана {calls} раз(а)")
        return x * factor
    
    return multiplier

print("=== ЗАМЫКАНИЯ ===")
counter = create_counter()
print(f"Счетчик: {counter()}")
print(f"Счетчик: {counter()}")
print(f"Счетчик: {counter()}")

multiplier = create_multiplier_with_state(3)
print(f"Результат: {multiplier(5)}")
print(f"Результат: {multiplier(7)}")
print()

# 12. Функции с частичным применением
# ==================================

from functools import partial

def greet(greeting, name):
    """Функция приветствия"""
    return f"{greeting}, {name}!"

print("=== ЧАСТИЧНОЕ ПРИМЕНЕНИЕ ===")
hello_greeter = partial(greet, "Привет")
goodbye_greeter = partial(greet, "До свидания")

print(hello_greeter("Анна"))
print(goodbye_greeter("Петр"))

# Частичное применение с именованными аргументами
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(f"Квадрат 5: {square(5)}")
print(f"Куб 3: {cube(3)}")
print()

print("=== ЗАКЛЮЧЕНИЕ ===")
print("Это полный обзор функций в Python, включающий:")
print("- Базовые функции")
print("- Различные типы параметров")
print("- Лямбда-функции")
print("- Вложенные функции")
print("- Рекурсию")
print("- Области видимости")
print("- Декораторы")
print("- Генераторы")
print("- Функции высшего порядка")
print("- Аннотации типов")
print("- Обработку исключений")
print("- Документирование")
print("- Замыкания")
print("- Частичное применение") 