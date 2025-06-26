"""
Примеры использования кортежей (tuple) в Python
1. Базовые примеры
2. Примеры из коммерческой разработки
"""

# 1. Базовые примеры использования tuple

# Создание кортежа
point = (10, 20)
print("Кортеж point:", point)

# Кортеж из одного элемента (обязательно запятая!)
single = (5,)
print("Кортеж из одного элемента:", single)

# Доступ к элементам по индексу
print("X:", point[0])
print("Y:", point[1])

# Распаковка кортежа
x, y = point
print(f"Распаковка: x={x}, y={y}")

# Кортежи могут быть элементами списков и словарей
points = [(0, 0), (1, 2), (3, 4)]
print("Список точек:", points)

# Кортежи неизменяемы (immutable)
try:
    point[0] = 100
except TypeError as e:
    print("Ошибка изменения кортежа:", e)

# Использование в качестве ключа словаря
locations = { (55.75, 37.61): "Москва", (59.93, 30.31): "Санкт-Петербург" }
print("Город по координатам (55.75, 37.61):", locations[(55.75, 37.61)])

# 2. Примеры использования tuple в коммерческой разработке

# --- Пример 1: Возврат нескольких значений из функции

def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [3, 7, 2, 9, 4]
min_val, max_val = get_min_max(nums)
print(f"Минимум: {min_val}, Максимум: {max_val}")

# --- Пример 2: Использование tuple для представления записей из базы данных
rows = [
    (1, "Alice", "admin"),
    (2, "Bob", "user"),
    (3, "Eve", "user")
]
for user_id, name, role in rows:
    print(f"ID: {user_id}, Name: {name}, Role: {role}")

# --- Пример 3: Использование tuple для координат, RGB-цветов и других фиксированных структур
rgb = (255, 200, 100)
print("Цвет RGB:", rgb)

# --- Пример 4: Возврат статуса и сообщения из функции

def process_payment(amount):
    if amount > 0:
        return True, "Оплата прошла успешно"
    else:
        return False, "Ошибка оплаты"

success, message = process_payment(1000)
print(f"Статус: {success}, Сообщение: {message}")

# --- Пример 5: Использование enumerate для получения индекса и значения
products = ["apple", "banana", "cherry"]
for idx, product in enumerate(products, 1):
    print(f"{idx}: {product}") 