# Информация по PEP в Python

## Полный перечень основных PEP с их названиями

### Фундаментальные PEP для разработки

**PEP 1** - PEP Purpose and Guidelines (Цель и руководящие принципы PEP)[^1]
**PEP 8** - Style Guide for Python Code (Руководство по стилю кода Python)[^2][^3]
**PEP 20** - The Zen of Python (Дзен Python)[^4][^5]
**PEP 257** - Docstring Conventions (Соглашения по строкам документации)[^6]

### PEP для типизации и аннотаций

**PEP 484** - Type Hints (Подсказки типов)[^7]
**PEP 526** - Syntax for Variable Annotations (Синтаксис для аннотаций переменных)[^8]
**PEP 585** - Type Hinting Generics In Standard Collections (Типизация дженериков в стандартных коллекциях)[^9]
**PEP 563** - Postponed Evaluation of Annotations (Отложенное вычисление аннотаций)[^10]
**PEP 647** - User-Defined Type Guards (Пользовательские типовые стражи)[^11]
**PEP 3107** - Function Annotations (Аннотации функций)[^12]

### PEP для импортов и структуры проекта

**PEP 328** - Imports: Multi-Line and Absolute/Relative (Импорты: многострочные и абсолютные/относительные)[^13]
**PEP 518** - Specifying Minimum Build System Requirements (Спецификация минимальных требований системы сборки)[^14]
**PEP 621** - Storing project metadata in pyproject.toml (Хранение метаданных проекта в pyproject.toml)[^15]

### PEP для современных возможностей языка

**PEP 615** - Support for the IANA Time Zone Database (Поддержка базы данных часовых поясов IANA)[^16]
**PEP 634** - Structural Pattern Matching: Specification (Структурное сопоставление с образцом: спецификация)[^17]
**PEP 440** - Version Identification and Dependency Specification (Идентификация версий и спецификация зависимостей)[^18]

## Основные тезисы по каждому PEP

### PEP 1 - PEP Purpose and Guidelines

PEP 1 определяет процесс создания и утверждения Python Enhancement Proposals[^1]. Основные принципы:

- **Типы PEP**: Standards Track (новые возможности), Informational (информационные), Process (процессы)[^1]
- **Процесс утверждения**: от драфта до финального статуса через обсуждение в сообществе[^1]
- **Целевая аудитория**: основные разработчики CPython и их избранный Руководящий совет[^1]


### PEP 8 - Style Guide for Python Code

PEP 8 является официальным руководством по стилю кода Python[^2][^3]. Ключевые рекомендации:

**Отступы**: использовать 4 пробела для каждого уровня отступа[^19]

```python
def function_example():
    if condition:
        return True
    return False
```

**Длина строк**: максимум 79 символов для кода, 72 для комментариев[^3]

**Соглашения по именованию**[^3]:

- Переменные и функции: snake_case (`my_variable`, `calculate_sum`)
- Классы: CamelCase (`MyClassName`)
- Константы: UPPER_CASE (`MAX_SIZE`)

**Импорты**: каждый импорт на отдельной строке[^3]

```python
# Правильно
import os
import sys

# Неправильно
import os, sys
```


### PEP 20 - The Zen of Python

PEP 20 содержит 19 руководящих принципов философии Python[^4][^5]:

- **Beautiful is better than ugly** (Красивое лучше уродливого)
- **Explicit is better than implicit** (Явное лучше неявного)
- **Simple is better than complex** (Простое лучше сложного)
- **Readability counts** (Читаемость имеет значение)
- **There should be one obvious way to do it** (Должен быть один очевидный способ сделать это)[^4]

Эти принципы влияют на дизайн самого языка Python и служат руководством для разработчиков[^4].

### PEP 257 - Docstring Conventions

PEP 257 стандартизирует соглашения по строкам документации[^6]. Основные правила:

**Структура docstring**:

- Все модули, функции и классы должны иметь docstring[^6]
- Использование тройных кавычек `"""`[^6]
- Первая строка - краткое описание в повелительном наклонении[^20]

```python
def calculate_sum(a, b):
    """Return the sum of a and b.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
    """
    return a + b
```


### PEP 484 - Type Hints

PEP 484 введи систему подсказок типов в Python[^7]. Ключевые возможности:

**Аннотации переменных**[^7]:

```python
name: str = "John"
age: int = 30
is_valid: bool = True
```

**Аннотации функций**[^7]:

```python
def greet(name: str) -> str:
    return f"Hello, {name}"
```

**Сложные типы**[^7]:

```python
from typing import List, Dict, Optional

numbers: List[int] = [1, 2, 3]
scores: Dict[str, int] = {"Math": 90, "Science": 85}
maybe_age: Optional[int] = None
```


### PEP 3107 - Function Annotations

PEP 3107 ввёл синтаксис для аннотаций функций[^12]. Принципы:

- **Необязательность**: аннотации полностью опциональны[^12]
- **Произвольные выражения**: можно использовать любые Python-выражения[^12]
- **Интерпретация**: Python не придаёт аннотациям особого значения[^12]

```python
def compile(source: "something compilable", 
           filename: "where the compilable thing comes from",
           mode: "is this a single statement or a suite?"):
    pass
```


### PEP 526 - Syntax for Variable Annotations

PEP 526 добавил синтаксис для аннотаций переменных[^8]. Основные возможности:

**Аннотации переменных**[^8]:

```python
primes: List[int] = []
captain: str  # Без начального значения

class Starship:
    stats: ClassVar[Dict[str, int]] = {}
```

**Преимущества над комментариями типов**:

- Лучшая поддержка в редакторах[^8]
- Более чистый синтаксис[^8]
- Интеграция с системой типов[^8]


### PEP 328 - Imports: Multi-Line and Absolute/Relative

PEP 328 решает проблемы с импортами[^13]. Ключевые изменения:

**Многострочные импорты**[^13]:

```python
from Tkinter import (Tk, Frame, Button, Entry, Canvas, Text,
                     LEFT, DISABLED, NORMAL, RIDGE, END)
```

**Абсолютные и относительные импорты**[^13]:

```python
# Абсолютный импорт
import sys

# Относительный импорт
from . import sibling_module
from ..parent import parent_module
```


### PEP 563 - Postponed Evaluation of Annotations

PEP 563 изменил способ обработки аннотаций[^10]. Основные принципы:

- **Отложенное вычисление**: аннотации сохраняются как строки[^10]
- **Активация**: `from __future__ import annotations`[^21]
- **Преимущества**: решение проблем с forward references[^21]

```python
from __future__ import annotations

class TreeNode:
    def __init__(self, left: TreeNode, right: TreeNode):
        self.left = left
        self.right = right
```


### PEP 585 - Type Hinting Generics In Standard Collections

PEP 585 позволил использовать встроенные коллекции как дженерики[^9]. Нововведения:

**Прямое использование встроенных типов**[^9]:

```python
# Старый способ (до Python 3.9)
from typing import List, Dict

numbers: List[int] = [1, 2, 3]
scores: Dict[str, int] = {"a": 1}

# Новый способ (Python 3.9+)
numbers: list[int] = [1, 2, 3]
scores: dict[str, int] = {"a": 1}
```


### PEP 615 - Support for the IANA Time Zone Database

PEP 615 добавил модуль `zoneinfo` для работы с часовыми поясами[^16]. Возможности:

**Работа с часовыми поясами**[^22]:

```python
from zoneinfo import ZoneInfo
from datetime import datetime

ams = ZoneInfo('Europe/Amsterdam')
dt = datetime(2015, 10, 21, 13, 40, tzinfo=ams)

la = ZoneInfo('America/Los_Angeles')
dt_la = dt.astimezone(la)
```


### PEP 634 - Structural Pattern Matching

PEP 634 ввёл оператор `match-case` в Python 3.10[^17]. Основные возможности:

**Структурное сопоставление с образцом**[^23]:

```python
match day:
    case 1:
        return 'Monday'
    case 2:
        return 'Tuesday'
    case 3:
        return 'Wednesday'
    case _:
        return 'Unknown day'
```

**Сложные паттерны**[^17]:

```python
match data:
    case {'type': 'user', 'name': str(name)}:
        return f"User: {name}"
    case {'type': 'product', 'id': int(product_id)}:
        return f"Product ID: {product_id}"
```


### PEP 647 - User-Defined Type Guards

PEP 647 добавил пользовательские типовые стражи[^11]. Применение:

**Определение типовых стражей**[^11]:

```python
from typing import TypeGuard

def is_str_list(val: list[object]) -> TypeGuard[list[str]]:
    """Проверяет, что все объекты в списке - строки"""
    return all(isinstance(x, str) for x in val)

def process_list(val: list[object]):
    if is_str_list(val):
        # Здесь val имеет тип list[str]
        print(" ".join(val))
```


### PEP 518 и PEP 621 - Современная система сборки

**PEP 518** ввёл `pyproject.toml` для спецификации зависимостей сборки[^14]:

```toml
[build-system]
requires = ["setuptools", "wheel", "numpy>=1.13"]
build-backend = "setuptools.build_meta"
```

**PEP 621** стандартизировал метаданные проекта в `pyproject.toml`[^15]:

```toml
[project]
name = "my-package"
version = "0.1.0"
description = "A sample Python package"
dependencies = ["requests>=2.25.0"]
```

Эти PEP представляют собой основу современной разработки на Python, охватывая стиль кода, типизацию, структуру проектов и новые возможности языка. Их понимание и применение является ключевым для написания качественного, читаемого и поддерживаемого Python-кода[^24][^25][^26].

<div style="text-align: center">⁂</div>

[^1]: https://peps.python.org/pep-0001/

[^2]: https://realpython.com/python-pep8/

[^3]: https://llego.dev/posts/writing-clean-pep-8-compliant-code-better-collaboration/

[^4]: https://python.land/the-zen-of-python

[^5]: https://www.cs.odu.edu/~tkennedy/cs263/f24/Public/perspectivePEP20/index.html

[^6]: https://peps.python.org/pep-0257/

[^7]: https://www.rittmanmead.com/blog/2024/03/tip-tuesday-python-data-type-hints/

[^8]: https://peps.python.org/pep-0526/

[^9]: https://peps.python.org/pep-0585/

[^10]: https://peps.python.org/pep-0563/

[^11]: https://peps.python.org/pep-0647/

[^12]: https://peps.python.org/pep-3107/

[^13]: https://peps.python.org/pep-0328/

[^14]: https://pydevtools.com/handbook/explanation/what-is-pep-517/

[^15]: https://pydevtools.com/handbook/explanation/what-is-pep-621-compatability/

[^16]: https://peps.python.org/pep-0615/

[^17]: https://peps.python.org/pep-0634/

[^18]: https://peps.python.org/pep-0440/

[^19]: https://elpythonista.com/pep8

[^20]: https://gist.github.com/doolio/ea4d5e96975005b523ed7c92c3626030

[^21]: https://python.plainenglish.io/understand-postponed-evaluation-of-type-annotations-in-python-497155a339a0

[^22]: https://pythonetc.orsinium.dev/posts/zoneinfo

[^23]: https://www.thomascollart.com/python-switch-case/

[^24]: https://www.linkedin.com/pulse/pep-evolution-python-nuno-bispo-eytqe

[^25]: https://www.diegor.it/2017/06/15/the-must-read-pythons-peps/

[^26]: https://pydevtools.com/handbook/explanation/pep/

[^27]: https://peps.python.org

[^28]: https://github.com/python/peps

[^29]: https://stackoverflow.com/questions/10017776/where-can-i-find-proper-examples-of-the-pep-257-docstring-conventions

[^30]: https://www.rdegges.com/2010/python-docstring-symmetry/

[^31]: https://pypi.org/project/pep257/0.3.2/

[^32]: https://www.jetbrains.com/help/pycharm/type-hinting-in-product.html

[^33]: https://stackoverflow.com/questions/3038033/what-are-good-uses-for-python3s-function-annotations

[^34]: https://edoras.sdsu.edu/doc/Python-Docs-2.5/whatsnew/pep-328.html

[^35]: https://documentation.help/Python-PEP/node10.html

[^36]: https://github.com/beartype/beartype/issues/4

[^37]: http://ref.readthedocs.io/en/latest/understanding_python/imports/

[^38]: https://stackoverflow.com/questions/74666784/try-to-understand-class-and-instance-variable-annotations-in-pep-526

[^39]: https://github.com/apple/pfl-research/issues/89

[^40]: https://stackoverflow.com/questions/63554905/install-pep-518-build-system-requirements-only-to-build-sdist

[^41]: https://stackoverflow.com/questions/62529054/will-python-type-checker-respect-annotations-set-dynamically

[^42]: https://pep621.readthedocs.io

[^43]: https://discuss.python.org/t/pep-615-support-for-the-iana-time-zone-database-in-the-standard-library/3468

[^44]: https://gdevops.frama.io/dev/tuto-programming/datetime/python/zoneinfo/zoneinfo.html

[^45]: https://github.com/python/steering-council/issues/22

[^46]: https://github.com/python/typing/issues/926

[^47]: https://peps-aaturner.readthedocs.io

[^48]: https://onestopdataanalysis.com/python-pep-cheatsheet/

[^49]: https://en.wikipedia.org/wiki/Python_(programming_language)

[^50]: https://stackoverflow.com/questions/8852561/complete-code-example-that-demonstrates-all-pep-8-rules

[^51]: https://github.com/pepkit/example_peps

[^52]: https://pep.databio.org/spec/simple-example/

[^53]: https://www.datacamp.com/tutorial/pep8-tutorial-python-code

[^54]: https://docs.dasch.swiss/latest/DSP-TOOLS/developers/code-quality-tools/python-docstring-formatting/

[^55]: https://stackoverflow.com/questions/46313872/pep-484-exclusive-type-for-type-hint

[^56]: https://jimit105.github.io/pytricks/Function Annotations.html

[^57]: https://code.tutsplus.com/python-3-function-annotations--cms-25689t

[^58]: https://simonklug.de/python-function-annotation

[^59]: https://docs.astral.sh/ruff/rules/non-pep585-annotation/

[^60]: https://peps.python.org/pep-0008/

[^61]: https://habr.com/ru/articles/499358/

[^62]: https://jingwen-z.github.io/python-pep-328-import-and-build-package/

[^63]: https://stackoverflow.com/questions/47961723/pep-328-relative-import-beyond-top-level-package

[^64]: https://www.reddit.com/r/Python/comments/muyz5h/pep_563_getting_rolled_back_from_python_310/

[^65]: https://discuss.python.org/t/unexpected-behaviour-related-to-pep-563-postponed-evaluation-of-annotations/57938

[^66]: https://pythonz.net/peps/named/0615/

[^67]: https://stackoverflow.com/questions/1382648/which-peps-are-must-reads

[^68]: https://peps.python.org/pep-0012/

[^69]: https://python-future.org/func_annotations.html

