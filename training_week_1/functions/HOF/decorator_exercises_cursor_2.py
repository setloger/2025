"""
Практические упражнения: Декораторы с параметрами

Этот файл содержит упражнения для закрепления знаний о декораторах с параметрами
и сохранении свойств декорируемых функций.
"""

import functools
import time
import random
from typing import Callable, Any, Optional


# ============================================================================
# УПРАЖНЕНИЕ 1: Декоратор для ограничения времени выполнения
# ============================================================================

def timeout(seconds: float):
    """
    Создайте декоратор, который прерывает выполнение функции,
    если она выполняется дольше указанного времени.
    
    Подсказка: используйте threading.Timer или signal (на Unix)
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Реализуйте логику ограничения времени
            # Если функция выполняется дольше seconds, 
            # должно быть вызвано исключение TimeoutError
            pass
        return wrapper
    return decorator


# ============================================================================
# УПРАЖНЕНИЕ 2: Декоратор для профилирования памяти
# ============================================================================

def memory_profile(func: Callable) -> Callable:
    """
    Создайте декоратор, который измеряет использование памяти функцией.
    
    Подсказка: используйте psutil или tracemalloc
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Реализуйте измерение памяти
        # Должно выводиться количество использованной памяти
        pass
    return wrapper


# ============================================================================
# УПРАЖНЕНИЕ 3: Декоратор для кэширования с LRU
# ============================================================================

def lru_cache(maxsize: int = 128):
    """
    Создайте декоратор для кэширования с политикой LRU (Least Recently Used).
    
    Args:
        maxsize: Максимальное количество элементов в кэше
    """
    def decorator(func: Callable) -> Callable:
        # TODO: Реализуйте LRU кэш
        # Используйте OrderedDict или собственную реализацию
        pass
    return decorator


# ============================================================================
# УПРАЖНЕНИЕ 4: Декоратор для валидации возвращаемого значения
# ============================================================================

def validate_return(validator: Callable[[Any], bool], error_message: str = "Некорректное возвращаемое значение"):
    """
    Создайте декоратор, который валидирует возвращаемое значение функции.
    
    Args:
        validator: Функция валидации, возвращающая True/False
        error_message: Сообщение об ошибке
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Реализуйте валидацию возвращаемого значения
            pass
        return wrapper
    return decorator


# ============================================================================
# УПРАЖНЕНИЕ 5: Декоратор для rate limiting
# ============================================================================

def rate_limit(calls: int, period: float):
    """
    Создайте декоратор, который ограничивает количество вызовов функции
    в указанный период времени.
    
    Args:
        calls: Максимальное количество вызовов
        period: Период времени в секундах
    """
    def decorator(func: Callable) -> Callable:
        # TODO: Реализуйте rate limiting
        # Используйте список временных меток вызовов
        pass
    return decorator


# ============================================================================
# УПРАЖНЕНИЕ 6: Декоратор для логирования в файл
# ============================================================================

def log_to_file(filename: str, level: str = "INFO"):
    """
    Создайте декоратор, который логирует вызовы функции в файл.
    
    Args:
        filename: Имя файла для логирования
        level: Уровень логирования (INFO, WARNING, ERROR)
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # TODO: Реализуйте логирование в файл
            # Формат: [TIMESTAMP] [LEVEL] [FUNCTION_NAME] - [MESSAGE]
            pass
        return wrapper
    return decorator


# ============================================================================
# УПРАЖНЕНИЕ 7: Декоратор для дебаунсинга
# ============================================================================

def debounce(delay: float):
    """
    Создайте декоратор, который откладывает выполнение функции
    до тех пор, пока не пройдет указанное время с последнего вызова.
    
    Args:
        delay: Задержка в секундах
    """
    def decorator(func: Callable) -> Callable:
        # TODO: Реализуйте дебаунсинг
        # Используйте threading.Timer
        pass
    return decorator


# ============================================================================
# УПРАЖНЕНИЕ 8: Декоратор для мемоизации с TTL
# ============================================================================

def memoize_with_ttl(ttl_seconds: int = 300, max_size: int = 100):
    """
    Создайте декоратор для кэширования с временем жизни и ограничением размера.
    
    Args:
        ttl_seconds: Время жизни кэша в секундах
        max_size: Максимальное количество элементов в кэше
    """
    def decorator(func: Callable) -> Callable:
        # TODO: Реализуйте кэширование с TTL и ограничением размера
        # Удаляйте устаревшие элементы и ограничивайте размер кэша
        pass
    return decorator


# ============================================================================
# ТЕСТОВЫЕ ФУНКЦИИ ДЛЯ ПРОВЕРКИ
# ============================================================================

def slow_function():
    """Функция, которая выполняется долго"""
    time.sleep(2)
    return "Готово!"


def memory_intensive_function(n: int):
    """Функция, которая использует много памяти"""
    return [i for i in range(n)]


def random_function():
    """Функция, возвращающая случайное число"""
    return random.randint(1, 100)


def validate_positive(value: int) -> bool:
    """Проверяет, является ли число положительным"""
    return value > 0


def test_function():
    """Тестовая функция для проверки декораторов"""
    print("Выполняется тестовая функция")
    return 42


# ============================================================================
# ПРИМЕРЫ РЕШЕНИЙ (раскомментируйте для проверки)
# ============================================================================

"""
# Пример решения для Exercise 1 (timeout)
import threading
import _thread

def timeout(seconds: float):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = [None]
            exception = [None]
            
            def target():
                try:
                    result[0] = func(*args, **kwargs)
                except Exception as e:
                    exception[0] = e
            
            thread = threading.Thread(target=target)
            thread.daemon = True
            thread.start()
            thread.join(seconds)
            
            if thread.is_alive():
                _thread.interrupt_main()
                raise TimeoutError(f"Функция {func.__name__} превысила лимит времени {seconds} секунд")
            
            if exception[0]:
                raise exception[0]
            
            return result[0]
        return wrapper
    return decorator

# Пример решения для Exercise 3 (lru_cache)
from collections import OrderedDict

def lru_cache(maxsize: int = 128):
    def decorator(func: Callable) -> Callable:
        cache = OrderedDict()
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            key = str(args) + str(sorted(kwargs.items()))
            
            if key in cache:
                # Перемещаем в конец (LRU)
                cache.move_to_end(key)
                return cache[key]
            
            result = func(*args, **kwargs)
            cache[key] = result
            
            # Удаляем самый старый элемент, если превышен размер
            if len(cache) > maxsize:
                cache.popitem(last=False)
            
            return result
        return wrapper
    return decorator

# Пример решения для Exercise 4 (validate_return)
def validate_return(validator: Callable[[Any], bool], error_message: str = "Некорректное возвращаемое значение"):
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not validator(result):
                raise ValueError(error_message)
            return result
        return wrapper
    return decorator

# Пример решения для Exercise 5 (rate_limit)
def rate_limit(calls: int, period: float):
    def decorator(func: Callable) -> Callable:
        call_times = []
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            
            # Удаляем старые вызовы
            call_times[:] = [t for t in call_times if current_time - t < period]
            
            if len(call_times) >= calls:
                raise Exception(f"Превышен лимит вызовов: {calls} за {period} секунд")
            
            call_times.append(current_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator
"""


# ============================================================================
# ФУНКЦИЯ ДЛЯ ТЕСТИРОВАНИЯ
# ============================================================================

def test_decorators():
    """Тестирует все декораторы"""
    print("Тестирование декораторов...")
    
    # Здесь можно добавить тесты для каждого декоратора
    # после их реализации
    
    print("Тестирование завершено!")


if __name__ == "__main__":
    test_decorators() 