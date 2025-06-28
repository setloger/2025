"""
Примеры использования словарей (dict) в Python
1. Базовые примеры
2. Примеры из коммерческой разработки
"""

# 1. Базовые примеры использования dict

# Создание словаря
person = {"name": "Alice", "age": 30, "city": "Moscow"}
print("Словарь person:", person)

# Доступ к значениям по ключу
print("Имя:", person["name"])

# Добавление новой пары ключ-значение
person["email"] = "alice@example.com"
print("Добавлен email:", person)

# Изменение значения по ключу
person["age"] = 31
print("Изменён возраст:", person)

# Удаление пары по ключу
person.pop("city")
print("Удалён город:", person)

# Перебор ключей и значений
for key, value in person.items():
    print(f"{key}: {value}")

# Проверка наличия ключа
if "email" in person:
    print("Email найден:", person["email"])

# Получение всех ключей и значений
print("Ключи:", list(person.keys()))
print("Значения:", list(person.values()))

# 2. Примеры использования dict в коммерческой разработке

# --- Пример 1: Хранение и обработка данных пользователей (например, из базы данных)
users = [
    {"id": 1, "name": "Alice", "role": "admin"},
    {"id": 2, "name": "Bob", "role": "user"},
    {"id": 3, "name": "Eve", "role": "user"}
]
# Получить имена всех администраторов
admins = [user["name"] for user in users if user["role"] == "admin"]
print("Администраторы:", admins)

# --- Пример 2: Подсчёт количества заказов по статусу
orders = [
    {"id": 101, "status": "new"},
    {"id": 102, "status": "shipped"},
    {"id": 103, "status": "new"},
    {"id": 104, "status": "delivered"},
    {"id": 105, "status": "shipped"}
]
order_stats = {}
for order in orders:
    status = order["status"]
    order_stats[status] = order_stats.get(status, 0) + 1
print("Статистика заказов по статусу:", order_stats)

# --- Пример 3: Быстрый доступ к объекту по id (маппинг)
user_map = {user["id"]: user for user in users}
print("Пользователь с id=2:", user_map[2])

# --- Пример 4: Группировка данных по ключу
from collections import defaultdict
groups = defaultdict(list)
for user in users:
    groups[user["role"]].append(user["name"])
print("Группировка пользователей по ролям:", dict(groups))

# --- Пример 5: Использование dict для передачи параметров в функцию (kwargs)
def send_email(to, subject, **kwargs):
    print(f"Отправка письма {to} с темой '{subject}' и параметрами: {kwargs}")

params = {"cc": "boss@example.com", "priority": "high"}
send_email("client@example.com", "Invoice", **params) 