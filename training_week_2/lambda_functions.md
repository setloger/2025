<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Анонимные (lambda) функции в Python: Углубленное руководство для Middle-разработчика

## Что такое lambda-функции

**Lambda-функции** — это анонимные функции в Python, которые позволяют создавать небольшие функции без использования ключевого слова `def`. Они особенно полезны для функционального программирования и работы с функциями высшего порядка.

### Базовый синтаксис

```python
lambda параметры: выражение
```

Простейший пример:

```python
square = lambda x: x ** 2
print(square(5))  # 25
```


## Детальное сравнение с обычными функциями

| Характеристика | def-функция | lambda-функция |
| :-- | :-- | :-- |
| **Имя** | Обязательно | Отсутствует |
| **Тело функции** | Множество инструкций | Одно выражение |
| **return** | Явный | Неявный |
| **Аннотации типов** | Поддерживаются | Ограниченная поддержка |
| **Документация** | docstring | Невозможна |
| **Отладка** | Легкая (есть имя) | Сложная (анонимная) |

## Продвинутые примеры использования

### 1. Множественные параметры и сложные выражения

```python
# Несколько параметров
multiply = lambda x, y, z: x * y * z
print(multiply(2, 3, 4))  # 24

# Условные выражения
max_value = lambda a, b: a if a > b else b
print(max_value(10, 15))  # 15

# Работа со структурами данных
get_name = lambda person: person.get('name', 'Unknown')
person = {'name': 'Alice', 'age': 30}
print(get_name(person))  # Alice
```


### 2. Lambda с функциями высшего порядка

#### Продвинутое использование map()

```python
# Преобразование строк
words = ['hello', 'world', 'python']
capitalized = list(map(lambda s: s.capitalize(), words))
print(capitalized)  # ['Hello', 'World', 'Python']

# Работа с кортежами
points = [(1, 2), (3, 4), (5, 6)]
distances = list(map(lambda p: (p[0]**2 + p[1]**2)**0.5, points))
print(distances)  # [2.236..., 5.0, 7.810...]
```


#### Сложная фильтрация с filter()

```python
# Фильтрация по нескольким условиям
numbers = range(1, 21)
filtered = list(filter(lambda x: x % 3 == 0 and x % 2 != 0, numbers))
print(filtered)  # [3, 9, 15]

# Фильтрация объектов
students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 92},
    {'name': 'Charlie', 'grade': 78}
]
top_students = list(filter(lambda s: s['grade'] >= 85, students))
print(top_students)  # [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}]
```


### 3. Сложная сортировка

```python
# Сортировка по нескольким критериям
employees = [
    {'name': 'Alice', 'department': 'IT', 'salary': 70000},
    {'name': 'Bob', 'department': 'HR', 'salary': 65000},
    {'name': 'Charlie', 'department': 'IT', 'salary': 75000}
]

# Сортировка по отделу, затем по зарплате
sorted_employees = sorted(employees, 
                         key=lambda emp: (emp['department'], -emp['salary']))
print(sorted_employees)
```


## Замыкания и области видимости

### Захват переменных из внешней области

```python
def create_multiplier(factor):
    return lambda x: x * factor

double = create_multiplier(2)
triple = create_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15
```


### Ловушка с поздним связыванием

```python
# Проблема
functions = []
for i in range(3):
    functions.append(lambda x: x * i)  # i захватывается по ссылке!

# Все функции используют последнее значение i (2)
for f in functions:
    print(f(10))  # 20, 20, 20

# Решение: явное связывание
functions_fixed = []
for i in range(3):
    functions_fixed.append(lambda x, multiplier=i: x * multiplier)

for f in functions_fixed:
    print(f(10))  # 0, 10, 20
```


## Функциональное программирование с lambda

### Композиция функций

```python
# Создание композиции функций
def compose(f, g):
    return lambda x: f(g(x))

add_one = lambda x: x + 1
multiply_by_two = lambda x: x * 2

# Сначала умножить на 2, потом прибавить 1
composed = compose(add_one, multiply_by_two)
print(composed(5))  # 11
```


### Каррирование

```python
# Каррированная функция сложения
add_curried = lambda x: lambda y: x + y

add_five = add_curried(5)
print(add_five(3))  # 8

# Более сложный пример
multiply_curried = lambda x: lambda y: lambda z: x * y * z
result = multiply_curried(2)(3)(4)
print(result)  # 24
```


## Производительность и оптимизация

### Сравнение производительности

```python
import timeit

# Обычная функция
def square_def(x):
    return x ** 2

# Lambda функция
square_lambda = lambda x: x ** 2

# Тестирование производительности
numbers = list(range(1000000))

time_def = timeit.timeit(lambda: list(map(square_def, numbers)), number=10)
time_lambda = timeit.timeit(lambda: list(map(square_lambda, numbers)), number=10)

print(f"def функция: {time_def:.4f} сек")
print(f"lambda функция: {time_lambda:.4f} сек")
# Разница минимальна
```


## Ограничения и альтернативы

### Что нельзя делать в lambda

```python
# ❌ Нельзя: множественные инструкции
# lambda x: print(x); return x * 2  # SyntaxError

# ❌ Нельзя: присваивания
# lambda x: x = x + 1  # SyntaxError

# ❌ Нельзя: циклы
# lambda x: for i in range(x): print(i)  # SyntaxError
```


### Альтернативы для сложной логики

```python
# Вместо сложной lambda
# lambda x: x if x > 0 else -x if x < 0 else 0

# Лучше использовать обычную функцию
def absolute_value(x):
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0
```


## Практические паттерны для Middle-разработчика

### 1. Обработка данных

```python
# Чистка и преобразование данных
raw_data = ['  Alice  ', '  BOB  ', 'charlie']
cleaned = list(map(lambda s: s.strip().title(), raw_data))
print(cleaned)  # ['Alice', 'Bob', 'Charlie']

# Агрегация данных
from functools import reduce
sales = [100, 200, 150, 300, 250]
total = reduce(lambda acc, x: acc + x, sales, 0)
average = total / len(sales)
print(f"Общие продажи: {total}, Среднее: {average}")
```


### 2. Конфигурация и настройки

```python
# Создание конфигурационных функций
create_validator = lambda min_val, max_val: lambda x: min_val <= x <= max_val

age_validator = create_validator(0, 120)
score_validator = create_validator(0, 100)

print(age_validator(25))    # True
print(score_validator(150)) # False
```


### 3. Декораторы с lambda

```python
# Простой логирующий декоратор
def log_calls(func):
    return lambda *args, **kwargs: (
        print(f"Вызов {func.__name__} с аргументами {args}"),
        func(*args, **kwargs)
    )[1]  # Возвращаем результат функции

@log_calls
def add(a, b):
    return a + b

result = add(3, 5)  # Выведет лог и вернет 8
```


## Лучшие практики для Middle-разработчика

### ✅ Рекомендуется

- Использовать для простых преобразований данных
- Применять с `map`, `filter`, `sorted`, `reduce`
- Создавать фабрики простых функций
- Использовать для коротких callback-функций


### ❌ Не рекомендуется

- Создавать сложную бизнес-логику
- Использовать для функций, которые будут переиспользоваться
- Злоупотреблять вложенностью
- Игнорировать читаемость кода


## Отладка lambda-функций

```python
# Проблема: сложно отлаживать
data = [1, 2, 3, 4, 5]
result = list(filter(lambda x: x % 2 == 0 and x > 2, data))

# Решение: разбить на этапы для отладки
def debug_filter(x):
    is_even = x % 2 == 0
    is_greater_than_two = x > 2
    result = is_even and is_greater_than_two
    print(f"x={x}, even={is_even}, >2={is_greater_than_two}, result={result}")
    return result

result_debug = list(filter(debug_filter, data))
```


## Заключение

Lambda-функции — это мощный инструмент функционального программирования в Python. Для Middle-разработчика важно понимать не только синтаксис, но и знать, когда их использование оправдано. Они отлично подходят для простых преобразований данных и работы с функциями высшего порядка, но не должны заменять обычные функции в случаях, где важны читаемость, отладка и документирование кода.

Ключ к эффективному использованию lambda-функций — это баланс между краткостью и читаемостью кода.

# Анонимные (lambda) функции в Python

## 1. Что такое анонимные функции?

**Анонимные функции** — это функции без имени, которые создаются с помощью ключевого слова `lambda`. В Python их часто называют **lambda-функциями**.

**Синтаксис:**
```python
lambda аргументы: выражение
```
- `lambda` — ключевое слово.
- `аргументы` — список параметров, как у обычной функции.
- `выражение` — одно выражение, результат которого возвращается.

**Пример:**
```python
add = lambda x, y: x + y
print(add(2, 3))  # 5
```

---

## 2. Отличия от обычных функций

| Обычная функция         | Lambda-функция                |
|------------------------|-------------------------------|
| def my_func(x): ...    | lambda x: ...                 |
| Может содержать блоки  | Только одно выражение         |
| Может иметь имя        | Обычно безымянная             |
| Может содержать return | return не пишется, всегда есть|

**Пример:**
```python
def square(x):
    return x * x

square_lambda = lambda x: x * x
```

---

## 3. Где применяются lambda-функции?

- В качестве аргументов функций (`key`, `map`, `filter`, `sorted` и др.)
- Для создания простых функций "на лету"
- В функциональном программировании

### Примеры использования

#### 3.1. В функции `map`
```python
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16]
```

#### 3.2. В функции `filter`
```python
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # [2, 4]
```

#### 3.3. В функции `sorted` с параметром `key`
```python
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)  # ['date', 'apple', 'banana', 'cherry']
```

#### 3.4. В функции `reduce` (из модуля `functools`)
```python
from functools import reduce
numbers = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 24
```

---

## 4. Особенности и ограничения

- Lambda-функция может содержать только **одно выражение** (statement запрещены).
- Не поддерживает аннотацию типов (до Python 3.10).
- Не может содержать сложную логику, циклы, условия (только через тернарный оператор).
- Возвращает результат выражения автоматически.

**Пример с тернарным оператором:**
```python
max_func = lambda x, y: x if x > y else y
print(max_func(10, 5))  # 10
```

---

## 5. Lambda-функции и замыкания

Lambda-функции могут захватывать переменные из внешней области видимости (closure):

```python
def make_incrementor(n):
    return lambda x: x + n

inc5 = make_incrementor(5)
print(inc5(2))  # 7
```

---

## 6. Lambda-функции в качестве return

```python
def power(n):
    return lambda x: x ** n

square = power(2)
cube = power(3)
print(square(4))  # 16
print(cube(2))    # 8
```

---

## 7. Lambda-функции и именованные функции

Lambda-функции часто используются там, где нужна простая функция на короткое время. Для сложной логики лучше использовать `def`.

**Плохо:**
```python
# Сложная логика в lambda — плохо читается!
func = lambda x: x ** 2 if x > 0 else -x + 10 if x < 0 else 0
```

**Лучше:**
```python
def func(x):
    if x > 0:
        return x ** 2
    elif x < 0:
        return -x + 10
    else:
        return 0
```

---

## 8. Lambda-функции и отладка

Lambda-функции анонимны, поэтому их сложнее отлаживать (нет имени, не выводится в traceback). Для сложных случаев используйте именованные функции.

---

## 9. Lambda-функции и аннотации типов (Python 3.10+)

С Python 3.10 можно использовать аннотации типов:

```python
from typing import Callable
f: Callable[[int, int], int] = lambda x, y: x + y
```

---

## 10. Lambda-функции и PEP 8

- Используйте lambda только для простых выражений.
- Не злоупотребляйте, если можно использовать `def` — используйте его.

---

## Кратко: когда использовать lambda-функции?

- Когда нужна простая функция на короткое время (например, для сортировки, фильтрации, преобразования).
- Когда не требуется сложная логика.
- Когда функция используется только в одном месте.

---

## Практические задачи

1. **Отсортировать список кортежей по второму элементу:**
   ```python
   pairs = [(1, 3), (2, 2), (4, 1)]
   sorted_pairs = sorted(pairs, key=lambda x: x[1])
   print(sorted_pairs)  # [(4, 1), (2, 2), (1, 3)]
   ```

2. **Фильтровать строки, начинающиеся с определённой буквы:**
   ```python
   words = ['apple', 'banana', 'cherry', 'avocado']
   a_words = list(filter(lambda w: w.startswith('a'), words))
   print(a_words)  # ['apple', 'avocado']
   ```

3. **Преобразовать список чисел в их строки:**
   ```python
   numbers = [1, 2, 3]
   str_numbers = list(map(lambda x: str(x), numbers))
   print(str_numbers)  # ['1', '2', '3']
   ```

---

## Заключение

Lambda-функции — мощный инструмент Python, который позволяет писать компактный и выразительный код. Однако их следует использовать с умом: для сложной логики предпочтительнее обычные функции. 
