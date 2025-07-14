# Принципы SOLID и паттерны проектирования: Руководство для Middle-разработчиков

## Часть 1: Теория

### Введение в SOLID

SOLID — это акроним пяти принципов объектно-ориентированного программирования, которые помогают создавать более гибкий, понятный и поддерживаемый код. Эти принципы не являются догмой, но служат ориентиром для принятия архитектурных решений.

## 1. Single Responsibility Principle (SRP)

**Принцип единственной ответственности**: 
Это принцип объектно-ориентированного программирования, который гласит, что каждый класс или модуль должен иметь только одну причину для изменения. Иными словами, каждый класс или модуль должен отвечать за одну конкретную функциональность или задачу, и все его действия должны быть направлены на ее выполнение.
**Определение ответственности:**
Каждый класс или модуль должен иметь четко определенную область ответственности. Это означает, что он должен решать только одну задачу и не должен быть перегружен несвязанными функциями.
**Преимущества SRP:**
Улучшенная читаемость и понимание кода: Разделение ответственности упрощает понимание каждого класса или модуля. 
Повышенная гибкость и переиспользование: Классы с четкой ответственностью легче переиспользовать в других частях системы или в других проектах. 
Упрощенное тестирование: Тестирование классов с одной ответственностью значительно проще, так как они имеют меньшую сложность. 
Снижение вероятности ошибок: Изменения в одном классе, как правило, не должны влиять на другие, что уменьшает вероятность ошибок при внесении изменений. 

### Плохой пример:

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        # Логика сохранения в БД
        print(f"Saving {self.name} to database")
    
    def send_email(self, message):
        # Логика отправки email
        print(f"Sending email to {self.email}: {message}")
    
    def validate_email(self):
        # Логика валидации email
        return "@" in self.email
```

**Проблемы:**

- Класс отвечает за данные пользователя, работу с БД и отправку email
- Изменения в логике БД затронут класс User
- Сложно тестировать отдельные функции


### Хороший пример:

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to database")

class EmailService:
    def send(self, email, message):
        print(f"Sending email to {email}: {message}")

class EmailValidator:
    @staticmethod
    def validate(email):
        return "@" in email
```


### Почему это важно:

- **Поддерживаемость**: Изменения в одной области не влияют на другие
- **Тестируемость**: Каждый класс можно тестировать изолированно
- **Переиспользование**: Компоненты можно использовать в разных контекстах


## 2. Open/Closed Principle (OCP)

**Принцип открытости/закрытости**: 
Принцип открытости/закрытости (Open/Closed Principle - OCP) является одним из пяти принципов SOLID и гласит, что программные сущности (классы, модули, функции и т.д.) должны быть открыты для расширения, но закрыты для модификации. Это означает, что поведение сущности можно расширять, не изменяя существующий код этой сущности. 
**Суть принципа:**
**Открытость для расширения:**
Сущность должна позволять добавлять новую функциональность без необходимости изменения ее исходного кода.
Закрытость для модификации:
После того, как сущность была разработана и протестирована, ее исходный код не должен изменяться. 
Зачем нужен OCP?
**Снижение рисков:**
Изменение существующего кода может привести к неожиданным ошибкам и сбоям в работе системы. OCP помогает минимизировать эти риски, позволяя расширять функциональность, не затрагивая проверенный код. 
**Улучшение поддерживаемости:**
Когда новые функции добавляются через расширение, а не через изменение существующего кода, система становится более предсказуемой и легче поддерживаемой. 
**Повышение гибкости:**
OCP способствует созданию более гибких систем, которые могут легко адаптироваться к меняющимся требованиям без значительных переделок. 
**Как реализовать OCP?**
Существует несколько подходов к реализации OCP, включая:
Интерфейсы и абстрактные классы:
Определение интерфейсов или абстрактных классов, которые задают общую структуру поведения, а затем создание конкретных реализаций, наследующих или реализующих эти интерфейсы. 
**Полиморфизм:**
Использование полиморфизма позволяет вызывать методы объектов разных классов, не зная их конкретного типа, что позволяет расширять функциональность без изменения существующего кода. 
**Наследование:**
Расширение функциональности существующего класса путем создания подклассов, которые наследуют его поведение и добавляют новое. 
**Композиция:**
Создание новых классов путем объединения существующих, что позволяет строить сложную функциональность из простых блоков, не изменяя исходный код базовых классов.

### Плохой пример:

```python
class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Processing credit card payment: ${amount}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment: ${amount}")
        elif payment_type == "bitcoin":  # Новый тип - нужно модифицировать класс
            print(f"Processing Bitcoin payment: ${amount}")
```


### Хороший пример:

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing credit card payment: ${amount}")

class PayPalPayment(PaymentMethod):
    def process(self, amount):
        print(f"Processing PayPal payment: ${amount}")

class BitcoinPayment(PaymentMethod):  # Новый тип - просто добавляем класс
    def process(self, amount):
        print(f"Processing Bitcoin payment: ${amount}")

class PaymentProcessor:
    def process_payment(self, payment_method: PaymentMethod, amount):
        payment_method.process(amount)
```


### Почему это важно:

- **Расширяемость**: Новый функционал добавляется без изменения существующего кода
- **Стабильность**: Меньше риска сломать работающий код
- **Масштабируемость**: Легко добавлять новые типы без рефакторинга


## 3. Liskov Substitution Principle (LSP)

**Принцип подстановки Лисков**: 
Принцип подстановки Барбары Лисков (LSP) гласит, что объекты-наследники должны быть заменяемы объектами-родителями без нарушения корректности работы программы. Иными словами, если функция ожидает объект базового класса, то она должна корректно работать и с объектом любого его подкласса. 
**Суть принципа:**
**Заменяемость:**
Подтипы должны вести себя так, чтобы их можно было использовать вместо базового типа в любом месте, где он используется, не вызывая ошибок или неожиданного поведения. 
**Контракт:**
Подклассы не должны изменять предусловия, постусловия или инварианты базового класса. Если метод в базовом классе принимает объект определенного типа, то метод в подклассе не должен требовать большего или возвращать меньше, чем предусмотрено в базовом классе. 
**Исключения:**
Подкласс не должен генерировать исключения, не предусмотренные базовым классом. 
**Пример:**
Предположим, у нас есть базовый класс Shape (Фигура) и подкласс Rectangle (Прямоугольник). Если функция ожидает объект Shape, она должна корректно работать и с объектом Rectangle, не ожидая, что это обязательно прямоугольник. 
Нарушением LSP будет, если, например, метод, предназначенный для работы с Shape, ожидает, что у фигуры будет только два измерения (ширина и высота), а Rectangle имеет еще и четвертое измерение, или метод, работающий с Shape, не может корректно обработать объект Rectangle, если его ширина и высота отличаются. 
**Значение LSP:**
**Улучшение полиморфизма:**
LSP позволяет использовать полиморфизм в полной мере, делая код более гибким и расширяемым.
**Упрощение поддержки кода:**
Благодаря LSP, при изменении или добавлении новых подклассов нет необходимости переписывать код, использующий базовый класс.
**Повышение надежности:**
Соблюдение LSP уменьшает вероятность ошибок и неожиданного поведения в программе.
**Сокращение дублирования кода:**
LSP позволяет повторно использовать код, написанный для базового класса, в подклассах. 
*В заключение:* LSP является важным принципом объектно-ориентированного проектирования, который способствует созданию надежного, гибкого и поддерживаемого программного обеспечения. Его соблюдение обеспечивает возможность безопасной замены подклассов базовыми классами, что является основой полиморфизма и модульности.

### Плохой пример:

```python
class Bird:
    def fly(self):
        print("Flying")

class Penguin(Bird):
    def fly(self):
        raise Exception("Penguins can't fly!")  # Нарушает контракт

def make_bird_fly(bird: Bird):
    bird.fly()  # Может упасть с пингвином
```


### Хороший пример:

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        self.fly()
    
    def fly(self):
        print("Flying")

class FlightlessBird(Bird):
    def move(self):
        self.walk()
    
    def walk(self):
        print("Walking")

class Eagle(FlyingBird):
    pass

class Penguin(FlightlessBird):
    pass

def make_bird_move(bird: Bird):
    bird.move()  # Работает для всех подтипов
```


### Почему это важно:

- **Предсказуемость**: Подклассы ведут себя как ожидается от базового класса
- **Полиморфизм**: Можно безопасно использовать наследование
- **Надежность**: Меньше неожиданных исключений в runtime


## 4. Interface Segregation Principle (ISP)

**Принцип разделения интерфейсов**: 
Принцип разделения интерфейсов (Interface Segregation Principle, ISP) гласит, что клиенты не должны зависеть от методов, которые они не используют. Другими словами, интерфейсы должны быть "маленькими" и "узкоспециализированными", чтобы классы реализовывали только те методы, которые им действительно нужны. Это предотвращает ситуацию, когда класс вынужден реализовывать методы, не относящиеся к его функциональности, и упрощает разработку и сопровождение кода. 
Подробное объяснение:
Принцип ISP, как часть принципов SOLID, направлен на уменьшение связанности между классами и повышение гибкости системы. Вот как это работает на практике: 
**Избегание "жирных" интерфейсов:**
Если у вас есть интерфейс с большим количеством методов, некоторые из которых не относятся к конкретной задаче, то класс, реализующий этот интерфейс, будет вынужден реализовывать все методы, даже если они не нужны. Это приводит к избыточности и усложнению кода.
**Разделение на более мелкие интерфейсы:**
Вместо одного "жирного" интерфейса, следует создавать несколько более мелких, каждый из которых предоставляет конкретный набор методов для определенной цели.
**Улучшение поддержки и расширяемости:**
Когда интерфейсы разделены, изменения в одном интерфейсе не влияют на другие, если они не зависят от этого интерфейса. Это делает систему более устойчивой к изменениям и упрощает добавление новой функциональности.
**Упрощение тестирования:**
Когда интерфейсы маленькие и узкоспециализированные, их легче тестировать, так как каждый интерфейс отвечает за определенную функциональность.
**Пример нарушения ISP:**
Предположим, у нас есть интерфейс Worker, который содержит методы work(), eat(), sleep(), drink(). Если класс Programmer реализует этот интерфейс, он будет вынужден реализовывать все методы, включая eat(), sleep(), drink(), хотя они не имеют отношения к его основной задаче. Это нарушение ISP. 
Пример применения ISP:
Вместо одного интерфейса Worker, можно создать несколько интерфейсов: IWorkable, IEatable, ISleepable. Класс Programmer может реализовывать только IWorkable, класс Human может реализовывать все три, а класс Robot может реализовывать только IWorkable. Такой подход позволяет каждому классу реализовывать только необходимые ему интерфейсы. 
В заключение:
Принцип разделения интерфейсов (ISP) является важной частью проектирования гибких и поддерживаемых систем. Следуя этому принципу, можно избежать создания "жирных" интерфейсов, повысить связанность кода и упростить процесс разработки и сопровождения. 

### Плохой пример:

```python
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass

class Robot(Worker):
    def work(self):
        print("Robot working")
    
    def eat(self):
        raise NotImplementedError("Robots don't eat")  # Вынужден реализовывать
    
    def sleep(self):
        raise NotImplementedError("Robots don't sleep")  # Вынужден реализовывать
```


### Хороший пример:

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working")
    
    def eat(self):
        print("Human eating")
    
    def sleep(self):
        print("Human sleeping")

class Robot(Workable):  # Реализует только нужный интерфейс
    def work(self):
        print("Robot working")
```


### Почему это важно:

- **Гибкость**: Классы реализуют только нужные им интерфейсы
- **Минимизация зависимостей**: Меньше связанности между компонентами
- **Простота тестирования**: Легче создавать моки для небольших интерфейсов


## 5. Dependency Inversion Principle (DIP)

**Принцип инверсии зависимостей**: 
Принцип инверсии зависимостей (DIP) утверждает, что модули верхних уровней не должны зависеть от модулей нижних уровней. Оба типа модулей должны зависеть от абстракций. Абстракции, в свою очередь, не должны зависеть от деталей, детали должны зависеть от абстракций. Другими словами, для уменьшения связности и повышения гибкости кода, необходимо избегать жесткой привязки к конкретным реализациям, а вместо этого использовать абстракции, такие как интерфейсы или абстрактные классы. 
**Суть принципа в двух частях:**
1. Модули верхних уровней (бизнес-логика, основные компоненты системы) не должны зависеть от модулей нижних уровней (конкретных реализаций, деталей).
Вместо этого, они должны зависеть от абстракций. 
2. Абстракции не должны зависеть от деталей. Детали должны зависеть от абстракций.
Это означает, что конкретные реализации должны быть "подчинены" абстракциям, а не наоборот. 
Как применяется DIP:
**Работа с абстракциями:**
Вместо того, чтобы использовать конкретные классы в качестве зависимостей, необходимо использовать интерфейсы или абстрактные классы. 
**Инверсия зависимостей:**
Зависимости должны "внедряться" извне, например, через конструктор или сеттеры, а не создаваться внутри класса. Это часто достигается с помощью шаблонов проектирования, таких как внедрение зависимостей (Dependency Injection). 
**Минимизация жёсткой связанности:**
Высокоуровневые модули не должны знать о деталях реализации низкоуровневых, чтобы изменения в последних не влияли на первые. 
Пример:
Представьте систему, в которой есть класс EmailSender, который отправляет электронные письма. Вместо того, чтобы этот класс напрямую зависел от конкретного SMTP-сервера, лучше создать интерфейс MessageSender с методом send(message) и реализовать его для разных протоколов (например, SmtpSender, RestApiSender). Тогда EmailSender будет зависеть от MessageSender (абстракции), а не от конкретной реализации. 
Преимущества DIP:
**Повышенная гибкость:**
Изменение реализации не требует изменений в других частях системы.
**Улучшенная модульность:**
Система становится более разделенной на независимые модули, что облегчает разработку и поддержку.
**Упрощенное тестирование:**
Можно легко подменять конкретные реализации абстракций тестовыми заглушками.
**Более удобная масштабируемость:**
Новые функциональности могут быть добавлены без внесения изменений в существующий код. 

### Плохой пример:

```python
class MySQLDatabase:
    def save(self, data):
        print(f"Saving to MySQL: {data}")

class UserService:
    def __init__(self):
        self.db = MySQLDatabase()  # Жесткая зависимость
    
    def create_user(self, user_data):
        # Логика создания пользователя
        self.db.save(user_data)
```


### Хороший пример:

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving to MySQL: {data}")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving to PostgreSQL: {data}")

class UserService:
    def __init__(self, database: Database):  # Зависимость от абстракции
        self.db = database
    
    def create_user(self, user_data):
        # Логика создания пользователя
        self.db.save(user_data)

# Использование
mysql_db = MySQLDatabase()
user_service = UserService(mysql_db)
```


### Почему это важно:

- **Тестируемость**: Легко подставлять моки вместо реальных зависимостей
- **Гибкость**: Можно менять реализации без изменения бизнес-логики
- **Развязанность**: Компоненты не знают о конкретных реализациях


## Часть 2: Практика

### Рефакторинг "грязного" кода

Рассмотрим пример веб-приложения с нарушениями SOLID:

#### Исходный код (с нарушениями):

```python
import json
import smtplib
from email.mime.text import MIMEText

class UserManager:
    def __init__(self):
        self.users = []
    
    def create_user(self, name, email, password):
        # Валидация (нарушение SRP)
        if not email or "@" not in email:
            raise ValueError("Invalid email")
        if len(password) < 8:
            raise ValueError("Password too short")
        
        # Создание пользователя
        user = {
            "id": len(self.users) + 1,
            "name": name,
            "email": email,
            "password": password
        }
        
        # Сохранение (нарушение SRP)
        self.users.append(user)
        with open("users.json", "w") as f:
            json.dump(self.users, f)
        
        # Отправка email (нарушение SRP)
        msg = MIMEText(f"Welcome, {name}!")
        msg['Subject'] = 'Welcome'
        msg['From'] = 'admin@example.com'
        msg['To'] = email
        
        server = smtplib.SMTP('localhost')
        server.send_message(msg)
        server.quit()
        
        return user
    
    def get_user_report(self, user_id, format_type):
        # Нарушение OCP - для нового формата нужно менять метод
        user = next((u for u in self.users if u["id"] == user_id), None)
        if not user:
            return None
        
        if format_type == "json":
            return json.dumps(user)
        elif format_type == "xml":
            return f"<user><name>{user['name']}</name><email>{user['email']}</email></user>"
        elif format_type == "csv":
            return f"{user['name']},{user['email']}"
```


#### Рефакторинг по шагам:

**Шаг 1: Применяем SRP**

```python
from abc import ABC, abstractmethod
from typing import Dict, List, Optional

class User:
    def __init__(self, user_id: int, name: str, email: str, password: str):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password

class UserValidator:
    @staticmethod
    def validate_email(email: str) -> bool:
        return email and "@" in email
    
    @staticmethod
    def validate_password(password: str) -> bool:
        return len(password) >= 8

class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> None:
        pass
    
    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        pass

class FileUserRepository(UserRepository):
    def __init__(self, filename: str = "users.json"):
        self.filename = filename
        self.users: List[User] = []
    
    def save(self, user: User) -> None:
        self.users.append(user)
        # Сохранение в файл
    
    def find_by_id(self, user_id: int) -> Optional[User]:
        return next((u for u in self.users if u.id == user_id), None)

class EmailService(ABC):
    @abstractmethod
    def send_welcome_email(self, user: User) -> None:
        pass

class SMTPEmailService(EmailService):
    def send_welcome_email(self, user: User) -> None:
        # Логика отправки email
        print(f"Sending welcome email to {user.email}")
```

**Шаг 2: Применяем OCP с паттерном Strategy**

```python
class ReportFormatter(ABC):
    @abstractmethod
    def format(self, user: User) -> str:
        pass

class JSONReportFormatter(ReportFormatter):
    def format(self, user: User) -> str:
        return json.dumps({
            "id": user.id,
            "name": user.name,
            "email": user.email
        })

class XMLReportFormatter(ReportFormatter):
    def format(self, user: User) -> str:
        return f"<user><name>{user.name}</name><email>{user.email}</email></user>"

class CSVReportFormatter(ReportFormatter):
    def format(self, user: User) -> str:
        return f"{user.name},{user.email}"

class ReportService:
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def generate_report(self, user_id: int, formatter: ReportFormatter) -> Optional[str]:
        user = self.repository.find_by_id(user_id)
        if not user:
            return None
        return formatter.format(user)
```

**Шаг 3: Применяем DIP**

```python
class UserService:
    def __init__(self, 
                 repository: UserRepository, 
                 email_service: EmailService,
                 validator: UserValidator):
        self.repository = repository
        self.email_service = email_service
        self.validator = validator
        self._next_id = 1
    
    def create_user(self, name: str, email: str, password: str) -> User:
        # Валидация
        if not self.validator.validate_email(email):
            raise ValueError("Invalid email")
        if not self.validator.validate_password(password):
            raise ValueError("Password too short")
        
        # Создание пользователя
        user = User(self._next_id, name, email, password)
        self._next_id += 1
        
        # Сохранение
        self.repository.save(user)
        
        # Отправка email
        self.email_service.send_welcome_email(user)
        
        return user
```


### Применение паттернов проектирования

#### 1. Factory Pattern + SRP

```python
class UserRepositoryFactory:
    @staticmethod
    def create(repo_type: str) -> UserRepository:
        if repo_type == "file":
            return FileUserRepository()
        elif repo_type == "database":
            return DatabaseUserRepository()
        else:
            raise ValueError(f"Unknown repository type: {repo_type}")

class EmailServiceFactory:
    @staticmethod
    def create(service_type: str) -> EmailService:
        if service_type == "smtp":
            return SMTPEmailService()
        elif service_type == "mock":
            return MockEmailService()
        else:
            raise ValueError(f"Unknown email service type: {service_type}")
```


#### 2. Observer Pattern + OCP

```python
class UserEvent:
    def __init__(self, event_type: str, user: User):
        self.event_type = event_type
        self.user = user

class UserEventListener(ABC):
    @abstractmethod
    def handle(self, event: UserEvent) -> None:
        pass

class EmailNotificationListener(UserEventListener):
    def __init__(self, email_service: EmailService):
        self.email_service = email_service
    
    def handle(self, event: UserEvent) -> None:
        if event.event_type == "user_created":
            self.email_service.send_welcome_email(event.user)

class LoggingListener(UserEventListener):
    def handle(self, event: UserEvent) -> None:
        print(f"Event: {event.event_type} for user {event.user.name}")

class UserEventPublisher:
    def __init__(self):
        self.listeners: List[UserEventListener] = []
    
    def subscribe(self, listener: UserEventListener) -> None:
        self.listeners.append(listener)
    
    def publish(self, event: UserEvent) -> None:
        for listener in self.listeners:
            listener.handle(event)

# Обновленный UserService
class UserService:
    def __init__(self, 
                 repository: UserRepository, 
                 validator: UserValidator,
                 event_publisher: UserEventPublisher):
        self.repository = repository
        self.validator = validator
        self.event_publisher = event_publisher
        self._next_id = 1
    
    def create_user(self, name: str, email: str, password: str) -> User:
        # Валидация и создание пользователя
        if not self.validator.validate_email(email):
            raise ValueError("Invalid email")
        if not self.validator.validate_password(password):
            raise ValueError("Password too short")
        
        user = User(self._next_id, name, email, password)
        self._next_id += 1
        
        # Сохранение
        self.repository.save(user)
        
        # Публикация события
        self.event_publisher.publish(UserEvent("user_created", user))
        
        return user
```


#### 3. Decorator Pattern + SRP

```python
class UserServiceDecorator(ABC):
    def __init__(self, user_service: UserService):
        self.user_service = user_service
    
    def create_user(self, name: str, email: str, password: str) -> User:
        return self.user_service.create_user(name, email, password)

class LoggingUserServiceDecorator(UserServiceDecorator):
    def create_user(self, name: str, email: str, password: str) -> User:
        print(f"Creating user: {name}")
        try:
            user = super().create_user(name, email, password)
            print(f"User created successfully: {user.id}")
            return user
        except Exception as e:
            print(f"Failed to create user: {e}")
            raise

class CachingUserServiceDecorator(UserServiceDecorator):
    def __init__(self, user_service: UserService):
        super().__init__(user_service)
        self.cache = {}
    
    def create_user(self, name: str, email: str, password: str) -> User:
        cache_key = f"{name}:{email}"
        if cache_key in self.cache:
            return self.cache[cache_key]
        
        user = super().create_user(name, email, password)
        self.cache[cache_key] = user
        return user
```


### Реальные кейсы применения

#### Кейс 1: Рефакторинг CLI-инструмента

```python
# До рефакторинга
class CLITool:
    def run(self, args):
        if args[0] == "backup":
            # Логика бэкапа
            files = os.listdir(".")
            with zipfile.ZipFile("backup.zip", "w") as zf:
                for file in files:
                    zf.write(file)
            print("Backup created")
        elif args[0] == "restore":
            # Логика восстановления
            with zipfile.ZipFile("backup.zip", "r") as zf:
                zf.extractall(".")
            print("Backup restored")

# После рефакторинга
class Command(ABC):
    @abstractmethod
    def execute(self, args: List[str]) -> None:
        pass

class BackupCommand(Command):
    def __init__(self, backup_service: BackupService):
        self.backup_service = backup_service
    
    def execute(self, args: List[str]) -> None:
        self.backup_service.create_backup()

class RestoreCommand(Command):
    def __init__(self, backup_service: BackupService):
        self.backup_service = backup_service
    
    def execute(self, args: List[str]) -> None:
        self.backup_service.restore_backup()

class CommandRegistry:
    def __init__(self):
        self.commands: Dict[str, Command] = {}
    
    def register(self, name: str, command: Command) -> None:
        self.commands[name] = command
    
    def execute(self, name: str, args: List[str]) -> None:
        if name in self.commands:
            self.commands[name].execute(args)
        else:
            print(f"Unknown command: {name}")
```


#### Кейс 2: Рефакторинг микросервиса

```python
# Применение всех принципов SOLID в микросервисе
class OrderService:
    def __init__(self, 
                 order_repository: OrderRepository,
                 payment_processor: PaymentProcessor,
                 notification_service: NotificationService,
                 event_publisher: EventPublisher):
        self.order_repository = order_repository
        self.payment_processor = payment_processor
        self.notification_service = notification_service
        self.event_publisher = event_publisher
    
    def process_order(self, order_data: Dict) -> Order:
        # SRP: каждый компонент отвечает за свою область
        order = Order.from_dict(order_data)
        
        # DIP: зависим от абстракций
        self.order_repository.save(order)
        
        # OCP: можем добавлять новые способы оплаты
        payment_result = self.payment_processor.process(order.payment_info)
        
        if payment_result.success:
            order.mark_as_paid()
            self.order_repository.update(order)
            
            # Observer: публикуем события
            self.event_publisher.publish(OrderPaidEvent(order))
        
        return order
```


## Чек-лист для Middle-разработчика

### ✅ Single Responsibility Principle

- [ ] Каждый класс имеет одну четко определенную ответственность
- [ ] Класс изменяется только по одной причине
- [ ] Методы класса связаны с его основной ответственностью
- [ ] Нет "божественных объектов" (God Objects)


### ✅ Open/Closed Principle

- [ ] Новый функционал добавляется через наследование или композицию
- [ ] Существующий код не модифицируется при добавлении новых возможностей
- [ ] Используются абстракции для расширения поведения
- [ ] Условные конструкции (if/elif) заменены полиморфизмом где возможно


### ✅ Liskov Substitution Principle

- [ ] Подклассы могут заменять базовые классы без нарушения логики
- [ ] Предусловия в подклассах не усиливаются
- [ ] Постусловия в подклассах не ослабляются
- [ ] Исключения в подклассах соответствуют базовому классу


### ✅ Interface Segregation Principle

- [ ] Интерфейсы содержат только связанные методы
- [ ] Клиенты не зависят от неиспользуемых методов
- [ ] Большие интерфейсы разделены на более мелкие и специфичные
- [ ] Используется композиция интерфейсов вместо наследования


### ✅ Dependency Inversion Principle

- [ ] Высокоуровневые модули не зависят от низкоуровневых
- [ ] Зависимости инжектируются через конструктор или параметры
- [ ] Используются абстракции вместо конкретных классов
- [ ] Легко подменять зависимости для тестирования


### ✅ Общие вопросы архитектуры

- [ ] Код легко тестируется (высокая тестируемость)
- [ ] Компоненты слабо связаны (low coupling)
- [ ] Компоненты высоко сплочены (high cohesion)
- [ ] Архитектура поддерживает изменения требований
- [ ] Код читается и понимается другими разработчиками


### ✅ Паттерны проектирования

- [ ] Паттерны применяются осознанно, а не ради самих паттернов
- [ ] Выбранные паттерны решают реальные проблемы
- [ ] Паттерны не усложняют простые задачи
- [ ] Код остается понятным после применения паттернов

**Помните**: SOLID — это инструмент, а не цель. Главная цель — создание качественного, поддерживаемого кода, который решает бизнес-задачи.

