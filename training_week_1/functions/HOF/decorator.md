## Декораторы в Python: подробное объяснение с примерами

**Что такое декораторы?**

Декораторы — это функции высшего порядка, которые позволяют изменять или расширять поведение других функций или методов без изменения их исходного кода. Декораторы часто используют для логирования, проверки прав доступа, измерения времени выполнения, кэширования и других задач[^1][^2][^3].

**Как работают декораторы?**

В Python функции — это объекты, их можно передавать как аргументы, возвращать из других функций и определять внутри других функций. Декоратор — это функция, которая принимает другую функцию и возвращает новую функцию-обёртку, которая может выполнять дополнительные действия до и/или после вызова исходной функции[^2][^4][^1].

### Пример простого декоратора

```python
def my_decorator(func):
    def wrapper():
        print("Что-то происходит перед вызовом функции")
        func()
        print("Что-то происходит после вызова функции")
    return wrapper

@my_decorator
def say_hello():
    print("Привет, мир!")

say_hello()
```

**Результат:**

```
Что-то происходит перед вызовом функции
Привет, мир!
Что-то происходит после вызова функции
```

Здесь `@my_decorator` — синтаксический сахар для `say_hello = my_decorator(say_hello)`[^1][^4].

## Декораторы с аргументами

Если декорируемая функция принимает аргументы, обёртка (`wrapper`) тоже должна их принимать и передавать дальше с помощью `*args` и `**kwargs`:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Аргументы:", args, kwargs)
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    print(f"Привет, {name}!")

greet("Алиса")
```

**Результат:**

```
Аргументы: ('Алиса',) {}
Привет, Алиса!
```


## Практический пример: проверка деления на ноль

```python
def smart_divide(func):
    def wrapper(a, b):
        print(f"Делим {a} на {b}")
        if b == 0:
            print("Ошибка: деление на ноль!")
            return None
        return func(a, b)
    return wrapper

@smart_divide
def divide(a, b):
    print(a / b)

divide(10, 2)
divide(5, 0)
```

**Результат:**

```
Делим 10 на 2
5.0
Делим 5 на 0
Ошибка: деление на ноль!
```


## Цепочка декораторов

Можно применять несколько декораторов к одной функции. Они выполняются в порядке, обратном объявлению (сначала внутренний, потом внешний):

```python
def star(func):
    def wrapper(*args, **kwargs):
        print("*" * 10)
        func(*args, **kwargs)
        print("*" * 10)
    return wrapper

def percent(func):
    def wrapper(*args, **kwargs):
        print("%" * 10)
        func(*args, **kwargs)
        print("%" * 10)
    return wrapper

@star
@percent
def printer(msg):
    print(msg)

printer("Hello")
```

**Результат:**

```
**********
%%%%%%%%%%
Hello
%%%%%%%%%%
**********
```


## Для чего используют декораторы

- Логирование вызовов функций
- Кэширование результатов
- Проверка прав доступа
- Валидация входных данных
- Измерение времени выполнения
- Повторное использование кода (DRY-принцип)[^1][^2]


## Кратко: как создать свой декоратор

1. Определить функцию-декоратор, принимающую функцию как аргумент.
2. Внутри неё определить функцию-обёртку (`wrapper`), которая выполняет дополнительные действия.
3. Вернуть функцию-обёртку из декоратора.
4. Применить декоратор через `@имя_декоратора`[^1][^2][^4].

## Заключение

Декораторы — мощный инструмент Python, который позволяет элегантно и прозрачно расширять функциональность функций и методов без изменения их исходного кода. Это ключевая концепция для любого разработчика уровня middle и выше.

<div style="text-align: center">⁂</div>

[^1]: https://sky.pro/media/chto-takoe-dekoratory-v-python/

[^2]: https://pythonworld.ru/osnovy/dekoratory.html

[^3]: https://realpython.com/primer-on-python-decorators/

[^4]: https://www.programiz.com/python-programming/decorator

[^5]: file.csv

[^6]: https://www.datacamp.com/tutorial/decorators-python

[^7]: https://blog.hubspot.com/website/decorators-in-python

[^8]: https://stackoverflow.com/questions/5952641/decorating-decorators-try-to-get-my-head-around-understanding-it

[^9]: https://www.youtube.com/watch?v=U-G-mSd4KAE

[^10]: https://www.youtube.com/watch?v=BeNH2WdETYc

[^11]: https://towardsdatascience.com/six-levels-of-python-decorators-1f12c9067b23/

