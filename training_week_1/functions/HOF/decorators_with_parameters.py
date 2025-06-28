"""
Декораторы с параметрами и сохранение свойств декорируемых функций

Этот модуль демонстрирует:
1. Декораторы с параметрами
2. Сохранение метаданных декорируемых функций
3. Использование functools.wraps
4. Практические примеры применения
"""

import functools
import time
import logging
from typing import Callable, Any, Optional


# ============================================================================
# 1. ДЕКОРАТОРЫ С ПАРАМЕТРАМИ
# ============================================================================

def repeat(times: int = 1):
    """
    Декоратор с параметром - повторяет выполнение функции указанное количество раз
    
    Args:
        times: Количество повторений (по умолчанию 1)
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)  # Сохраняем метаданные функции
        def wrapper(*args, **kwargs):
            result = None
            for i in range(times):
                print(f"Выполнение {i + 1}/{times}")
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Декоратор с параметрами для повторных попыток выполнения функции
    
    Args:
        max_attempts: Максимальное количество попыток
        delay: Задержка между попытками в секундах
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    if attempt < max_attempts - 1:
                        print(f"Попытка {attempt + 1} не удалась: {e}")
                        print(f"Ожидание {delay} секунд...")
                        time.sleep(delay)
            
            print(f"Все {max_attempts} попыток не удались")
            raise last_exception
        
        return wrapper
    return decorator


def validate_input(validator: Callable[[Any], bool], error_message: str = "Валидация не пройдена"):
    """
    Декоратор с параметрами для валидации входных данных
    
    Args:
        validator: Функция валидации, возвращающая True/False
        error_message: Сообщение об ошибке
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not validator(*args, **kwargs):
                raise ValueError(error_message)
            return func(*args, **kwargs)
        return wrapper
    return decorator


def cache_with_ttl(ttl_seconds: int = 300):
    """
    Декоратор с параметрами для кэширования с временем жизни
    
    Args:
        ttl_seconds: Время жизни кэша в секундах
    """
    def decorator(func: Callable) -> Callable:
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Создаем ключ кэша из аргументов
            cache_key = str(args) + str(sorted(kwargs.items()))
            current_time = time.time()
            
            # Проверяем, есть ли в кэше и не истек ли срок
            if cache_key in cache:
                result, timestamp = cache[cache_key]
                if current_time - timestamp < ttl_seconds:
                    print(f"Возвращаем результат из кэша для {func.__name__}")
                    return result
            
            # Выполняем функцию и сохраняем результат
            result = func(*args, **kwargs)
            cache[cache_key] = (result, current_time)
            print(f"Сохраняем результат в кэш для {func.__name__}")
            return result
        
        return wrapper
    return decorator


# ============================================================================
# 2. СОХРАНЕНИЕ СВОЙСТВ ДЕКОРИРУЕМЫХ ФУНКЦИЙ
# ============================================================================

def preserve_metadata_example():
    """
    Демонстрация важности сохранения метаданных функций
    """
    
    # БЕЗ functools.wraps - теряем метаданные
    def bad_decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    # С functools.wraps - сохраняем метаданные
    def good_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    
    @bad_decorator
    def example_function():
        """Это документация функции"""
        pass
    
    @good_decorator
    def example_function_good():
        """Это документация функции"""
        pass
    
    print("=== БЕЗ functools.wraps ===")
    print(f"Имя функции: {example_function.__name__}")
    print(f"Документация: {example_function.__doc__}")
    print(f"Модуль: {example_function.__module__}")
    
    print("\n=== С functools.wraps ===")
    print(f"Имя функции: {example_function_good.__name__}")
    print(f"Документация: {example_function_good.__doc__}")
    print(f"Модуль: {example_function_good.__module__}")


# ============================================================================
# 3. ПРАКТИЧЕСКИЕ ПРИМЕРЫ
# ============================================================================

@repeat(times=3)
def greet(name: str) -> str:
    """Приветствует пользователя"""
    message = f"Привет, {name}!"
    print(message)
    return message


@retry(max_attempts=3, delay=0.5)
def risky_operation(should_fail: bool = False) -> str:
    """Операция, которая может завершиться неудачей"""
    if should_fail:
        raise ValueError("Операция завершилась неудачей")
    return "Операция выполнена успешно"


def is_positive(value: int) -> bool:
    """Проверяет, является ли число положительным"""
    return value > 0


@validate_input(is_positive, "Число должно быть положительным")
def calculate_square_root(number: int) -> float:
    """Вычисляет квадратный корень из положительного числа"""
    import math
    return math.sqrt(number)


@cache_with_ttl(ttl_seconds=5)
def expensive_calculation(n: int) -> int:
    """Дорогостоящее вычисление (симулируем задержкой)"""
    print(f"Выполняем дорогостоящее вычисление для {n}")
    time.sleep(1)  # Симулируем долгое вычисление
    return n * n


# ============================================================================
# 4. ДЕКОРАТОРЫ ДЛЯ ЛОГИРОВАНИЯ
# ============================================================================

def log_function_call(logger: Optional[logging.Logger] = None):
    """
    Декоратор для логирования вызовов функций
    
    Args:
        logger: Логгер для записи (если None, используется print)
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Логируем вход
            if logger:
                logger.info(f"Вызов {func.__name__} с аргументами: {args}, {kwargs}")
            else:
                print(f"[INFO] Вызов {func.__name__} с аргументами: {args}, {kwargs}")
            
            try:
                result = func(*args, **kwargs)
                # Логируем успешный выход
                if logger:
                    logger.info(f"Функция {func.__name__} завершилась успешно")
                else:
                    print(f"[INFO] Функция {func.__name__} завершилась успешно")
                return result
            except Exception as e:
                # Логируем ошибку
                if logger:
                    logger.error(f"Ошибка в функции {func.__name__}: {e}")
                else:
                    print(f"[ERROR] Ошибка в функции {func.__name__}: {e}")
                raise
        
        return wrapper
    return decorator


@log_function_call()
def divide_numbers(a: float, b: float) -> float:
    """Делит два числа"""
    return a / b


# ============================================================================
# 5. ДЕКОРАТОРЫ ДЛЯ ИЗМЕРЕНИЯ ПРОИЗВОДИТЕЛЬНОСТИ
# ============================================================================

def measure_time(description: str = ""):
    """
    Декоратор для измерения времени выполнения функции
    
    Args:
        description: Описание операции для логирования
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            
            operation_name = description or func.__name__
            execution_time = end_time - start_time
            print(f"Операция '{operation_name}' выполнена за {execution_time:.4f} секунд")
            
            return result
        return wrapper
    return decorator


@measure_time("Факториал")
def factorial(n: int) -> int:
    """Вычисляет факториал числа"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# ============================================================================
# 6. ДЕМОНСТРАЦИЯ РАБОТЫ
# ============================================================================

def demonstrate_decorators():
    """Демонстрирует работу всех декораторов"""
    
    print("=" * 60)
    print("ДЕМОНСТРАЦИЯ ДЕКОРАТОРОВ С ПАРАМЕТРАМИ")
    print("=" * 60)
    
    print("\n1. Декоратор repeat:")
    greet("Алиса")
    
    print("\n2. Декоратор retry (успешная операция):")
    try:
        result = risky_operation(should_fail=False)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n3. Декоратор retry (неудачная операция):")
    try:
        result = risky_operation(should_fail=True)
        print(f"Результат: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n4. Декоратор validate_input:")
    try:
        result = calculate_square_root(16)
        print(f"Квадратный корень из 16: {result}")
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
    
    try:
        result = calculate_square_root(-4)
        print(f"Квадратный корень из -4: {result}")
    except ValueError as e:
        print(f"Ошибка валидации: {e}")
    
    print("\n5. Декоратор cache_with_ttl:")
    print("Первый вызов:")
    result1 = expensive_calculation(5)
    print(f"Результат: {result1}")
    
    print("Второй вызов (должен быть из кэша):")
    result2 = expensive_calculation(5)
    print(f"Результат: {result2}")
    
    print("\n6. Декоратор log_function_call:")
    try:
        result = divide_numbers(10, 2)
        print(f"Результат деления: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    try:
        result = divide_numbers(10, 0)
        print(f"Результат деления: {result}")
    except Exception as e:
        print(f"Ошибка: {e}")
    
    print("\n7. Декоратор measure_time:")
    result = factorial(10)
    print(f"Факториал 10: {result}")
    
    print("\n8. Сохранение метаданных:")
    preserve_metadata_example()


if __name__ == "__main__":
    demonstrate_decorators() 