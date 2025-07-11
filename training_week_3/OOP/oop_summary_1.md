<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" class="logo" width="120"/>

# Полный конспект по ООП в Python для Middle-разработчика (Расширенная версия)

## 📋 План обучения (7-10 дней интенсивной подготовки)

### Этап 1: Фундаментальные основы (3-4 дня)

#### День 1-2: Классы и объекты

**Время изучения:** 6-8 часов

**Подробная теоретическая база:**

**Класс** — это фундаментальная концепция объектно-ориентированного программирования, представляющая собой шаблон или чертеж для создания объектов. Класс определяет структуру данных (атрибуты) и поведение (методы), которые будут характерны для всех объектов, созданных на его основе. В Python класс создается с помощью ключевого слова `class`, за которым следует имя класса (по соглашению с заглавной буквы) и двоеточие.

**Объект (экземпляр)** — это конкретная реализация класса, созданная в памяти компьютера. Каждый объект имеет свое уникальное состояние (значения атрибутов), но разделяет общее поведение (методы) с другими объектами того же класса. Процесс создания объекта называется инстанцированием.

**Ключевые концепции:**

1. **Атрибуты класса** — переменные, которые принадлежат самому классу и разделяются всеми его экземплярами. Они определяются непосредственно в теле класса, вне методов.
2. **Атрибуты экземпляра** — переменные, которые принадлежат конкретному объекту и уникальны для каждого экземпляра. Обычно определяются в методе `__init__`.
3. **Методы** — функции, определенные внутри класса, которые описывают поведение объектов. Первым параметром всегда принимают `self` (ссылку на текущий экземпляр).
```python
# Определение класса
class Car:
    # Атрибуты класса (общие для всех экземпляров)
    wheels = 4
    manufacturer_country = "Unknown"
    total_cars_created = 0  # Счетчик созданных автомобилей
    
    # Конструктор класса - специальный метод для инициализации объекта
    def __init__(self, brand, model, year, color="white", engine_volume=1.6):
        # Атрибуты экземпляра (уникальные для каждого объекта)
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.engine_volume = engine_volume
        self.mileage = 0
        self.is_running = False
        self.fuel_level = 50  # Процент топлива
        self.max_speed = 180
        
        # Увеличиваем счетчик созданных автомобилей
        Car.total_cars_created += 1
        
        # Генерируем уникальный VIN номер
        self.vin = self._generate_vin()
    
    def _generate_vin(self):
        """Приватный метод для генерации VIN номера"""
        import random
        return f"VIN{random.randint(100000, 999999)}"
    
    # Методы экземпляра
    def start_engine(self):
        """Запуск двигателя с проверкой условий"""
        if self.fuel_level <= 0:
            return f"{self.brand} {self.model}: Нет топлива для запуска"
        
        if not self.is_running:
            self.is_running = True
            self.fuel_level -= 1  # Расход топлива при запуске
            return f"{self.brand} {self.model} заведена. Уровень топлива: {self.fuel_level}%"
        return f"{self.brand} {self.model} уже работает"
    
    def drive(self, distance):
        """Поездка на определенное расстояние"""
        if not self.is_running:
            return "Сначала заведите машину!"
        
        if distance <= 0:
            return "Расстояние должно быть положительным"
        
        # Расчет расхода топлива (1 литр на 10 км)
        fuel_needed = distance / 10
        
        if fuel_needed > self.fuel_level:
            max_distance = self.fuel_level * 10
            return f"Недостаточно топлива. Можно проехать максимум {max_distance} км"
        
        self.mileage += distance
        self.fuel_level -= fuel_needed
        return f"Проехали {distance} км. Общий пробег: {self.mileage} км. Топлива осталось: {self.fuel_level:.1f}%"
    
    def stop_engine(self):
        """Остановка двигателя"""
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model} заглушена"
        return f"{self.brand} {self.model} уже не работает"
    
    def refuel(self, amount):
        """Заправка автомобиля"""
        if amount <= 0:
            return "Количество топлива должно быть положительным"
        
        if self.fuel_level + amount > 100:
            amount = 100 - self.fuel_level
        
        self.fuel_level += amount
        return f"Заправлено {amount}% топлива. Текущий уровень: {self.fuel_level}%"
    
    def get_info(self):
        """Получение полной информации об автомобиле"""
        status = "работает" if self.is_running else "заглушена"
        return (f"{self.brand} {self.model} ({self.year}), цвет: {self.color}, "
                f"объем двигателя: {self.engine_volume}л, пробег: {self.mileage} км, "
                f"топливо: {self.fuel_level}%, статус: {status}")
    
    # Методы класса
    @classmethod
    def get_total_cars(cls):
        """Получение общего количества созданных автомобилей"""
        return f"Всего создано автомобилей: {cls.total_cars_created}"
    
    @classmethod
    def create_default_car(cls):
        """Создание автомобиля с параметрами по умолчанию"""
        return cls("Generic", "Model", 2020)
    
    # Статические методы
    @staticmethod
    def calculate_fuel_cost(distance, fuel_price_per_liter, consumption_per_100km):
        """Расчет стоимости топлива для поездки"""
        fuel_needed = (distance / 100) * consumption_per_100km
        total_cost = fuel_needed * fuel_price_per_liter
        return f"Для поездки на {distance} км потребуется {fuel_needed:.2f} л топлива, стоимость: {total_cost:.2f} руб."

# Создание объектов (экземпляров)
car1 = Car("Toyota", "Camry", 2020, "red", 2.5)
car2 = Car("BMW", "X5", 2021, "black", 3.0)
car3 = Car("Lada", "Vesta", 2019)  # Используем значения по умолчанию

# Использование методов экземпляра
print(car1.start_engine())  # Toyota Camry заведена. Уровень топлива: 49%
print(car1.drive(50))       # Проехали 50 км. Общий пробег: 50 км. Топлива осталось: 44.0%
print(car1.refuel(20))      # Заправлено 20% топлива. Текущий уровень: 64.0%
print(car1.get_info())      # Полная информация об автомобиле

# Использование методов класса
print(Car.get_total_cars())  # Всего создано автомобилей: 3
default_car = Car.create_default_car()

# Использование статических методов
print(Car.calculate_fuel_cost(100, 50, 8))  # Расчет стоимости топлива

# Доступ к атрибутам класса и экземпляра
print(f"У {car1.brand} {car1.wheels} колеса")  # У Toyota 4 колеса
print(f"Цвет BMW: {car2.color}")               # Цвет BMW: black
```

**Важные концепции с подробными объяснениями:**

**1. Разница между атрибутами класса и экземпляра:**

```python
class Example:
    class_attr = "Я принадлежу классу"  # Атрибут класса
    
    def __init__(self, instance_value):
        self.instance_attr = instance_value  # Атрибут экземпляра

obj1 = Example("Первый объект")
obj2 = Example("Второй объект")

# Атрибуты класса одинаковы для всех экземпляров
print(obj1.class_attr)     # Я принадлежу классу
print(obj2.class_attr)     # Я принадлежу классу

# Атрибуты экземпляра уникальны
print(obj1.instance_attr)  # Первый объект
print(obj2.instance_attr)  # Второй объект

# Изменение атрибута класса влияет на все экземпляры
Example.class_attr = "Изменено для всех"
print(obj1.class_attr)     # Изменено для всех
print(obj2.class_attr)     # Изменено для всех

# Но можно переопределить атрибут класса для конкретного экземпляра
obj1.class_attr = "Только для obj1"
print(obj1.class_attr)     # Только для obj1
print(obj2.class_attr)     # Изменено для всех
```

**2. Типы методов в классах:**

```python
class MathUtils:
    pi = 3.14159
    calculation_count = 0
    
    def __init__(self, name):
        self.name = name
        self.history = []
    
    # Метод экземпляра (имеет доступ к self и может изменять состояние объекта)
    def instance_method(self, value):
        """Метод экземпляра работает с конкретным объектом"""
        self.history.append(f"Вычисление: {value}")
        MathUtils.calculation_count += 1
        return f"Вызван из экземпляра {self.name}, значение: {value}"
    
    # Метод класса (имеет доступ к cls, может изменять атрибуты класса)
    @classmethod
    def class_method(cls, radius):
        """Метод класса работает с классом в целом"""
        cls.calculation_count += 1
        area = cls.pi * radius ** 2
        return f"Площадь круга с радиусом {radius}: {area:.2f}"
    
    # Статический метод (не имеет доступа ни к self, ни к cls)
    @staticmethod
    def static_method(x, y):
        """Статический метод - обычная функция в пространстве имен класса"""
        return f"Сумма {x} + {y} = {x + y}"
    
    @classmethod
    def get_calculation_stats(cls):
        """Получение статистики вычислений"""
        return f"Всего выполнено вычислений: {cls.calculation_count}"

# Использование разных типов методов
math_obj = MathUtils("Калькулятор")

# Метод экземпляра - вызывается через объект
print(math_obj.instance_method(42))    # Вызван из экземпляра Калькулятор, значение: 42

# Метод класса - можно вызывать через класс или объект
print(MathUtils.class_method(5))       # Площадь круга с радиусом 5: 78.54
print(math_obj.class_method(3))        # Площадь круга с радиусом 3: 28.27

# Статический метод - можно вызывать через класс или объект
print(MathUtils.static_method(5, 3))   # Сумма 5 + 3 = 8
print(math_obj.static_method(10, 7))   # Сумма 10 + 7 = 17

# Проверка статистики
print(MathUtils.get_calculation_stats())  # Всего выполнено вычислений: 3
```


#### День 3-4: Инкапсуляция

**Подробная теоретическая база:**

**Инкапсуляция** — это один из основополагающих принципов объектно-ориентированного программирования, который заключается в объединении данных и методов, работающих с этими данными, в единую структуру (класс), а также в сокрытии внутренней реализации объекта от внешнего мира. Инкапсуляция обеспечивает контролируемый доступ к внутреннему состоянию объекта через публичные методы, что позволяет поддерживать целостность данных и предотвращать их некорректное использование.

**Уровни доступа в Python:**

В отличие от языков как Java или C\#, Python не имеет строгих модификаторов доступа. Вместо этого используются соглашения об именовании:

1. **Публичный доступ** (`attribute`) — атрибут или метод доступен отовсюду
2. **Защищенный доступ** (`_attribute`) — соглашение "не использовать извне класса"
3. **Приватный доступ** (`__attribute`) — Python применяет name mangling для усложнения доступа

**Механизм name mangling:**
Когда Python встречает атрибут, начинающийся с двух подчеркиваний, он автоматически изменяет его имя, добавляя префикс `_ClassName`. Это не делает атрибут полностью недоступным, но усложняет случайный доступ к нему.

```python
class BankAccount:
    # Атрибут класса для отслеживания всех счетов
    total_accounts = 0
    bank_name = "Secure Bank"
    
    def __init__(self, account_holder, initial_balance=0, account_type="savings"):
        # Публичные атрибуты
        self.account_holder = account_holder
        self.account_type = account_type
        self.creation_date = self._get_current_date()
        
        # Защищенные атрибуты (соглашение - не использовать извне)
        self._balance = initial_balance
        self._transaction_history = []
        self._account_status = "active"
        
        # Приватные атрибуты (name mangling)
        self.__account_number = self._generate_account_number()
        self.__pin = None
        self.__security_code = self._generate_security_code()
        
        # Увеличиваем счетчик аккаунтов
        BankAccount.total_accounts += 1
        
        # Записываем первую транзакцию
        if initial_balance > 0:
            self._add_transaction("deposit", initial_balance, "Начальный баланс")
    
    def _generate_account_number(self):
        """Защищенный метод для генерации номера счета"""
        import random
        return f"ACC{random.randint(100000, 999999)}"
    
    def _generate_security_code(self):
        """Защищенный метод для генерации кода безопасности"""
        import random
        return f"{random.randint(1000, 9999)}"
    
    def _get_current_date(self):
        """Защищенный метод для получения текущей даты"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d")
    
    def _add_transaction(self, transaction_type, amount, description=""):
        """Защищенный метод для добавления транзакции в историю"""
        from datetime import datetime
        transaction = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": transaction_type,
            "amount": amount,
            "description": description,
            "balance_after": self._balance
        }
        self._transaction_history.append(transaction)
    
    def __check_pin(self, pin):
        """Приватный метод проверки PIN"""
        return self.__pin == pin
    
    def __validate_amount(self, amount):
        """Приватный метод валидации суммы"""
        if not isinstance(amount, (int, float)):
            return False, "Сумма должна быть числом"
        if amount <= 0:
            return False, "Сумма должна быть положительной"
        return True, "OK"
    
    # Публичные методы для работы с аккаунтом
    def set_pin(self, pin):
        """Публичный метод для установки PIN с валидацией"""
        if not isinstance(pin, int):
            return "PIN должен быть числом"
        
        pin_str = str(pin)
        if len(pin_str) != 4:
            return "PIN должен состоять из 4 цифр"
        
        if not pin_str.isdigit():
            return "PIN должен содержать только цифры"
        
        self.__pin = pin
        return "PIN успешно установлен"
    
    def change_pin(self, old_pin, new_pin):
        """Смена PIN с проверкой старого"""
        if not self.__check_pin(old_pin):
            return "Неверный текущий PIN"
        
        result = self.set_pin(new_pin)
        if result == "PIN успешно установлен":
            return "PIN успешно изменен"
        return result
    
    def get_balance(self, pin):
        """Получение баланса с проверкой PIN"""
        if not self.__check_pin(pin):
            return "Неверный PIN"
        
        return f"Баланс счета: {self._balance:.2f} руб."
    
    def deposit(self, amount, pin, description="Пополнение счета"):
        """Пополнение счета с полной валидацией"""
        if not self.__check_pin(pin):
            return "Неверный PIN"
        
        if self._account_status != "active":
            return "Счет заблокирован"
        
        is_valid, message = self.__validate_amount(amount)
        if not is_valid:
            return message
        
        self._balance += amount
        self._add_transaction("deposit", amount, description)
        return f"Счет пополнен на {amount:.2f} руб. Текущий баланс: {self._balance:.2f} руб."
    
    def withdraw(self, amount, pin, description="Снятие средств"):
        """Снятие средств с проверками"""
        if not self.__check_pin(pin):
            return "Неверный PIN"
        
        if self._account_status != "active":
            return "Счет заблокирован"
        
        is_valid, message = self.__validate_amount(amount)
        if not is_valid:
            return message
        
        if amount > self._balance:
            return f"Недостаточно средств. Доступно: {self._balance:.2f} руб."
        
        self._balance -= amount
        self._add_transaction("withdrawal", amount, description)
        return f"Снято {amount:.2f} руб. Остаток: {self._balance:.2f} руб."
    
    def transfer(self, amount, recipient_account, pin, description="Перевод"):
        """Перевод средств на другой счет"""
        if not self.__check_pin(pin):
            return "Неверный PIN"
        
        # Снимаем с текущего счета
        withdraw_result = self.withdraw(amount, pin, f"Перевод для {recipient_account.account_holder}")
        if "Снято" not in withdraw_result:
            return withdraw_result
        
        # Пополняем счет получателя (используем системный PIN)
        recipient_account._balance += amount
        recipient_account._add_transaction("transfer_in", amount, f"Перевод от {self.account_holder}")
        
        return f"Переведено {amount:.2f} руб. на счет {recipient_account.account_holder}"
    
    def get_transaction_history(self, pin, limit=10):
        """Получение истории транзакций"""
        if not self.__check_pin(pin):
            return "Неверный PIN"
        
        if not self._transaction_history:
            return "История транзакций пуста"
        
        recent_transactions = self._transaction_history[-limit:]
        history = "История транзакций:\n"
        for i, transaction in enumerate(recent_transactions, 1):
            history += (f"{i}. {transaction['date']} - {transaction['type']} - "
                       f"{transaction['amount']:.2f} руб. - {transaction['description']} "
                       f"(Баланс: {transaction['balance_after']:.2f})\n")
        
        return history
    
    def get_account_info(self):
        """Публичная информация о счете (без PIN)"""
        return (f"Владелец: {self.account_holder}\n"
                f"Тип счета: {self.account_type}\n"
                f"Дата создания: {self.creation_date}\n"
                f"Статус: {self._account_status}\n"
                f"Банк: {self.bank_name}")
    
    def block_account(self, admin_code):
        """Блокировка счета (административная функция)"""
        if admin_code == "ADMIN123":
            self._account_status = "blocked"
            return "Счет заблокирован"
        return "Неверный административный код"
    
    def unblock_account(self, admin_code):
        """Разблокировка счета"""
        if admin_code == "ADMIN123":
            self._account_status = "active"
            return "Счет разблокирован"
        return "Неверный административный код"
    
    @classmethod
    def get_bank_stats(cls):
        """Статистика банка"""
        return f"Банк '{cls.bank_name}' обслуживает {cls.total_accounts} счетов"

# Демонстрация использования инкапсуляции
account1 = BankAccount("Иван Иванов", 1000, "checking")
account2 = BankAccount("Петр Петров", 500)

# Установка PIN
print(account1.set_pin(1234))           # PIN успешно установлен
print(account2.set_pin(5678))           # PIN успешно установлен

# Работа с балансом
print(account1.deposit(500, 1234))      # Счет пополнен на 500.00 руб. Текущий баланс: 1500.00 руб.
print(account1.withdraw(200, 1234))     # Снято 200.00 руб. Остаток: 1300.00 руб.
print(account1.get_balance(1234))       # Баланс счета: 1300.00 руб.

# Перевод между счетами
print(account1.transfer(300, account2, 1234))  # Переведено 300.00 руб. на счет Петр Петров

# Попытка доступа с неверным PIN
print(account1.get_balance(4321))       # Неверный PIN

# Получение истории транзакций
print(account1.get_transaction_history(1234, 3))

# Публичная информация
print(account1.get_account_info())

# Демонстрация уровней доступа
print("\n=== Демонстрация уровней доступа ===")

# Публичный доступ - работает нормально
print(account1.account_holder)          # Иван Иванов

# Защищенный доступ - работает, но не рекомендуется
print(account1._balance)                # 1000.0 (но это нарушение соглашения)

# Приватный доступ - AttributeError при прямом обращении
try:
    print(account1.__pin)               # AttributeError!
except AttributeError as e:
    print(f"Ошибка доступа: {e}")

try:
    print(account1.__account_number)    # AttributeError!
except AttributeError as e:
    print(f"Ошибка доступа: {e}")

# Name mangling - как Python "прячет" приватные атрибуты
print("Доступ через name mangling:")
print(account1._BankAccount__pin)       # 1234 (не рекомендуется!)
print(account1._BankAccount__account_number)  # ACC123456

# Статистика банка
print(BankAccount.get_bank_stats())     # Банк 'Secure Bank' обслуживает 2 счетов
```

**Преимущества инкапсуляции:**

1. **Контроль доступа** — можно валидировать данные перед их изменением
2. **Безопасность** — критичные данные защищены от случайного изменения
3. **Гибкость** — можно изменить внутреннюю реализацию без влияния на внешний код
4. **Отладка** — легче отследить, где и как изменяются данные
5. **Документирование** — четкое разделение публичного и приватного API

### Этап 2: Наследование и полиморфизм (2-3 дня)

#### День 5-6: Наследование

**Подробная теоретическая база:**

**Наследование** — это механизм объектно-ориентированного программирования, который позволяет создавать новые классы на основе существующих, при этом новый класс (дочерний, производный) автоматически получает все атрибуты и методы родительского класса (базового, суперкласса). Наследование реализует отношение "является" (is-a) между классами и позволяет создавать иерархии классов с общей функциональностью.

**Ключевые концепции наследования:**

1. **Базовый класс (суперкласс)** — класс, от которого наследуются другие классы
2. **Производный класс (подкласс)** — класс, который наследует от базового класса
3. **Переопределение методов** — изменение поведения унаследованного метода
4. **Расширение функциональности** — добавление новых методов и атрибутов
5. **Функция `super()`** — обращение к методам родительского класса
```python
# Базовый класс (родительский)
class Animal:
    # Атрибуты класса
    kingdom = "Animalia"
    total_animals = 0
    
    def __init__(self, name, species, age, weight=0):
        # Базовые атрибуты для всех животных
        self.name = name
        self.species = species
        self.age = age
        self.weight = weight
        self.is_alive = True
        self.energy_level = 100
        self.hunger_level = 0
        self.health_status = "healthy"
        
        # Увеличиваем счетчик животных
        Animal.total_animals += 1
        
        # Уникальный ID для каждого животного
        self.animal_id = self._generate_id()
    
    def _generate_id(self):
        """Защищенный метод для генерации ID"""
        import random
        return f"ANIMAL_{random.randint(1000, 9999)}"
    
    def eat(self, food, amount=10):
        """Базовый метод питания"""
        if not self.is_alive:
            return f"{self.name} не может есть - не живое"
        
        if self.hunger_level <= 0:
            return f"{self.name} не голодное"
        
        self.hunger_level = max(0, self.hunger_level - amount)
        self.energy_level = min(100, self.energy_level + amount // 2)
        return f"{self.name} ест {food}. Голод: {self.hunger_level}, Энергия: {self.energy_level}"
    
    def sleep(self, hours=8):
        """Базовый метод сна"""
        if not self.is_alive:
            return f"{self.name} не может спать - не живое"
        
        energy_restored = min(hours * 10, 100 - self.energy_level)
        self.energy_level += energy_restored
        return f"{self.name} спит {hours} часов. Энергия восстановлена до {self.energy_level}"
    
    def make_sound(self):
        """Базовый метод издавания звука (будет переопределен в подклассах)"""
        return f"{self.name} издает звук"
    
    def move(self):
        """Базовый метод движения"""
        if not self.is_alive:
            return f"{self.name} не может двигаться"
        
        if self.energy_level < 10:
            return f"{self.name} слишком устал для движения"
        
        self.energy_level -= 5
        self.hunger_level = min(100, self.hunger_level + 5)
        return f"{self.name} движется. Энергия: {self.energy_level}, Голод: {self.hunger_level}"
    
    def get_info(self):
        """Получение информации о животном"""
        status = "живое" if self.is_alive else "мертвое"
        return (f"{self.name} - {self.species}, возраст: {self.age} лет, "
                f"вес: {self.weight} кг, статус: {status}, "
                f"энергия: {self.energy_level}, голод: {self.hunger_level}")
    
    def age_up(self):
        """Увеличение возраста"""
        self.age += 1
        # С возрастом максимальная энергия может снижаться
        if self.age > 10:
            self.energy_level = max(0, self.energy_level - 2)
        return f"{self.name} стал старше. Теперь {self.age} лет"
    
    @classmethod
    def get_total_animals(cls):
        """Получение общего количества животных"""
        return f"Всего животных создано: {cls.total_animals}"
    
    @staticmethod
    def calculate_bmi(weight, height):
        """Расчет индекса массы тела"""
        if height <= 0:
            return "Рост должен быть положительным"
        bmi = weight / (height ** 2)
        return f"ИМТ: {bmi:.2f}"

# Дочерний класс - Собака
class Dog(Animal):
    # Атрибуты, специфичные для собак
    breed_groups = ["Охотничьи", "Пастушьи", "Терьеры", "Декоративные", "Служебные"]
    
    def __init__(self, name, breed, age, weight=20, owner=None, is_trained=False):
        # Вызов конструктора родительского класса
        super().__init__(name, "Собака", age, weight)
        
        # Дополнительные атрибуты для собак
        self.breed = breed
        self.owner = owner
        self.is_trained = is_trained
        self.loyalty_level = 80
        self.barking_volume = 50
        self.favorite_toys = []
        self.commands_known = []
        
        # Собаки по умолчанию более активны
        self.energy_level = 90
    
    # Переопределение метода родительского класса
    def make_sound(self):
        """Переопределенный метод для собак"""
        sound_intensity = "громко" if self.barking_volume > 70 else "тихо"
        return f"{self.name} лает {sound_intensity}: Гав-гав!"
    
    def move(self):
        """Переопределенный метод движения для собак"""
        base_result = super().move()  # Вызываем родительский метод
        if "движется" in base_result:
            return base_result.replace("движется", "бегает и играет")
        return base_result
    
    # Новые методы, специфичные для собак
    def fetch(self, item="мячик"):
        """Команда 'принеси'"""
        if not self.is_alive:
            return f"{self.name} не может принести предмет"
        
        if self.energy_level < 15:
            return f"{self.name} слишком устал, чтобы принести {item}"
        
        if not self.is_trained:
            success_chance = 30  # Необученная собака может не послушаться
        else:
            success_chance = 90
        
        import random
        if random.randint(1, 100) <= success_chance:
            self.energy_level -= 10
            self.loyalty_level = min(100, self.loyalty_level + 5)
            return f"{self.name} приносит {item}! Лояльность: {self.loyalty_level}"
        else:
            return f"{self.name} отвлекся и не принес {item}"
    
    def train(self, command):
        """Обучение новой команде"""
        if command in self.commands_known:
            return f"{self.name} уже знает команду '{command}'"
        
        if self.energy_level < 20:
            return f"{self.name} слишком устал для обучения"
        
        self.commands_known.append(command)
        self.energy_level -= 15
        self.hunger_level = min(100, self.hunger_level + 10)
        
        if len(self.commands_known) >= 5:
            self.is_trained = True
        
        return f"{self.name} выучил команду '{command}'. Знает команд: {len(self.commands_known)}"
    
    def guard(self):
        """Охрана территории"""
        if not self.is_alive:
            return f"{self.name} не может охранять"
        
        if self.energy_level < 30:
            return f"{self.name} слишком устал для охраны"
        
        self.energy_level -= 20
        self.barking_volume = min(100, self.barking_volume + 10)
        return f"{self.name} охраняет дом! Уровень лая: {self.barking_volume}"
    
    def play_with_toy(self, toy):
        """Игра с игрушкой"""
        if toy not in self.favorite_toys:
            self.favorite_toys.append(toy)
        
        if self.energy_level < 10:
            return f"{self.name} слишком устал для игры"
        
        self.energy_level -= 8
        self.loyalty_level = min(100, self.loyalty_level + 3)
        return f"{self.name} играет с {toy}. Энергия: {self.energy_level}, Лояльность: {self.loyalty_level}"

# Дочерний класс - Кошка
class Cat(Animal):
    # Атрибуты, специфичные для кошек
    coat_types = ["Короткошерстная", "Длинношерстная", "Бесшерстная"]
    
    def __init__(self, name, breed, age, weight=4, is_indoor=True, independence_level=70):
        super().__init__(name, "Кошка", age, weight)
        
        self.breed = breed
        self.is_indoor = is_indoor
        self.independence_level = independence_level
        self.curiosity_level = 80
        self.hunting_instinct = 60
        self.favorite_spots = []
        self.lives_left = 9  # Шутка про 9 жизней кошки
        
        # Кошки более спокойные
        self.energy_level = 70
    
    def make_sound(self):
        """Переопределенный метод для кошек"""
        if self.hunger_level > 70:
            return f"{self.name} громко мяукает: МЯУ! (требует еду)"
        elif self.energy_level < 30:
            return f"{self.name} тихо мурлычет"
        else:
            return f"{self.name} мяукает: Мяу!"
    
    def move(self):
        """Переопределенный метод движения для кошек"""
        base_result = super().move()
        if "движется" in base_result:
            movement_style = "грациозно крадется" if self.hunting_instinct > 50 else "лениво прогуливается"
            return base_result.replace("движется", movement_style)
        return base_result
    
    def climb(self, object_name="дерево"):
        """Лазание (специфично для кошек)"""
        if not self.is_alive:
            return f"{self.name} не может лазать"
        
        if self.energy_level < 15:
            return f"{self.name} слишком устал для лазания"
        
        self.energy_level -= 12
        self.curiosity_level = min(100, self.curiosity_level + 5)
        
        if object_name not in self.favorite_spots:
            self.favorite_spots.append(object_name)
        
        return f"{self.name} лазает по {object_name}. Любопытство: {self.curiosity_level}"
    
    def hunt(self, prey="мышь"):
        """Охота"""
        if self.is_indoor and prey not in ["игрушечная мышь", "лазерная точка"]:
            return f"{self.name} домашняя и не может охотиться на настоящую {prey}"
        
        if self.energy_level < 25:
            return f"{self.name} слишком устал для охоты"
        
        import random
        success_chance = self.hunting_instinct
        
        if random.randint(1, 100) <= success_chance:
            self.energy_level -= 20
            self.hunger_level = max(0, self.hunger_level - 15)
            return f"{self.name} успешно поймал {prey}!"
        else:
            self.energy_level -= 10
            return f"{self.name} не смог поймать {prey}"
    
    def purr(self):
        """Мурлыканье"""
        if self.energy_level > 80 and self.hunger_level < 30:
            self.energy_level = min(100, self.energy_level + 5)
            return f"{self.name} довольно мурлычет: мур-мур-мур"
        else:
            return f"{self.name} не в настроении мурлыкать"
    
    def knock_over(self, item):
        """Сбрасывание предметов (типичное поведение кошек)"""
        if self.curiosity_level < 50:
            return f"{self.name} не интересуется {item}"
        
        import random
        if random.randint(1, 100) <= self.curiosity_level:
            self.curiosity_level = min(100, self.curiosity_level + 2)
            return f"{self.name} сбросил {item} со стола! Любопытство: {self.curiosity_level}"
        else:
            return f"{self.name} обнюхал {item}, но не стал его трогать"

# Дочерний класс - Птица
class Bird(Animal):
    migration_patterns = ["Перелетная", "Оседлая", "Кочующая"]
    
    def __init__(self, name, species, age, weight=0.5, can_fly=True, wingspan=20):
        super().__init__(name, species, age, weight)
        
        self.can_fly = can_fly
        self.wingspan = wingspan  # размах крыльев в см
        self.altitude = 0
        self.nest_location = None
        self.migration_distance = 0
        
        # Птицы обычно более активны
        self.energy_level = 85
    
    def make_sound(self):
        """Переопределенный метод для птиц"""
        if self.altitude > 0:
            return f"{self.name} чирикает в полете: Чик-чирик!"
        else:
            return f"{self.name} поет: Чик-чирик-чирик!"
    
    def fly(self, height, distance=0):
        """Полет (специфично для птиц)"""
        if not self.is_alive:
            return f"{self.name} не может летать"
        
        if not self.can_fly:
            return f"{self.name} не умеет летать"
        
        energy_needed = height // 10 + distance // 5
        if self.energy_level < energy_needed:
            return f"{self.name} слишком устал для полета на такую высоту"
        
        self.altitude = height
        self.energy_level -= energy_needed
        self.hunger_level = min(100, self.hunger_level + energy_needed // 2)
        
        result = f"{self.name} летает на высоте {height} метров"
        if distance > 0:
            self.migration_distance += distance
            result += f" и пролетел {distance} км"
        
        return result
    
    def land(self):
        """Приземление"""
        if self.altitude == 0:
            return f"{self.name} уже на земле"
        
        self.altitude = 0
        return f"{self.name} приземлился"
    
    def build_nest(self, location):
        """Строительство гнезда"""
        if self.energy_level < 30:
            return f"{self.name} слишком устал для строительства гнезда"
        
        self.nest_location = location
        self.energy_level -= 25
        return f"{self.name} построил гнездо в {location}"
    
    def migrate(self, distance):
        """Миграция"""
        if not self.can_fly:
            return f"{self.name} не может мигрировать без способности к полету"
        
        energy_needed = distance // 2
        if self.energy_level < energy_needed:
            return f"{self.name} недостаточно энергии для миграции на {distance} км"
        
        self.migration_distance += distance
        self.energy_level -= energy_needed
        return f"{self.name} мигрировал на {distance} км. Общая дистанция миграции: {self.migration_distance} км"

# Демонстрация наследования
print("=== Создание животных ===")
dog = Dog("Бобик", "Овчарка", 3, 25, "Иван", True)
cat = Cat("Мурка", "Персидская", 2, 4, True, 80)
bird = Bird("Кеша", "Попугай", 1, 0.3, True, 15)

print("=== Базовая информация ===")
print(dog.get_info())
print(cat.get_info())
print(bird.get_info())

print("\n=== Звуки животных (полиморфизм) ===")
animals = [dog, cat, bird]
for animal in animals:
    print(animal.make_sound())

print("\n=== Специфичное поведение ===")
print(dog.train("сидеть"))
print(dog.fetch("палка"))
print(dog.guard())

print(cat.climb("шкаф"))
print(cat.hunt("игрушечная мышь"))
print(cat.purr())

print(bird.fly(50, 10))
print(bird.build_nest("дуб"))
print(bird.land())

print("\n=== Общие методы (наследование) ===")
print(dog.eat("корм", 15))
print(cat.sleep(6))
print(bird.age_up())

print("\n=== Статистика ===")
print(Animal.get_total_animals())
```

**Множественное наследование и MRO (Method Resolution Order):**

```python
# Демонстрация множественного наследования
class Mammal:
    def __init__(self):
        self.body_temperature = 37
        self.has_fur = True
    
    def regulate_temperature(self):
        return "Регулирует температуру тела"
    
    def feed_milk(self):
        return "Кормит детенышей молоком"

class Aquatic:
    def __init__(self):
        self.can_swim = True
        self.water_resistance = 90
    
    def swim(self):
        return "Плавает в воде"
    
    def dive(self, depth):
        return f"Ныряет на глубину {depth} метров"

class Carnivore:
    def __init__(self):
        self.diet = "мясо"
        self.hunting_skill = 80
    
    def hunt_prey(self, prey):
        return f"Охотится на {prey}"

# Множественное наследование
class Seal(Mammal, Aquatic, Carnivore):
    def __init__(self, name, age):
        # Вызываем конструкторы всех родительских классов
        Mammal.__init__(self)
        Aquatic.__init__(self)
        Carnivore.__init__(self)
        
        self.name = name
        self.age = age
    
    def get_info(self):
        return (f"{self.name} - тюлень, {self.age} лет, "
                f"температура тела: {self.body_temperature}°C, "
                f"может плавать: {self.can_swim}, "
                f"диета: {self.diet}")

# Проверка порядка разрешения методов (MRO)
print("=== Method Resolution Order ===")
print(Seal.__mro__)
# (<class '__main__.Seal'>, <class '__main__.Mammal'>, <class '__main__.Aquatic'>, <class '__main__.Carnivore'>, <class 'object'>)

seal = Seal("Морж", 5)
print(seal.get_info())
print(seal.regulate_temperature())
print(seal.swim())
print(seal.hunt_prey("рыба"))
```


#### День 7: Полиморфизм

**Подробная теоретическая база:**

**Полиморфизм** — это принцип объектно-ориентированного программирования, который позволяет объектам разных классов реагировать на одинаковые методы по-разному. Слово "полиморфизм" происходит от греческих слов "поли" (много) и "морф" (форма), что означает "много форм". В Python полиморфизм реализуется через несколько механизмов:

1. **Полиморфизм через наследование** — переопределение методов в дочерних классах
2. **Duck typing** — "Если это ходит как утка и крякает как утка, то это утка"
3. **Полиморфизм через интерфейсы** — реализация общих методов в разных классах
```python
# Полиморфизм через наследование
def animal_concert(animals):
    """Функция демонстрирует полиморфизм через наследование"""
    print("🎵 Концерт животных начинается! 🎵")
    for i, animal in enumerate(animals, 1):
        print(f"{i}. {animal.name}: {animal.make_sound()}")
        print(f"   Информация: {animal.get_info()}")
        print(f"   Движение: {animal.move()}")
        print()

# Создаем разных животных
pets = [
    Dog("Рекс", "Лабрадор", 4, 30, "Анна", True),
    Cat("Васька", "Британская", 3, 5, True, 75),
    Bird("Чижик", "Канарейка", 1, 0.2, True, 12)
]

animal_concert(pets)

# Duck typing - полиморфизм без наследования
class Robot:
    def __init__(self, model, battery_level=100):
        self.model = model
        self.name = f"Робот {model}"
        self.battery_level = battery_level
        self.is_alive = True  # Для совместимости с животными
    
    def make_sound(self):
        if self.battery_level < 20:
            return f"{self.name} тихо пищит: бип... (низкий заряд)"
        return f"{self.name} издает: БИП-БИП-БИП!"
    
    def move(self):
        if self.battery_level < 10:
            return f"{self.name} не может двигаться - разряжена батарея"
        
        self.battery_level -= 5
        return f"{self.name} движется на колесах. Заряд: {self.battery_level}%"
    
    def get_info(self):
        status = "активен" if self.battery_level > 0 else "разряжен"
        return f"{self.name} - искусственное существо, заряд: {self.battery_level}%, статус: {status}"

class Alien:
    def __init__(self, name, planet):
        self.name = name
        self.planet = planet
        self.is_alive = True
        self.telepathy_level = 80
    
    def make_sound(self):
        return f"{self.name} телепатически передает: 'Приветствую, земляне!'"
    
    def move(self):
        return f"{self.name} левитирует над поверхностью"
    
    def get_info(self):
        return f"{self.name} - инопланетянин с планеты {self.planet}, телепатия: {self.telepathy_level}%"

# Робот и инопланетянин не наследуются от Animal, но имеют нужные методы
robot = Robot("R2D2", 85)
alien = Alien("Зорг", "Альфа Центавра")

# Благодаря duck typing, они могут участвовать в концерте!
all_creatures = pets + [robot, alien]
print("=== Расширенный концерт с роботом и инопланетянином ===")
animal_concert(all_creatures)

# Полиморфизм в действии - разные объекты, одинаковый интерфейс
def creature_battle(creature1, creature2):
    """Демонстрация полиморфизма в игровой механике"""
    print(f"⚔️ Битва между {creature1.name} и {creature2.name}!")
    
    # Все объекты имеют метод make_sound, но реализуют его по-разному
    print(f"{creature1.name} издает боевой клич: {creature1.make_sound()}")
    print(f"{creature2.name} отвечает: {creature2.make_sound()}")
    
    # Движение также полиморфно
    print(f"{creature1.name} готовится к атаке: {creature1.move()}")
    print(f"{creature2.name} занимает позицию: {creature2.move()}")
    
    print("Битва завершена!")

creature_battle(dog, robot)
print()
creature_battle(cat, alien)
```

**Продвинутый полиморфизм с абстрактными классами:**

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    """Абстрактный базовый класс для всех транспортных средств"""
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    @abstractmethod
    def start_engine(self):
        """Абстрактный метод запуска двигателя"""
        pass
    
    @abstractmethod
    def stop_engine(self):
        """Абстрактный метод остановки двигателя"""
        pass
    
    @abstractmethod
    def get_fuel_type(self):
        """Абстрактный метод получения типа топлива"""
        pass
    
    # Конкретный метод (не абстрактный)
    def get_info(self):
        status = "работает" if self.is_running else "заглушен"
        return f"{self.brand} {self.model} ({self.year}) - {status}, топливо: {self.get_fuel_type()}"

class GasolineCar(Vehicle):
    def __init__(self, brand, model, year, engine_volume):
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume
        self.fuel_level = 50
    
    def start_engine(self):
        if self.fuel_level <= 0:
            return f"{self.brand} {self.model}: Нет бензина!"
        
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model}: Бензиновый двигатель {self.engine_volume}л запущен"
        return f"{self.brand} {self.model}: Двигатель уже работает"
    
    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model}: Двигатель заглушен"
        return f"{self.brand} {self.model}: Двигатель уже заглушен"
    
    def get_fuel_type(self):
        return "Бензин"

class ElectricCar(Vehicle):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity
        self.charge_level = 80
    
    def start_engine(self):
        if self.charge_level <= 0:
            return f"{self.brand} {self.model}: Батарея разряжена!"
        
        if not self.is_running:
            self.is_running = True
            return f"{self.brand} {self.model}: Электродвигатель активирован бесшумно"
        return f"{self.brand} {self.model}: Система уже активна"
    
    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model}: Электросистема деактивирована"
        return f"{self.brand} {self.model}: Система уже деактивирована"
    
    def get_fuel_type(self):
        return "Электричество"
    
    def charge(self, hours):
        charge_added = min(hours * 10, 100 - self.charge_level)
        self.charge_level += charge_added
        return f"{self.brand} {self.model}: Заряжен на {charge_added}%. Текущий заряд: {self.charge_level}%"

class HybridCar(Vehicle):
    def __init__(self, brand, model, year, engine_volume, battery_capacity):
        super().__init__(brand, model, year)
        self.engine_volume = engine_volume
        self.battery_capacity = battery_capacity
        self.fuel_level = 40
        self.charge_level = 60
        self.current_mode = "hybrid"  # hybrid, electric, gasoline
    
    def start_engine(self):
        if self.fuel_level <= 0 and self.charge_level <= 0:
            return f"{self.brand} {self.model}: Нет ни топлива, ни заряда!"
        
        if not self.is_running:
            self.is_running = True
            if self.charge_level > 20:
                self.current_mode = "electric"
                return f"{self.brand} {self.model}: Запущен в электрическом режиме"
            else:
                self.current_mode = "gasoline"
                return f"{self.brand} {self.model}: Запущен бензиновый двигатель"
        return f"{self.brand} {self.model}: Система уже работает в режиме {self.current_mode}"
    
    def stop_engine(self):
        if self.is_running:
            self.is_running = False
            return f"{self.brand} {self.model}: Гибридная система остановлена"
        return f"{self.brand} {self.model}: Система уже остановлена"
    
    def get_fuel_type(self):
        return f"Гибрид (бензин + электричество), режим: {self.current_mode}"
    
    def switch_mode(self, mode):
        if mode not in ["hybrid", "electric", "gasoline"]:
            return "Неверный режим. Доступны: hybrid, electric, gasoline"
        
        if mode == "electric" and self.charge_level <= 0:
            return "Нельзя переключиться в электрический режим - батарея разряжена"
        
        if mode == "gasoline" and self.fuel_level <= 0:
            return "Нельзя переключиться в бензиновый режим - нет топлива"
        
        self.current_mode = mode
        return f"{self.brand} {self.model}: Переключен в режим {mode}"

# Демонстрация полиморфизма с абстрактными классами
vehicles = [
    GasolineCar("Toyota", "Camry", 2020, 2.5),
    ElectricCar("Tesla", "Model 3", 2021, 75),
    HybridCar("Toyota", "Prius", 2022, 1.8, 8.8)
]

print("=== Полиморфизм транспортных средств ===")
for vehicle in vehicles:
    print(f"🚗 {vehicle.get_info()}")
    print(f"   Запуск: {vehicle.start_engine()}")
    print(f"   Остановка: {vehicle.stop_engine()}")
    print()

# Функция, работающая с любым транспортным средством
def test_vehicle(vehicle: Vehicle):
    """Т```

