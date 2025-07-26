# Конструкция match/case со словарями и множествами

Конструкция `match/case` в Python 3.10+ представляет собой мощный инструмент для сопоставления с образцом (pattern matching), который особенно эффективен при работе со словарями и множествами. Рассмотрим подробно, как использовать эту конструкцию с данными структурами данных.

## Основы конструкции match/case

Синтаксис `match/case` позволяет проверять значение на соответствие различным образцам (patterns) и выполнять соответствующий код:

```python
match значение:
    case образец1:
        # код для образца1
    case образец2:
        # код для образца2
    case _:  # default случай
        # код по умолчанию
```


## Работа со словарями

### Базовое сопоставление словарей

При работе со словарями `match/case` позволяет проверять наличие определенных ключей и их значений:

```python
def process_user(user_data):
    match user_data:
        case {"name": str(name), "age": int(age)} if age >= 18:
            return f"Взрослый пользователь: {name}, {age} лет"
        case {"name": str(name), "age": int(age)} if age < 18:
            return f"Несовершеннолетний: {name}, {age} лет"
        case {"name": str(name)}:
            return f"Пользователь без указанного возраста: {name}"
        case {}:
            return "Пустой словарь"
        case _:
            return "Неверный формат данных"

# Примеры использования
print(process_user({"name": "Анна", "age": 25}))  # Взрослый пользователь: Анна, 25 лет
print(process_user({"name": "Петя", "age": 16}))  # Несовершеннолетний: Петя, 16 лет
print(process_user({"name": "Мария"}))           # Пользователь без указанного возраста: Мария
```


### Сопоставление с дополнительными ключами

Можно использовать оператор `**rest` для захвата дополнительных ключей:

```python
def analyze_product(product):
    match product:
        case {"name": str(name), "price": float(price), **extras}:
            result = f"Товар: {name}, цена: {price}"
            if extras:
                result += f", дополнительно: {extras}"
            return result
        case {"name": str(name), **rest}:
            return f"Товар {name} без цены, данные: {rest}"
        case _:
            return "Неизвестный формат товара"

# Примеры
product1 = {"name": "Ноутбук", "price": 50000.0, "brand": "ASUS", "warranty": 2}
print(analyze_product(product1))
# Товар: Ноутбук, цена: 50000.0, дополнительно: {'brand': 'ASUS', 'warranty': 2}

product2 = {"name": "Мышь", "color": "черная"}
print(analyze_product(product2))
# Товар Мышь без цены, данные: {'color': 'черная'}
```


### Вложенные словари

`match/case` отлично работает с вложенными структурами:

```python
def process_order(order):
    match order:
        case {
            "id": int(order_id),
            "customer": {"name": str(customer_name), "email": str(email)},
            "items": list(items)
        }:
            return f"Заказ #{order_id} для {customer_name} ({email}), товаров: {len(items)}"
        case {"id": int(order_id), "status": "cancelled"}:
            return f"Заказ #{order_id} отменен"
        case _:
            return "Неполные данные заказа"

# Пример использования
order = {
    "id": 12345,
    "customer": {"name": "Иван Петров", "email": "ivan@example.com"},
    "items": ["товар1", "товар2", "товар3"]
}
print(process_order(order))
# Заказ #12345 для Иван Петров (ivan@example.com), товаров: 3
```


## Работа с множествами

### Базовое сопоставление множеств

С множествами можно использовать различные подходы:

```python
def analyze_permissions(permissions):
    match permissions:
        case set() if not permissions:  # пустое множество
            return "Нет разрешений"
        case {"read", "write", "admin"}:
            return "Полный доступ администратора"
        case {"read", "write"}:
            return "Доступ на чтение и запись"
        case {"read"}:
            return "Только чтение"
        case perms if "admin" in perms:
            return f"Административные права: {perms}"
        case _:
            return f"Другие разрешения: {permissions}"

# Примеры
print(analyze_permissions({"read", "write", "admin"}))  # Полный доступ администратора
print(analyze_permissions({"read", "write"}))           # Доступ на чтение и запись
print(analyze_permissions({"read"}))                    # Только чтение
print(analyze_permissions(set()))                       # Нет разрешений
```


### Проверка подмножеств

Можно проверять, содержит ли множество определенные элементы:

```python
def check_skills(user_skills):
    match user_skills:
        case skills if {"Python", "Django", "PostgreSQL"}.issubset(skills):
            return "Веб-разработчик Python (полный стек)"
        case skills if {"Python", "pandas", "numpy"}.issubset(skills):
            return "Data Scientist"
        case skills if {"JavaScript", "React", "Node.js"}.issubset(skills):
            return "Fullstack JavaScript разработчик"
        case skills if "Python" in skills:
            return "Python разработчик"
        case _:
            return "Профиль не определен"

# Примеры
skills1 = {"Python", "Django", "PostgreSQL", "HTML", "CSS"}
print(check_skills(skills1))  # Веб-разработчик Python (полный стек)

skills2 = {"Python", "pandas", "numpy", "matplotlib"}
print(check_skills(skills2))  # Data Scientist

skills3 = {"Java", "Spring", "MySQL"}
print(check_skills(skills3))  # Профиль не определен
```


## Комбинированное использование

Словари и множества часто используются вместе:

```python
def process_user_data(data):
    match data:
        case {
            "username": str(username),
            "roles": set(roles),
            "preferences": dict(prefs)
        }:
            if "admin" in roles:
                return f"Администратор {username} с настройками: {prefs}"
            elif "moderator" in roles:
                return f"Модератор {username}"
            else:
                return f"Пользователь {username} с ролями: {roles}"
        case {"username": str(username), "roles": set(roles)}:
            return f"Пользователь {username} без настроек, роли: {roles}"
        case _:
            return "Неверный формат данных пользователя"

# Пример
user_data = {
    "username": "alex_admin",
    "roles": {"admin", "user"},
    "preferences": {"theme": "dark", "language": "ru"}
}
print(process_user_data(user_data))
# Администратор alex_admin с настройками: {'theme': 'dark', 'language': 'ru'}
```


## Практический пример: система конфигурации

```python
def validate_config(config):
    match config:
        case {
            "database": {
                "host": str(host),
                "port": int(port),
                "name": str(db_name)
            },
            "features": set(features),
            **other_settings
        }:
            # Проверяем обязательные функции
            required_features = {"authentication", "logging"}
            if required_features.issubset(features):
                return {
                    "status": "valid",
                    "db_config": f"{host}:{port}/{db_name}",
                    "enabled_features": features,
                    "additional_settings": other_settings
                }
            else:
                missing = required_features - features
                return {
                    "status": "invalid",
                    "error": f"Отсутствуют обязательные функции: {missing}"
                }
        case {"database": dict(db_config)} if "host" not in db_config:
            return {"status": "invalid", "error": "Не указан хост базы данных"}
        case _:
            return {"status": "invalid", "error": "Неверная структура конфигурации"}

# Тестируем
config = {
    "database": {"host": "localhost", "port": 5432, "name": "myapp"},
    "features": {"authentication", "logging", "caching"},
    "debug": True,
    "max_connections": 100
}

result = validate_config(config)
print(f"Статус: {result['status']}")
if result['status'] == 'valid':
    print(f"БД: {result['db_config']}")
    print(f"Функции: {result['enabled_features']}")
```


## Ключевые особенности

**Преимущества match/case со словарями и множествами:**

- **Читаемость**: код становится более декларативным и понятным
- **Мощность**: можно проверять сложные структуры данных одним выражением
- **Гибкость**: поддержка guards (условий) с `if`
- **Производительность**: часто быстрее цепочки `if/elif`

**Важные моменты:**

- Образцы проверяются сверху вниз, первое совпадение выполняется
- Используйте `case _:` для обработки всех остальных случаев
- Guards с `if` позволяют добавлять дополнительные условия
- Сопоставление происходит по структуре, а не по идентичности объектов

Конструкция `match/case` значительно упрощает работу со сложными структурами данных и делает код более выразительным и безопасным.

