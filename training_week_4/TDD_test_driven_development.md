# TDD (Test Driven Development) — Подготовка к собеседованию Middle Python Developer

## Что такое TDD?

**Test Driven Development (TDD)** — это методология разработки программного обеспечения, при которой тесты пишутся **до написания самого кода**[^1][^2]. TDD следует принципу "сначала тест, потом код", что кардинально меняет подход к разработке и обеспечивает высокое качество программного продукта.

TDD — это не просто написание тестов, это **философия разработки**, которая влияет на архитектуру, дизайн и качество кода[^3][^4].

## Цикл TDD: Red-Green-Refactor

TDD основан на трехэтапном цикле, известном как **Red-Green-Refactor**[^2][^5]:

### 1. Red (Красный) — Написание failing теста

- Пишется тест для функциональности, которая еще не существует
- Тест **должен провалиться** — это подтверждает, что он действительно тестирует новую функциональность
- Начинайте только с **одного теста** — не должно быть более одного failing теста одновременно


### 2. Green (Зеленый) — Написание минимального кода

- Пишется **минимальное количество кода**, необходимое для прохождения теста
- Не нужно думать об оптимизации или красоте кода
- Цель — просто сделать тест зеленым


### 3. Refactor (Рефакторинг) — Улучшение кода

- Улучшение качества и структуры кода без изменения его поведения
- Все тесты должны продолжать проходить после рефакторинга
- Устранение дублирования и улучшение читаемости


## Практический пример: Calculator Class

Рассмотрим пошаговую реализацию простого калькулятора с использованием TDD[^6][^7].

### Шаг 1: Red — Первый тест

```python
# tests/test_calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add_two_numbers(self):
        calc = Calculator()
        result = calc.add(4, 5)
        self.assertEqual(result, 9)

if __name__ == '__main__':
    unittest.main()
```

**Результат**: Тест провалится с ошибкой `ModuleNotFoundError`, так как класс `Calculator` не существует.

### Шаг 2: Green — Минимальный код

```python
# calculator.py
class Calculator:
    def add(self, a, b):
        return 9
```

Да, именно `return 9`! Это минимальный код для прохождения теста[^6].

### Шаг 3: Расширение тестов

```python
# tests/test_calculator.py
def test_add_different_numbers(self):
    calc = Calculator()
    result = calc.add(10, 15)
    self.assertEqual(result, 25)
```

Теперь наша функция с `return 9` провалится, и нам нужно написать правильную реализацию:

```python
# calculator.py
class Calculator:
    def add(self, a, b):
        return a + b
```


### Шаг 4: Добавление новой функциональности

```python
# tests/test_calculator.py
def test_subtract_two_numbers(self):
    calc = Calculator()
    result = calc.subtract(10, 3)
    self.assertEqual(result, 7)

def test_multiply_two_numbers(self):
    calc = Calculator()
    result = calc.multiply(6, 4)
    self.assertEqual(result, 24)
```


## Преимущества TDD

### Для разработчика среднего уровня TDD обеспечивает:

**Качество кода:**

- Код покрыт тестами по умолчанию
- Раннее обнаружение багов
- Лучшая архитектура за счет "testable" дизайна

**Уверенность при рефакторинге:**

- Можно безопасно изменять код
- Тесты служат safety net
- Регрессионные баги обнаруживаются сразу

**Документация:**

- Тесты служат живой документацией
- Показывают, как должен использоваться код
- Примеры использования API


## Инструменты для TDD в Python

### pytest — Современный фреймворк

```python
# test_banking.py
import pytest
from banking import BankAccount

class TestBankAccount:
    def setup_method(self):
        self.account = BankAccount(initial_balance=1000)
    
    def test_deposit_increases_balance(self):
        self.account.deposit(500)
        assert self.account.balance == 1500
    
    def test_withdraw_decreases_balance(self):
        self.account.withdraw(300)
        assert self.account.balance == 700
    
    def test_withdraw_insufficient_funds_raises_error(self):
        with pytest.raises(ValueError, match="Insufficient funds"):
            self.account.withdraw(1500)
```


### unittest — Встроенный фреймворк

```python
# test_string_manipulator.py
import unittest
from string_manipulator import StringManipulator

class TestStringManipulator(unittest.TestCase):
    def setUp(self):
        self.manipulator = StringManipulator()
    
    def test_to_lowercase(self):
        result = self.manipulator.to_lower_case("HELLO")
        self.assertEqual(result, "hello")
    
    def test_reverse_string(self):
        result = self.manipulator.reverse("python")
        self.assertEqual(result, "nohtyp")
```


## Практические рекомендации для Middle разработчика

### Структура проекта

```
project/
├── src/
│   ├── __init__.py
│   ├── calculator.py
│   └── banking.py
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py
│   └── test_banking.py
├── requirements.txt
└── requirements-dev.txt
```


### Лучшие практики

**Именование тестов:**

- Используйте описательные имена: `test_deposit_increases_balance`
- Формат: `test_<what>_<when>_<expected>`

**Структура теста (AAA pattern):**

```python
def test_withdraw_valid_amount_decreases_balance():
    # Arrange
    account = BankAccount(1000)
    
    # Act
    account.withdraw(300)
    
    # Assert
    assert account.balance == 700
```

**Тестирование исключений:**

```python
def test_invalid_input_raises_value_error(self):
    with self.assertRaises(ValueError):
        self.calculator.divide(10, 0)
```


## Типичные ошибки и как их избежать

### Ошибка 1: Написание слишком много кода сразу

**Неправильно:**

```python
def add(self, a, b):
    # Сразу пишем полную реализацию
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    return a + b
```

**Правильно:** Пишите минимум кода для прохождения текущего теста.

### Ошибка 2: Пропуск фазы рефакторинга

После того, как тест проходит, не забывайте улучшать код:

- Удалять дублирование
- Улучшать читаемость
- Оптимизировать производительность


### Ошибка 3: Тестирование implementation details

**Неправильно:**

```python
def test_internal_method_called(self):
    # Тестируем внутренние детали реализации
    pass
```

**Правильно:** Тестируйте поведение, а не реализацию.

## Интеграция TDD с современными инструментами

### Continuous Integration

```yaml
# .github/workflows/tests.yml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
    - name: Install dependencies
      run: pip install -r requirements-dev.txt
    - name: Run tests
      run: pytest --cov=src tests/
```


### Coverage отчеты

```bash
pip install pytest-cov
pytest --cov=src --cov-report=html tests/
```


## Вопросы для собеседования

### Базовые вопросы:

- Что такое TDD и чем оно отличается от обычного тестирования?
- Объясните цикл Red-Green-Refactor
- Почему в TDD тесты пишутся до кода?
- Какие инструменты для TDD в Python вы знаете?


### Средний уровень:

- Как TDD влияет на архитектуру приложения?
- В каких случаях TDD может быть неэффективным?
- Как тестировать исключения в Python?
- Что такое test fixtures и зачем они нужны?


### Продвинутые вопросы:

- Как совмещать TDD с legacy кодом?
- Разница между unit, integration и acceptance тестами в контексте TDD
- Как TDD работает в команде? Код-ревью тестов?
- Мокирование и TDD — лучшие практики


## Заключение

TDD — это не просто методика тестирования, а **способ мышления** разработчика среднего уровня[^8]. Это дисциплина, которая приводит к написанию более качественного, поддерживаемого и надежного кода[^5].

Основные преимущества для Middle Python Developer:

- **Высокое покрытие тестами** по умолчанию
- **Лучший дизайн** благодаря "testability first" подходу
- **Уверенность в рефакторинге** и изменениях
- **Живая документация** через тесты
- **Быстрая обратная связь** при разработке

TDD требует практики и дисциплины, но результат — это код, который легко поддерживать, изменять и расширять. Это критически важный навык для современного Python-разработчика среднего уровня.

<div style="text-align: center">⁂</div>

[^1]: https://www.datacamp.com/tutorial/test-driven-development-in-python

[^2]: https://pytest-with-eric.com/tdd/pytest-tdd/

[^3]: https://testdriven.io/blog/modern-tdd/

[^4]: https://www.freecodecamp.org/news/learning-to-test-with-python-997ace2d8abe/

[^5]: https://bluebirdinternational.com/python-interview-questions-and-answers/

[^6]: https://www.thedigitalcatonline.com/blog/2020/09/10/tdd-in-python-with-pytest-part-1/

[^7]: https://www.xenonstack.com/blog/test-driven-development-python

[^8]: https://testlify.com/test-library/test-driven-development-tdd-test/

[^9]: https://ieeexplore.ieee.org/document/10500548/

[^10]: https://www.semanticscholar.org/paper/3d653d9fcf958b97cc553aa6f95388b5b2e43012

[^11]: https://ieeexplore.ieee.org/document/10530647/

[^12]: https://arxiv.org/abs/2211.06294

[^13]: https://journals.sagepub.com/doi/10.1177/0272989X231188027

[^14]: https://journals.humankinetics.com/view/journals/jmld/11/3/article-p555.xml

[^15]: https://bmcmedresmethodol.biomedcentral.com/articles/10.1186/s12874-022-01673-y

[^16]: https://link.springer.com/10.1007/s12206-022-0728-z

[^17]: https://www.youtube.com/watch?v=2jhFkFFwz-g

[^18]: https://www.w3resource.com/python-interview/testing.php

[^19]: https://www.youtube.com/watch?v=eAPmXQ0dC7Q

[^20]: https://github.com/JohnTrapp/python-tdd-example

[^21]: https://bridgeteams.com/blog/25-python-developer-interview-questions-to-ask-junior-middle-and-senior-programmers/

[^22]: https://www.reddit.com/r/learnpython/comments/10ss95z/how_important_is_tdd_in_python_and_other_testing/

[^23]: https://www.youtube.com/watch?v=ibVSPVz2LAA

[^24]: https://devskiller.com/coding-tests-skill/python/

[^25]: https://ieeexplore.ieee.org/document/10015309/

[^26]: https://onlinelibrary.wiley.com/doi/10.1002/sim.9234

[^27]: https://arxiv.org/pdf/1007.1722.pdf

[^28]: https://arxiv.org/pdf/2407.13249.pdf

[^29]: https://arxiv.org/pdf/2211.04630.pdf

[^30]: http://arxiv.org/pdf/1612.04251.pdf

[^31]: https://arxiv.org/pdf/2401.07576.pdf

[^32]: https://arxiv.org/html/2503.10699v1

[^33]: http://arxiv.org/pdf/2402.13521.pdf

[^34]: https://www.mdpi.com/1424-8220/22/23/9498/pdf?version=1670244368

[^35]: https://arxiv.org/pdf/1611.05994.pdf

[^36]: https://arxiv.org/pdf/2211.05939.pdf

[^37]: https://www.datacamp.com/blog/top-python-interview-questions-and-answers

[^38]: https://devskiller.com/coding-tests-seniority/middle/

[^39]: https://www.geeksforgeeks.org/python/python-interview-questions/

[^40]: https://resumeworded.com/interview-questions/junior-python-developer

