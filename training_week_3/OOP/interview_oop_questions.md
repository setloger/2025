### Блок 1: Фундаментальные концепции ООП

#### 1.1 Глубокое понимание классов и объектов

**Вопрос:** "Объясните разницу между `__new__` и `__init__`. Когда использовать каждый?"

**Полный ответ:**

```python
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        """__new__ вызывается для создания экземпляра"""
        print(f"__new__ вызван для {cls}")
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Создан новый экземпляр")
        else:
            print("Возвращен существующий экземпляр")
        return cls._instance
    
    def __init__(self, name):
        """__init__ вызывается для инициализации экземпляра"""
        print(f"__init__ вызван с name={name}")
        if not hasattr(self, 'initialized'):
            self.name = name
            self.initialized = True
            print("Экземпляр инициализирован")
        else:
            print("Экземпляр уже был инициализирован")

# Демонстрация
s1 = Singleton("Первый")
s2 = Singleton("Второй")
print(f"s1 is s2: {s1 is s2}")  # True
print(f"s1.name: {s1.name}")    # Первый
```

**Ключевые моменты:**

- `__new__` создает объект, `__init__` инициализирует его
- `__new__` - статический метод, возвращает экземпляр
- `__init__` - метод экземпляра, ничего не возвращает
- `__new__` используется для Singleton, неизменяемых типов, метаклассов


#### 1.2 Продвинутая работа с атрибутами

**Вопрос:** "Реализуйте класс с динамическими атрибутами и контролем доступа"

```python
class DynamicAttributes:
    def __init__(self):
        self._data = {}
        self._readonly_attrs = set()
        self._private_attrs = set()
    
    def __getattr__(self, name):
        """Вызывается когда атрибут не найден обычным способом"""
        if name in self._private_attrs:
            raise AttributeError(f"Атрибут '{name}' приватный")
        
        if name in self._data:
            return self._data[name]
        
        raise AttributeError(f"Атрибут '{name}' не существует")
    
    def __setattr__(self, name, value):
        """Контролирует установку атрибутов"""
        # Системные атрибуты устанавливаем напрямую
        if name.startswith('_'):
            super().__setattr__(name, value)
            return
        
        # Проверяем readonly атрибуты
        if hasattr(self, '_readonly_attrs') and name in self._readonly_attrs:
            raise AttributeError(f"Атрибут '{name}' только для чтения")
        
        # Сохраняем в _data
        if hasattr(self, '_data'):
            self._data[name] = value
        else:
            super().__setattr__(name, value)
    
    def __delattr__(self, name):
        """Контролирует удаление атрибутов"""
        if name in self._readonly_attrs:
            raise AttributeError(f"Нельзя удалить readonly атрибут '{name}'")
        
        if name in self._data:
            del self._data[name]
        else:
            super().__delattr__(name)
    
    def make_readonly(self, name):
        """Делает атрибут только для чтения"""
        self._readonly_attrs.add(name)
    
    def make_private(self, name):
        """Делает атрибут приватным"""
        self._private_attrs.add(name)
    
    def list_attributes(self):
        """Список всех динамических атрибутов"""
        return {
            'public': [k for k in self._data.keys() 
                      if k not in self._private_attrs],
            'readonly': list(self._readonly_attrs),
            'private': list(self._private_attrs)
        }

# Использование
obj = DynamicAttributes()
obj.name = "Тест"
obj.value = 42
obj.make_readonly('name')
obj.make_private('secret')
obj.secret = "секретная информация"

print(obj.name)    # Тест
print(obj.value)   # 42

try:
    obj.name = "Новое имя"  # AttributeError
except AttributeError as e:
    print(f"Ошибка: {e}")

try:
    print(obj.secret)  # AttributeError
except AttributeError as e:
    print(f"Ошибка: {e}")

print(obj.list_attributes())
```


### Блок 2: Продвинутое наследование

#### 2.1 Сложные случаи множественного наследования

**Вопрос:** "Решите Diamond Problem и объясните cooperative inheritance"

```python
class LoggerMixin:
    def log(self, message):
        print(f"[{self.__class__.__name__}] {message}")

class Base:
    def __init__(self, name):
        self.name = name
        print(f"Base.__init__({name})")
    
    def process(self):
        print(f"Base.process() для {self.name}")
        return "base_result"

class ProcessorA(Base):
    def __init__(self, name, config_a=None):
        print(f"ProcessorA.__init__({name}, {config_a})")
        super().__init__(name)
        self.config_a = config_a
    
    def process(self):
        print(f"ProcessorA.process() для {self.name}")
        result = super().process()
        return f"A({result})"
    
    def specific_a(self):
        return f"Специфичный метод A для {self.name}"

class ProcessorB(Base):
    def __init__(self, name, config_b=None):
        print(f"ProcessorB.__init__({name}, {config_b})")
        super().__init__(name)
        self.config_b = config_b
    
    def process(self):
        print(f"ProcessorB.process() для {self.name}")
        result = super().process()
        return f"B({result})"
    
    def specific_b(self):
        return f"Специфичный метод B для {self.name}"

class CombinedProcessor(LoggerMixin, ProcessorA, ProcessorB):
    def __init__(self, name, config_a=None, config_b=None, combined_config=None):
        print(f"CombinedProcessor.__init__({name})")
        self.combined_config = combined_config
        
        # Правильный способ вызова родительских конструкторов
        ProcessorA.__init__(self, name, config_a)
        ProcessorB.__init__(self, name, config_b)
        
        self.log(f"Создан комбинированный процессор {name}")
    
    def process(self):
        self.log("Начинаем комбинированную обработку")
        
        # Используем cooperative inheritance
        result = super().process()
        
        # Добавляем свою логику
        combined_result = f"Combined({result})"
        
        self.log(f"Результат: {combined_result}")
        return combined_result
    
    def process_with_both(self):
        """Явно используем методы обоих родителей"""
        result_a = ProcessorA.process(self)
        result_b = ProcessorB.process(self)
        return f"Both: {result_a} + {result_b}"

# Анализ MRO
print("MRO для CombinedProcessor:")
for i, cls in enumerate(CombinedProcessor.__mro__):
    print(f"  {i}: {cls}")

print("\n" + "="*50)

# Создание и использование
processor = CombinedProcessor(
    "TestProcessor", 
    config_a="A_config", 
    config_b="B_config",
    combined_config="Combined_config"
)

print("\n" + "="*50)
print("Вызов process():")
result1 = processor.process()

print("\n" + "="*50)
print("Вызов process_with_both():")
result2 = processor.process_with_both()

print(f"\nРезультаты:")
print(f"process(): {result1}")
print(f"process_with_both(): {result2}")
```


#### 2.2 Миксины и композиция возможностей

**Вопрос:** "Создайте систему миксинов для добавления функциональности"

```python
from datetime import datetime
import json
from typing import Dict, Any

class TimestampMixin:
    """Миксин для добавления временных меток"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.created_at = datetime.now()
        self.updated_at = self.created_at
    
    def touch(self):
        """Обновляет временную метку"""
        self.updated_at = datetime.now()
    
    def age_seconds(self):
        """Возраст объекта в секундах"""
        return (datetime.now() - self.created_at).total_seconds()

class SerializableMixin:
    """Миксин для сериализации объектов"""
    
    def to_dict(self):
        """Преобразование в словарь"""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            elif hasattr(value, 'to_dict'):
                result[key] = value.to_dict()
            elif isinstance(value, (list, tuple)):
                result[key] = [
                    item.to_dict() if hasattr(item, 'to_dict') else item 
                    for item in value
                ]
            else:
                result[key] = value
        return result
    
    def to_json(self):
        """Преобразование в JSON"""
        return json.dumps(self.to_dict(), indent=2, ensure_ascii=False)
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]):
        """Создание объекта из словаря"""
        # Базовая реализация - должна быть переопределена в классах
        return cls(**data)

class ValidatedMixin:
    """Миксин для валидации данных"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validate()
    
    def validate(self):
        """Валидация объекта - переопределяется в дочерних классах"""
        pass
    
    def is_valid(self):
        """Проверка валидности объекта"""
        try:
            self.validate()
            return True
        except Exception:
            return False

class CacheableMixin:
    """Миксин для кеширования вычислений"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._cache = {}
    
    def cached_property(self, name, calculator):
        """Кешированное свойство"""
        if name not in self._cache:
            self._cache[name] = calculator()
        return self._cache[name]
    
    def invalidate_cache(self, name=None):
        """Инвалидация кеша"""
        if name:
            self._cache.pop(name, None)
        else:
            self._cache.clear()

# Пример использования миксинов
class User(TimestampMixin, SerializableMixin, ValidatedMixin, CacheableMixin):
    def __init__(self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
        super().__init__()  # Вызываем конструкторы миксинов
    
    def validate(self):
        """Валидация пользователя"""
        if not self.username or len(self.username) < 3:
            raise ValueError("Username должен быть не менее 3 символов")
        
        if '@' not in self.email:
            raise ValueError("Некорректный email")
        
        if self.age < 0 or self.age > 150:
            raise ValueError("Возраст должен быть от 0 до 150")
    
    @property
    def display_name(self):
        """Кешированное отображаемое имя"""
        return self.cached_property(
            'display_name',
            lambda: f"{self.username} ({self.email})"
        )
    
    def update_email(self, new_email):
        """Обновление email с инвалидацией кеша"""
        self.email = new_email
        self.touch()  # Из TimestampMixin
        self.invalidate_cache('display_name')  # Из CacheableMixin
        self.validate()  # Из ValidatedMixin

class Product(TimestampMixin, SerializableMixin, CacheableMixin):
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category
        super().__init__()
    
    @property
    def price_with_tax(self):
        """Кешированная цена с налогом"""
        return self.cached_property(
            'price_with_tax',
            lambda: self.price * 1.2
        )
    
    def update_price(self, new_price):
        """Обновление цены"""
        self.price = new_price
        self.touch()
        self.invalidate_cache('price_with_tax')

# Демонстрация
print("=== Создание пользователя ===")
user = User("john_doe", "john@example.com", 25)
print(f"Пользователь создан: {user.display_name}")
print(f"Возраст объекта: {user.age_seconds():.2f} секунд")

print("\n=== Сериализация ===")
print(user.to_json())

print("\n=== Обновление email ===")
user.update_email("john.doe@newdomain.com")
print(f"Новое отображаемое имя: {user.display_name}")

print("\n=== Создание продукта ===")
product = Product("Ноутбук", 50000, "Электроника")
print(f"Цена с налогом: {product.price_with_tax}")

print("\n=== Обновление цены ===")
product.update_price(45000)
print(f"Новая цена с налогом: {product.price_with_tax}")

print("\n=== Валидация ===")
try:
    invalid_user = User("ab", "invalid-email", -5)
except ValueError as e:
    print(f"Ошибка валидации: {e}")
```


### Блок 3: Метапrogramming и продвинутые техники

#### 3.1 Создание DSL с помощью метаклассов

**Вопрос:** "Создайте метакласс для автоматической генерации API методов"

```python
import inspect
from typing import Dict, Any, Callable

class APIMethodMeta(type):
    """Метакласс для автоматической генерации API методов"""
    
    def __new__(mcs, name, bases, namespace):
        # Собираем все методы, помеченные как API
        api_methods = {}
        
        for attr_name, attr_value in namespace.items():
            if hasattr(attr_value, '_is_api_method'):
                api_methods[attr_name] = attr_value
        
        # Создаем автоматические методы
        if api_methods:
            namespace['_api_methods'] = api_methods
            namespace['list_api_methods'] = mcs._create_list_methods()
            namespace['call_api_method'] = mcs._create_call_method()
            namespace['get_api_documentation'] = mcs._create_docs_method()
        
        return super().__new__(mcs, name, bases, namespace)
    
    @staticmethod
    def _create_list_methods():
        def list_api_methods(self):
            """Список всех API методов"""
            return list(self._api_methods.keys())
        return list_api_methods
    
    @staticmethod
    def _create_call_method():
        def call_api_method(self, method_name, *args, **kwargs):
            """Вызов API метода по имени"""
            if method_name not in self._api_methods:
                raise ValueError(f"API метод '{method_name}' не найден")
            
            method = getattr(self, method_name)
            return method(*args, **kwargs)
        return call_api_method
    
    @staticmethod
    def _create_docs_method():
        def get_api_documentation(self):
            """Документация по всем API методам"""
            docs = {}
            for method_name, method in self._api_methods.items():
                sig = inspect.signature(method)
                docs[method_name] = {
                    'signature': str(sig),
                    'docstring': method.__doc__ or "Нет описания",
                    'parameters': [
                        {
                            'name': param.name,
                            'type': param.annotation.__name__ if param.annotation != param.empty else 'Any',
                            'default': param.default if param.default != param.empty else None
                        }
                        for param in sig.parameters.values()
                        if param.name != 'self'
                    ]
                }
            return docs
        return get_api_documentation

def api_method(func):
    """Декоратор для пометки методов как API"""
    func._is_api_method = True
    return func

class UserAPI(metaclass=APIMethodMeta):
    """API для работы с пользователями"""
    
    def __init__(self):
        self.users = {}
        self.next_id = 1
    
    @api_method
    def create_user(self, name: str, email: str, age: int = 18) -> Dict[str, Any]:
        """Создание нового пользователя"""
        user_id = self.next_id
        self.next_id += 1
        
        user = {
            'id': user_id,
            'name': name,
            'email': email,
            'age': age
        }
        
        self.users[user_id] = user
        return user
    
    @api_method
    def get_user(self, user_id: int) -> Dict[str, Any]:
        """Получение пользователя по ID"""
        if user_id not in self.users:
            raise ValueError(f"Пользователь с ID {user_id} не найден")
        return self.users[user_id]
    
    @api_method
    def update_user(self, user_id: int, **updates) -> Dict[str, Any]:
        """Обновление данных пользователя"""
        if user_id not in self.users:
            raise ValueError(f"Пользователь с ID {user_id} не найден")
        
        self.users[user_id].update(updates)
        return self.users[user_id]
    
    @api_method
    def delete_user(self, user_id: int) -> bool:
        """Удаление пользователя"""
        if user_id not in self.users:
            return False
        
        del self.users[user_id]
        return True
    
    @api_method
    def list_users(self, min_age: int = 0, max_age: int = 150) -> list:
        """Список пользователей с фильтрацией по возрасту"""
        return [
            user for user in self.users.values()
            if min_age <= user['age'] <= max_age
        ]
    
    # Обычный метод (не API)
    def _internal_method(self):
        """Внутренний метод, не доступный через API"""
        return "Это внутренний метод"

# Демонстрация
api = UserAPI()

print("=== Список API методов ===")
for method in api.list_api_methods():
    print(f"- {method}")

print("\n=== Документация API ===")
docs = api.get_api_documentation()
for method_name, doc in docs.items():
    print(f"\n{method_name}{doc['signature']}:")
    print(f"  {doc['docstring']}")
    if doc['parameters']:
        print("  Параметры:")
        for param in doc['parameters']:
            default_info = f" = {param['default']}" if param['default'] is not None else ""
            print(f"    - {param['name']}: {param['type']}{default_info}")

print("\n=== Использование API ===")
# Создаем пользователей
user1 = api.call_api_method('create_user', 'Иван Иванов', 'ivan@example.com', 25)
user2 = api.call_api_method('create_user', 'Анна Петрова', 'anna@example.com', 30)

print(f"Создан пользователь: {user1}")
print(f"Создан пользователь: {user2}")

# Получаем пользователя
retrieved_user = api.call_api_method('get_user', 1)
print(f"Получен пользователь: {retrieved_user}")

# Обновляем пользователя
updated_user = api.call_api_method('update_user', 1, age=26, city='Москва')
print(f"Обновлен пользователь: {updated_user}")

# Список пользователей
users_list = api.call_api_method('list_users', min_age=25)
print(f"Пользователи от 25 лет: {users_list}")
```


#### 3.2 Продвинутые дескрипторы

**Вопрос:** "Создайте дескриптор с lazy loading и кешированием"

```python
import time
from typing import Any, Callable, Optional
from functools import wraps

class LazyProperty:
    """Дескриптор для ленивой загрузки свойств с кешированием"""
    
    def __init__(self, func: Callable, cache_ttl: Optional[float] = None):
        self.func = func
        self.cache_ttl = cache_ttl
        self.attr_name = f'_lazy_{func.__name__}'
        self.cache_time_attr = f'_lazy_{func.__name__}_time'
        
        # Сохраняем метаданные функции
        wraps(func)(self)
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        
        # Проверяем кеш
        cached_value = getattr(obj, self.attr_name, None)
        
        if cached_value is not None:
            # Проверяем TTL если он установлен
            if self.cache_ttl:
                cache_time = getattr(obj, self.cache_time_attr, 0)
                if time.time() - cache_time > self.cache_ttl:
                    # Кеш устарел, удаляем его
                    delattr(obj, self.attr_name)
                    if hasattr(obj, self.cache_time_attr):
                        delattr(obj, self.cache_time_attr)
                else:
                    # Кеш актуален
                    print(f"🔍 Возвращаем кешированное значение для {self.func.__name__}")
                    return cached_value
            else:
                # TTL не установлен, возвращаем кешированное значение
                print(f"🔍 Возвращаем кешированное значение для {self.func.__name__}")
                return cached_value
        
        # Вычисляем значение
        print(f"⚡ Вычисляем значение для {self.func.__name__}")
        value = self.func(obj)
        
        # Кешируем результат
        setattr(obj, self.attr_name, value)
        if self.cache_ttl:
            setattr(obj, self.cache_time_attr, time.time())
        
        return value
    
    def __set__(self, obj, value):
        """Позволяет принудительно установить значение"""
        setattr(obj, self.attr_name, value)
        if self.cache_ttl:
            setattr(obj, self.cache_time_attr, time.time())
    
    def __delete__(self, obj):
        """Очистка кеша"""
        if hasattr(obj, self.attr_name):
            delattr(obj, self.attr_name)
        if hasattr(obj, self.cache_time_attr):
            delattr(obj, self.cache_time_attr)

class TypedAttribute:
    """Дескриптор с проверкой типов"""
    
    def __init__(self, expected_type, default=None, validator=None):
        self.expected_type = expected_type
        self.default = default
        self.validator = validator
        self.name = None
    
    def __set_name__(self, owner, name):
        """Автоматически вызывается при создании класса"""
        self.name = name
        self.private_name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, self.default)
    
    def __set__(self, obj, value):
        # Проверка типа
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"Атрибут {self.name} должен быть типа {self.expected_type.__name__}, "
                f"получен {type(value).__name__}"
            )
        
        # Дополнительная валидация
        if self.validator and not self.validator(value):
            raise ValueError(f"Значение {value} не прошло валидацию для {self.name}")
        
        setattr(obj, self.private_name, value)

def lazy_property(cache_ttl=None):
    """Декоратор для создания ленивых свойств"""
    def decorator(func):
        return LazyProperty(func, cache_ttl)
    return decorator

# Пример использования
class DataProcessor:
    """Процессор данных с ленивой загрузкой"""
    
    # Типизированные атрибуты
    name = TypedAttribute(str, "Unnamed")
    batch_size = TypedAttribute(int, 100, lambda x: x > 0)
    
    def __init__(self, name: str, data_source: str):
        self.name = name
        self.data_source = data_source
        self.batch_size = 100
    
    @lazy_property(cache_ttl=5.0)  # Кеш на 5 секунд
    def expensive_data(self):
        """Дорогая операция загрузки данных"""
        print(f"🔄 Загружаем данные из {self.data_source}...")
        time.sleep(2)  # Имитация долгой операции
        return f"Данные из {self.data_source} (загружено в {time.strftime('%H:%M:%S')})"
    
    @lazy_property()  # Кеш без TTL
    def metadata(self):
        """Метаданные (кешируются навсегда)"""
        print("🔄 Вычисляем метаданные...")
        time.sleep(1)
        return {
            'processor_name': self.name,
            'data_source': self.data_source,
            'created_at': time.time()
        }
    
    @lazy_property(cache_ttl=3.0)  # Кеш на 3 секунды
    def statistics(self):
        """Статистика обработки"""
        print("🔄 Вычисляем статистику...")
        time.sleep(1.5)
        return {
            'total_records': 1000,
            'processed_records': 750,
            'errors': 5,
            'calculated_at': time.strftime('%H:%M:%S')
        }
    
    def clear_cache(self):
        """Очистка всех кешей"""
        for attr_name in ['expensive_data', 'metadata', 'statistics']:
            try:
                delattr(self, attr_name)
                print(f"🗑️ Очищен кеш для {attr_name}")
            except AttributeError:
                pass

# Демонстрация
print("=== Создание процессора ===")
processor = DataProcessor("Анализатор логов", "database://logs")

print(f"Имя процессора: {processor.name}")
print(f"Размер батча: {processor.batch_size}")

print("\n=== Первое обращение к expensive_data ===")
data1 = processor.expensive_data
print(f"Результат: {data1}")

print("\n=== Второе обращение к expensive_data (из кеша) ===")
data2 = processor.expensive_data
print(f"Результат: {data2}")

print("\n=== Обращение к metadata ===")
meta1 = processor.metadata
print(f"Метаданные: {meta1}")

print("\n=== Повторное обращение к metadata (из кеша) ===")
meta2 = processor.metadata
print(f"Метаданные: {meta2}")

print("\n=== Ждем истечения TTL для expensive_data ===")
time.sleep(6)
data3 = processor.expensive_data  # Должно пересчитаться
print(f"Результат после TTL: {data3}")

print("\n=== Тестирование типизированных атрибутов ===")
try:
    processor.batch_size = "invalid"  # TypeError
except TypeError as e:
    print(f"Ошибка типа: {e}")

try:
    processor.batch_size = -10  # ValueError (валидация)
except ValueError as e:
    print(f"Ошибка валидации: {e}")

processor.batch_size = 200  # OK
print(f"Новый размер батча: {processor.batch_size}")

print("\n=== Очистка кеша ===")
processor.clear_cache()
```


### Блок 4: Паттерны проектирования

#### 4.1 Реализация паттерна Command с undo/redo

**Вопрос:** "Реализуйте паттерн Command с поддержкой отмены операций"

```python
from abc import ABC, abstractmethod
from typing import List, Any, Dict
from datetime import datetime
import copy

class Command(ABC):
    """Абстрактная команда"""
    
    @abstractmethod
    def execute(self) -> Any:
        """Выполнить команду"""
        pass
    
    @abstractmethod
    def undo(self) -> Any:
        """Отменить команду"""
        pass
    
    @abstractmethod
    def get_description(self) -> str:
        """Описание команды"""
        pass

class Document:
    """Документ для демонстрации команд"""
    
    def __init__(self, content: str = ""):
        self.content = content
        self.metadata = {}
    
    def insert_text(self, position: int, text: str):
        """Вставка текста в позицию"""
        self.content = self.content[:position] + text + self.content[position:]
    
    def delete_text(self, position: int, length: int) -> str:
        """Удаление текста и возврат удаленного"""
        deleted = self.content[position:position + length]
        self.content = self.content[:position] + self.content[position + length:]
        return deleted
    
    def replace_text(self, position: int, length: int, new_text: str) -> str:
        """Замена текста и возврат замененного"""
        old_text = self.content[position:position + length]
        self.content = self.content[:position] + new_text + self.content[position + length:]
        return old_text
    
    def set_metadata(self, key: str, value: Any) -> Any:
        """Установка метаданных и возврат старого значения"""
        old_value = self.metadata.get(key)
        self.metadata[key] = value
        return old_value
    
    def __str__(self):
        return f"Document(content='{self.content}', metadata={self.metadata})"

class InsertTextCommand(Command):
    """Команда вставки текста"""
    
    def __init__(self, document: Document, position: int, text: str):
        self.document = document
        self.position = position
        self.text = text
        self.executed = False
    
    def execute(self):
        if self.executed:
            raise RuntimeError("Команда уже выполнена")
        
        self.document.insert_text(self.position, self.text)
        self.executed = True
        return f"Вставлен текст '{self.text}' в позицию {self.position}"
    
    def undo(self):
        if not self.executed:
            raise RuntimeError("Команда не была выполнена")
        
        self.document.delete_text(self.position, len(self.text))
        self.executed = False
        return f"Отменена вставка текста '{self.text}'"
    
    def get_description(self):
        return f"Вставить '{self.text}' в позицию {self.position}"

class DeleteTextCommand(Command):
    """Команда удаления текста"""
    
    def __init__(self, document: Document, position: int, length: int):
        self.document = document
        self.position = position
        self.length = length
        self.deleted_text = None
        self.executed = False
    
    def execute(self):
        if self.executed:
            raise RuntimeError("Команда уже выполнена")
        
        self.deleted_text = self.document.delete_text(self.position, self.length)
        self.executed = True
        return f"Удален текст '{self.deleted_text}' из позиции {self.position}"
    
    def undo(self):
        if not self.executed:
            raise RuntimeError("Команда не была выполнена")
        
        self.document.insert_text(self.position, self.deleted_text)
        self.executed = False
        return f"Восстановлен текст '{self.deleted_text}'"
    
    def get_description(self):
        return f"Удалить {self.length} символов из позиции {self.position}"

class ReplaceTextCommand(Command):
    """Команда замены текста"""
    
    def __init__(self, document: Document, position: int, length: int, new_text: str):
        self.document = document
        self.position = position
        self.length = length
        self.new_text = new_text
        self.old_text = None
        self.executed = False
    
    def execute(self):
        if self.executed:
            raise RuntimeError("Команда уже выполнена")
        
        self.old_text = self.document.replace_text(self.position, self.length, self.new_text)
        self.executed = True
        return f"Заменен текст '{self.old_text}' на '{self.new_text}'"
    
    def undo(self):
        if not self.executed:
            raise RuntimeError("Команда не была выполнена")
        
        self.document.replace_text(self.position, len(self.new_text), self.old_text)
        self.executed = False
        return f"Восстановлен текст '{self.old_text}'"
    
    def get_description(self):
        return f"Заменить {self.length} символов на '{self.new_text}'"

class MacroCommand(Command):
    """Макрокоманда - выполняет несколько команд как одну"""
    
    def __init__(self, commands: List[Command], description: str):
        self.commands = commands
        self.description = description
        self.executed_commands = []
    
    def execute(self):
        results = []
        self.executed_commands = []
        
        try:
            for command in self.commands:
                result = command.execute()
                results.append(result)
                self.executed_commands.append(command)
        except Exception as e:
            # Откатываем уже выполненные команды
            for executed_command in reversed(self.executed_commands):
                try:
                    executed_command.undo()
                except:
                    pass
            self.executed_commands = []
            raise e
        
        return f"Выполнена макрокоманда: {'; '.join(results)}"
    
    def undo(self):
        if not self.executed_commands:
            raise RuntimeError("Макрокоманда не была выполнена")
        
        results = []
        for command in reversed(self.executed_commands):
            result = command.undo()
            results.append(result)
        
        self.executed_commands = []
        return f"Отменена макрокоманда: {'; '.join(results)}"
    
    def get_description(self):
        return self.description

class CommandHistory:
    """История команд с поддержкой undo/redo"""
    
    def __init__(self, max_history: int = 100):
        self.max_history = max_history
        self.history: List[Command] = []
        self.current_position = -1
    
    def execute_command(self, command: Command) -> str:
        """Выполнить команду и добавить в историю"""
        result = command.execute()
        
        # Удаляем команды после текущей позиции (если делали undo)
        self.history = self.history[:self.current_position + 1]
        
        # Добавляем новую команду
        self.history.append(command)
        self.current_position += 1
        
        # Ограничиваем размер истории
        if len(self.history) > self.max_history:
            self.history.pop(0)
            self.current_position -= 1
        
        return result
    
    def undo(self) -> str:
        """Отменить последнюю команду"""
        if self.current_position < 0:
            return "Нет команд для отмены"
        
        command = self.history[self.current_position]
        result = command.undo()
        self.current_position -= 1
        
        return result
    
    def redo(self) -> str:
        """Повторить отмененную команду"""
        if self.current_position >= len(self.history) - 1:
            return "Нет команд для повтора"
        
        self.current_position += 1
        command = self.history[self.current_position]
        result = command.execute()
        
        return result
    
    def get_history(self) -> List[Dict[str, Any]]:
        """Получить историю команд"""
        history_info = []
        for i, command in enumerate(self.history):
            history_info.append({
                'index': i,
                'description': command.get_description(),
                'executed': i <= self.current_position,
                'current': i == self.current_position
            })
        return history_info
    
    def can_undo(self) -> bool:
        """Можно ли отменить команду"""
        return self.current_position >= 0
    
    def can_redo(self) -> bool:
        """Можно ли повторить команду"""
        return self.current_position < len(self.history) - 1

# Демонстрация
print("=== Создание документа и истории команд ===")
doc = Document("Привет, мир!")
history = CommandHistory()

print(f"Исходный документ: {doc}")

print("\n=== Выполнение команд ===")

# Команда 1: Вставка текста
cmd1 = InsertTextCommand(doc, 7, " прекрасный")
result1 = history.execute_command(cmd1)
print(f"1. {result1}")
print(f"   Документ: {doc}")

# Команда 2: Замена текста
cmd2 = ReplaceTextCommand(doc, 0, 6, "Добро пожаловать")
result2 = history.execute_command(cmd2)
print(f"2. {result2}")
print(f"   Документ: {doc}")

# Команда 3: Удаление текста
cmd3 = DeleteTextCommand(doc, 16, 11)  # Удаляем " прекрасный"
result3 = history.execute_command(cmd3)
print(f"3. {result3}")
print(f"   Документ: {doc}")

# Макрокоманда
macro_commands = [
    InsertTextCommand(doc, 16, " и"),
    InsertTextCommand(doc, 18, " удивительный")
]
macro = MacroCommand(macro_commands, "Добавить эпитеты")
result4 = history.execute_command(macro)
print(f"4. {result4}")
print(f"   Документ: {doc}")

print("\n=== История команд ===")
for cmd_info in history.get_history():
    status = "✓" if cmd_info['executed'] else "○"
    current = " <- ТЕКУЩАЯ" if cmd_info['current'] else ""
    print(f"{status} {cmd_info['index']}: {cmd_info['description']}{current}")

print(f"\nМожно отменить: {history.can_undo()}")
print(f"Можно повторить: {history.can_redo()}")

print("\n=== Отмена команд ===")
undo1 = history.undo()
print(f"Отмена 1: {undo1}")
print(f"Документ: {doc}")

undo2 = history.undo()
print(f"Отмена 2: {undo2}")
print(f"Документ: {doc}")

print("\n=== Повтор команд ===")
redo1 = history.redo()
print(f"Повтор 1: {redo1}")
print(f"Документ: {doc}")

print("\n=== Финальная история ===")
for cmd_info in history.get_history():
    status = "✓" if cmd_info['executed'] else "○"
    current = " <- ТЕКУЩАЯ" if cmd_info['current'] else ""
    print(f"{status} {cmd_info['index']}: {cmd_info['description']}{current}")
```


### Блок 5: Тестирование ООП кода

#### 5.1 Моки и заглушки для тестирования

**Вопрос:** "Как тестировать классы с внешними зависимостями?"

```python
import unittest
from unittest.mock import Mock, patch, MagicMock
from typing import Protocol
import requests

# Интерфейс для внешнего API
class PaymentGateway(Protocol):
    def process_payment(self, amount: float, card_token: str) -> dict:
        ...
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        ...

# Реальная реализация
class StripePaymentGateway:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.stripe.com/v1"
    
    def process_payment(self, amount: float, card_token: str) -> dict:
        # В реальности здесь был бы HTTP запрос
        response = requests.post(
            f"{self.base_url}/charges",
            headers={"Authorization": f"Bearer {self.api_key}"},
            data={
                "amount": int(amount * 100),  # В центах
                "currency": "usd",
                "source": card_token
            }
        )
        return response.json()
    
    def refund_payment(self, transaction_id: str, amount: float) -> dict:
        response = requests.post(
            f"{self.base_url}/refunds",
            headers={"Authorization": f"Bearer {self.api_key}"},
            data={
                "charge": transaction_id,
                "amount": int(amount * 100)
            }
        )
        return response.json()

# Класс для тестирования
class PaymentService:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway
        self.processed_payments = []
    
    def charge_customer(self, customer_id: str, amount: float, card_token: str) -> dict:
        if amount <= 0:
            raise ValueError("Сумма должна быть положительной")
        
        if amount > 10000:
            raise ValueError("Сумма превышает лимит")
        
        try:
            result = self.payment_gateway.process_payment(amount, card_token)
            
            payment_record = {
                'customer_id': customer_id,
                'amount': amount,
                'transaction_id': result.get('id'),
                'status': 'success' if result.get('paid') else 'failed',
                'gateway_response': result
            }
            
            self.processed_payments.append(payment_record)
            return payment_record
            
        except Exception as e:
            payment_record = {
                'customer_id': customer_id,
                'amount': amount,
                'transaction_id': None,
                'status': 'error',
                'error': str(e)
            }
            self.processed_payments.append(payment_record)
            raise
    
    def refund_customer(self, transaction_id: str, amount: float) -> dict:
        # Найти оригинальный платеж
        original_payment = None
        for payment in self.processed_payments:
            if payment['transaction_id'] == transaction_id:
                original_payment = payment
                break
        
        if not original_payment:
            raise ValueError("Транзакция не найдена")
        
        if original_payment['status'] != 'success':
            raise ValueError("Можно возвращать только успешные платежи")
        
        if amount > original_payment['amount']:
            raise ValueError("Сумма возврата больше оригинального платежа")
        
        result = self.payment_gateway.refund_payment(transaction_id, amount)
        
        refund_record = {
            'original_transaction_id': transaction_id,
            'refund_amount': amount,
            'refund_id': result.get('id'),
            'status': 'success' if result.get('status') == 'succeeded' else 'failed',
            'gateway_response': result
        }
        
        return refund_record
    
    def get_payment_history(self, customer_id: str) -> list:
        return [p for p in self.processed_payments if p['customer_id'] == customer_id]

# Тесты
class TestPaymentService(unittest.TestCase):
    
    def setUp(self):
        """Настройка для каждого теста"""
        self.mock_gateway = Mock(spec=PaymentGateway)
        self.payment_service = PaymentService(self.mock_gateway)
    
    def test_successful_payment(self):
        """Тест успешного платежа"""
        # Настраиваем мок
        self.mock_gateway.process_payment.return_value = {
            'id': 'ch_test123',
            'paid': True,
            'amount': 5000,  # В центах
            'currency': 'usd'
        }
        
        # Выполняем операцию
        result = self.payment_service.charge_customer(
            customer_id='cust_123',
            amount=50.0,
            card_token='tok_visa'
        )
        
        # Проверяем результат
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['customer_id'], 'cust_123')
        self.assertEqual(result['amount'], 50.0)
        self.assertEqual(result['transaction_id'], 'ch_test123')
        
        # Проверяем, что мок был вызван правильно
        self.mock_gateway.process_payment.assert_called_once_with(50.0, 'tok_visa')
        
        # Проверяем историю
        self.assertEqual(len(self.payment_service.processed_payments), 1)
    
    def test_payment_validation(self):
        """Тест валидации платежей"""
        # Тест отрицательной суммы
        with self.assertRaises(ValueError) as context:
            self.payment_service.charge_customer('cust_123', -10.0, 'tok_visa')
        self.assertIn("положительной", str(context.exception))
        
        # Тест превышения лимита
        with self.assertRaises(ValueError) as context:
            self.payment_service.charge_customer('cust_123', 15000.0, 'tok_visa')
        self.assertIn("лимит", str(context.exception))
        
        # Проверяем, что gateway не вызывался
        self.mock_gateway.process_payment.assert_not_called()
    
    def test_payment_gateway_error(self):
        """Тест ошибки от платежного шлюза"""
        # Настраиваем мок на выброс исключения
        self.mock_gateway.process_payment.side_effect = Exception("Network error")
        
        # Проверяем, что исключение пробрасывается
        with self.assertRaises(Exception) as context:
            self.payment_service.charge_customer('cust_123', 50.0, 'tok_visa')
        self.assertIn("Network error", str(context.exception))
        
        # Проверяем, что ошибка записана в историю
        self.assertEqual(len(self.payment_service.processed_payments), 1)
        error_record = self.payment_service.processed_payments[0]
        self.assertEqual(error_record['status'], 'error')
        self.assertIn("Network error", error_record['error'])
    
    def test_successful_refund(self):
        """Тест успешного возврата"""
        # Сначала создаем успешный платеж
        self.mock_gateway.process_payment.return_value = {
            'id': 'ch_test123',
            'paid': True,
            'amount': 5000
        }
        
        self.payment_service.charge_customer('cust_123', 50.0, 'tok_visa')
        
        # Настраиваем мок для возврата
        self.mock_gateway.refund_payment.return_value = {
            'id': 'ref_test456',
            'status': 'succeeded',
            'amount': 2500
        }
        
        # Выполняем возврат
        refund_result = self.payment_service.refund_customer('ch_test123', 25.0)
        
        # Проверяем результат
        self.assertEqual(refund_result['status'], 'success')
        self.assertEqual(refund_result['refund_amount'], 25.0)
        self.assertEqual(refund_result['refund_id'], 'ref_test456')
        
        # Проверяем вызов мока
        self.mock_gateway.refund_payment.assert_called_once_with('ch_test123', 25.0)
    
    def test_refund_validation(self):
        """Тест валидации возвратов"""
        # Тест возврата несуществующей транзакции
        with self.assertRaises(ValueError) as context:
            self.payment_service.refund_customer('nonexistent', 10.0)
        self.assertIn("не найдена", str(context.exception))
        
        # Создаем неуспешный платеж
        self.payment_service.processed_payments.append({
            'customer_id': 'cust_123',
            'amount': 50.0,
            'transaction_id': 'ch_failed',
            'status': 'failed'
        })
        
        # Тест возврата неуспешного платежа
        with self.assertRaises(ValueError) as context:
            self.payment_service.refund_customer('ch_failed', 10.0)
        self.assertIn("успешные платежи", str(context.exception))
    
    @patch('requests.post')
    def test_real_gateway_integration(self, mock_post):
        """Тест интеграции с реальным gateway через patch"""
        # Настраиваем мок для requests.post
        mock_response = Mock()
        mock_response.json.return_value = {
            'id': 'ch_real123',
            'paid': True,
            'amount': 5000
        }
        mock_post.return_value = mock_response
        
        # Создаем реальный gateway
        real_gateway = StripePaymentGateway('sk_test_123')
        real_service = PaymentService(real_gateway)
        
        # Выполняем операцию
        result = real_service.charge_customer('cust_123', 50.0, 'tok_visa')
        
        # Проверяем результат
        self.assertEqual(result['status'], 'success')
        self.assertEqual(result['transaction_id'], 'ch_real123')
        
        # Проверяем, что HTTP запрос был сделан правильно
        mock_post.assert_called_once()
        call_args = mock_post.call_args
        self.assertIn('https://api.stripe.com/v1/charges', call_args[0])
        self.assertIn('Authorization', call_args[1]['headers'])

# Запуск тестов
if __name__ == '__main__':
    # Создаем test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPaymentService)
    
    # Запускаем тесты с подробным выводом
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    print(f"\nВыполнено тестов: {result.testsRun}")
    print(f"Ошибок: {len(result.errors)}")
    print(f"Неудач: {len(result.failures)}")
    
    if result.errors:
        print("\nОшибки:")
        for test, error in result.errors:
            print(f"- {test}: {error}")
    
    if result.failures:
        print("\nНеудачи:")
        for test, failure in result.failures:
            print(f"- {test}: {failure}")
```


## 🎯 Дополнительные сложные вопросы

### 6.1 Работа с памятью и производительностью

**Вопрос:** "Как оптимизировать классы для экономии памяти?"

```python
import sys
from typing import NamedTuple

# Обычный класс
class RegularPoint:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Класс с __slots__
class SlottedPoint:
    __slots__ = ['x', 'y', 'z']
    
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# NamedTuple
class TuplePoint(NamedTuple):
    x: float
    y: float
    z: float

# Сравнение использования памяти
regular = RegularPoint(1.0, 2.0, 3.0)
slotted = SlottedPoint(1.0, 2.0, 3.0)
tuple_point = TuplePoint(1.0, 2.0, 3.0)

print(f"Обычный класс: {sys.getsizeof(regular)} + {sys.getsizeof(regular.__dict__)} = {sys.getsizeof(regular) + sys.getsizeof(regular.__dict__)} байт")
print(f"Класс с __slots__: {sys.getsizeof(slotted)} байт")
print(f"NamedTuple: {sys.getsizeof(tuple_point)} байт")
```


### 6.2 Продвинутая работа с исключениями

**Вопрос:** "Создайте иерархию исключений для API"

```python
class APIException(Exception):
    """Базовое исключение API"""
    
    def __init__(self, message, error_code=None, details=None):
        super().__init__(message)
        self.error_code = error_code
        self.details = details or {}
        self.timestamp = datetime.now()
    
    def to_dict(self):
        return {
            'error': self.__class__.__name__,
            'message': str(self),
            'error_code': self.error_code,
            'details': self.details,
            'timestamp': self.timestamp.isoformat()
        }

class ValidationError(APIException):
    """Ошибка валидации данных"""
    pass

class AuthenticationError(APIException):
    """Ошибка аутентификации"""
    pass

class AuthorizationError(APIException):
    """Ошибка авторизации"""
    pass

class ResourceNotFoundError(APIException):
    """Ресурс не найден"""
    pass

class RateLimitError(APIException):
    """Превышен лимит запросов"""
    
    def __init__(self, message, retry_after=None):
        super().__init__(message, error_code="RATE_LIMIT_EXCEEDED")
        self.retry_after = retry_after
        if retry_after:
            self.details['retry_after'] = retry_after

# Использование
try:
    raise RateLimitError("Слишком много запросов", retry_after=60)
except APIException as e:
    print(f"API Error: {e.to_dict()}")
```


## 📝 Финальные рекомендации для собеседования

### Что обязательно нужно знать:

1. **Основы ООП** - инкапсуляция, наследование, полиморфизм, абстракция
2. **Магические методы** - `__init__`, `__str__`, `__repr__`, `__eq__`, `__hash__`
3. **Дескрипторы и свойства** - `@property`, создание собственных дескрипторов
4. **Метаклассы** - понимание `type`, создание простых метаклассов
5. **Паттерны проектирования** - Singleton, Factory, Observer, Strategy, Command
6. **MRO и множественное наследование** - понимание алгоритма C3
7. **Контекстные менеджеры** - `__enter__`, `__exit__`
8. **ABC и протоколы** -
