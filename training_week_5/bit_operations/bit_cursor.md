# Объяснение битовых операций для разработчиков

**Cursor**

### Битовые операции в Python

**Битовые операции** — это операции, которые выполняются над отдельными битами целых чисел. Они часто используются для оптимизации, работы с флагами, низкоуровневого программирования, взаимодействия с оборудованием, протоколами и т.д.

#### Основные битовые операции

| Операция         | Оператор | Описание                                 |
|------------------|----------|------------------------------------------|
| AND (И)          | `&`      | Побитовое И                              |
| OR (ИЛИ)         | `\|`     | Побитовое ИЛИ                            |
| XOR (исключающее ИЛИ) | `^`      | Побитовое исключающее ИЛИ                |
| NOT (НЕ)         | `~`      | Побитовое отрицание                      |
| Сдвиг влево      | `<<`     | Сдвигает биты влево                      |
| Сдвиг вправо     | `>>`     | Сдвигает биты вправо                     |

---

#### Примеры: от простого к сложному

##### 1. Простые примеры

```python
a = 5      # 0b0101
b = 3      # 0b0011

print(a & b)   # 1  (0b0001)
print(a | b)   # 7  (0b0111)
print(a ^ b)   # 6  (0b0110)
print(~a)      # -6 (инверсия всех битов: -(a+1))
print(a << 1)  # 10 (0b1010) — сдвиг влево на 1 бит
print(a >> 1)  # 2  (0b0010) — сдвиг вправо на 1 бит
```

##### 2. Использование битовых флагов

В реальных проектах часто используют битовые флаги для хранения множества булевых значений в одном числе.

```python
# Определим флаги
READ = 0b0001   # 1
WRITE = 0b0010  # 2
EXECUTE = 0b0100 # 4

# У пользователя есть права на чтение и выполнение
user_permissions = READ | EXECUTE  # 0b0101

# Проверка прав
can_read = bool(user_permissions & READ)      # True
can_write = bool(user_permissions & WRITE)    # False
can_execute = bool(user_permissions & EXECUTE) # True
```

##### 3. Маскирование и извлечение битов

```python
# Допустим, у нас есть байт, где каждый бит — это флаг
flags = 0b10110101

# Проверим, установлен ли 3-й бит (считаем с нуля)
is_third_bit_set = bool(flags & (1 << 3))  # True, т.к. 0b1000 & 0b10110101 = 0b1000

# Сбросим 2-й бит
flags = flags & ~(1 << 2)  # 0b10110001
```

##### 4. Пример из продакшн: оптимизация хранения состояний

В системах с большим количеством однотипных флагов (например, права доступа, состояния устройств) битовые операции позволяют экономить память и ускорять обработку.

```python
class DeviceStatus:
    ONLINE = 1 << 0
    ERROR = 1 << 1
    BUSY = 1 << 2
    MAINTENANCE = 1 << 3

    def __init__(self):
        self.status = 0

    def set_status(self, flag):
        self.status |= flag

    def clear_status(self, flag):
        self.status &= ~flag

    def is_status(self, flag):
        return bool(self.status & flag)

# Использование
device = DeviceStatus()
device.set_status(DeviceStatus.ONLINE)
device.set_status(DeviceStatus.BUSY)

if device.is_status(DeviceStatus.BUSY):
    print("Device is busy")
```

---

### Практические советы

- **Читаемость**: Используйте именованные константы для флагов, чтобы код был понятен.
- **Документация**: Описывайте, что означает каждый бит.
- **Тесты**: Покрывайте битовые операции тестами, чтобы избежать ошибок при изменении флагов.

---

### Когда использовать битовые операции

- Оптимизация по памяти (например, хранение множества флагов в одном числе).
- Работа с низкоуровневыми протоколами, оборудованием, сетевыми пакетами.
- Быстрая обработка множества булевых значений.

---

### Итог

Битовые операции — мощный инструмент, который часто используется в продакшн-коде для оптимизации и работы с флагами. Главное — использовать их осознанно и не жертвовать читаемостью ради микроскопической оптимизации без необходимости.

```python
a = 5      # 0b0101
b = 3      # 0b0011

print(a & b)   # 1  (0b0001)
print(a | b)   # 7  (0b0111)
print(a ^ b)   # 6  (0b0110)
print(~a)      # -6 (инверсия всех битов: -(a+1))
print(a << 1)  # 10 (0b1010) — сдвиг влево на 1 бит
print(a >> 1)  # 2  (0b0010) — сдвиг вправо на 1 бит
```

```python
# Определим флаги
READ = 0b0001   # 1
WRITE = 0b0010  # 2
EXECUTE = 0b0100 # 4

# У пользователя есть права на чтение и выполнение
user_permissions = READ | EXECUTE  # 0b0101

# Проверка прав
can_read = bool(user_permissions & READ)      # True
can_write = bool(user_permissions & WRITE)    # False
can_execute = bool(user_permissions & EXECUTE) # True
```

```python
# Допустим, у нас есть байт, где каждый бит — это флаг
flags = 0b10110101

# Проверим, установлен ли 3-й бит (считаем с нуля)
is_third_bit_set = bool(flags & (1 << 3))  # True, т.к. 0b1000 & 0b10110101 = 0b1000

# Сбросим 2-й бит
flags = flags & ~(1 << 2)  # 0b10110001
```

```python
class DeviceStatus:
    ONLINE = 1 << 0
    ERROR = 1 << 1
    BUSY = 1 << 2
    MAINTENANCE = 1 << 3

    def __init__(self):
        self.status = 0

    def set_status(self, flag):
        self.status |= flag

    def clear_status(self, flag):
        self.status &= ~flag

    def is_status(self, flag):
        return bool(self.status & flag)

# Использование
device = DeviceStatus()
device.set_status(DeviceStatus.ONLINE)
device.set_status(DeviceStatus.BUSY)

if device.is_status(DeviceStatus.BUSY):
    print("Device is busy")
```

