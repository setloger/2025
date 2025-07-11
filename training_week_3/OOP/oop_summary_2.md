
Продолжаю с того места, где остановился:

```python
# Функция, работающая с любым транспортным средством
def test_vehicle(vehicle: Vehicle):
    """Тестирование любого транспортного средства через полиморфизм"""
    print(f"🔧 Тестирование {vehicle.brand} {vehicle.model}")
    print(f"   Информация: {vehicle.get_info()}")
    print(f"   Тест запуска: {vehicle.start_engine()}")
    print(f"   Тест остановки: {vehicle.stop_engine()}")
    print(f"   Тип топлива: {vehicle.get_fuel_type()}")
    print()

# Полиморфное тестирование всех транспортных средств
print("=== Полиморфное тестирование ===")
for vehicle in vehicles:
    test_vehicle(vehicle)
```


### Этап 3: Абстракция и интерфейсы (1-2 дня)

#### День 8: Абстрактные классы и интерфейсы

**Подробная теоретическая база:**

**Абстракция** — это принцип ООП, который позволяет выделить существенные характеристики объекта, игнорируя несущественные детали. Абстракция помогает создать упрощенную модель сложной системы, скрывая детали реализации и предоставляя только необходимый интерфейс для взаимодействия.

**Абстрактный класс** — это класс, который не может быть инстанцирован напрямую и содержит один или более абстрактных методов. Абстрактные методы объявляются без реализации и должны быть переопределены в дочерних классах. В Python абстрактные классы создаются с помощью модуля `abc` (Abstract Base Classes).

**Интерфейс** — это контракт, который определяет набор методов, которые должен реализовать класс. В Python интерфейсы обычно реализуются через абстрактные классы, содержащие только абстрактные методы.

```python
from abc import ABC, abstractmethod
import math

# Абстрактный базовый класс для геометрических фигур
class Shape(ABC):
    """Абстрактный класс для всех геометрических фигур"""
    
    def __init__(self, name, color="white"):
        self.name = name
        self.color = color
        self.created_at = self._get_timestamp()
    
    def _get_timestamp(self):
        """Защищенный метод для получения времени создания"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @abstractmethod
    def area(self):
        """Абстрактный метод для вычисления площади"""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Абстрактный метод для вычисления периметра"""
        pass
    
    @abstractmethod
    def get_vertices_count(self):
        """Абстрактный метод для получения количества вершин"""
        pass
    
    # Конкретные методы (не абстрактные)
    def description(self):
        """Описание фигуры"""
        return (f"Фигура: {self.name}, цвет: {self.color}, "
                f"площадь: {self.area():.2f}, периметр: {self.perimeter():.2f}, "
                f"вершин: {self.get_vertices_count()}")
    
    def change_color(self, new_color):
        """Изменение цвета фигуры"""
        old_color = self.color
        self.color = new_color
        return f"{self.name}: цвет изменен с {old_color} на {new_color}"
    
    def get_info(self):
        """Получение полной информации о фигуре"""
        return (f"{self.name} ({self.color})\n"
                f"Создана: {self.created_at}\n"
                f"Площадь: {self.area():.2f}\n"
                f"Периметр: {self.perimeter():.2f}\n"
                f"Количество вершин: {self.get_vertices_count()}")
    
    @staticmethod
    def compare_areas(shape1, shape2):
        """Сравнение площадей двух фигур"""
        area1 = shape1.area()
        area2 = shape2.area()
        
        if area1 > area2:
            return f"{shape1.name} больше {shape2.name} на {area1 - area2:.2f}"
        elif area2 > area1:
            return f"{shape2.name} больше {shape1.name} на {area2 - area1:.2f}"
        else:
            return f"{shape1.name} и {shape2.name} имеют одинаковую площадь"

class Rectangle(Shape):
    """Конкретная реализация прямоугольника"""
    
    def __init__(self, width, height, color="white"):
        super().__init__("Прямоугольник", color)
        self.width = width
        self.height = height
        
        # Валидация размеров
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть положительными")
    
    def area(self):
        """Реализация вычисления площади прямоугольника"""
        return self.width * self.height
    
    def perimeter(self):
        """Реализация вычисления периметра прямоугольника"""
        return 2 * (self.width + self.height)
    
    def get_vertices_count(self):
        """Количество вершин прямоугольника"""
        return 4
    
    def is_square(self):
        """Проверка, является ли прямоугольник квадратом"""
        return self.width == self.height
    
    def get_diagonal(self):
        """Вычисление диагонали прямоугольника"""
        return math.sqrt(self.width**2 + self.height**2)
    
    def resize(self, width_factor, height_factor):
        """Изменение размеров прямоугольника"""
        old_area = self.area()
        self.width *= width_factor
        self.height *= height_factor
        new_area = self.area()
        return f"Размер изменен. Площадь: {old_area:.2f} → {new_area:.2f}"

class Circle(Shape):
    """Конкретная реализация круга"""
    
    def __init__(self, radius, color="white"):
        super().__init__("Круг", color)
        self.radius = radius
        
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным")
    
    def area(self):
        """Реализация вычисления площади круга"""
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """Реализация вычисления длины окружности"""
        return 2 * math.pi * self.radius
    
    def get_vertices_count(self):
        """У круга нет вершин"""
        return 0
    
    def get_diameter(self):
        """Вычисление диаметра"""
        return 2 * self.radius
    
    def get_circumference(self):
        """Альтернативное название для периметра"""
        return self.perimeter()
    
    def resize(self, factor):
        """Изменение размера круга"""
        old_area = self.area()
        self.radius *= factor
        new_area = self.area()
        return f"Радиус изменен в {factor} раз. Площадь: {old_area:.2f} → {new_area:.2f}"

class Triangle(Shape):
    """Конкретная реализация треугольника"""
    
    def __init__(self, side_a, side_b, side_c, color="white"):
        super().__init__("Треугольник", color)
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        
        # Валидация треугольника
        if not self._is_valid_triangle():
            raise ValueError("Невозможно создать треугольник с такими сторонами")
    
    def _is_valid_triangle(self):
        """Проверка правила треугольника"""
        return (self.side_a + self.side_b > self.side_c and
                self.side_a + self.side_c > self.side_b and
                self.side_b + self.side_c > self.side_a)
    
    def area(self):
        """Вычисление площади по формуле Герона"""
        s = self.perimeter() / 2  # полупериметр
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        """Вычисление периметра треугольника"""
        return self.side_a + self.side_b + self.side_c
    
    def get_vertices_count(self):
        """Количество вершин треугольника"""
        return 3
    
    def get_triangle_type(self):
        """Определение типа треугольника"""
        sides = sorted([self.side_a, self.side_b, self.side_c])
        
        if sides[0] == sides[1] == sides[2]:
            return "Равносторонний"
        elif sides[0] == sides[1] or sides[1] == sides[2]:
            return "Равнобедренный"
        else:
            return "Разносторонний"
    
    def is_right_triangle(self):
        """Проверка, является ли треугольник прямоугольным"""
        sides = sorted([self.side_a, self.side_b, self.side_c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-10

# Использование абстрактных классов
print("=== Создание геометрических фигур ===")
rectangle = Rectangle(5, 3, "красный")
circle = Circle(4, "синий")
triangle = Triangle(3, 4, 5, "зеленый")

# shape = Shape("фигура")  # TypeError! Нельзя создать экземпляр абстрактного класса

shapes = [rectangle, circle, triangle]

print("=== Информация о фигурах ===")
for shape in shapes:
    print(shape.get_info())
    print()

print("=== Сравнение площадей ===")
print(Shape.compare_areas(rectangle, circle))
print(Shape.compare_areas(circle, triangle))
print(Shape.compare_areas(rectangle, triangle))

# Интерфейсы через абстрактные классы
class Drawable(ABC):
    """Интерфейс для объектов, которые можно рисовать"""
    
    @abstractmethod
    def draw(self):
        """Метод для рисования объекта"""
        pass
    
    @abstractmethod
    def move(self, x, y):
        """Метод для перемещения объекта"""
        pass
    
    @abstractmethod
    def get_position(self):
        """Получение текущей позиции"""
        pass

class Resizable(ABC):
    """Интерфейс для объектов, размер которых можно изменять"""
    
    @abstractmethod
    def resize(self, factor):
        """Изменение размера объекта"""
        pass
    
    @abstractmethod
    def get_size(self):
        """Получение текущего размера"""
        pass

class Colorable(ABC):
    """Интерфейс для объектов, цвет которых можно изменять"""
    
    @abstractmethod
    def set_color(self, color):
        """Установка цвета"""
        pass
    
    @abstractmethod
    def get_color(self):
        """Получение текущего цвета"""
        pass

# Класс, реализующий несколько интерфейсов
class GraphicShape(Drawable, Resizable, Colorable):
    """Графическая фигура, реализующая несколько интерфейсов"""
    
    def __init__(self, shape: Shape, x=0, y=0):
        self.shape = shape
        self.x = x
        self.y = y
        self.scale_factor = 1.0
    
    def draw(self):
        """Реализация рисования"""
        return (f"Рисую {self.shape.name} в позиции ({self.x}, {self.y}), "
                f"цвет: {self.shape.color}, масштаб: {self.scale_factor}")
    
    def move(self, x, y):
        """Реализация перемещения"""
        old_pos = (self.x, self.y)
        self.x = x
        self.y = y
        return f"{self.shape.name} перемещен с {old_pos} в ({self.x}, {self.y})"
    
    def get_position(self):
        """Получение позиции"""
        return (self.x, self.y)
    
    def resize(self, factor):
        """Реализация изменения размера"""
        old_scale = self.scale_factor
        self.scale_factor *= factor
        return f"{self.shape.name} изменен с масштаба {old_scale} на {self.scale_factor}"
    
    def get_size(self):
        """Получение размера"""
        return f"Площадь: {self.shape.area() * self.scale_factor**2:.2f}"
    
    def set_color(self, color):
        """Установка цвета"""
        return self.shape.change_color(color)
    
    def get_color(self):
        """Получение цвета"""
        return self.shape.color
    
    def get_full_info(self):
        """Полная информация о графической фигуре"""
        return (f"{self.shape.name} в позиции ({self.x}, {self.y})\n"
                f"Цвет: {self.shape.color}\n"
                f"Масштаб: {self.scale_factor}\n"
                f"Площадь (с учетом масштаба): {self.shape.area() * self.scale_factor**2:.2f}")

# Демонстрация интерфейсов
print("\n=== Демонстрация интерфейсов ===")
graphic_shapes = [
    GraphicShape(rectangle, 10, 20),
    GraphicShape(circle, 50, 60),
    GraphicShape(triangle, 100, 150)
]

for graphic_shape in graphic_shapes:
    print(f"🎨 {graphic_shape.draw()}")
    print(f"   {graphic_shape.move(graphic_shape.x + 10, graphic_shape.y + 10)}")
    print(f"   {graphic_shape.resize(1.5)}")
    print(f"   {graphic_shape.set_color('фиолетовый')}")
    print(f"   Размер: {graphic_shape.get_size()}")
    print()

# Полиморфное использование интерфейсов
def process_drawable_objects(drawables):
    """Функция для работы с любыми рисуемыми объектами"""
    for drawable in drawables:
        print(f"Обработка объекта: {drawable.draw()}")

def process_resizable_objects(resizables):
    """Функция для работы с объектами, размер которых можно изменять"""
    for resizable in resizables:
        print(f"Изменение размера: {resizable.resize(0.8)}")

print("=== Полиморфное использование интерфейсов ===")
process_drawable_objects(graphic_shapes)
print()
process_resizable_objects(graphic_shapes)
```


### Этап 4: Магические методы (1-2 дня)

#### День 9: Магические методы (Dunder methods)

**Подробная теоретическая база:**

**Магические методы** (также называемые "dunder methods" от "double underscore") — это специальные методы в Python, которые начинаются и заканчиваются двумя подчеркиваниями (`__method__`). Эти методы позволяют определить, как объекты вашего класса будут вести себя при использовании встроенных функций Python и операторов. Магические методы являются основой протокола Python и позволяют создавать объекты, которые ведут себя как встроенные типы данных.

**Основные категории магических методов:**

1. **Создание и уничтожение объектов**: `__init__`, `__new__`, `__del__`
2. **Строковое представление**: `__str__`, `__repr__`, `__format__`
3. **Арифметические операции**: `__add__`, `__sub__`, `__mul__`, `__div__`, etc.
4. **Операции сравнения**: `__eq__`, `__lt__`, `__gt__`, `__le__`, `__ge__`, `__ne__`
5. **Доступ к атрибутам**: `__getattr__`, `__setattr__`, `__delattr__`
6. **Контейнерные операции**: `__len__`, `__getitem__`, `__setitem__`, `__delitem__`
7. **Итерация**: `__iter__`, `__next__`
8. **Контекстные менеджеры**: `__enter__`, `__exit__`
9. **Вызов объекта**: `__call__`
10. **Хеширование**: `__hash__`
```python
import math
from functools import total_ordering

@total_ordering  # Автоматически генерирует все операции сравнения на основе __eq__ и __lt__
class Vector:
    """Класс для работы с двумерными векторами с полным набором магических методов"""
    
    def __init__(self, x=0, y=0):
        """Конструктор вектора"""
        self.x = float(x)
        self.y = float(y)
    
    # === Строковое представление ===
    def __str__(self):
        """Человекочитаемое представление (для print и str())"""
        return f"Вектор({self.x}, {self.y})"
    
    def __repr__(self):
        """Техническое представление (для отладки и eval())"""
        return f"Vector(x={self.x}, y={self.y})"
    
    def __format__(self, format_spec):
        """Форматированное представление"""
        if format_spec == 'polar':
            magnitude = self.magnitude()
            angle = self.angle()
            return f"({magnitude:.2f}, {angle:.2f}°)"
        elif format_spec == 'unit':
            unit = self.normalize()
            return f"({unit.x:.3f}, {unit.y:.3f})"
        else:
            return f"({self.x:{format_spec}}, {self.y:{format_spec}})"
    
    # === Арифметические операции ===
    def __add__(self, other):
        """Сложение векторов: v1 + v2"""
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        return NotImplemented
    
    def __radd__(self, other):
        """Обратное сложение: 5 + vector"""
        return self.__add__(other)
    
    def __iadd__(self, other):
        """Сложение с присваиванием: v1 += v2"""
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            return self
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
            return self
        return NotImplemented
    
    def __sub__(self, other):
        """Вычитание векторов: v1 - v2"""
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        return NotImplemented
    
    def __rsub__(self, other):
        """Обратное вычитание: 5 - vector"""
        if isinstance(other, (int, float)):
            return Vector(other - self.x, other - self.y)
        return NotImplemented
    
    def __mul__(self, scalar):
        """Умножение на скаляр: v * 3"""
        if isinstance(scalar, (int, float)):
            return Vector(self.x * scalar, self.y * scalar)
        elif isinstance(scalar, Vector):
            # Скалярное произведение
            return self.x * scalar.x + self.y * scalar.y
        return NotImplemented
    
    def __rmul__(self, scalar):
        """Обратное умножение: 3 * v"""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """Деление на скаляр: v / 2"""
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Деление вектора на ноль")
            return Vector(self.x / scalar, self.y / scalar)
        return NotImplemented
    
    def __floordiv__(self, scalar):
        """Целочисленное деление: v // 2"""
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Деление вектора на ноль")
            return Vector(self.x // scalar, self.y // scalar)
        return NotImplemented
    
    def __mod__(self, scalar):
        """Остаток от деления: v % 2"""
        if isinstance(scalar, (int, float)):
            if scalar == 0:
                raise ZeroDivisionError("Деление вектора на ноль")
            return Vector(self.x % scalar, self.y % scalar)
        return NotImplemented
    
    def __pow__(self, power):
        """Возведение в степень: v ** 2"""
        if isinstance(power, (int, float)):
            return Vector(self.x ** power, self.y ** power)
        return NotImplemented
    
    def __neg__(self):
        """Унарный минус: -v"""
        return Vector(-self.x, -self.y)
    
    def __pos__(self):
        """Унарный плюс: +v"""
        return Vector(self.x, self.y)
    
    def __abs__(self):
        """Абсолютное значение: abs(v) - возвращает длину вектора"""
        return self.magnitude()
    
    # === Операции сравнения ===
    def __eq__(self, other):
        """Равенство: v1 == v2"""
        if isinstance(other, Vector):
            return abs(self.x - other.x) < 1e-10 and abs(self.y - other.y) < 1e-10
        return False
    
    def __lt__(self, other):
        """Меньше: v1 < v2 (по длине)"""
        if isinstance(other, Vector):
            return self.magnitude() < other.magnitude()
        return NotImplemented
    
    def __hash__(self):
        """Хеш объекта (для использования в множествах и словарях)"""
        return hash((round(self.x, 10), round(self.y, 10)))
    
    # === Контейнерные операции ===
    def __len__(self):
        """Длина вектора (целое число): len(v)"""
        return int(self.magnitude())
    
    def __getitem__(self, index):
        """Доступ по индексу: v[0], v[1]"""
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        else:
            raise IndexError("Индекс должен быть 0 или 1")
    
    def __setitem__(self, index, value):
        """Установка по индексу: v[0] = 5"""
        if index == 0:
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        else:
            raise IndexError("Индекс должен быть 0 или 1")
    
    def __iter__(self):
        """Итерация по компонентам вектора"""
        yield self.x
        yield self.y
    
    def __contains__(self, value):
        """Проверка принадлежности: 5 in vector"""
        return value in (self.x, self.y)
    
    # === Логические операции ===
    def __bool__(self):
        """Логическое значение: bool(v)"""
        return self.x != 0 or self.y != 0
    
    # === Вызов объекта ===
    def __call__(self, scalar=1):
        """Вызов объекта как функции: v(2) - нормализация с масштабированием"""
        normalized = self.normalize()
        return normalized * scalar
    
    # === Копирование ===
    def __copy__(self):
        """Поверхностное копирование"""
        return Vector(self.x, self.y)
    
    def __deepcopy__(self, memo):
        """Глубокое копирование"""
        return Vector(self.x, self.y)
    
    # === Вспомогательные методы ===
    def magnitude(self):
        """Длина (модуль) вектора"""
        return math.sqrt(self.x**2 + self.y**2)
    
    def angle(self):
        """Угол вектора в градусах"""
        return math.degrees(math.atan2(self.y, self.x))
    
    def normalize(self):
        """Нормализация вектора (единичный вектор)"""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0)
        return Vector(self.x / mag, self.y / mag)
    
    def dot_product(self, other):
        """Скалярное произведение"""
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        raise TypeError("Скалярное произведение возможно только с другим вектором")
    
    def cross_product(self, other):
        """Векторное произведение (в 2D возвращает скаляр)"""
        if isinstance(other, Vector):
            return self.x * other.y - self.y * other.x
        raise TypeError("Векторное произведение возможно только с другим вектором")
    
    def distance_to(self, other):
        """Расстояние до другого вектора"""
        if isinstance(other, Vector):
            return (self - other).magnitude()
        raise TypeError("Расстояние можно вычислить только до другого вектора")
    
    def rotate(self, angle_degrees):
        """Поворот вектора на заданный угол"""
        angle_rad = math.radians(angle_degrees)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)
        
        new_x = self.x * cos_a - self.y * sin_a
        new_y = self.x * sin_a + self.y * cos_a
        
        return Vector(new_x, new_y)

# Демонстрация использования магических методов
print("=== Создание векторов ===")
v1 = Vector(3, 4)
v2 = Vector(1, 2)
v3 = Vector(3, 4)  # Равен v1

print(f"v1 = {v1}")  # Использует __str__
print(f"v2 = {repr(v2)}")  # Использует __repr__
print(f"v1 в полярных координатах: {v1:polar}")  # Использует __format__
print(f"v2 как единичный вектор: {v2:unit}")

print("\n=== Арифметические операции ===")
print(f"v1 + v2 = {v1 + v2}")  # __add__
print(f"v1 - v2 = {v1 - v2}")  # __sub__
print(f"v1 * 2 = {v1 * 2}")    # __mul__
print(f"3 * v1 = {3 * v1}")    # __rmul__
print(f"v1 / 2 = {v1 / 2}")    # __truediv__
print(f"-v1 = {-v1}")          # __neg__
print(f"abs(v1) = {abs(v1)}")  # __abs__

print("\n=== Операции сравнения ===")
print(f"v1 == v3: {v1 == v3}")  # __eq__
print(f"v1 == v2: {v1 == v2}")
print(f"v1 > v2: {v1 > v2}")    # __gt__ (через @total_ordering)
print(f"v1 < v2: {v1 < v2}")    # __lt__

print("\n=== Контейнерные операции ===")
print(f"len(v1) = {len(v1)}")   # __len__
print(f"v1[0] = {v1[0]}")       # __getitem__
print(f"v1[1] = {v1[1]}")
print(f"3 in v1: {3 in v1}")    # __contains__
print(f"5 in v1: {5 in v1}")

print("\n=== Итерация ===")
print("Компоненты v1:")
for component in v1:  # __iter__
    print(f"  {component}")

print("\n=== Логические операции ===")
print(f"bool(v1): {bool(v1)}")  # __bool__
print(f"bool(Vector(0, 0)): {bool(Vector(0, 0))}")

print("\n=== Вызов как функции ===")
print(f"v1(2) = {v1(2)}")  # __call__ - нормализация с масштабированием

print("\n=== Использование в коллекциях ===")
vectors = {v1, v2, v3}  # Множество (работает благодаря __hash__ и __eq__)
print(f"Уникальных векторов: {len(vectors)}")  # 2, так как v1 и v3 равны

vector_dict = {v1: "первый", v2: "второй"}
print(f"Словарь с векторами как ключами: {vector_dict}")

# Контекстные менеджеры
class VectorCalculator:
    """Контекстный менеджер для вычислений с векторами"""
    
    def __init__(self, name):
        self.name = name
        self.operations = []
    
    def __enter__(self):
        """Вход в контекст"""
        print(f"🧮 Начинаю вычисления '{self.name}'")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Выход из контекста"""
        if exc_type:
            print(f"❌ Ошибка в вычислениях '{self.name}': {exc_value}")
        else:
            print(f"✅ Вычисления '{self.name}' завершены успешно")
            print(f"Выполнено операций: {len(self.operations)}")
        
        # Возвращаем False, чтобы исключение не подавлялось
        return False
    
    def add_vectors(self, v1, v2):
        """Сложение векторов с записью в историю"""
        result = v1 + v2
        self.operations.append(f"{v1} + {v2} = {result}")
        return result
    
    def multiply_vector(self, vector, scalar):
        """Умножение вектора на скаляр"""
        result = vector * scalar
        self.operations.append(f"{vector} * {scalar} = {result}")
        return result

# Использование контекстного менеджера
print("\n=== Контекстный менеджер ===")
with VectorCalculator("Базовые операции") as calc:
    result1 = calc.add_vectors(v1, v2)
    result2 = calc.multiply_vector(result1, 2)
    print(f"Результат: {result2}")

# Пример с ошибкой
print("\n=== Контекстный менеджер с ошибкой ===")
try:
    with VectorCalculator("Операции с ошибкой") as calc:
        result = calc.add_vectors(v1, v2)
        # Намеренная ошибка
        bad_result = result / 0
except ZeroDivisionError:
    print("Ошибка обработана вне контекстного менеджера")
```

**Продвинутые магические методы:**

```python
class Matrix:
    """Класс матрицы с расширенным набором магических методов"""
    
    def __init__(self, data):
        """Инициализация матрицы из списка списков"""
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Данные должны быть списком списков")
        
        self.rows = len(data)
        self.cols = len(data[0])
        
        # Проверяем, что все строки одинаковой длины
        if not all(len(row) == self.cols for row in data):
            raise ValueError("Все строки должны быть одинаковой длины")
        
        self.data = [row[:] for row in data]  # Создаем копию
    
    def __str__(self):
        """Красивое отображение матрицы"""
        max_width = max(len(str(item)) for row in self.data for item in row)
        lines = []
        for row in self.data:
            formatted_row = [str(item).rjust(max_width) for item in row]
            lines.append("│ " + " ".join(formatted_row) + " │")
        
        return "\n".join(lines)
    
    def __repr__(self):
        """Техническое представление"""
        return f"Matrix({self.data})"
    
    def __getitem__(self, key):
        """Доступ к элементам: matrix[i][j] или matrix[i, j]"""
        if isinstance(key, tuple):
            row, col = key
            return self.data[row][col]
        else:
            return self.data[key]
    
    def __setitem__(self, key, value):
        """Установка элементов: matrix[i][j] = value или matrix[i, j] = value"""
        if isinstance(key, tuple):
            row, col = key
            self.data[row][col] = value
        else:
            if isinstance(value, list):
                self.data[key] = value[:]
            else:
                raise ValueError("Значение должно быть списком")
    
    def __add__(self, other):
        """Сложение матриц"""
        if not isinstance(other, Matrix):
            return NotImplemented
        
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера")
        
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)
        
        return Matrix(result)
    
    def __mul__(self, other):
        """Умножение матрицы на число или на другую матрицу"""
        if isinstance(other, (int, float)):
            # Умножение на скаляр
            result = []
            for row in self.data:
                result.append([item * other for item in row])
            return Matrix(result)
        
        elif isinstance(other, Matrix):
            # Умножение матриц
            if self.cols != other.rows:
                raise ValueError("Количество столбцов первой матрицы должно равняться количеству строк второй")
            
            result = []
            for i in range(self.rows):
                row = []
                for j in range(other.cols):
                    sum_product = 0
                    for k in range(self.cols):
                        sum_product += self.data[i][k] * other.data[k][j]
                    row.append(sum_product)
                result.append(row)
            
            return Matrix(result)
        
        return NotImplemented
    
    def __len__(self):
        """Количество элементов в матрице"""
        return self.rows * self.cols
    
    def __iter__(self):
        """Итерация по всем элементам матрицы"""
        for row in self.data:
            for item in row:
                yield item
    
    def __contains__(self, value):
        """Проверка наличия элемента в матрице"""
        return any(value in row for row in self.data)
    
    def __eq__(self, other):
        """Сравнение матриц на равенство"""
        if not isinstance(other, Matrix):
            return False
        
        return (self.rows == other.rows and 
                self.cols == other.cols and 
                self.data == other.data)
    
    def transpose(self):
        """Транспонирование матрицы"""
        result = []
        for j in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append(self.data[i][j])
            result.append(row)
        return Matrix(result)
    
    def get_shape(self):
        """Получение размеров матрицы"""
        return (self.rows, self.cols)

# Демонстрация работы с матрицами
print("\n=== Работа с матрицами ===")
m1 = Matrix([[1, 2, 3], [4, 5, 6]])
m2 = Matrix([[7, 8, 9], [10, 11, 12]])

print("Матрица m1:")
print(m1)
print(f"\nПредставление: {repr(m1)}")

print(f"\nЭлемент m1[0, 1] = {m1[0, 1]}")
print(f"Размер матрицы: {m1.get_shape()}")
print(f"Количество элементов: {len(m1)}")
print(f"Содержит 5: {5 in m1}")

print("\nСложение матриц:")
m3 = m1 + m2
print(m3)

print("\nУмножение на скаляр:")
m4 = m1 * 3
print(m4)

print("\nТранспонирование:")
m5 = m1.transpose()
print(m5)

print("\nИтерация по элементам:")
print("Элементы m1:", list(m1))
```


### Этап 5: Свойства и декораторы (1 день)

#### День 10: @property и декораторы

**Подробная теоретическая база:**

**Свойства (Properties)** — это механизм Python, который позволяет использовать методы как атрибуты, обеспечивая контролируемый доступ к данным объекта. Свойства реализуют принцип инкапсуляции, позволяя валидировать данные при установке, вычислять значения на лету и контролировать доступ к атрибутам. Свойства создаются с помощью декоратора `@property` и связанных с ним `@setter` и `@deleter`.

**Преимущества использования свойств:**

1. **Валидация данных** — можно проверять корректность значений
2. **Вычисляемые атрибуты** — значения могут вычисляться динамически
3. **Совместимость** — можно превратить обычный атрибут в свойство без изменения интерфейса
4. **Логирование** — можно отслеживать доступ к атрибутам
5. **Ленивые вычисления** — значения вычисляются только при необходимости
```python
import math
import time
from datetime import datetime
from functools import wraps

class Temperature:
    """Класс для работы с температурой с автоматическим преобразованием единиц"""
    
    def __init__(self, celsius=0):
        self._celsius = celsius
        self._last_updated = datetime.now()
        self._access_count = 0
    
    @property
    def celsius(self):
        """Геттер для температуры в Цельсиях"""
        self._access_count += 1
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Сеттер для температуры в Цельсиях с валидацией"""
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля (-273.15°C)")
        
        if value > 1000:
            raise ValueError("Слишком высокая температура (максимум 1000°C)")
        
        self._celsius = float(value)
        self._last_updated = datetime.now()
    
    @celsius.deleter
    def celsius(self):
        """Делетер для температуры"""
        print("Сброс температуры до 0°C")
        self._celsius = 0
        self._last_updated = datetime.now()
    
    @property
    def fahrenheit(self):
        """Температура в Фаренгейтах (вычисляется динамически)"""
        self._access_count += 1
        return self._celsius * 9/5 + 32
    
    @fahrenheit.setter
    def fahrenheit(self, value):
        """Установка температуры через Фаренгейты"""
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        
        celsius_value = (value - 32) * 5/9
        self.celsius = celsius_value  # Используем сеттер celsius для валидации
    
    @property
    def kelvin(self):
        """Температура в Кельвинах (только чтение)"""
        self._access_count += 1
        return self._celsius + 273.15
    
    @kelvin.setter
    def kelvin(self, value):
        """Установка температуры через Кельвины"""
        if not isinstance(value, (int, float)):
            raise TypeError("Температура должна быть числом")
        
        celsius_value = value - 273.15
        self.celsius = celsius_value
    
    @property
    def last_updated(self):
        """Время последнего обновления (только чтение)"""
        return self._last_updated.strftime("%Y-%m-%d %H:%M:%S")
    
    @property
    def access_count(self):
        """Количество обращений к температуре (только чтение)"""
        return self._access_count
    
    @property
    def state_of_matter(self):
        """Агрегатное состояние воды при данной температуре"""
        if self._celsius < 0:
            return "лед"
        elif self._celsius < 100:
            return "вода"
        else:
            return "пар"
    
    @property
    def is_freezing(self):
        """Проверка, замерзает ли вода"""
        return self._celsius <= 0
    
    @property
    def is_boiling(self):
        """Проверка, кипит ли вода"""
        return self._celsius >= 100
    
    def get_info(self):
        """Полная информация о температуре"""
        return (f"Температура: {self._celsius}°C / {self.fahrenheit:.1f}°F / {self.kelvin:.1f}K\n"
                f"Состояние воды: {self.state_of_matter}\n"
                f"Последнее обновление: {self.last_updated}\n"
                f"Количество обращений: {self.access_count}")

# Демонстрация работы со свойствами
print("=== Работа со свойствами ===")
temp = Temperature(25)
print(f"Начальная температура: {temp.celsius}°C")
print(f"В Фаренгейтах: {temp.fahrenheit}°F")
print(f"В Кельвинах: {temp.kelvin}K")
print(f"Состояние воды: {temp.state_of_matter}")

# Изменение через разные единицы
temp.fahrenheit = 100
print(f"\nПосле установки 100°F: {temp.celsius}°C")

temp.kelvin = 300
print(f"После установки 300K: {temp.celsius}°C")

# Валидация
try:
    temp.celsius = -300  # Ошибка!
except ValueError as e:
    print(f"Ошибка валидации: {e}")

print(f"\nИнформация о температуре:")
print(temp.get_info())

# Удаление свойства
del temp.celsius
print(f"После удаления: {temp.celsius}°C")
```

**Продвинутые декораторы для классов:**

```python
import functools
import time
from collections import defaultdict

def timer(func):
    """Декоратор для измерения времени выполнения метода"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} выполнен за {end - start:.4f} секунд")
        return result
    return wrapper

def validate_positive(func):
    """Декоратор для валидации положительных чисел"""
    @functools.wraps(func)
    def wrapper(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Значение должно быть числом")
        if value <= 0:
            raise ValueError("Значение должно быть положительным")
        return func(self, value)
    return wrapper

def cache_result(func):
    """Декоратор для кеширования результатов методов"""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Создаем ключ кеша
        cache_key = (func.__name__, args, tuple(sorted(kwargs.items())))
        
        # Проверяем, есть ли кеш у объекта
        if not hasattr(self, '_cache'):
            self._cache = {}
        
        # Возвращаем кешированный результат или вычисляем новый
        if cache_key in self._cache:
            print(f"📋 Возвращен кешированный результат для {func.__name__}")
            return self._cache[cache_key]
        
        result = func(self, *args, **kwargs)
        self._cache[cache_key] = result
        print(f"💾 Результат {func.__name__} сохранен в кеш")
        return result
    return wrapper

def log_access(func):
    """Декоратор для логирования доступа к методам"""
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        # Создаем лог, если его нет
        if not hasattr(self, '_access_log'):
            self._access_log = []
        
        timestamp = datetime.now().strftime("%H:%M:%S")
        self._access_log.append(f"{timestamp}: {func.__name__} вызван")
        
        return func(self, *args, **kwargs)
    return wrapper

def retry(max_attempts=3, delay=1):
    """Декоратор для повторных попыток выполнения метода"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"🔄 Попытка {attempt + 1} неудачна: {e}. Повтор через {delay} сек...")
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

class Circle:
    """Класс круга с использованием различных декораторов"""
    
    def __init__(self, radius):
        self._radius = radius
        self._color = "white"
        self._position = (0, 0)
    
    @property
    def radius(self):
        """Радиус круга"""
        return self._radius
    
    @radius.setter
    @validate_positive
    @log_access
    def radius(self, value):
        """Установка радиуса с валидацией и логированием"""
        old_radius = self._radius
        self._radius = value
        print(f"🔄 Радиус изменен с {old_radius} на {value}")
    
    @property
    def color(self):
        """Цвет круга"""
        return self._color
    
    @color.setter
    @log_access
    def color(self, value):
        """Установка цвета с логированием"""
        if not isinstance(value, str):
            raise TypeError("Цвет должен быть строкой")
        old_color = self._color
        self._color = value
        print(f"🎨 Цвет изменен с {old_color} на {value}")
    
    @property
    @timer
    @cache_result
    def area(self):
        """Площадь круга (с кешированием и замером времени)"""
        # Имитация сложных вычислений
        time.sleep(0.1)
        return math.pi * self._radius ** 2
    
    @property
    @timer
    @cache_result
    def circumference(self):
        """Длина окружности (с кешированием и замером времени)"""
        time.sleep(0.05)
        return 2 * math.pi * self._radius
    
    @property
    @cache_result
    def diameter(self):
        """Диаметр круга"""
        return 2 * self._radius
    
    @log_access
    def move(self, x, y):
        """Перемещение круга"""
        old_position = self._position
        self._position = (x, y)
        return f"Круг перемещен с {old_position} в {self._position}"
    
    @retry(max_attempts=3, delay=0.5)
    def unstable_operation(self):
        """Нестабильная операция для демонстрации retry"""
        import random
        if random.random() < 0.7:  # 70% вероятность ошибки
            raise Exception("Случайная ошибка")
        return "Операция выполнена успешно!"
    
    def clear_cache(self):
        """Очистка кеша"""
        if hasattr(self, '_cache'):
            cache_size = len(self._cache)
            self._cache.clear()
            print(f"🗑️ Кеш очищен ({cache_size} элементов)")
    
    def get_access_log(self):
        """Получение лога доступа"""
        if hasattr(self, '_access_log'):
            return "\n".join(self._access_log)
        return "Лог доступа пуст"
    
    def get_info(self):
        """Полная информация о круге"""
        return (f"Круг: радиус={self._radius}, цвет={self._color}, позиция={self._position}\n"
                f"Площадь: {self.area:.2f}, Длина окружности: {self.circumference:.2f}")

# Демонстрация работы декораторов
print("\n=== Демонстрация декораторов ===")
circle = Circle(5)

print("Первый доступ к площади:")
print(f"Площадь: {circle.area:.2f}")

print("\nВторой доступ к площади (из кеша):")
print(f"Площадь: {circle.area:.2f}")

print("\nИзменение радиуса:")
circle.radius = 10

print("\nДоступ к площади после изменения:")
print(f"Площадь: {circle.area:.2f}")

print("\nИзменение цвета:")
circle.color = "красный"

print("\nПеремещение:")
print(circle.move(10, 20))

print("\nТестирование retry декоратора:")
try:
    result = circle.unstable_operation()
    print(f"✅ {result}")
except Exception as e:
    print(f"❌ Все попытки неудачны: {e}")

print("\nЛог доступа:")
print(circle.get_access_log())

print("\nОчистка кеша:")
circle.clear_cache()

# Валидация
try:
    circle.radius = -5  # Ошибка!
except ValueError as e:
    print(f"Ошибка валидации: {e}")
```

**Дескрипторы - продвинутый механизм свойств:**

```python
class ValidatedAttribute:
    """Дескриптор для валидации атрибутов"""
    
    def __init__(self, name, validator=None, default=None):
        self.name = name
        self.validator = validator
        self.default = default
        self.private_name = f'_{name}'
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.private_name, self.default)
    
    def __set__(self, obj, value):
        if self.validator:
            self.validator(value)
        setattr(obj, self.private_name, value)
    
    def __delete__(self, obj):
        delattr(obj, self.private_name)

def positive_number(value):
    """Валидатор для положительных чисел"""
    if not isinstance(value, (int, float)):
        raise TypeError("Значение должно быть числом")
    if value <= 0:
        raise ValueError("Значение должно быть положительным")

def non_empty_string(value):
    """Валидатор для непустых строк"""
    if not isinstance(value, str):
        raise TypeError("Значение должно быть строкой")
    if not value.strip():
        raise ValueError("Строка не должна быть пустой")

class Product:
    """Класс товара с использованием дескрипторов"""
    
    name = ValidatedAttribute('name', non_empty_string, 'Без названия')
    price = ValidatedAttribute('price', positive_number, 0)
    quantity = ValidatedAttribute('quantity', positive_number, 0)
    
    def __init__(self, name, price, quantity=1):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.created_at = datetime.now()
    
    @property
    def total_cost(self):
        """Общая стоимость товара"""
        return self.price * self.quantity
    
    def __str__(self):
        return f"{self.name}: {self.price}₽ × {self.quantity} = {self.total_cost}₽"

# Демонстрация дескрипторов
print("\n=== Демонстрация дескрипторов ===")
product = Product("Ноутбук", 50000, 2)
print(product)

# Валидация через дескрипторы
try:
    product.price = -1000  # Ошибка!
except ValueError as e:
    print(f"Ошибка валидации цены: {e}")

try:
    product.name = ""  # Ошибка!
except ValueError as e:
    print(f"Ошибка валидации названия: {e}")

print(f"Итоговая стоимость: {product.total_cost}₽")
```


## 🎯 Полный список вопросов для собеседования с ответами

### Базовые вопросы (Junior → Middle)

**1. Что такое класс и объект? Приведите пример.**

**Ответ по структуре:**

- **Определение:** Класс — это шаблон или чертеж для создания объектов, который определяет атрибуты (данные) и методы (поведение). Объект — это конкретный экземпляр класса, созданный в памяти.
- **Принцип работы:** Класс описывает общую структуру, а объекты имеют конкретные значения атрибутов, но разделяют общие методы.
- **Практический пример:**

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand  # атрибут экземпляра
        self.model = model
    
    def start(self):  # метод
        return f"{self.brand} {self.model} заведена"

# Создание объектов
car1 = Car("Toyota", "Camry")  # объект 1
car2 = Car("BMW", "X5")        # объект 2
```

- **Преимущества:** Переиспользование кода, организация данных, моделирование реальных объектов.
- **Альтернативы:** Функциональное программирование, процедурный подход.

**2. В чем разница между атрибутами класса и атрибутами экземпляра?**

**Ответ:**

- **Определение:** Атрибуты класса принадлежат самому классу и разделяются всеми экземплярами. Атрибуты экземпляра уникальны для каждого объекта.
- **Принцип работы:** Атрибуты класса хранятся в памяти один раз, атрибуты экземпляра — для каждого объекта отдельно.
- **Практический пример:**

```python
class Student:
    school = "Школа №1"  # атрибут класса
    
    def __init__(self, name):
        self.name = name  # атрибут экземпляра

s1 = Student("Иван")
s2 = Student("Петр")
print(s1.school)  # Школа №1 (одинаково для всех)
print(s1.name```

