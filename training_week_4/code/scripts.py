# 5. Декораторы
# ============

# def timer_decorator(func):
#     """Декоратор для измерения времени выполнения функции"""
#     import time

#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"Функция {func.__name__} выполнилась за {end_time -
#         start_time:.4f} секунд")
#         return result
#     return wrapper


# @timer_decorator
# def slow_function():
#     """Медленная функция для демонстрации декоратора"""
#     import time
#     time.sleep(2)
#     return "Функция завершена"


# print("=== ДЕКОРАТОРЫ ===")
# result = slow_function()
# print(f"Результат: {result}")


def cache_decorator(func):
    """Простой декоратор-кэш"""
    cache = {}

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


@cache_decorator
def expensive_calculation(n):
    """Дорогая операция для демонстрации кэширования"""
    import time
    time.sleep(1)
    return n * n


print("\nКэширование:")
print(f"Первый вызов: {expensive_calculation(5)}")
print(f"Второй вызов (из кэша): {expensive_calculation(5)}")
print()




# Разбиваем строки по разделителю и преобразуем в вложенные кортежи
data = [tuple(row.split(';')) for row in lst_in]

# Заголовки
header = data[0]

# Преобразуем числовые строки в целые числа, если это числовые колонки
converted = [tuple(int(x) if i in [0, 2] else x for i, x in enumerate(row)) for row in data[1:]]

# Объединяем заголовок и данные
t = (tuple(header), *converted)

# Новый порядок заголовков
new_order = ['Имя', 'Зачет', 'Оценка', 'Номер']

# Получаем индексы нового порядка
idx_map = [header.index(col) for col in new_order]

# Перестраиваем кортежи согласно новому порядку
t_reordered = (tuple(new_order), *[tuple(row[i] for i in idx_map) for row in t[1:]])

# Сортируем по алфавиту, по 'Имя'
t_sorted = (t_reordered[0], *sorted(t_reordered[1:], key=lambda x: x[0]))
