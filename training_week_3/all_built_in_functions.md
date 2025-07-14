# Встроенные функции Python (71 функция)

## 1. Математические функции (7 функций)

1. **abs()** - возвращает абсолютное значение числа
2. **divmod()** - возвращает частное и остаток от деления
3. **max()** - возвращает наибольший элемент
4. **min()** - возвращает наименьший элемент
5. **pow()** - возводит число в степень
6. **round()** - округляет число
7. **sum()** - суммирует элементы итерируемого объекта


## 1. Математические функции (7 функций)

### 1.1 abs()

**Описание:** Возвращает абсолютное значение числа (модуль числа). Работает с целыми числами, числами с плавающей точкой и комплексными числами.

**Пример кода:**

```python
# Для целых чисел
print(abs(-5))        # 5
print(abs(10))        # 10

# Для чисел с плавающей точкой
print(abs(-3.14))     # 3.14

# Для комплексных чисел
print(abs(3 + 4j))    # 5.0
```


### 1.2 divmod()

**Описание:** Возвращает кортеж из частного и остатка от деления двух чисел. Эквивалентно `(a // b, a % b)`.

**Пример кода:**

```python
# Деление целых чисел
result = divmod(17, 5)
print(result)         # (3, 2)

# Деление чисел с плавающей точкой
result = divmod(10.5, 3.2)
print(result)         # (3.0, 0.8999999999999995)

# Распаковка результата
quotient, remainder = divmod(23, 7)
print(f"Частное: {quotient}, Остаток: {remainder}")  # Частное: 3, Остаток: 2
```


### 1.3 max()

**Описание:** Возвращает наибольший элемент из итерируемого объекта или наибольший из переданных аргументов. Поддерживает параметр `key` для кастомной функции сравнения.

**Пример кода:**

```python
# Максимум из нескольких аргументов
print(max(1, 5, 3, 9, 2))     # 9

# Максимум из списка
numbers = [10, 45, 22, 89, 21]
print(max(numbers))           # 89

# Максимум строк по длине
words = ['python', 'java', 'javascript', 'go']
print(max(words, key=len))    # 'javascript'

# Максимум с default значением для пустого итератора
print(max([], default=0))     # 0
```


### 1.4 min()

**Описание:** Возвращает наименьший элемент из итерируемого объекта или наименьший из переданных аргументов. Поддерживает параметр `key` для кастомной функции сравнения.

**Пример кода:**

```python
# Минимум из нескольких аргументов
print(min(1, 5, 3, 9, 2))     # 1

# Минимум из списка
numbers = [10, 45, 22, 89, 21]
print(min(numbers))           # 10

# Минимум строк по длине
words = ['python', 'java', 'javascript', 'go']
print(min(words, key=len))    # 'go'

# Минимум с default значением для пустого итератора
print(min([], default=float('inf')))  # inf
```


### 1.5 pow()

**Описание:** Возводит число в степень. Может принимать третий аргумент для вычисления остатка от деления результата на это число (модульное возведение в степень).

**Пример кода:**

```python
# Обычное возведение в степень
print(pow(2, 3))      # 8
print(pow(5, 2))      # 25

# Возведение в дробную степень
print(pow(9, 0.5))    # 3.0

# Модульное возведение в степень
print(pow(2, 10, 1000))  # 24 (2^10 % 1000)

# Отрицательная степень
print(pow(2, -3))     # 0.125
```


### 1.6 round()

**Описание:** Округляет число до указанного количества знаков после запятой. По умолчанию округляет до ближайшего целого числа.

**Пример кода:**

```python
# Округление до целого
print(round(3.7))        # 4
print(round(3.2))        # 3

# Округление до определенного количества знаков
print(round(3.14159, 2)) # 3.14
print(round(3.14159, 4)) # 3.1416

# Округление больших чисел
print(round(1234.5678, 1))  # 1234.6

# Округление до десятков, сотен и т.д.
print(round(1234, -1))   # 1230
print(round(1234, -2))   # 1200
```


### 1.7 sum()

**Описание:** Суммирует элементы итерируемого объекта. Может принимать начальное значение как второй аргумент.

**Пример кода:**

```python
# Сумма списка чисел
numbers = [1, 2, 3, 4, 5]
print(sum(numbers))      # 15

# Сумма с начальным значением
print(sum(numbers, 10))  # 25

# Сумма кортежа
print(sum((1.5, 2.5, 3.0)))  # 7.0

# Сумма генератора
print(sum(x**2 for x in range(5)))  # 30

# Сумма пустого итератора с начальным значением
print(sum([], 100))      # 100
```




## 2. Функции для работы с типами данных (8 функций)

8. **bool()** - преобразует значение в булевый тип
9. **int()** - преобразует в целое число
10. **float()** - преобразует в число с плавающей точкой
11. **complex()** - создает комплексное число
12. **str()** - преобразует в строку
13. **bytes()** - создает объект bytes
14. **bytearray()** - создает изменяемый массив байтов
15. **memoryview()** - создает представление памяти


### 2.1 bool()

**Описание:** Преобразует значение в булевый тип (True или False). Возвращает False для пустых коллекций, None, 0 и пустых строк.

**Пример кода:**

```python
# Преобразование чисел
print(bool(1))       # True
print(bool(0))       # False
print(bool(-5))      # True

# Преобразование строк
print(bool("hello")) # True
print(bool(""))      # False

# Преобразование коллекций
print(bool([1, 2]))  # True
print(bool([]))      # False
print(bool(None))    # False
```


### 2.2 int()

**Описание:** Преобразует число или строку в целое число. Поддерживает различные системы счисления через параметр base.

**Пример кода:**

```python
# Преобразование из строки
print(int("123"))     # 123
print(int("42"))      # 42

# Преобразование из числа с плавающей точкой
print(int(3.14))      # 3
print(int(9.99))      # 9

# Различные системы счисления
print(int("1010", 2))  # 10 (двоичная)
print(int("FF", 16))   # 255 (шестнадцатеричная)
print(int("77", 8))    # 63 (восьмеричная)
```


### 2.3 float()

**Описание:** Преобразует число или строку в число с плавающей точкой.

**Пример кода:**

```python
# Преобразование из строки
print(float("3.14"))    # 3.14
print(float("123"))     # 123.0

# Преобразование из целого числа
print(float(42))        # 42.0

# Специальные значения
print(float("inf"))     # inf
print(float("-inf"))    # -inf
print(float("nan"))     # nan
```


### 2.4 complex()

**Описание:** Создает комплексное число из действительной и мнимой частей.

**Пример кода:**

```python
# Создание комплексного числа
print(complex(3, 4))      # (3+4j)
print(complex(2))         # (2+0j)
print(complex(0, 5))      # 5j

# Из строки
print(complex("3+4j"))    # (3+4j)
print(complex("5j"))      # 5j

# Операции с комплексными числами
z = complex(1, 2)
print(z.real)             # 1.0
print(z.imag)             # 2.0
```


### 2.5 str()

**Описание:** Преобразует объект в строковое представление.

**Пример кода:**

```python
# Преобразование чисел
print(str(123))         # "123"
print(str(3.14))        # "3.14"

# Преобразование коллекций
print(str([1, 2, 3]))   # "[1, 2, 3]"
print(str({'a': 1}))    # "{'a': 1}"

# Преобразование булевых значений
print(str(True))        # "True"
print(str(False))       # "False"
```


### 2.6 bytes()

**Описание:** Создает неизменяемый объект bytes из строки, списка целых чисел или указанного размера.

**Пример кода:**

```python
# Из строки с указанием кодировки
print(bytes("hello", "utf-8"))    # b'hello'
print(bytes("привет", "utf-8"))   # b'\xd0\xbf\xd1\x80\xd0\xb8\xd0\xb2\xd0\xb5\xd1\x82'

# Из списка целых чисел
print(bytes([65, 66, 67]))        # b'ABC'

# Создание пустого объекта указанного размера
print(bytes(5))                   # b'\x00\x00\x00\x00\x00'
```


### 2.7 bytearray()

**Описание:** Создает изменяемый массив байтов. Аналогичен bytes(), но позволяет изменять содержимое.

**Пример кода:**

```python
# Создание из строки
ba = bytearray("hello", "utf-8")
print(ba)                # bytearray(b'hello')

# Изменение содержимого
ba[^0] = 72  # ASCII код 'H'
print(ba)                # bytearray(b'Hello')

# Из списка
ba2 = bytearray([65, 66, 67])
ba2.append(68)
print(ba2)               # bytearray(b'ABCD')
```


### 2.8 memoryview()

**Описание:** Создает объект представления памяти, который позволяет работать с данными объекта без копирования.

**Пример кода:**

```python
# Создание из bytes
data = b"hello world"
mv = memoryview(data)
print(mv[^0])             # 104 (ASCII код 'h')
print(mv[0:5])           # <memory at 0x...>
print(mv[0:5].tobytes()) # b'hello'

# Создание из bytearray
ba = bytearray(b"python")
mv2 = memoryview(ba)
mv2[^0] = 80  # ASCII код 'P'
print(ba)                # bytearray(b'Python')
```


## 3. Функции для работы с коллекциями (6 функций)

16. **list()** - создает список
17. **tuple()** - создает кортеж
18. **set()** - создает множество
19. **frozenset()** - создает неизменяемое множество
20. **dict()** - создает словарь
21. **range()** - создает последовательность чисел


### 3.1 list()

**Описание:** Создает список из итерируемого объекта или пустой список.

**Пример кода:**

```python
# Создание пустого списка
empty_list = list()
print(empty_list)        # []

# Из строки
print(list("hello"))     # ['h', 'e', 'l', 'l', 'o']

# Из кортежа
print(list((1, 2, 3)))   # [1, 2, 3]

# Из множества
print(list({3, 1, 2}))   # [1, 2, 3] (порядок может отличаться)

# Из range
print(list(range(5)))    # [0, 1, 2, 3, 4]
```


### 3.2 tuple()

**Описание:** Создает кортеж из итерируемого объекта или пустой кортеж.

**Пример кода:**

```python
# Создание пустого кортежа
empty_tuple = tuple()
print(empty_tuple)       # ()

# Из списка
print(tuple([1, 2, 3]))  # (1, 2, 3)

# Из строки
print(tuple("abc"))      # ('a', 'b', 'c')

# Из множества
print(tuple({1, 2, 3}))  # (1, 2, 3) (порядок может отличаться)
```


### 3.3 set()

**Описание:** Создает множество из итерируемого объекта или пустое множество. Удаляет дубликаты.

**Пример кода:**

```python
# Создание пустого множества
empty_set = set()
print(empty_set)         # set()

# Из списка с дубликатами
print(set([1, 2, 2, 3, 3, 3]))  # {1, 2, 3}

# Из строки
print(set("hello"))      # {'h', 'e', 'l', 'o'}

# Операции с множествами
set1 = set([1, 2, 3])
set2 = set([3, 4, 5])
print(set1 | set2)       # {1, 2, 3, 4, 5} (объединение)
print(set1 & set2)       # {3} (пересечение)
```


### 3.4 frozenset()

**Описание:** Создает неизменяемое множество из итерируемого объекта.

**Пример кода:**

```python
# Создание из списка
fs = frozenset([1, 2, 3, 2, 1])
print(fs)                # frozenset({1, 2, 3})

# Неизменяемость
# fs.add(4)  # Вызовет AttributeError

# Использование как ключ в словаре
dict_with_frozenset = {frozenset([1, 2]): "value"}
print(dict_with_frozenset)  # {frozenset({1, 2}): 'value'}

# Операции
fs1 = frozenset([1, 2, 3])
fs2 = frozenset([3, 4, 5])
print(fs1 | fs2)         # frozenset({1, 2, 3, 4, 5})
```


### 3.5 dict()

**Описание:** Создает словарь из различных источников данных или пустой словарь.

**Пример кода:**

```python
# Создание пустого словаря
empty_dict = dict()
print(empty_dict)        # {}

# Из списка кортежей
print(dict([('a', 1), ('b', 2)]))  # {'a': 1, 'b': 2}

# Из именованных аргументов
print(dict(name="John", age=30))    # {'name': 'John', 'age': 30}

# Из zip
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(dict(zip(keys, values)))      # {'a': 1, 'b': 2, 'c': 3}
```


### 3.6 range()

**Описание:** Создает последовательность чисел. Поддерживает start, stop и step параметры.

**Пример кода:**

```python
# Только stop
print(list(range(5)))           # [0, 1, 2, 3, 4]

# Start и stop
print(list(range(2, 8)))        # [2, 3, 4, 5, 6, 7]

# Start, stop и step
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]

# Отрицательный step
print(list(range(10, 0, -2)))   # [10, 8, 6, 4, 2]

# Использование в циклах
for i in range(3):
    print(f"Итерация {i}")
```


## 4. Функции для работы с итераторами (9 функций)

22. **iter()** - создает итератор
23. **next()** - получает следующий элемент итератора
24. **enumerate()** - создает пронумерованный итератор
25. **zip()** - объединяет несколько итераторов
26. **map()** - применяет функцию к элементам итератора
27. **filter()** - фильтрует элементы итератора
28. **sorted()** - возвращает отсортированный список
29. **reversed()** - возвращает обращенный итератор
30. **slice()** - создает объект среза



### 4.1 iter()

**Описание:** Создает итератор из итерируемого объекта или вызываемого объекта.

**Пример кода:**

```python
# Из списка
my_list = [1, 2, 3]
iterator = iter(my_list)
print(next(iterator))    # 1
print(next(iterator))    # 2

# Из строки
str_iter = iter("abc")
print(next(str_iter))    # 'a'

# С sentinel значением
import random
random.seed(42)
iterator = iter(lambda: random.randint(1, 6), 6)
for value in iterator:
    print(value)  # Печатает случайные числа до первой 6
```


### 4.2 next()

**Описание:** Получает следующий элемент из итератора. Может принимать значение по умолчанию.

**Пример кода:**

```python
# Базовое использование
my_iter = iter([1, 2, 3])
print(next(my_iter))     # 1
print(next(my_iter))     # 2
print(next(my_iter))     # 3

# С значением по умолчанию
print(next(my_iter, "Конец"))  # "Конец"

# Без значения по умолчанию вызовет StopIteration
# print(next(my_iter))   # StopIteration
```


### 4.3 enumerate()

**Описание:** Создает пронумерованный итератор, возвращающий кортежи (индекс, значение).

**Пример кода:**

```python
# Базовое использование
fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
# 0: apple
# 1: banana
# 2: orange

# С начальным значением
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}: {fruit}")
# 1: apple
# 2: banana
# 3: orange

# Преобразование в список
print(list(enumerate("abc")))  # [(0, 'a'), (1, 'b'), (2, 'c')]
```


### 4.4 zip()

**Описание:** Объединяет несколько итераторов в один, возвращая кортежи соответствующих элементов.

**Пример кода:**

```python
# Объединение двух списков
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Объединение трех списков
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [10, 20, 30]
print(list(zip(list1, list2, list3)))  # [(1, 'a', 10), (2, 'b', 20), (3, 'c', 30)]

# Разная длина - останавливается на самом коротком
print(list(zip([1, 2, 3, 4], ['a', 'b'])))  # [(1, 'a'), (2, 'b')]
```


### 4.5 map()

**Описание:** Применяет функцию к каждому элементу итерируемого объекта и возвращает итератор результатов.

**Пример кода:**

```python
# Применение функции к списку
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x**2, numbers)
print(list(squared))     # [1, 4, 9, 16, 25]

# Использование встроенной функции
strings = ['1', '2', '3', '4']
integers = map(int, strings)
print(list(integers))    # [1, 2, 3, 4]

# Несколько итераторов
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)
print(list(result))      # [5, 7, 9]
```


### 4.6 filter()

**Описание:** Фильтрует элементы итерируемого объекта с помощью функции-предиката.

**Пример кода:**

```python
# Фильтрация четных чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # [2, 4, 6, 8, 10]

# Фильтрация строк по длине
words = ['python', 'java', 'go', 'javascript', 'rust']
long_words = filter(lambda word: len(word) > 4, words)
print(list(long_words))    # ['python', 'javascript']

# Фильтрация истинных значений (None как предикат)
mixed = [0, 1, False, True, '', 'hello', [], [1, 2]]
truthy = filter(None, mixed)
print(list(truthy))        # [1, True, 'hello', [1, 2]]
```


### 4.7 sorted()

**Описание:** Возвращает новый отсортированный список из элементов итерируемого объекта.

**Пример кода:**

```python
# Сортировка чисел
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(sorted(numbers))     # [1, 1, 2, 3, 4, 5, 6, 9]

# Обратная сортировка
print(sorted(numbers, reverse=True))  # [9, 6, 5, 4, 3, 2, 1, 1]

# Сортировка строк по длине
words = ['python', 'java', 'go', 'javascript']
print(sorted(words, key=len))  # ['go', 'java', 'python', 'javascript']

# Сортировка кортежей по второму элементу
students = [('Alice', 85), ('Bob', 90), ('Charlie', 78)]
print(sorted(students, key=lambda x: x[^1]))  # [('Charlie', 78), ('Alice', 85), ('Bob', 90)]
```


### 4.8 reversed()

**Описание:** Возвращает обращенный итератор для последовательности.

**Пример кода:**

```python
# Обращение списка
numbers = [1, 2, 3, 4, 5]
print(list(reversed(numbers)))  # [5, 4, 3, 2, 1]

# Обращение строки
print(list(reversed("hello")))  # ['o', 'l', 'l', 'e', 'h']

# Обращение кортежа
print(tuple(reversed((1, 2, 3))))  # (3, 2, 1)

# Использование в цикле
for item in reversed(['a', 'b', 'c']):
    print(item)  # c, b, a
```


### 4.9 slice()

**Описание:** 
Функция `slice()` в Python — это встроенный инструмент для создания объекта среза, который можно применять к последовательностям: строкам, спискам, кортежам и другим индексируемым коллекциям. Она особенно полезна, когда необходимо динамически формировать диапазоны, а не использовать литеральный синтаксис срезов (`[:]`).

---

### Основной синтаксис

```python
slice(start, stop, step)
```

- `start` — индекс, с которого начинается срез (включительно).
- `stop` — индекс, на котором срез заканчивается (не включается).
- `step` — шаг, с которым выбираются элементы.

---

### Пример использования

```python
s = 'abcdefg'
sl = slice(2, 6)     # от индекса 2 до 6 (не включая 6)
print(s[sl])         # 'cdef'
```

Также можно указать `step`:

```python
sl = slice(1, 7, 2)
print(s[sl])         # 'bdf'
```

---

### Применение к спискам

```python
lst = [10, 20, 30, 40, 50, 60]
sl = slice(1, 5)
print(lst[sl])       # [20, 30, 40, 50]
```

---

### 🔧 Комбинация со `range()` и `map()`

Slice удобно использовать совместно с `map()` или `filter()` при работе с частями данных:

```python
data = list(range(20))
sl = slice(5, 15, 2)
filtered = data[sl]
print(filtered)      # [5, 7, 9, 11, 13]
```

---

### Сравнение с литеральным срезом `[:]`

```python
s = 'abcdefg'
print(s[2:6])        # литеральный
print(s[slice(2,6)]) # эквивалент через slice()
```

Функция `slice()` особенно полезна, когда:
- срез нужно передавать как аргумент функции;
- срез формируется динамически;
- требуется более гибкое управление.

---

**Пример кода:**

```python
# Создание объекта среза
s = slice(1, 5, 2)
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[s])        # [1, 3]

# Эквивалентно
print(my_list[1:5:2])    # [1, 3]

# Различные параметры
s1 = slice(3)            # slice(None, 3, None)
s2 = slice(2, 8)         # slice(2, 8, None)
s3 = slice(1, 10, 3)     # slice(1, 10, 3)

print(my_list[s1])       # [0, 1, 2]
print(my_list[s2])       # [2, 3, 4, 5, 6, 7]
print(my_list[s3])       # [1, 4, 7]
```


## 5. Функции для работы с объектами и атрибутами (10 функций)

31. **getattr()** - получает атрибут объекта
32. **setattr()** - устанавливает атрибут объекта
33. **delattr()** - удаляет атрибут объекта
34. **hasattr()** - проверяет наличие атрибута
35. **dir()** - возвращает список атрибутов объекта
36. **vars()** - возвращает словарь атрибутов объекта
37. **type()** - возвращает тип объекта
38. **isinstance()** - проверяет принадлежность к типу
39. **issubclass()** - проверяет наследование классов
40. **object()** - создает базовый объект



### 5.1 getattr()

**Описание:** Получает значение атрибута объекта по имени. Может возвращать значение по умолчанию, если атрибут не найден.

**Пример кода:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

# Получение существующего атрибута
print(getattr(person, 'name'))     # Alice
print(getattr(person, 'age'))      # 30

# Получение несуществующего атрибута с значением по умолчанию
print(getattr(person, 'salary', 0))  # 0

# Без значения по умолчанию вызовет AttributeError
# print(getattr(person, 'salary'))  # AttributeError
```


### 5.2 setattr()

**Описание:** Устанавливает значение атрибута объекта. Создает атрибут, если он не существует.

**Пример кода:**

```python
class Person:
    def __init__(self, name):
        self.name = name

person = Person("Bob")

# Установка нового атрибута
setattr(person, 'age', 25)
print(person.age)        # 25

# Изменение существующего атрибута
setattr(person, 'name', 'Robert')
print(person.name)       # Robert

# Динамическое создание атрибутов
attributes = {'salary': 50000, 'department': 'IT'}
for attr, value in attributes.items():
    setattr(person, attr, value)

print(person.salary)     # 50000
print(person.department) # IT
```


### 5.3 delattr()

**Описание:** Удаляет атрибут объекта по имени.

**Пример кода:**

```python
class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

person = Person("Charlie", 35, 60000)

print(hasattr(person, 'salary'))  # True
delattr(person, 'salary')
print(hasattr(person, 'salary'))  # False

# Попытка удалить несуществующий атрибут вызовет AttributeError
# delattr(person, 'salary')  # AttributeError

# Эквивалентно del person.salary
```


### 5.4 hasattr()

**Описание:** Проверяет, есть ли у объекта атрибут с указанным именем.

**Пример кода:**

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        return "Engine started"

car = Car("Toyota", "Camry")

# Проверка атрибутов
print(hasattr(car, 'brand'))    # True
print(hasattr(car, 'model'))    # True
print(hasattr(car, 'color'))    # False

# Проверка методов
print(hasattr(car, 'start'))    # True
print(hasattr(car, 'stop'))     # False

# Условное использование атрибута
if hasattr(car, 'color'):
    print(car.color)
else:
    print("Цвет не указан")
```


### 5.5 dir()

**Описание:** Возвращает список имен атрибутов и методов объекта.

**Пример кода:**

```python
class Sample:
    def __init__(self):
        self.attribute = "value"
    
    def method(self):
        pass

obj = Sample()

# Атрибуты объекта
print(dir(obj))  # Список всех атрибутов и методов

# Атрибуты встроенных типов
print(dir(str))  # Методы строк
print(dir([]))   # Методы списков

# Без аргументов - локальные имена
x = 10
y = 20
print(dir())     # Включает x, y и другие локальные имена
```


### 5.6 vars()

**Описание:** Возвращает словарь атрибутов объекта (__dict__). Без аргументов возвращает локальные переменные.

**Пример кода:**

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("David", 28)

# Словарь атрибутов объекта
print(vars(person))      # {'name': 'David', 'age': 28}

# Изменение через vars()
vars(person)['salary'] = 45000
print(person.salary)     # 45000

# Без аргументов (в функции)
def example():
    local_var = "test"
    return vars()

print(example())         # {'local_var': 'test'}
```


### 5.7 type()

**Описание:** Возвращает тип объекта или создает новый тип класса.

**Пример кода:**

```python
# Определение типа объекта
print(type(42))          # <class 'int'>
print(type("hello"))     # <class 'str'>
print(type([1, 2, 3]))   # <class 'list'>
print(type({}))          # <class 'dict'>

# Сравнение типов
x = 10
if type(x) == int:
    print("x is an integer")

# Создание нового класса динамически
def init_method(self, value):
    self.value = value

MyClass = type('MyClass', (object,), {
    '__init__': init_method,
    'class_var': 'Hello'
})

obj = MyClass(42)
print(obj.value)         # 42
print(obj.class_var)     # Hello
```


### 5.8 isinstance()

**Описание:** Проверяет, является ли объект экземпляром указанного класса или его подкласса.

**Пример кода:**

```python
# Проверка встроенных типов
print(isinstance(42, int))        # True
print(isinstance("hello", str))   # True
print(isinstance([1, 2], list))   # True

# Проверка нескольких типов
print(isinstance(42, (int, float)))     # True
print(isinstance(3.14, (int, float)))   # True
print(isinstance("test", (int, float))) # False

# Пользовательские классы
class Animal:
    pass

class Dog(Animal):
    pass

dog = Dog()
print(isinstance(dog, Dog))      # True
print(isinstance(dog, Animal))   # True (наследование)
print(isinstance(dog, str))      # False
```


### 5.9 issubclass()

**Описание:** Проверяет, является ли класс подклассом другого класса.

**Пример кода:**

```python
class Animal:
    pass

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

# Проверка наследования
print(issubclass(Dog, Animal))    # True
print(issubclass(Dog, Mammal))    # True
print(issubclass(Mammal, Animal)) # True
print(issubclass(Animal, Dog))    # False

# Класс является подклассом самого себя
print(issubclass(Dog, Dog))       # True

# Проверка нескольких классов
print(issubclass(Dog, (Animal, str)))  # True
```


### 5.10 object()

**Описание:** Создает новый базовый объект. Это базовый класс для всех классов в Python.

**Пример кода:**

```python
# Создание базового объекта
obj = object()
print(type(obj))         # <class 'object'>

# У объекта есть базовые методы
print(hasattr(obj, '__str__'))    # True
print(hasattr(obj, '__repr__'))   # True

# Использование как базовый класс
class MyClass(object):  # Явное наследование (необязательно в Python 3)
    def __init__(self, value):
        self.value = value

# Все классы неявно наследуют от object
class AnotherClass:
    pass

print(issubclass(AnotherClass, object))  # True
```


## 6. Функции для работы со строками и символами (5 функций)

41. **chr()** - преобразует код Unicode в символ
42. **ord()** - возвращает код Unicode символа
43. **ascii()** - возвращает ASCII-представление объекта
44. **repr()** - возвращает строковое представление объекта
45. **format()** - форматирует значение


### 6.1 chr()

**Описание:** Преобразует код Unicode в соответствующий символ.

**Пример кода:**

```python
# ASCII символы
print(chr(65))           # A
print(chr(97))           # a
print(chr(48))           # 0

# Unicode символы
print(chr(8364))         # € (евро)
print(chr(9829))         # ♥ (сердце)
print(chr(128512))       # 😀 (смайлик)

# Создание строки из кодов
codes = [72, 101, 108, 108, 111]
text = ''.join(chr(code) for code in codes)
print(text)              # Hello
```


### 6.2 ord()

**Описание:** Возвращает код Unicode символа.

**Пример кода:**

```python
# ASCII символы
print(ord('A'))          # 65
print(ord('a'))          # 97
print(ord('0'))          # 48

# Unicode символы
print(ord('€'))          # 8364
print(ord('♥'))          # 9829
print(ord('😀'))         # 128512

# Обработка строки
text = "Hello"
codes = [ord(char) for char in text]
print(codes)             # [72, 101, 108, 108, 111]

# Обратное преобразование
restored = ''.join(chr(code) for code in codes)
print(restored)          # Hello
```


### 6.3 ascii()

**Описание:** Возвращает строку с печатным представлением объекта, экранируя не-ASCII символы.

**Пример кода:**

```python
# Строки с не-ASCII символами
print(ascii("Hello"))         # 'Hello'
print(ascii("Привет"))        # '\u041f\u0440\u0438\u0432\u0435\u0442'
print(ascii("café"))          # 'caf\xe9'

# Различные объекты
print(ascii(['hello', 'мир']))  # ['hello', '\u043c\u0438\u0440']
print(ascii({'key': 'значение'}))  # {'key': '\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435'}

# Сравнение с repr()
text = "café"
print(repr(text))             # 'café'
print(ascii(text))            # 'caf\xe9'
```


### 6.4 repr()

**Описание:** Возвращает строковое представление объекта, которое может быть использовано для воссоздания объекта.

**Пример кода:**

```python
# Базовые типы
print(repr(42))              # 42
print(repr("hello"))         # 'hello'
print(repr([1, 2, 3]))       # [1, 2, 3]

# Разница между str() и repr()
text = "hello\nworld"
print(str(text))             # hello
                             # world
print(repr(text))            # 'hello\nworld'

# Пользовательский класс
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(3, 4)
print(repr(p))               # Point(3, 4)
```


### 6.5 format()

**Описание:** Форматирует значение согласно спецификации формата.

**Пример кода:**

```python
# Базовое форматирование
print(format(42))            # 42
print(format(3.14159, '.2f'))  # 3.14
print(format(1000, ','))     # 1,000

# Различные форматы чисел
print(format(255, 'b'))      # 11111111 (двоичный)
print(format(255, 'o'))      # 377 (восьмеричный)
print(format(255, 'x'))      # ff (шестнадцатеричный)
print(format(255, 'X'))      # FF (шестнадцатеричный верхний регистр)

# Форматирование строк
print(format("hello", '>10'))    # "     hello"
print(format("hello", '<10'))    # "hello     "
print(format("hello", '^10'))    # "  hello   "

# Пользовательское форматирование
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __format__(self, format_spec):
        if format_spec == 'full':
            return f"{self.name} ({self.age} years old)"
        return f"{self.name}"

person = Person("Alice", 30)
print(format(person))            # Alice
print(format(person, 'full'))    # Alice (30 years old)
```


## 7. Функции для работы с числовыми системами (3 функции)

46. **bin()** - преобразует в двоичную систему
47. **oct()** - преобразует в восьмеричную систему
48. **hex()** - преобразует в шестнадцатеричную систему

### 7.1 bin()

**Описание:** Преобразует целое число в двоичную строку с префиксом '0b'.

**Пример кода:**

```python
# Положительные числа
print(bin(10))           # 0b1010
print(bin(255))          # 0b11111111
print(bin(1))            # 0b1

# Отрицательные числа
print(bin(-10))          # -0b1010
print(bin(-1))           # -0b1

# Удаление префикса
number = 42
binary = bin(number)[2:]  # Убираем '0b'
print(binary)            # 101010

# Форматирование с заполнением нулями
print(bin(5)[2:].zfill(8))  # 00000101
```


### 7.2 oct()

**Описание:** Преобразует целое число в восьмеричную строку с префиксом '0o'.

**Пример кода:**

```python
# Положительные числа
print(oct(8))            # 0o10
print(oct(64))           # 0o100
print(oct(255))          # 0o377

# Отрицательные числа
print(oct(-8))           # -0o10

# Удаление префикса
number = 100
octal = oct(number)[2:]  # Убираем '0o'
print(octal)             # 144

# Обратное преобразование
print(int('144', 8))     # 100
```


### 7.3 hex()

**Описание:** Преобразует целое число в шестнадцатеричную строку с префиксом '0x'.

**Пример кода:**

```python
# Положительные числа
print(hex(16))           # 0x10
print(hex(255))          # 0xff
print(hex(4095))         # 0xfff

# Отрицательные числа
print(hex(-16))          # -0x10

# Удаление префикса
number = 255
hexadecimal = hex(number)[2:]  # Убираем '0x'
print(hexadecimal)       # ff

# Верхний регистр
print(hex(255).upper())  # 0XFF
print(hex(255)[2:].upper())  # FF

# Обратное преобразование
print(int('ff', 16))     # 255
```


## 8. Логические функции (2 функции)

49. **all()** - возвращает True, если все элементы истинны
50. **any()** - возвращает True, если хотя бы один элемент истинен


### 8.1 all()

**Описание:** Возвращает True, если все элементы итерируемого объекта истинны (или если итератор пуст).

**Пример кода:**

```python
# Все элементы истинны
print(all([True, True, True]))     # True
print(all([1, 2, 3]))              # True
print(all(['a', 'b', 'c']))        # True

# Есть ложные элементы
print(all([True, False, True]))    # False
print(all([1, 0, 3]))              # False
print(all(['a', '', 'c']))         # False

# Пустой итератор
print(all([]))                     # True
print(all(()))                     # True

# Практическое применение
numbers = [2, 4, 6, 8, 10]
print(all(n % 2 == 0 for n in numbers))  # True (все четные)

words = ['hello', 'world', 'python']
print(all(len(word) > 3 for word in words))  # True (все длиннее 3 символов)
```


### 8.2 any()

**Описание:** Возвращает True, если хотя бы один элемент итерируемого объекта истинен.

**Пример кода:**

```python
# Есть истинные элементы
print(any([False, True, False]))   # True
print(any([0, 1, 0]))              # True
print(any(['', 'hello', '']))      # True

# Все элементы ложны
print(any([False, False, False]))  # False
print(any([0, 0, 0]))              # False
print(any(['', '', '']))           # False

# Пустой итератор
print(any([]))                     # False
print(any(()))                     # False

# Практическое применение
numbers = [1, 3, 5, 7, 8]
print(any(n % 2 == 0 for n in numbers))  # True (есть четные)

words = ['hi', 'a', 'hello']
print(any(len(word) > 5 for word in words))  # False (нет слов длиннее 5)
```


## 9. Функции для работы с кодом (3 функции)

51. **eval()** - выполняет выражение Python
52. **exec()** - выполняет код Python
53. **compile()** - компилирует код в объект


### 9.1 eval()

**Описание:** Выполняет строку как выражение Python и возвращает результат.

**Пример кода:**

```python
# Математические выражения
print(eval("2 + 3"))             # 5
print(eval("10 * 5"))            # 50
print(eval("2 ** 8"))            # 256

# Строковые выражения
print(eval("'hello' + ' world'"))  # hello world
print(eval("len('python')"))       # 6

# Использование переменных
x = 10
y = 20
print(eval("x + y"))             # 30

# С глобальными и локальными переменными
globals_dict = {'x': 5}
locals_dict = {'y': 3}
print(eval("x * y", globals_dict, locals_dict))  # 15

# ВНИМАНИЕ: eval() может быть опасным!
# Никогда не используйте с недоверенным вводом
# eval("__import__('os').system('ls')")  # Опасно!
```


### 9.2 exec()

**Описание:** Выполняет код Python. В отличие от eval(), может выполнять statements (присваивания, циклы, функции).

**Пример кода:**

```python
# Выполнение простого кода
exec("print('Hello from exec!')")  # Hello from exec!

# Присваивание переменных
code = """
x = 10
y = 20
result = x + y
print(f'Result: {result}')
"""
exec(code)  # Result: 30

# Определение функции
function_code = """
def greet(name):
    return f'Hello, {name}!'

message = greet('Alice')
print(message)
"""
exec(function_code)  # Hello, Alice!

# С пространством имен
namespace = {}
exec("x = 42; y = x * 2", namespace)
print(namespace['y'])  # 84

# Выполнение цикла
loop_code = """
for i in range(3):
    print(f'Iteration {i}')
"""
exec(loop_code)
```


### 9.3 compile()

**Описание:** Компилирует строку в объект кода, который может быть выполнен с помощью exec() или eval().

**Пример кода:**

```python
# Компиляция выражения
expr_code = compile("2 + 3", "<string>", "eval")
result = eval(expr_code)
print(result)  # 5

# Компиляция statement
stmt_code = compile("print('Hello, World!')", "<string>", "exec")
exec(stmt_code)  # Hello, World!

# Компиляция многострочного кода
multi_code = """
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
"""
compiled = compile(multi_code, "<string>", "exec")
exec(compiled)  # 120

# Режим 'single' для интерактивного режима
single_code = compile("x = 42", "<string>", "single")
exec(single_code)
print(x)  # 42

# Проверка синтаксиса
try:
    compile("if True print('test')", "<string>", "exec")
except SyntaxError as e:
    print(f"Syntax error: {e}")
```


## 10. Служебные функции (6 функций)

54. **id()** - возвращает идентификатор объекта
55. **hash()** - возвращает хеш-значение объекта
56. **len()** - возвращает длину объекта
57. **callable()** - проверяет, является ли объект вызываемым
58. **super()** - обеспечивает доступ к родительскому классу
59. **property()** - создает свойство класса

### 10.1 id()

**Описание:** Возвращает уникальный идентификатор объекта (адрес в памяти).

**Пример кода:**

```python
# Идентификаторы различных объектов
a = 42
b = 42
print(id(a))  # Например: 140712345678912
print(id(b))  # Тот же ID для небольших чисел (кэширование)

# Разные объекты
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(id(list1))  # Например: 140712345678976
print(id(list2))  # Другой ID

# Проверка идентичности
print(a is b)      # True (тот же объект)
print(list1 is list2)  # False (разные объекты)

# Изменение объекта не меняет ID
original_id = id(list1)
list1.append(4)
print(id(list1) == original_id)  # True
```


### 10.2 hash()

**Описание:** Возвращает хеш-значение объекта (если он хешируемый).

**Пример кода:**

```python
# Хешируемые объекты
print(hash(42))          # Например: 42
print(hash("hello"))     # Например: 2314058222102390712
print(hash((1, 2, 3)))   # Например: 2528502973977326415

# Одинаковые объекты имеют одинаковый хеш
print(hash("test") == hash("test"))  # True

# Нехешируемые объекты
try:
    print(hash([1, 2, 3]))  # TypeError: unhashable type: 'list'
except TypeError as e:
    print(f"Error: {e}")

# Использование в множествах и словарях
hashable_items = {1, "hello", (1, 2), frozenset([3, 4])}
print(hashable_items)

# Пользовательский класс
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

p1 = Point(1, 2)
p2 = Point(1, 2)
print(hash(p1) == hash(p2))  # True
```


### 10.3 len()

**Описание:** Возвращает количество элементов в объекте (длину).

**Пример кода:**

```python
# Строки
print(len("hello"))      # 5
print(len(""))           # 0
print(len("привет"))     # 6

# Списки и кортежи
print(len([1, 2, 3, 4]))    # 4
print(len((1, 2)))          # 2
print(len([]))              # 0

# Словари и множества
print(len({'a': 1, 'b': 2}))  # 2
print(len({1, 2, 3, 2}))      # 3 (дубликаты удаляются)

# Пользовательский класс
class MyCollection:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)

collection = MyCollection([1, 2, 3, 4, 5])
print(len(collection))    # 5
```


### 10.4 callable()

**Описание:** Проверяет, является ли объект вызываемым (можно ли его вызвать как функцию).

**Пример кода:**

```python
# Функции
def my_function():
    return "Hello"

print(callable(my_function))  # True

# Встроенные функции
print(callable(len))          # True
print(callable(print))        # True

# Классы
class MyClass:
    def __call__(self):
        return "Called!"

print(callable(MyClass))      # True (конструктор)

obj = MyClass()
print(callable(obj))          # True (имеет __call__)

# Не вызываемые объекты
print(callable(42))           # False
print(callable("hello"))      # False
print(callable([1, 2, 3]))    # False

# Лямбда-функции
lambda_func = lambda x: x * 2
print(callable(lambda_func))  # True
```


### 10.5 super()

**Описание:** Обеспечивает доступ к методам родительского класса.

**Пример кода:**

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Вызов конструктора родителя
        self.breed = breed
    
    def speak(self):
        parent_result = super().speak()
        return f"{parent_result} - Woof!"

# Использование
dog = Dog("Buddy", "Golden Retriever")
print(dog.speak())  # Buddy makes a sound - Woof!

# Множественное наследование
class Mammal:
    def breathe(self):
        return "Breathing air"

class Pet:
    def play(self):
        return "Playing with owner"

class Dog(Mammal, Pet, Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def info(self):
        return f"{self.name}: {super().breathe()}, {super().play()}"

dog2 = Dog("Rex")
print(dog2.info())  # Rex: Breathing air, Playing with owner
```


### 10.6 property()

**Описание:** Создает свойство класса, которое может иметь getter, setter и deleter.

**Пример кода:**

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    def get_radius(self):
        return self._radius
    
    def set_radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    def del_radius(self):
        print("Deleting radius")
        del self._radius
    
    # Создание свойства
    radius = property(get_radius, set_radius, del_radius, "Circle radius")

# Использование
circle = Circle(5)
print(circle.radius)     # 5
circle.radius = 10
print(circle.radius)     # 10

# Декораторный синтаксис (более современный)
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return self._width * self._height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value

rect = Rectangle(4, 5)
print(rect.area)    # 20
rect.width = 6
print(rect.area)    # 30
```



## 11. Функции ввода-вывода и отладки (5 функций)

60. **print()** - выводит значения
61. **input()** - получает ввод от пользователя
62. **open()** - открывает файл
63. **help()** - вызывает справочную систему
64. **breakpoint()** - вызывает отладчик


### 11.1 print()

**Описание:** Выводит объекты в текстовый поток, по умолчанию в stdout.

**Пример кода:**

```python
# Базовый вывод
print("Hello, World!")

# Несколько аргументов
print("Name:", "Alice", "Age:", 30)

# Разделитель
print("apple", "banana", "cherry", sep=", ")  # apple, banana, cherry

# Окончание строки
print("Hello", end=" ")
print("World")  # Hello World

# Вывод в файл
with open("output.txt", "w") as f:
    print("This goes to file", file=f)

# Форматирование
name = "Bob"
age = 25
print(f"Name: {name}, Age: {age}")

# Различные типы данных
print(42, 3.14, [1, 2, 3], {"key": "value"})
```


### 11.2 input()

**Описание:** Получает строку ввода от пользователя.

**Пример кода:**

```python
# Базовый ввод
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Ввод с преобразованием типа
age = int(input("Enter your age: "))
print(f"You are {age} years old")

# Ввод числа с плавающей точкой
height = float(input("Enter your height in meters: "))
print(f"Your height is {height} meters")

# Обработка ошибок ввода
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a valid number")

print(f"You entered: {number}")

# Ввод списка
items = input("Enter items separated by commas: ").split(",")
items = [item.strip() for item in items]
print(f"Items: {items}")
```


### 11.3 open()

**Описание:** Открывает файл и возвращает файловый объект.

**Пример кода:**

```python
# Запись в файл
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is a test file.\n")

# Чтение файла
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

# Чтение по строкам
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Добавление в файл
with open("example.txt", "a") as file:
    file.write("This line is appended.\n")

# Различные режимы
modes = {
    "r": "read (default)",
    "w": "write (overwrites)",
    "a": "append",
    "r+": "read and write",
    "rb": "read binary",
    "wb": "write binary"
}

# Работа с кодировкой
with open("utf8_file.txt", "w", encoding="utf-8") as file:
    file.write("Привет, мир! 🌍")

with open("utf8_file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
```


### 11.4 help()

**Описание:** Вызывает встроенную справочную систему.

**Пример кода:**

```python
# Справка по функции
help(len)

# Справка по модулю
import math
help(math)

# Справка по методу
help(str.split)

# Справка по классу
help(list)

# Справка по объекту
my_list = [1, 2, 3]
help(my_list)

# Интерактивная справка
# help()  # Запускает интерактивный режим справки

# Справка по ключевым словам
help("if")
help("for")
help("class")

# Пользовательская функция с docstring
def my_function(x, y):
    """
    Складывает два числа.
    
    Args:
        x: Первое число
        y: Второе число
    
    Returns:
        Сумма x и y
    """
    return x + y

help(my_function)
```


### 11.5 breakpoint()

**Описание:** Вызывает отладчик в точке вызова. Введена в Python 3.7.

**Пример кода:**

```python
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        breakpoint()  # Отладчик остановится здесь
        total += num
    return total

# При выполнении откроется отладчик pdb
# Команды отладчика:
# n (next) - следующая строка
# s (step) - войти в функцию
# c (continue) - продолжить выполнение



## 12. Декораторы и методы классов (2 функции)

65. **classmethod()** - создает метод класса
66. **staticmethod()** - создает статический метод

### 12.1 classmethod()

**Описание:** Создает метод класса, который получает класс как первый аргумент вместо экземпляра.

**Пример кода:**

```python
class Person:
    species = "Homo sapiens"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @classmethod
    def get_species(cls):
        return cls.species
    
    @classmethod
    def from_string(cls, person_str):
        name, age = person_str.split('-')
        return cls(name, int(age))
    
    def __str__(self):
        return f"{self.name}, {self.age} years old"

# Вызов метода класса
print(Person.get_species())  # Homo sapiens

# Альтернативный конструктор
person_data = "Alice-30"
person = Person.from_string(person_data)
print(person)  # Alice, 30 years old

# Наследование
class Student(Person):
    species = "Homo sapiens (student)"

print(Student.get_species())  # Homo sapiens (student)
```


### 12.2 staticmethod()

**Описание:** Создает статический метод, который не получает ни экземпляр, ни класс как первый аргумент.

**Пример кода:**

```python
class MathUtils:
    @staticmethod
    def add(x, y):
        return x + y
    
    @staticmethod
    def is_even(number):
        return number % 2 == 0
    
    @staticmethod
    def factorial(n):
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)

# Вызов статических методов
print(MathUtils.add(5, 3))        # 8
print(MathUtils.is_even(4))       # True
print(MathUtils.factorial(5))     # 120

# Можно вызывать и через экземпляр
utils = MathUtils()
print(utils.add(10, 20))          # 30

# Без декоратора (эквивалентно)
class Calculator:
    def multiply(x, y):
        return x * y
    
    multiply = staticmethod(multiply)

print(Calculator.multiply(4, 5))   # 20
```


## 13. Асинхронные функции (2 функции)

67. **aiter()** - создает асинхронный итератор
68. **anext()** - получает следующий элемент асинхронного итератора


### 13.1 aiter()

**Описание:** Создает асинхронный итератор из асинхронного итерируемого объекта.

**Пример кода:**

```python
import asyncio

class AsyncRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.start >= self.stop:
            raise StopAsyncIteration
        current = self.start
        self.start += 1
        await asyncio.sleep(0.1)  # Имитация асинхронной операции
        return current

async def main():
    # Использование aiter()
    async_range = AsyncRange(1, 4)
    async_iterator = aiter(async_range)
    
    # Итерация через асинхронный итератор
    async for value in async_iterator:
        print(f"Получено значение: {value}")

# Запуск асинхронной функции
# asyncio.run(main())

# Альтернативный пример с генератором
async def async_generator():
    for i in range(3):
        await asyncio.sleep(0.1)
        yield i

async def example2():
    async_gen = async_generator()
    async_iter = aiter(async_gen)
    
    try:
        while True:
            value = await anext(async_iter)
            print(f"Значение: {value}")
    except StopAsyncIteration:
        print("Итерация завершена")

# asyncio.run(example2())
```


### 13.2 anext()

**Описание:** Получает следующий элемент из асинхронного итератора.

**Пример кода:**

```python
import asyncio

class AsyncCounter:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
    
    def __aiter__(self):
        return self
    
    async def __anext__(self):
        if self.count >= self.max_count:
            raise StopAsyncIteration
        
        current = self.count
        self.count += 1
        await asyncio.sleep(0.2)  # Имитация асинхронной работы
        return current

async def manual_iteration():
    counter = AsyncCounter(3)
    async_iter = aiter(counter)
    
    # Ручная итерация с помощью anext()
    try:
        value1 = await anext(async_iter)
        print(f"Первое значение: {value1}")
        
        value2 = await anext(async_iter)
        print(f"Второе значение: {value2}")
        
        value3 = await anext(async_iter)
        print(f"Третье значение: {value3}")
        
        # Это вызовет StopAsyncIteration
        value4 = await anext(async_iter)
        
    except StopAsyncIteration:
        print("Больше элементов нет")

# asyncio.run(manual_iteration())

# Пример с значением по умолчанию
async def with_default():
    counter = AsyncCounter(2)
    async_iter = aiter(counter)
    
    # Получаем существующие элементы
    print(await anext(async_iter))  # 0
    print(await anext(async_iter))  # 1
    
    # Получаем значение по умолчанию
    print(await anext(async_iter, "Конец"))  # Конец

# asyncio.run(with_default())
```


## 14. Функции для работы с пространством имен (2 функции)

69. **globals()** - возвращает глобальное пространство имен
70. **locals()** - возвращает локальное пространство имен

### 14.1 globals()

**Описание:** Возвращает словарь, представляющий глобальное пространство имен текущего модуля.

**Пример кода:**

```python
# Глобальные переменные
global_var = "Я глобальная переменная"
another_global = 42

def show_globals():
    # Получение глобального пространства имен
    global_dict = globals()
    
    # Вывод некоторых глобальных переменных
    print("Глобальные переменные:")
    for key, value in global_dict.items():
        if not key.startswith('__'):  # Пропускаем служебные переменные
            print(f"  {key}: {value}")

# Динамическое создание глобальной переменной
globals()['dynamic_var'] = "Создана динамически"

def modify_global():
    # Изменение глобальной переменной через globals()
    globals()['global_var'] = "Изменена через globals()"

print("До изменения:", global_var)
modify_global()
print("После изменения:", global_var)

# Проверка существования переменной
if 'dynamic_var' in globals():
    print(f"dynamic_var существует: {dynamic_var}")

# Удаление глобальной переменной
if 'another_global' in globals():
    del globals()['another_global']
    print("another_global удалена")

show_globals()
```


### 14.2 locals()

**Описание:** Возвращает словарь, представляющий локальное пространство имен текущей области видимости.

**Пример кода:**

```python
def demonstrate_locals():
    local_var1 = "Локальная переменная 1"
    local_var2 = 100
    
    # Получение локального пространства имен
    local_dict = locals()
    
    print("Локальные переменные:")
    for key, value in local_dict.items():
        print(f"  {key}: {value}")
    
    # Динамическое создание локальной переменной
    locals()['dynamic_local'] = "Создана динамически"
    
    # ВНИМАНИЕ: изменения через locals() могут не работать
    # в некоторых случаях из-за оптимизации Python
    print("\nПосле добавления через locals():")
    print(f"locals(): {locals()}")
    
    # Проверим, существует ли переменная
    try:
        print(f"dynamic_local: {dynamic_local}")
    except NameError:
        print("dynamic_local не доступна напрямую")

def nested_function_example():
    outer_var = "Внешняя переменная"
    
    def inner_function():
        inner_var = "Внутренняя переменная"
        
        print("Локальные переменные во внутренней функции:")
        for key, value in locals().items():
            print(f"  {key}: {value}")
        
        # Доступ к внешней переменной
        print(f"Доступ к outer_var: {outer_var}")
    
    print("Локальные переменные во внешней функции:")
    for key, value in locals().items():
        print(f"  {key}: {value}")
    
    inner_function()

demonstrate_locals()
print("\n" + "="*50 + "\n")
nested_function_example()

# В глобальной области locals() == globals()
print("\nВ глобальной области:")
print(f"locals() is globals(): {locals() is globals()}")
```


## 15. Дополнительная функция (1 функция)

71. **__import__()** - импортирует модуль (низкоуровневая функция)

### 15.1 __import__()

**Описание:** Низкоуровневая функция для импорта модулей. Обычно используется внутренне интерпретатором Python.

**Пример кода:**

```python
# Базовый импорт модуля
math_module = __import__('math')
print(math_module.pi)  # 3.141592653589793
print(math_module.sqrt(16))  # 4.0

# Импорт с указанием уровня (для относительного импорта)
# __import__('module', globals(), locals(), ['attribute'], level)

# Импорт подмодуля
os_path = __import__('os.path', fromlist=[''])
print(os_path.join('folder', 'file.txt'))  # folder/file.txt

# Динамический импорт
module_name = 'random'
random_module = __import__(module_name)
print(random_module.randint(1, 10))

# Импорт с fromlist
datetime_module = __import__('datetime', fromlist=['datetime', 'date'])
now = datetime_module.datetime.now()
print(f"Текущее время: {now}")

# Функция-обертка для более удобного использования
def dynamic_import(module_name, attribute=None):
    """Динамический импорт модуля или атрибута"""
    try:
        if '.' in module_name:
            # Для подмодулей
            module = __import__(module_name, fromlist=[''])
        else:
            module = __import__(module_name)
        
        if attribute:
            return getattr(module, attribute)
        return module
    
    except ImportError as e:
        print(f"Ошибка импорта: {e}")
        return None

# Использование функции-обертки
json_module = dynamic_import('json')
if json_module:
    data = {'name': 'Alice', 'age': 30}
    json_string = json_module.dumps(data)
    print(f"JSON: {json_string}")

# Импорт конкретной функции
sqrt_func = dynamic_import('math', 'sqrt')
if sqrt_func:
    print(f"Квадратный корень из 25: {sqrt_func(25)}")

# ВНИМАНИЕ: Обычно лучше использовать import или importlib
# __import__() предназначена для внутреннего использования
```
## Заключение

Все **71 встроенная функция Python** предоставляют мощный инструментарий для работы с различными аспектами программирования:

- **Математические операции** (7 функций): abs, divmod, max, min, pow, round, sum
- **Работа с типами данных** (8 функций): bool, int, float, complex, str, bytes, bytearray, memoryview
- **Коллекции** (6 функций): list, tuple, set, frozenset, dict, range
- **Итераторы** (9 функций): iter, next, enumerate, zip, map, filter, sorted, reversed, slice
- **Объекты и атрибуты** (10 функций): getattr, setattr, delattr, hasattr, dir, vars, type, isinstance, issubclass, object
- **Строки и символы** (5 функций): chr, ord, ascii, repr, format
- **Числовые системы** (3 функции): bin, oct, hex
- **Логические операции** (2 функции): all, any
- **Выполнение кода** (3 функции): eval, exec, compile
- **Служебные функции** (6 функций): id, hash, len, callable, super, property
- **Ввод-вывод и отладка** (5 функций): print, input, open, help, breakpoint
- **Методы классов** (2 функции): classmethod, staticmethod
- **Асинхронное программирование** (2 функции): aiter, anext
- **Пространство имен** (2 функции): globals, locals
- **Импорт модулей** (1 функция): __import__
Эти функции составляют основу языка Python и доступны без необходимости импорта дополнительных модулей, что делает их незаменимыми инструментами для ежедневного программирования