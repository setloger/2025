# Декораторы с параметрами и сохранение свойств функций

## Содержание
1. [Декораторы с параметрами](#декораторы-с-параметрами)
2. [Сохранение метаданных функций](#сохранение-метаданных-функций)
3. [Лучшие практики](#лучшие-практики)
4. [Продвинутые техники](#продвинутые-техники)
5. [Частые ошибки](#частые-ошибки)

## Декораторы с параметрами

### Концепция
Декораторы с параметрами позволяют настраивать поведение декоратора при его применении. Это достигается за счет создания "фабрики декораторов" - функции, которая возвращает декоратор.

### Структура
```python
def decorator_with_params(param1, param2, ...):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Логика с использованием param1, param2, ...
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

### Примеры использования

#### 1. Декоратор с одним параметром
```python
def repeat(times=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    print(f"Привет, {name}!")
```

#### 2. Декоратор с несколькими параметрами
```python
def retry(max_attempts=3, delay=1.0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt < max_attempts - 1:
                        time.sleep(delay)
                    else:
                        raise e
        return wrapper
    return decorator

@retry(max_attempts=5, delay=0.5)
def risky_function():
    # Может вызвать исключение
    pass
```

## Сохранение метаданных функций

### Проблема
При создании декораторов без `functools.wraps` теряются важные метаданные декорируемой функции:

```python
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@bad_decorator
def example():
    """Документация функции"""
    pass

print(example.__name__)  # 'wrapper' вместо 'example'
print(example.__doc__)   # None вместо документации
```

### Решение с functools.wraps
```python
import functools

def good_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def example():
    """Документация функции"""
    pass

print(example.__name__)  # 'example'
print(example.__doc__)   # 'Документация функции'
```

### Что сохраняет functools.wraps
- `__name__` - имя функции
- `__doc__` - документация
- `__module__` - модуль
- `__annotations__` - аннотации типов
- `__qualname__` - квалифицированное имя
- `__defaults__` - значения по умолчанию
- `__kwdefaults__` - значения по умолчанию для keyword-only аргументов

## Лучшие практики

### 1. Всегда используйте functools.wraps
```python
import functools

def my_decorator(func):
    @functools.wraps(func)  # ✅ Хорошо
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 2. Используйте типизацию
```python
from typing import Callable, Any

def my_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return func(*args, **kwargs)
    return wrapper
```

### 3. Обрабатывайте исключения правильно
```python
def safe_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            # Логируем ошибку, но не скрываем её
            print(f"Ошибка в {func.__name__}: {e}")
            raise  # Перебрасываем исключение
    return wrapper
```

### 4. Используйте параметры по умолчанию
```python
def configurable_decorator(param1="default1", param2="default2"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Используем param1 и param2
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Можно использовать без параметров
@configurable_decorator()
def func1():
    pass

# Или с параметрами
@configurable_decorator(param1="custom", param2="value")
def func2():
    pass
```

## Продвинутые техники

### 1. Декораторы для методов классов
```python
def class_method_decorator(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Доступ к self и методам класса
        print(f"Вызов метода {func.__name__} класса {self.__class__.__name__}")
        return func(self, *args, **kwargs)
    return wrapper

class MyClass:
    @class_method_decorator
    def my_method(self, value):
        return value * 2
```

### 2. Декораторы с состоянием
```python
def stateful_decorator():
    state = {"counter": 0}
    
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            state["counter"] += 1
            print(f"Вызов #{state['counter']}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@stateful_decorator()
def counter_function():
    print("Выполнение функции")
```

### 3. Декораторы для валидации
```python
def validate_args(*validators):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Проверяем каждый аргумент
            for i, (arg, validator) in enumerate(zip(args, validators)):
                if not validator(arg):
                    raise ValueError(f"Аргумент {i} не прошел валидацию")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def is_positive(x): return x > 0
def is_string(x): return isinstance(x, str)

@validate_args(is_positive, is_string)
def process_data(number, text):
    return f"{number} - {text}"
```

### 4. Декораторы для кэширования
```python
def memoize(max_size=128):
    def decorator(func):
        cache = {}
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Создаем ключ кэша
            key = str(args) + str(sorted(kwargs.items()))
            
            if key in cache:
                return cache[key]
            
            result = func(*args, **kwargs)
            
            # Ограничиваем размер кэша
            if len(cache) >= max_size:
                # Удаляем самый старый элемент
                cache.pop(next(iter(cache)))
            
            cache[key] = result
            return result
        return wrapper
    return decorator

@memoize(max_size=100)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## Частые ошибки

### 1. Забывают functools.wraps
```python
# ❌ Плохо - теряются метаданные
def bad_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# ✅ Хорошо - сохраняются метаданные
def good_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

### 2. Неправильная обработка исключений
```python
# ❌ Плохо - скрывает исключения
def bad_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка: {e}")
            # Исключение потеряно!
    return wrapper

# ✅ Хорошо - логирует и перебрасывает исключение
def good_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ошибка в {func.__name__}: {e}")
            raise  # Перебрасываем исключение
    return wrapper
```

### 3. Неправильная передача аргументов
```python
# ❌ Плохо - не передает keyword аргументы
def bad_decorator(func):
    @functools.wraps(func)
    def wrapper(*args):  # Только позиционные аргументы
        return func(*args)
    return wrapper

# ✅ Хорошо - передает все аргументы
def good_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):  # Все типы аргументов
        return func(*args, **kwargs)
    return wrapper
```

### 4. Проблемы с замыканиями
```python
# ❌ Плохо - все функции используют последнее значение i
def bad_decorator():
    decorators = []
    for i in range(3):
        def decorator(func):
            def wrapper(*args, **kwargs):
                print(f"i = {i}")  # Всегда будет 2!
                return func(*args, **kwargs)
            return wrapper
        decorators.append(decorator)
    return decorators

# ✅ Хорошо - каждая функция получает свое значение i
def good_decorator():
    decorators = []
    for i in range(3):
        def decorator(func, i=i):  # Захватываем текущее значение i
            def wrapper(*args, **kwargs):
                print(f"i = {i}")
                return func(*args, **kwargs)
            return wrapper
        decorators.append(decorator)
    return decorators
```

## Заключение

Декораторы с параметрами - это мощный инструмент для создания гибкого и переиспользуемого кода. Ключевые моменты:

1. **Всегда используйте `functools.wraps`** для сохранения метаданных
2. **Правильно обрабатывайте исключения** - логируйте, но не скрывайте
3. **Используйте типизацию** для лучшей читаемости кода
4. **Тестируйте декораторы** отдельно от декорируемых функций
5. **Документируйте параметры** декораторов

Декораторы позволяют элегантно добавлять функциональность без изменения исходного кода, что делает их незаменимым инструментом в арсенале Python-разработчика. 