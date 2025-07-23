<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Изучение ООП Python для Middle Developer: Полный гайд к собеседованию

## 1. Введение в ООП

**Объектно-ориентированное программирование (ООП)** — это парадигма программирования, основанная на концепции объектов, которые содержат данные (атрибуты) и код (методы)[^1]. ООП повышает модульность, переиспользуемость и поддерживаемость кода[^1].

### Основные принципы ООП

#### Инкапсуляция

Объединение данных и методов в единый класс с ограничением прямого доступа к внутренней реализации[^1].

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Приватный атрибут
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
# print(account.__balance)  # AttributeError
```


#### Наследование

Механизм создания нового класса на основе существующего класса[^1].

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Buddy")
print(dog.speak())  # Buddy says Woof!
```


#### Полиморфизм

Способность объектов разных классов отвечать на одинаковые сообщения[^2].

```python
def make_sound(animal):
    return animal.speak()

animals = [Dog("Rex"), Cat("Whiskers")]
for animal in animals:
    print(make_sound(animal))
```


#### Абстракция

Сокрытие сложности реализации и предоставление простого интерфейса[^1].

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
```


## 2. Классы и объекты

### Создание класса и экземпляра

```python
class Car:
    # Атрибут класса
    wheels = 4
    
    def __init__(self, make, model):
        # Атрибуты экземпляра
        self.make = make
        self.model = model
    
    def start_engine(self):
        return f"{self.make} {self.model} engine started"

# Создание экземпляра
my_car = Car("Toyota", "Camry")
print(my_car.start_engine())  # Toyota Camry engine started
```


### Конструктор __init__

Метод `__init__` автоматически вызывается при создании объекта и используется для инициализации атрибутов[^3].

```python
class Person:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        print(f"Person {name} created")

person = Person("Alice", 25)  # Person Alice created
```


### Уровни доступа к атрибутам

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name           # Public
        self._department = "IT"    # Protected (convention)
        self.__salary = salary     # Private (name mangling)
    
    def get_salary(self):
        return self.__salary

emp = Employee("John", 50000)
print(emp.name)                    # OK: Public
print(emp._department)             # OK: Protected (но не рекомендуется)
# print(emp.__salary)              # AttributeError
print(emp._Employee__salary)       # OK: Name mangling
```


## 3. Инкапсуляция и property

### Работа с разными уровнями доступа

```python
class Student:
    def __init__(self, name, grade):
        self.name = name          # Public
        self._grade = grade       # Protected
        self.__id = id(self)      # Private
    
    def get_id(self):
        return self.__id

student = Student("Alice", 85)
print(student.name)           # Alice
print(student._grade)         # 85 (доступно, но не рекомендуется)
print(student.get_id())       # ID через метод
```


### Использование property и setter

```python
class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature cannot be below absolute zero")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

temp = Temperature(25)
print(temp.celsius)     # 25
print(temp.fahrenheit)  # 77.0
temp.celsius = 30       # Setter validation
```


## 4. Наследование и композиция

### Обычное наследование

```python
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def start(self):
        return "Vehicle started"

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors
    
    def start(self):
        return f"{self.make} car started"

car = Car("Honda", "Civic", 4)
print(car.start())  # Honda car started
```


### Множественное наследование

```python
class Flyable:
    def fly(self):
        return "Flying through the sky"

class Swimmable:
    def swim(self):
        return "Swimming in water"

class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return f"{self.name} says quack!"

duck = Duck("Donald")
print(duck.fly())    # Flying through the sky
print(duck.swim())   # Swimming in water
```


### MRO (Method Resolution Order) и super()

```python
class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")
        super().method()

class C(A):
    def method(self):
        print("C method")
        super().method()

class D(B, C):
    def method(self):
        print("D method")
        super().method()

d = D()
d.method()
# D method
# B method  
# C method
# A method

print(D.__mro__)  # Показывает порядок разрешения методов
```


### Композиция vs Наследование

```python
# Композиция
class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine started"

class Car:
    def __init__(self, make, engine):
        self.make = make
        self.engine = engine  # Композиция
    
    def start(self):
        return f"{self.make}: {self.engine.start()}"

engine = Engine(200)
car = Car("BMW", engine)
print(car.start())  # BMW: Engine started
```

**Когда использовать:**

- **Наследование**: отношение "is-a" (собака - это животное)
- **Композиция**: отношение "has-a" (машина имеет двигатель)


## 5. Полиморфизм и абстракция

### Абстрактные классы

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    @abstractmethod
    def refund_payment(self, transaction_id):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via credit card"
    
    def refund_payment(self, transaction_id):
        return f"Refunding transaction {transaction_id}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing ${amount} via PayPal"
    
    def refund_payment(self, transaction_id):
        return f"PayPal refund for {transaction_id}"
```


### Полиморфная функция

```python
def handle_payment(processor: PaymentProcessor, amount: float):
    return processor.process_payment(amount)

# Использование
processors = [
    CreditCardProcessor(),
    PayPalProcessor()
]

for processor in processors:
    print(handle_payment(processor, 100.0))
```


## 6. Практические задачи

### Иерархия сотрудников с расчетом зарплаты

```python
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary
    
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, base_salary, bonus=0):
        super().__init__(name, base_salary)
        self.bonus = bonus
    
    def calculate_salary(self):
        return self.base_salary + self.bonus

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    
    def calculate_salary(self):
        regular_hours = min(self.hours_worked, 40)
        overtime_hours = max(0, self.hours_worked - 40)
        return (regular_hours * self.hourly_rate + 
                overtime_hours * self.hourly_rate * 1.5)

class Manager(FullTimeEmployee):
    def __init__(self, name, base_salary, bonus, team_size):
        super().__init__(name, base_salary, bonus)
        self.team_size = team_size
    
    def calculate_salary(self):
        base = super().calculate_salary()
        return base + (self.team_size * 1000)

# Использование
employees = [
    FullTimeEmployee("Alice", 50000, 5000),
    HourlyEmployee("Bob", 25, 45),
    Manager("Charlie", 70000, 10000, 5)
]

for emp in employees:
    print(f"{emp.name}: ${emp.calculate_salary()}")
```


### Декоратор-кэширование для методов класса

```python
def cache_method(func):
    def wrapper(self, *args, **kwargs):
        if not hasattr(self, '_cache'):
            self._cache = {}
        
        key = (func.__name__, args, tuple(kwargs.items()))
        if key not in self._cache:
            self._cache[key] = func(self, *args, **kwargs)
        return self._cache[key]
    return wrapper

class Calculator:
    @cache_method
    def expensive_operation(self, n):
        print(f"Computing for {n}...")
        result = sum(i**2 for i in range(n))
        return result

calc = Calculator()
print(calc.expensive_operation(1000))  # Computing for 1000...
print(calc.expensive_operation(1000))  # Cached result
```


### Контекст-менеджер

```python
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print(f"Opening {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing {self.filename}")
        if self.file:
            self.file.close()
        if exc_type:
            print(f"Exception occurred: {exc_val}")
        return False

# Использование
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
```


### Дескриптор с валидацией

```python
class ValidatedAttribute:
    def __init__(self, name, validator):
        self.name = name
        self.validator = validator
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)
    
    def __set__(self, instance, value):
        if not self.validator(value):
            raise ValueError(f"Invalid value for {self.name}: {value}")
        instance.__dict__[self.name] = value

def positive_number(value):
    return isinstance(value, (int, float)) and value > 0

def non_empty_string(value):
    return isinstance(value, str) and len(value.strip()) > 0

class Product:
    price = ValidatedAttribute("price", positive_number)
    name = ValidatedAttribute("name", non_empty_string)
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Использование
product = Product("Laptop", 999.99)
# product.price = -100  # ValueError
```


## 7. Расширенные темы

### Data-классы

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class Point:
    x: float
    y: float
    
    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

@dataclass
class Person:
    name: str
    age: int
    skills: List[str] = field(default_factory=list)
    
    def add_skill(self, skill):
        self.skills.append(skill)

point = Point(3.0, 4.0)
print(point.distance_from_origin())  # 5.0

person = Person("Alice", 30)
person.add_skill("Python")
print(person)  # Person(name='Alice', age=30, skills=['Python'])
```


### Статические методы и методы класса

```python
class MathUtils:
    PI = 3.14159
    
    def __init__(self, precision=2):
        self.precision = precision
    
    @staticmethod
    def add(a, b):
        """Статический метод - не зависит от класса или экземпляра"""
        return a + b
    
    @classmethod
    def circle_area(cls, radius):
        """Метод класса - работает с атрибутами класса"""
        return cls.PI * radius ** 2
    
    def format_number(self, number):
        """Обычный метод экземпляра"""
        return f"{number:.{self.precision}f}"

# Использование
print(MathUtils.add(5, 3))           # 8
print(MathUtils.circle_area(5))      # 78.53975

utils = MathUtils(precision=3)
print(utils.format_number(3.14159))  # 3.142
```


### Магические методы

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"
    
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
    def __len__(self):
        return int((self.x**2 + self.y**2)**0.5)
    
    def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Vector index out of range")

v1 = Vector(2, 3)
v2 = Vector(1, 4)
v3 = v1 + v2
print(v3)      # Vector(3, 7)
print(len(v1)) # 3
print(v1[^0])   # 2
```


### Основные паттерны проектирования

#### Singleton

```python
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.initialized = True
            self.data = {}

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```


#### Factory

```python
class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, name):
        if animal_type.lower() == "dog":
            return Dog(name)
        elif animal_type.lower() == "cat":
            return Cat(name)
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")

class Dog:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} barks"

class Cat:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} meows"

# Использование
factory = AnimalFactory()
pet = factory.create_animal("dog", "Buddy")
print(pet.speak())  # Buddy barks
```


#### Strategy

```python
from abc import ABC, abstractmethod

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data):
        pass

class BubbleSort(SortStrategy):
    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

class QuickSort(SortStrategy):
    def sort(self, data):
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy
    
    def sort_data(self, data):
        return self.strategy.sort(data.copy())

# Использование
data = [64, 34, 25, 12, 22, 11, 90]
sorter = Sorter(QuickSort())
print(sorter.sort_data(data))  # Отсортированный список
```


## 8. Памятка по подготовке к собеседованию

### Наследование vs Композиция

**Когда использовать наследование:**

- Отношение "is-a" (является)
- Нужно переопределить поведение родительского класса
- Есть общий интерфейс для группы классов

**Когда использовать композицию:**

- Отношение "has-a" (имеет)
- Нужна гибкость в изменении поведения
- Хотите избежать глубоких иерархий наследования

```python
# Наследование: Собака - это животное
class Animal:
    def move(self):
        pass

class Dog(Animal):
    def move(self):
        return "runs"

# Композиция: У машины есть двигатель
class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Композиция
    
    def start(self):
        return self.engine.start()
```


### Ограничения и альтернативы ООП

**Ограничения ООП:**

- Избыточность для простых задач
- Сложность при неправильном проектировании
- Производительность (overhead от вызовов методов)

**Альтернативы:**

- Функциональное программирование
- Процедурное программирование
- Компонентно-ориентированное программирование


### Объяснение архитектурных решений на интервью

**Структура ответа:**

1. **Контекст**: Какую проблему решаем
2. **Варианты**: Какие подходы рассматривали
3. **Решение**: Что выбрали и почему
4. **Компромиссы**: Какие trade-offs приняли

**Пример:**
> "Для системы уведомлений мы рассматривали наследование и композицию. Выбрали Strategy pattern с композицией, потому что нужна возможность динамически менять способы доставки уведомлений. Это дает гибкость, но добавляет сложности в коде."

### Практические советы для подготовки

**Тренировка без автодополнения:**

1. Используйте простой текстовый редактор
2. Пишите код на бумаге
3. Практикуйте типовые паттерны до автоматизма
4. Запоминайте часто используемые методы и их сигнатуры

**Ключевые темы для повторения:**

- Основы ООП (инкапсуляция, наследование, полиморфизм, абстракция)
- MRO и super()
- Магические методы
- Property и дескрипторы
- Контекст-менеджеры
- Паттерны проектирования

**Типичные вопросы на собеседовании:**[^4][^5][^6]

- Объясните разницу между `__str__` и `__repr__`
- Как работает множественное наследование в Python?
- Что такое MRO и как его посмотреть?
- В чем разница между `@staticmethod` и `@classmethod`?
- Как реализовать Singleton в Python?
- Когда использовать композицию вместо наследования?

Этот гайд покрывает все основные аспекты ООП в Python для уровня middle developer. Регулярная практика с примерами кода и понимание принципов поможет успешно пройти техническое собеседование.

<div style="text-align: center">⁂</div>

[^1]: https://www.iosrjournals.org/iosr-jce/papers/Vol26-issue5/Ser-1/E2605012632.pdf

[^2]: https://innovationyourself.com/polymorphism-in-python/

[^3]: https://www.w3schools.com/python/python_classes.asp

[^4]: https://pynative.com/python-oop-interview-questions/

[^5]: https://www.hipeople.io/interview-questions/python-oops-interview-questions

[^6]: https://www.adaface.com/blog/python-oops-interview-questions/

[^7]: https://arxiv.org/abs/2408.14566

[^8]: https://www.ijfmr.com/research-paper.php?id=38912

[^9]: https://www.mdpi.com/2073-445X/12/2/434

[^10]: https://www.ajol.info/index.php/ahs/article/view/268169

[^11]: https://onlinelibrary.wiley.com/doi/10.1002/spe.3409

[^12]: https://www.frontiersin.org/articles/10.3389/feduc.2025.1568153/full

[^13]: http://medrxiv.org/lookup/doi/10.1101/2025.05.28.25328220

[^14]: http://www.ijirss.com/index.php/ijirss/article/view/2037

[^15]: https://formative.jmir.org/2023/1/e45250

[^16]: http://arxiv.org/pdf/2411.13200.pdf

[^17]: https://www.aclweb.org/anthology/2021.naacl-main.160.pdf

[^18]: https://arxiv.org/ftp/arxiv/papers/2201/2201.00650.pdf

[^19]: https://arxiv.org/pdf/1007.1722.pdf

[^20]: https://arxiv.org/pdf/2302.03307.pdf

[^21]: http://arxiv.org/pdf/1405.7470.pdf

[^22]: http://arxiv.org/pdf/2409.19916.pdf

[^23]: http://arxiv.org/pdf/2410.01010.pdf

[^24]: https://arxiv.org/pdf/2407.16732.pdf

[^25]: https://gjeta.com/sites/default/files/GJETA-2021-0119.pdf

[^26]: https://itvdn.com/ru/blog/article/interview-questions-python-developer

[^27]: https://www.webasha.com/blog/python-object-oriented-programming-interview-questions

[^28]: https://dev.to/devasservice/object-oriented-programming-oop-in-python-classes-and-objects-explained-26ek

[^29]: https://www.programiz.com/python-programming/class

[^30]: https://pynative.com/python-encapsulation/

[^31]: https://www.geeksforgeeks.org/python/python-multiple-inheritance-with-super-function/

[^32]: http://www.cs.unibo.it/~nuzzoles/courses/sw-applications/slides/7_OOP_part3.pdf

[^33]: https://www.w3resource.com/python-exercises/class-exercises/python-class-real-life-problem-1.php

[^34]: https://www.w3resource.com/python-exercises/decorator/python-decorator-exercise-4.php

[^35]: https://www.geeksforgeeks.org/interview-prep/oops-interview-questions/

[^36]: https://realpython.com/python3-object-oriented-programming/

[^37]: https://www.w3resource.com/python/how-to-implement-and-use-encapsulation.php

[^38]: https://www.datacamp.com/tutorial/super-multiple-inheritance-diamond-problem

[^39]: https://www.scribd.com/document/878429286/Lab-2-OOP

[^40]: https://www.w3resource.com/python-exercises/decorator/python-decorator-exercise-12.php

