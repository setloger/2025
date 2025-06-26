Генераторы списков (List comprehensions) — это компактный и удобный способ создания списков в Python. Они позволяют создавать новый список, применяя выражение к каждому элементу последовательности (или итерируемого объекта), а также могут включать условие фильтрации.

**Общий синтаксис:**
```python
[выражение for элемент in последовательность if условие]
```

**Преимущества генераторов списков:**
- Компактность и читаемость кода.
- Часто работают быстрее, чем обычные циклы for с append.


### 1. Квадраты чисел
```python
squares = [x**2 for x in range(10)]
print(squares)
# Вывод: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

---

### 2. Только чётные числа
```python
evens = [x for x in range(20) if x % 2 == 0]
print(evens)
# Вывод: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

### 3. Преобразование строк в верхний регистр
```python
words = ['python', 'list', 'comprehension']
upper_words = [word.upper() for word in words]
print(upper_words)
# Вывод: ['PYTHON', 'LIST', 'COMPREHENSION']
```
---

### 4. Получить длины слов
```python
words = ['apple', 'banana', 'cherry']
lengths = [len(word) for word in words]
print(lengths)
# Вывод: [5, 6, 6]
```

---

### 5. Список пар (x, y)
```python
pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)
# Вывод: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
```

---

### 6. Замена отрицательных чисел на ноль
```python
numbers = [5, -3, 7, -1, 0]
no_negatives = [x if x > 0 else 0 for x in numbers]
print(no_negatives)
# Вывод: [5, 0, 7, 0, 0]
```

---

### 7. Извлечь только цифры из строки
```python
text = "a1b2c3"
digits = [char for char in text if char.isdigit()]
print(digits)
# Вывод: ['1', '2', '3']
```

---

### 8. Удалить пробелы из списка строк
```python
lines = ["  hello", "world  ", "  python  "]
stripped = [line.strip() for line in lines]
print(stripped)
# Вывод: ['hello', 'world', 'python']
```

---

### 9. Преобразовать список строк в числа
```python
str_numbers = ["1", "20", "300"]
numbers = [int(s) for s in str_numbers]
print(numbers)
# Вывод: [1, 20, 300]
```

---

### 10. Фильтрация списка: оставить только уникальные элементы
```python
items = [1, 2, 2, 3, 4, 4, 5]
unique = [x for i, x in enumerate(items) if x not in items[:i]]
print(unique)
# Вывод: [1, 2, 3, 4, 5]
```

---

### 11. Получить имена пользователей из списка словарей
```python
users = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 30},
    {"name": "Eve", "age": 22}
]
names = [user["name"] for user in users]
print(names)
# Вывод: ['Alice', 'Bob', 'Eve']
```

---

### 12. Преобразовать все элементы списка в строки
```python
values = [1, 2, 3, 4]
as_strings = [str(v) for v in values]
print(as_strings)
# Вывод: ['1', '2', '3', '4']
```

---

### 13. Получить только email-адреса из списка пользователей
```python
users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"}
]
emails = [user["email"] for user in users]
print(emails)
# Вывод: ['alice@example.com', 'bob@example.com']
```

---

### 14. Создать список квадратов только нечётных чисел
```python
odds_squared = [x**2 for x in range(10) if x % 2 != 0]
print(odds_squared)
# Вывод: [1, 9, 25, 49, 81]
```


---

### 15. Получить список файлов с определённым расширением в директории
```python
import os

files = os.listdir('.')  # список файлов в текущей папке
py_files = [f for f in files if f.endswith('.py')]
print(py_files)
# Вывод: ['main.py', 'utils.py', ...]
```

---

### 16. Извлечь значения определённого поля из JSON-ответа API
```python
response = [
    {"id": 1, "title": "First"},
    {"id": 2, "title": "Second"},
    {"id": 3, "title": "Third"}
]
titles = [item["title"] for item in response]
print(titles)
# Вывод: ['First', 'Second', 'Third']
```

---

### 17. Преобразовать список чисел в строки для вывода в шаблон
```python
numbers = [1, 2, 3, 4]
numbers_str = [str(n) for n in numbers]
print(", ".join(numbers_str))
# Вывод: '1, 2, 3, 4'
```

---

### 18. Фильтровать пользователей по возрасту (например, только совершеннолетние)
```python
users = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 21},
    {"name": "Eve", "age": 19}
]
adults = [user["name"] for user in users if user["age"] >= 18]
print(adults)
# Вывод: ['Bob', 'Eve']
```

---

### 19. Получить список ссылок из HTML-страницы (с помощью BeautifulSoup)
```python
from bs4 import BeautifulSoup

html = "<a href='link1'>1</a><a href='link2'>2</a>"
soup = BeautifulSoup(html, "html.parser")
links = [a['href'] for a in soup.find_all('a')]
print(links)
# Вывод: ['link1', 'link2']
```

---

### 20. Преобразовать список дат в объекты datetime
```python
from datetime import datetime

date_strings = ["2024-01-01", "2024-06-01"]
dates = [datetime.strptime(d, "%Y-%m-%d") for d in date_strings]
print(dates)
# Вывод: [datetime.datetime(2024, 1, 1, 0, 0), datetime.datetime(2024, 6, 1, 0, 0)]
```

---
