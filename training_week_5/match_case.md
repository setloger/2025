# Конструкция match/case в Python

Конструкция **match/case** была введена в Python 3.10 и представляет собой механизм структурного сопоставления с образцом (structural pattern matching)[^1][^2]. Это аналог оператора switch-case из других языков программирования, но с гораздо более широкими возможностями[^3][^4].

## Синтаксис и основные принципы

Общий синтаксис конструкции match/case выглядит следующим образом[^2][^3]:

```python
match выражение:
    case шаблон_1:
        действие_1
    case шаблон_2:
        действие_2
    case _:
        действие_по_умолчанию
```

Оператор **match** принимает выражение и сравнивает его значение с последовательными шаблонами, заданными в блоках **case**[^1]. Когда найдено соответствие, выполняются инструкции из соответствующего блока case, после чего выполнение конструкции завершается[^2].

### Простой пример использования

```python
day = "Monday"
match day:
    case "Sunday":
        print("Take it easy")
    case "Monday":
        print("Go to work")
    case "Tuesday":
        print("Work + Hobbies")
    case _:
        print("Other day")
```


## Типы шаблонов

### 1. Литеральные шаблоны (Literal patterns)

Самый простой тип шаблонов - сопоставление с конкретными значениями[^3]:

```python
http_status = 400
match http_status:
    case 400:
        print("Bad Request")
    case 403:
        print("Forbidden")
    case 404:
        print("Not Found")
    case _:
        print("Other")
```


### 2. Шаблоны захвата (Capture patterns)

Позволяют сохранить совпавшее значение в переменную[^3]:

```python
def greet(name=None):
    match name:
        case None:
            print("Hello there")
        case some_name:
            print(f"Hello {some_name}")
```


### 3. Шаблоны подстановки (Wildcard patterns)

Используют символ `_` для сопоставления с любым значением[^3]:

```python
coinflip = 4
match coinflip:
    case 1:
        print("Heads")
    case 0:
        print("Tails")
    case _:
        print("Must be 0 or 1")
```


### 4. Шаблоны последовательностей

Позволяют работать со списками, кортежами и другими последовательностями[^1][^3]:

```python
location = (1, 3)
match location:
    case x,:
        print(f"1D location: ({x})")
    case x, y:
        print(f"2D location: ({x}, {y})")
    case x, y, z:
        print(f"3D location: ({x}, {y}, {z})")
```

С использованием оператора `*` для захвата остальных элементов[^3]:

```python
location = (1, 3, 2, "a", "b", "c")
match location:
    case x, y, z, *names:
        print(f"3D location: ({x}, {y}, {z})")
        print(f"Extra data: {names}")
```


### 5. Сопоставление со словарями

Pattern matching поддерживает работу со словарями[^5]:

```python
def look(words):
    match words:
        case {"red": "красный", "blue": "синий"}:
            print("Слова red и blue есть в словаре")
        case {"red": red, **rest}:
            print(f"red: {red}")
            for key in rest:
                print(f"{key}: {rest[key]}")
        case {}:
            print("Пустой словарь")
```


## Guards (Защитники) - дополнительные условия

Guards позволяют добавить дополнительные условия к шаблонам с помощью ключевого слова `if`[^6]:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def enter(person):
    match person:
        case Person(name=name, age=age) if age < 18:
            print(f"{name}, доступ запрещён")
        case Person(name=name, age=age) if age < 22:
            print(f"{name}, доступ ограничен")
        case Person(name=name):
            print(f"{name}, у вас полноценный доступ!")
```


## Сопоставление с объектами классов

Match/case может работать с экземплярами классов[^1]:

```python
class Point:
    __match_args__ = ["x", "y"]
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

def describe_point(point):
    match point:
        case Point(0, 0):
            return "в начале координат"
        case Point(0, y):
            return f"на вертикальной оси, при y = {y}"
        case Point(x, 0):
            return f"на горизонтальной оси, при x = {x}"
        case Point(x, y):
            return f"в позиции ({x}, {y})"
```


## Комбинирование шаблонов

Можно использовать логический оператор `|` для проверки нескольких вариантов[^3]:

```python
day = "Monday"
match day:
    case "Saturday" | "Sunday":
        print("Weekend")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("Work")
```


## Работа с перечислениями (Enums)

Match/case отлично работает с перечислениями[^1]:

```python
from enum import Enum

class Color(Enum):
    RED = 0
    GREEN = 1
    BLUE = 2

match color:
    case Color.RED:
        print("Это красный")
    case Color.GREEN:
        print("Трава зелёная")
    case Color.BLUE:
        print("Небо синее")
```


## Преимущества match/case

1. **Читаемость кода**: Конструкция match/case делает код более читаемым по сравнению с длинными цепочками if-elif-else[^3][^4]
2. **Структурное сопоставление**: Позволяет легко работать со сложными структурами данных[^1]
3. **Безопасность типов**: Улучшает возможности статической проверки типов[^7]
4. **Производительность**: В некоторых случаях может быть быстрее, чем эквивалентные конструкции if-else[^1]

## Совместимость

Конструкция match/case доступна **только начиная с Python 3.10**[^2][^3][^7]. Это важно учитывать при разработке приложений, которые должны работать на более старых версиях Python.

## Заключение

Конструкция match/case представляет собой мощный инструмент для сопоставления с образцом, который значительно упрощает работу со сложными условными конструкциями в Python. Она особенно полезна при обработке структурированных данных, работе с различными типами объектов и создании более читаемого и maintainable кода[^1][^3].

<div style="text-align: center">⁂</div>

[^1]: https://docs-python.ru/tutorial/tsikly-upravlenie-vetvleniem-python/konstruktsija-match-case/

[^2]: https://metanit.com/python/tutorial/2.13.php

[^3]: https://pythonist.ru/konstrukcziya-match-case-v-python-polnoe-rukovodstvo/

[^4]: https://proghunter.ru/articles/match-case-statements-in-python

[^5]: https://metanit.com/python/tutorial/2.24.php

[^6]: https://metanit.com/python/tutorial/2.26.php

[^7]: https://opennet.ru/54563-python

[^8]: https://dl.acm.org/doi/10.1145/3610419.3610457

[^9]: https://www.semanticscholar.org/paper/179d83fb484357943755c7d181418f41051b6aee

[^10]: https://bmcresnotes.biomedcentral.com/articles/10.1186/s13104-023-06396-x

[^11]: https://ph.pollub.pl/index.php/jcsi/article/view/3109

[^12]: https://ieeexplore.ieee.org/document/10172867/

[^13]: https://pubs.acs.org/doi/10.1021/acs.jcim.5c00669

[^14]: https://ieeexplore.ieee.org/document/9871333/

[^15]: https://ieeexplore.ieee.org/document/10134151/

[^16]: https://habr.com/ru/articles/585216/

[^17]: https://code.mu/ru/python/book/prime/conditions/match-case/

[^18]: https://www.geeksforgeeks.org/python/python-match-case-statement/

[^19]: https://proproprogs.ru/python_base/python3-konstrukciya-matchcase-primery-i-osobennosti-ispolzovaniya

[^20]: https://sky.pro/wiki/python/ispolzovanie-operatora-case-v-python/

[^21]: https://javarush.com/groups/posts/68594-konstrukcija-matchcase-primerih-i-fishki-dlja-studentov-programmistov

[^22]: https://proproprogs.ru/python_base/python3-konstrukciya-matchcase-pervoe-znakomstvo

[^23]: https://www.youtube.com/watch?v=HUdu1EivXAo

[^24]: http://arxiv.org/pdf/2306.06557.pdf

[^25]: https://arxiv.org/pdf/1710.06915v1.pdf

[^26]: https://arxiv.org/pdf/1910.11829.pdf

[^27]: https://joss.theoj.org/papers/10.21105/joss.00670.pdf

[^28]: https://arxiv.org/pdf/2206.12600.pdf

[^29]: https://arxiv.org/html/2312.11873v1

[^30]: https://arxiv.org/pdf/1711.00046.pdf

[^31]: https://joss.theoj.org/papers/10.21105/joss.02169.pdf

[^32]: https://proproprogs.ru/python_base/python3-konstrukciya-matchcase-s-kortezhami-i-spiskami

[^33]: https://habr.com/ru/companies/yandex_praktikum/articles/547902/

[^34]: https://proproprogs.ru/python_base/python3-konstrukciya-matchcase-so-slovaryami-i-mnozhestvami

[^35]: https://pylot.me/article/52-match-case/

[^36]: https://habr.com/ru/articles/555804/

[^37]: https://www.reddit.com/r/Python/comments/t673bh/whats_the_point_of_a_switch_case_if_dictionaries/?tl=ru

[^38]: https://www.youtube.com/watch?v=yDlWEwG1eb0

[^39]: https://habr.com/ru/articles/585518/

[^40]: https://ru.stackoverflow.com/questions/1337907/Конструкция-match-case-в-python-3-10

[^41]: https://www.youtube.com/watch?v=dmwhEA1ISyk

[^42]: https://onlinelibrary.wiley.com/doi/10.1111/jopr.13994

[^43]: https://dl.acm.org/doi/10.1145/3448016.3457244

[^44]: https://arxiv.org/pdf/1710.06445.pdf

[^45]: https://arxiv.org/pdf/2401.07576.pdf

[^46]: https://www.aclweb.org/anthology/2020.emnlp-demos.9.pdf

[^47]: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/F13CECDAB2B6200135D45452CA44A8B3/S0956796819000182a.pdf/div-class-title-elaborating-dependent-co-pattern-matching-no-pattern-left-behind-div.pdf

[^48]: https://arxiv.org/pdf/2402.07732.pdf

[^49]: http://arxiv.org/pdf/2501.11501.pdf

[^50]: https://arxiv.org/pdf/2304.14395.pdf

[^51]: http://conference.scipy.org/proceedings/scipy2017/pdfs/manuel_krebber.pdf

[^52]: http://arxiv.org/pdf/2401.15189.pdf

[^53]: http://arxiv.org/pdf/2309.14401.pdf

[^54]: https://journal.r-project.org/archive/2014/RJ-2014-011/RJ-2014-011.pdf

[^55]: https://arxiv.org/pdf/2303.01142.pdf

[^56]: https://arxiv.org/abs/1710.00077

