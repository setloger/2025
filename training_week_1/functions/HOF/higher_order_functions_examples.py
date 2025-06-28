#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Расширенные примеры и задачи на функции высшего порядка в Python
"""

# 1. Функция, принимающая другую функцию как аргумент

def apply_operation(func, *args):
    """Применяет функцию func к аргументам args"""
    return func(*args)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

print("=== Пример 1: Передача функции как аргумента ===")
print(f"Сложение: {apply_operation(add, 2, 3)}")
print(f"Умножение: {apply_operation(multiply, 2, 3)}")
print()

# 2. Функция, возвращающая функцию (замыкание)

def make_power(exp):
    """Возвращает функцию, возводящую число в степень exp"""
    def power(x):
        return x ** exp
    return power

square = make_power(2)
cube = make_power(3)

print("=== Пример 2: Возврат функции (замыкание) ===")
print(f"Квадрат 5: {square(5)}")
print(f"Куб 2: {cube(2)}")
print()

# 3. Использование map, filter, reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x ** 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
sum_all = reduce(lambda x, y: x + y, numbers)

print("=== Пример 3: map, filter, reduce ===")
print(f"Квадраты: {squares}")
print(f"Четные: {evens}")
print(f"Сумма всех: {sum_all}")
print()

# 4. Декоратор как функция высшего порядка

def debug_decorator(func):
    """Декоратор, выводящий аргументы и результат функции"""
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@debug_decorator
def subtract(x, y):
    return x - y

print("=== Пример 4: Декоратор ===")
subtract(10, 3)
print()

# 5. Функция, принимающая список функций

def batch_apply(functions, value):
    """Применяет список функций к одному значению"""
    return [f(value) for f in functions]

print("=== Пример 5: Список функций ===")
funcs = [square, cube, abs]
print(f"Результаты: {batch_apply(funcs, -3)}")
print()

# 6. Задача: написать функцию, которая принимает список чисел и функцию, и возвращает новый список, где к каждому элементу применена функция

def transform_list(lst, func):
    """Применяет func к каждому элементу списка lst"""
    return [func(x) for x in lst]

print("=== Пример 6: Задача на применение функции к списку ===")
print(f"Удвоенные значения: {transform_list([1,2,3], lambda x: x*2)}")
print(f"Модули: {transform_list([-1, -2, 3], abs)}")
print()

# 7. Задача: функция, возвращающая декоратор с параметрами

def repeat_decorator(times):
    """Декоратор, повторяющий вызов функции times раз"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat_decorator(3)
def hello(name):
    print(f"Привет, {name}!")

print("=== Пример 7: Декоратор с параметрами ===")
hello("Мир")
print()

# 8. Задача: функция, возвращающая функцию с частично зафиксированными аргументами
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print("=== Пример 8: partial ===")
print(f"Квадрат 7: {square(7)}")
print(f"Куб 4: {cube(4)}")
print()

# 9. Задача: функция, принимающая другую функцию и список, и возвращающая True, если хотя бы один элемент удовлетворяет условию

def any_match(lst, predicate):
    """Возвращает True, если хотя бы один элемент lst удовлетворяет predicate"""
    return any(predicate(x) for x in lst)

print("=== Пример 9: any_match ===")
print(f"Есть ли четные? {any_match([1,3,5,6], lambda x: x%2==0)}")
print(f"Есть ли отрицательные? {any_match([1,2,3], lambda x: x<0)}")
print()

# 10. Задача: функция, возвращающая функцию, которая применяет несколько функций к значению и возвращает список результатов

def multi_apply(*funcs):
    """Возвращает функцию, применяющую все funcs к значению"""
    def applier(x):
        return [f(x) for f in funcs]
    return applier

print("=== Пример 10: multi_apply ===")
apply_all = multi_apply(abs, square, cube)
print(f"Результаты: {apply_all(-2)}") 