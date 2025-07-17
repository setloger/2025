# SQL для Middle Python разработчика: Расширенный теоретический материал

## Основные концепции баз данных

### Что такое база данных?

**База данных** — это структурированная коллекция данных, организованная таким образом, чтобы обеспечить эффективное хранение, поиск и управление информацией. В контексте реляционных баз данных, данные организованы в виде таблиц, связанных между собой отношениями.

### Ключевые принципы реляционных баз данных

#### 1. Атомарность данных

Каждое значение в таблице должно быть **атомарным** (неделимым). Это означает, что в одной ячейке не должно храниться несколько значений.

```sql
-- Неправильно: нарушение атомарности
CREATE TABLE bad_users (
    id INTEGER,
    name VARCHAR(100),
    phones VARCHAR(200)  -- "123-456-7890, 987-654-3210" - несколько номеров в одном поле
);

-- Правильно: атомарные значения
CREATE TABLE users (
    id INTEGER,
    name VARCHAR(100)
);

CREATE TABLE user_phones (
    user_id INTEGER,
    phone VARCHAR(20),
    phone_type VARCHAR(10)  -- 'mobile', 'home', 'work'
);
```


#### 2. Целостность данных

Система должна гарантировать **целостность данных** на нескольких уровнях:

- **Доменная целостность**: значения соответствуют определенному типу данных
- **Ссылочная целостность**: внешние ключи ссылаются на существующие записи
- **Ключевая целостность**: каждая запись имеет уникальный идентификатор

```sql
-- Создание таблицы с различными типами ограничений целостности
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,                    -- Ключевая целостность
    email VARCHAR(255) UNIQUE NOT NULL,       -- Уникальность и обязательность
    age INTEGER CHECK (age >= 18 AND age <= 120),  -- Доменная целостность
    department_id INTEGER,
    salary DECIMAL(10,2) CHECK (salary > 0),  -- Бизнес-правило
    
    -- Ссылочная целостность
    FOREIGN KEY (department_id) REFERENCES departments(id) 
        ON DELETE SET NULL    -- При удалении отдела, department_id становится NULL
        ON UPDATE CASCADE     -- При изменении id отдела, обновляется и здесь
);
```


#### 3. Нормализация

**Нормализация** — процесс организации данных в базе данных для уменьшения избыточности и предотвращения аномалий.

**Первая нормальная форма (1NF)**:

- Все значения атомарны
- Каждая запись уникальна
- Нет повторяющихся групп

```sql
-- Нарушение 1NF: повторяющиеся группы
CREATE TABLE bad_orders (
    order_id INTEGER,
    customer_name VARCHAR(100),
    product1 VARCHAR(100),
    quantity1 INTEGER,
    product2 VARCHAR(100),
    quantity2 INTEGER
);

-- Соответствие 1NF
CREATE TABLE orders (
    order_id INTEGER,
    customer_name VARCHAR(100)
);

CREATE TABLE order_items (
    order_id INTEGER,
    product_name VARCHAR(100),
    quantity INTEGER
);
```

**Вторая нормальная форма (2NF)**:

- Соответствует 1NF
- Все неключевые атрибуты полностью зависят от первичного ключа

```sql
-- Нарушение 2NF: частичная зависимость
CREATE TABLE bad_order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    customer_name VARCHAR(100),  -- Зависит только от order_id, не от всего ключа
    product_name VARCHAR(100),   -- Зависит только от product_id
    PRIMARY KEY (order_id, product_id)
);

-- Соответствие 2NF: разделение на отдельные таблицы
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_name VARCHAR(100)
);

CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    product_name VARCHAR(100)
);

CREATE TABLE order_items (
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

**Третья нормальная форма (3NF)**:

- Соответствует 2NF
- Нет транзитивных зависимостей неключевых атрибутов

```sql
-- Нарушение 3NF: транзитивная зависимость
CREATE TABLE bad_employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INTEGER,
    department_name VARCHAR(100),    -- Зависит от department_id, не от employee_id
    department_location VARCHAR(100) -- Транзитивная зависимость
);

-- Соответствие 3NF
CREATE TABLE departments (
    department_id INTEGER PRIMARY KEY,
    department_name VARCHAR(100),
    department_location VARCHAR(100)
);

CREATE TABLE employees (
    employee_id INTEGER PRIMARY KEY,
    employee_name VARCHAR(100),
    department_id INTEGER,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);
```


## Реляционная модель и SQL: Углубленное понимание

### Математические основы

Реляционная модель основана на **теории множеств** и **реляционной алгебре**:

- **Декартово произведение**: JOIN операции
- **Проекция**: SELECT определенных столбцов
- **Селекция**: WHERE условия
- **Объединение**: UNION операции
- **Пересечение**: INTERSECT операции
- **Разность**: EXCEPT операции

```sql
-- Пример операций реляционной алгебры

-- Проекция (π): выбор определенных столбцов
SELECT name, salary FROM employees;  -- π(name, salary)(employees)

-- Селекция (σ): фильтрация строк
SELECT * FROM employees WHERE salary > 50000;  -- σ(salary > 50000)(employees)

-- Декартово произведение (×): JOIN без условий
SELECT * FROM employees, departments;  -- employees × departments

-- Естественное соединение (⋈): JOIN с условием
SELECT * FROM employees e
JOIN departments d ON e.department_id = d.id;  -- employees ⋈ departments
```


### Свойства отношений

#### 1. Каждое отношение имеет уникальное имя

```sql
-- Создание отношения "employees" в схеме "hr"
CREATE TABLE hr.employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
```


#### 2. Каждый атрибут имеет уникальное имя в рамках отношения

```sql
-- Правильно: уникальные имена атрибутов
CREATE TABLE orders (
    order_id INTEGER,
    customer_id INTEGER,
    order_date DATE
);

-- Неправильно: дублирующиеся имена при JOIN
-- SELECT id, id FROM users JOIN orders ON users.id = orders.user_id;

-- Правильно: использование алиасов
SELECT u.id as user_id, o.id as order_id 
FROM users u 
JOIN orders o ON u.id = o.user_id;
```


#### 3. Порядок кортежей (строк) не важен

```sql
-- Эти запросы эквивалентны
SELECT * FROM users ORDER BY id;
SELECT * FROM users ORDER BY name;
-- Результат одинаков, только порядок вывода разный
```


#### 4. Порядок атрибутов (столбцов) не важен

```sql
-- Эти запросы логически эквивалентны
SELECT name, email FROM users;
SELECT email, name FROM users;
-- Содержат одну и ту же информацию, но в разном порядке
```


## Виды и типы баз данных: Детальный анализ

### Классификация по модели данных

#### 1. Реляционные базы данных (RDBMS)

**Характеристики**:

- Данные хранятся в таблицах с четко определенной схемой
- Поддержка ACID транзакций
- Использование SQL для запросов
- Строгая типизация данных

**Преимущества**:

- Высокая целостность данных
- Мощные возможности запросов
- Стандартизированный язык (SQL)
- Поддержка сложных отношений

**Недостатки**:

- Сложность масштабирования по горизонтали
- Жесткая схема данных
- Может быть избыточной для простых случаев

```sql
-- Пример создания реляционной структуры
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    -- Ограничение ссылочной целостности
    FOREIGN KEY (customer_id) REFERENCES customers(id)
        ON DELETE RESTRICT  -- Запрет удаления клиента с заказами
        ON UPDATE CASCADE   -- Автоматическое обновление при изменении id
);
```


#### 2. Документоориентированные базы данных

**Характеристики**:

- Данные хранятся в виде документов (обычно JSON/BSON)
- Гибкая схема данных
- Поддержка вложенных структур
- Оптимизация для чтения

**Применение**:

- Системы управления контентом
- Каталоги товаров
- Профили пользователей
- Логирование событий


#### 3. Графовые базы данных

**Характеристики**:

- Данные представлены в виде узлов и ребер
- Оптимизированы для обхода связей
- Поддержка сложных отношений
- Язык запросов для графов (например, Cypher)

**Применение**:

- Социальные сети
- Системы рекомендаций
- Анализ мошенничества
- Сетевой анализ


#### 4. Колоночные базы данных

**Характеристики**:

- Данные хранятся по столбцам, а не по строкам
- Высокая производительность для аналитики
- Эффективное сжатие данных
- Оптимизация для чтения больших объемов

**Применение**:

- Аналитические системы
- Хранилища данных
- Системы бизнес-аналитики
- Обработка временных рядов


## PostgreSQL: Глубокое погружение

### Архитектура PostgreSQL

#### 1. Процессная модель

PostgreSQL использует **мультипроцессную архитектуру**:

- **Postmaster**: главный процесс, принимает соединения
- **Backend процессы**: обслуживают клиентские соединения
- **Background processes**: фоновые задачи (WAL writer, checkpointer, autovacuum)

```sql
-- Просмотр активных процессов
SELECT 
    pid,
    usename,
    application_name,
    client_addr,
    state,
    query_start,
    query
FROM pg_stat_activity
WHERE state = 'active';
```


#### 2. Система хранения данных

**MVCC (Multi-Version Concurrency Control)**:

- Каждая строка имеет видимость для транзакций
- Версионирование данных для конкурентного доступа
- Отсутствие блокировок на чтение

```sql
-- Демонстрация MVCC
BEGIN;
-- Транзакция 1
UPDATE products SET price = price * 1.1 WHERE category = 'electronics';
-- Другие транзакции видят старые значения до COMMIT
COMMIT;
```


#### 3. Система индексов

PostgreSQL поддерживает различные типы индексов:

**B-tree индексы** (по умолчанию):

```sql
-- Создание B-tree индекса (по умолчанию)
CREATE INDEX idx_users_email ON users(email);

-- Составной индекс
CREATE INDEX idx_orders_customer_date ON orders(customer_id, order_date);

-- Частичный индекс
CREATE INDEX idx_active_users ON users(email) WHERE is_active = true;
```

**Hash индексы**:

```sql
-- Оптимизированы для равенства
CREATE INDEX idx_users_id_hash ON users USING hash(id);
```

**GIN индексы** (для полнотекстового поиска):

```sql
-- Создание GIN индекса для полнотекстового поиска
ALTER TABLE articles ADD COLUMN search_vector tsvector;
CREATE INDEX idx_articles_search ON articles USING gin(search_vector);

-- Обновление поискового вектора
UPDATE articles SET search_vector = to_tsvector('english', title || ' ' || content);
```

**GiST индексы** (для геометрических данных):

```sql
-- Создание GiST индекса для геоданных
CREATE INDEX idx_locations_geom ON locations USING gist(geom);
```


### Расширенные возможности PostgreSQL

#### 1. Поддержка JSON и JSONB

```sql
-- Создание таблицы с JSON данными
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    specifications JSON,     -- JSON: точное хранение
    metadata JSONB          -- JSONB: бинарное хранение, индексируемое
);

-- Вставка JSON данных
INSERT INTO products (name, specifications, metadata) VALUES 
(
    'Laptop',
    '{"brand": "Apple", "model": "MacBook Pro", "year": 2024}',
    '{"specs": {"ram": "16GB", "storage": "512GB", "processor": "M3"}, "warranty": "2 years"}'
);

-- Запросы к JSON данным
SELECT name, specifications->>'brand' as brand
FROM products
WHERE specifications->>'year' = '2024';

-- Использование JSON операторов
SELECT name, metadata->'specs'->>'ram' as ram
FROM products
WHERE metadata->'specs'->>'processor' LIKE '%M3%';

-- Создание индексов для JSON
CREATE INDEX idx_products_brand ON products USING gin((specifications->>'brand'));
CREATE INDEX idx_products_specs ON products USING gin(metadata);
```


#### 2. Массивы

```sql
-- Создание таблицы с массивами
CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200),
    tags TEXT[],              -- Массив строк
    ratings INTEGER[],        -- Массив чисел
    coordinates POINT[]       -- Массив геометрических точек
);

-- Вставка данных с массивами
INSERT INTO articles (title, tags, ratings, coordinates) VALUES 
(
    'PostgreSQL Tutorial',
    ARRAY['database', 'sql', 'postgresql', 'tutorial'],
    ARRAY[5, 4, 5, 3, 4],
    ARRAY[POINT(1,2), POINT(3,4)]
);

-- Запросы к массивам
SELECT title, tags[1] as first_tag          -- Доступ к элементу массива
FROM articles;

SELECT title, array_length(tags, 1) as tag_count  -- Длина массива
FROM articles;

-- Поиск в массиве
SELECT title
FROM articles
WHERE 'postgresql' = ANY(tags);              -- Поиск значения в массиве

-- Агрегация массивов
SELECT array_agg(title) as all_titles        -- Создание массива из строк
FROM articles;
```


#### 3. Пользовательские типы данных

```sql
-- Создание составного типа
CREATE TYPE address_type AS (
    street VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10)
);

-- Использование составного типа
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    billing_address address_type,
    shipping_address address_type
);

-- Вставка данных с составными типами
INSERT INTO customers (name, billing_address, shipping_address) VALUES 
(
    'John Doe',
    ROW('123 Main St', 'New York', 'NY', '10001'),
    ROW('456 Oak Ave', 'Brooklyn', 'NY', '11201')
);

-- Запросы к составным типам
SELECT name, (billing_address).city as billing_city
FROM customers;
```


## Типы данных в PostgreSQL: Полный обзор

### Числовые типы

#### Целые числа

```sql
-- Различные типы целых чисел
CREATE TABLE numeric_examples (
    small_int SMALLINT,        -- 2 байта, от -32768 до 32767
    regular_int INTEGER,       -- 4 байта, от -2147483648 до 2147483647
    big_int BIGINT,           -- 8 байт, очень большие числа
    
    -- Автоинкрементные типы
    auto_small SMALLSERIAL,    -- Автоинкрементный SMALLINT
    auto_regular SERIAL,       -- Автоинкрементный INTEGER
    auto_big BIGSERIAL         -- Автоинкрементный BIGINT
);

-- Пример использования с проверками
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    price INTEGER CHECK (price > 0),           -- Цена в копейках
    stock_quantity SMALLINT DEFAULT 0,         -- Небольшие количества
    total_views BIGINT DEFAULT 0               -- Большие счетчики
);
```


#### Десятичные числа

```sql
-- Различные типы десятичных чисел
CREATE TABLE decimal_examples (
    exact_decimal DECIMAL(10,2),    -- Точное представление, 10 цифр, 2 после запятой
    numeric_val NUMERIC(15,4),      -- Синоним DECIMAL
    
    -- Приблизительные типы
    real_val REAL,                  -- 4 байта, приблизительное представление
    double_val DOUBLE PRECISION,    -- 8 байт, приблизительное представление
    
    -- Специальные значения
    special_val REAL DEFAULT 'NaN'  -- Not a Number
);

-- Практический пример
CREATE TABLE financial_transactions (
    id SERIAL PRIMARY KEY,
    amount DECIMAL(12,2) NOT NULL,     -- Денежные суммы требуют точности
    exchange_rate NUMERIC(10,6),       -- Курсы валют с высокой точностью
    processing_fee REAL,               -- Комиссии можно хранить приблизительно
    
    CHECK (amount > 0),                -- Бизнес-правило
    CHECK (exchange_rate > 0)
);
```


### Строковые типы

#### Символьные типы

```sql
-- Различные строковые типы
CREATE TABLE string_examples (
    fixed_char CHAR(10),         -- Фиксированная длина, дополняется пробелами
    variable_char VARCHAR(255),   -- Переменная длина с ограничением
    unlimited_text TEXT,         -- Неограниченная длина
    
    -- Специальные строковые типы
    case_insensitive CITEXT,     -- Регистронезависимый текст (требует расширения)
    
    -- Ограничения на строки
    email VARCHAR(255) CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'),
    phone CHAR(12) CHECK (phone ~ '^\+\d{1,3}\d{8,}$')
);

-- Практический пример
CREATE TABLE user_profiles (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,      -- Ограниченная длина для производительности
    email VARCHAR(255) UNIQUE NOT NULL,        -- Стандартная длина для email
    first_name VARCHAR(100),                   -- Имена обычно короткие
    bio TEXT,                                  -- Биография может быть длинной
    status_code CHAR(3) DEFAULT 'ACT'          -- Фиксированные коды состояний
);
```


### Дата и время

#### Типы даты и времени

```sql
-- Различные типы даты и времени
CREATE TABLE datetime_examples (
    just_date DATE,                    -- Только дата: 2024-01-15
    just_time TIME,                    -- Только время: 14:30:00
    time_with_zone TIMETZ,             -- Время с часовым поясом
    
    -- Временные метки
    simple_timestamp TIMESTAMP,        -- Дата и время без часового пояса
    timestamp_with_zone TIMESTAMPTZ,   -- Дата и время с часовым поясом
    
    -- Интервалы
    duration INTERVAL,                 -- Период времени
    
    -- Значения по умолчанию
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Практический пример
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    start_date DATE NOT NULL,                                    -- Дата начала
    start_time TIME NOT NULL,                                    -- Время начала
    duration INTERVAL DEFAULT '1 hour',                         -- Продолжительность
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,           -- Когда создано
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,           -- Когда обновлено
    
    -- Проверка логики дат
    CHECK (start_date >= CURRENT_DATE)
);

-- Работа с датами и временем
INSERT INTO events (title, start_date, start_time, duration) VALUES 
(
    'Team Meeting',
    '2024-02-15',
    '14:00:00',
    INTERVAL '2 hours 30 minutes'
);

-- Запросы с датами
SELECT 
    title,
    start_date,
    start_time,
    start_date + start_time as full_start_datetime,    -- Объединение даты и времени
    duration,
    EXTRACT(HOUR FROM duration) as duration_hours      -- Извлечение часов
FROM events;
```


### Булевы типы

```sql
-- Булевы значения
CREATE TABLE boolean_examples (
    id SERIAL PRIMARY KEY,
    is_active BOOLEAN DEFAULT TRUE,     -- true, false, null
    is_verified BOOLEAN NOT NULL,       -- Обязательное булево значение
    is_premium BOOLEAN DEFAULT FALSE
);

-- Различные способы задания булевых значений
INSERT INTO boolean_examples (is_verified, is_premium) VALUES 
(TRUE, FALSE),
(true, false),                -- Регистр не важен
('yes', 'no'),               -- Текстовые представления
('1', '0'),                  -- Числовые представления
('t', 'f');                  -- Сокращенные формы
```


### Специальные типы

#### UUID (Universally Unique Identifier)

```sql
-- Работа с UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";  -- Подключение расширения

CREATE TABLE uuid_examples (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),  -- Автогенерация UUID
    user_id UUID NOT NULL,
    session_token UUID DEFAULT uuid_generate_v4(),
    
    -- Индексы на UUID работают эффективно
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Вставка с UUID
INSERT INTO uuid_examples (user_id) VALUES 
('550e8400-e29b-41d4-a716-446655440000');
```


#### Перечисления (ENUM)

```sql
-- Создание пользовательского ENUM типа
CREATE TYPE order_status AS ENUM ('pending', 'processing', 'shipped', 'delivered', 'cancelled');

-- Использование ENUM
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    status order_status DEFAULT 'pending',
    total_amount DECIMAL(10,2) NOT NULL,
    
    -- ENUM гарантирует только допустимые значения
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Вставка с ENUM
INSERT INTO orders (customer_id, status, total_amount) VALUES 
(1, 'pending', 99.99),
(2, 'processing', 149.50);

-- Запросы с ENUM
SELECT status, COUNT(*) as order_count
FROM orders
GROUP BY status
ORDER BY status;
```


#### Сетевые типы

```sql
-- Специальные типы для сетевых адресов
CREATE TABLE network_examples (
    id SERIAL PRIMARY KEY,
    ip_address INET,           -- IP адрес с маской подсети
    network_cidr CIDR,         -- Сетевой адрес
    mac_address MACADDR        -- MAC адрес
);

-- Вставка сетевых данных
INSERT INTO network_examples (ip_address, network_cidr, mac_address) VALUES 
('192.168.1.1/24', '192.168.1.0/24', '08:00:2b:01:02:03');

-- Запросы с сетевыми операторами
SELECT ip_address, network_cidr
FROM network_examples
WHERE ip_address << '192.168.1.0/24';  -- IP входит в подсеть
```


## Создание и управление базами данных

### Создание базы данных

```sql
-- Создание базы данных с полными параметрами
CREATE DATABASE ecommerce_db
    WITH 
    OWNER = ecommerce_user              -- Владелец базы данных
    ENCODING = 'UTF8'                   -- Кодировка символов
    LC_COLLATE = 'en_US.UTF-8'         -- Правила сортировки
    LC_CTYPE = 'en_US.UTF-8'           -- Правила классификации символов
    TABLESPACE = pg_default             -- Табличное пространство
    CONNECTION LIMIT = 100              -- Максимальное количество подключений
    IS_TEMPLATE = FALSE;                -- Не является шаблоном

-- Создание пользователя для базы данных
CREATE USER ecommerce_user WITH 
    PASSWORD 'secure_password'
    CREATEDB                           -- Право создания баз данных
    NOSUPERUSER                        -- Не суперпользователь
    INHERIT                            -- Наследование прав ролей
    LOGIN                              -- Может логиниться
    NOREPLICATION                      -- Не может создавать репликацию
    CONNECTION LIMIT 50;               -- Ограничение подключений

-- Предоставление прав на базу данных
GRANT ALL PRIVILEGES ON DATABASE ecommerce_db TO ecommerce_user;
```


### Создание схем

```sql
-- Подключение к базе данных
\c ecommerce_db;

-- Создание схем для организации объектов
CREATE SCHEMA sales                    -- Схема для продаж
    AUTHORIZATION ecommerce_user;

CREATE SCHEMA inventory                -- Схема для склада
    AUTHORIZATION ecommerce_user;

CREATE SCHEMA users                    -- Схема для пользователей
    AUTHORIZATION ecommerce_user;

CREATE SCHEMA audit                    -- Схема для аудита
    AUTHORIZATION ecommerce_user;

-- Установка пути поиска схем
SET search_path TO sales, inventory, users, public;

-- Просмотр текущего пути поиска
SHOW search_path;
```


### Создание таблиц с детальными пояснениями

```sql
-- Создание таблицы пользователей с полным набором опций
CREATE TABLE users.customers (
    -- Первичный ключ с автоинкрементом
    id SERIAL PRIMARY KEY,                              -- SERIAL = INTEGER + SEQUENCE
    
    -- Уникальные идентификаторы
    uuid UUID DEFAULT uuid_generate_v4() UNIQUE,        -- Универсальный идентификатор
    email VARCHAR(255) UNIQUE NOT NULL,                 -- Email должен быть уникальным
    username VARCHAR(50) UNIQUE NOT NULL,               -- Имя пользователя
    
    -- Персональная информация
    first_name VARCHAR(100) NOT NULL,                   -- Имя обязательно
    last_name VARCHAR(100) NOT NULL,                    -- Фамилия обязательна
    phone VARCHAR(20),                                  -- Телефон необязательный
    date_of_birth DATE,                                 -- Дата рождения
    
    -- Адресная информация (денормализованная для простоты)
    street_address TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50) DEFAULT 'USA',
    
    -- Аутентификация и безопасность
    password_hash VARCHAR(255) NOT NULL,               -- Хэш пароля
    salt VARCHAR(32) NOT NULL,                         -- Соль для хэширования
    failed_login_attempts INTEGER DEFAULT 0,           -- Счетчик неудачных попыток
    last_login_at TIMESTAMPTZ,                         -- Последний вход
    locked_until TIMESTAMPTZ,                          -- Блокировка до определенного времени
    
    -- Статус аккаунта
    is_active BOOLEAN DEFAULT TRUE,                    -- Активен ли аккаунт
    is_verified BOOLEAN DEFAULT FALSE,                 -- Подтвержден ли email
    is_premium BOOLEAN DEFAULT FALSE,                  -- Премиум аккаунт
    
    -- Временные метки
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,  -- Когда создан
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,  -- Когда обновлен
    deleted_at TIMESTAMPTZ,                           -- Мягкое удаление
    
    -- Бизнес-правила через CHECK ограничения
    CONSTRAINT valid_email CHECK (
        email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    ),
    CONSTRAINT valid_phone CHECK (
        phone IS NULL OR phone ~ '^\+?[\d\s\-\(\)]+$'
    ),
    CONSTRAINT valid_age CHECK (
        date_of_birth IS NULL OR 
        date_of_birth <= CURRENT_DATE - INTERVAL '13 years'
    ),
    CONSTRAINT valid_postal_code CHECK (
        postal_code IS NULL OR LENGTH(postal_code) >= 3
    )
);

-- Создание индексов для оптимизации запросов
CREATE INDEX idx_customers_email ON users.customers(email);                    -- Поиск по email
CREATE INDEX idx_customers_username ON users.customers(username);              -- Поиск по имени пользователя
CREATE INDEX idx_customers_phone ON users.customers(phone) WHERE phone IS NOT NULL;  -- Частичный индекс
CREATE INDEX idx_customers_location ON users.customers(city, state, country);  -- Составной индекс
CREATE INDEX idx_customers_created_at ON users.customers(created_at);          -- Сортировка по дате
CREATE INDEX idx_customers_active ON users.customers(is_active) WHERE is_active = TRUE;  -- Активные пользователи

-- Создание индекса для мягкого удаления
CREATE INDEX idx_customers_not_deleted ON users.customers(id) WHERE deleted_at IS NULL;
```


### Создание таблиц с отношениями

```sql
-- Создание таблицы категорий товаров
CREATE TABLE inventory.categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    parent_id INTEGER,                                  -- Для иерархических категорий
    slug VARCHAR(100) UNIQUE NOT NULL,                  -- URL-friendly название
    is_active BOOLEAN DEFAULT TRUE,
    sort_order INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    
    -- Самоссылающийся внешний ключ для иерархии
    FOREIGN KEY (parent_id) REFERENCES inventory.categories(id)
        ON DELETE SET NULL                              -- При удалении родителя, parent_id = NULL
        ON UPDATE CASCADE,                              -- При изменении id родителя, обновляем ссылки
    
    -- Проверка на циклические ссылки (упрощенная)
    CONSTRAINT no_self_reference CHECK (id != parent_id)
);

-- Создание таблицы товаров
CREATE TABLE inventory.products (
    id SERIAL PRIMARY KEY,
    sku VARCHAR(100) UNIQUE NOT NULL,                   -- Stock Keeping Unit
    name VARCHAR(200) NOT NULL,
    description TEXT,
    
    -- Ценовая информация
    price DECIMAL(10,2) NOT NULL,
    cost_price DECIMAL(10,2),                          -- Себестоимость
    compare_at_price DECIMAL(10,2),                    -- Цена до скидки
    
    -- Информация о складе
    stock_quantity INTEGER DEFAULT 0,
    reserved_quantity INTEGER DEFAULT 0,               -- Зарезервированное количество
    reorder_point INTEGER DEFAULT 0,                   -- Точка дозаказа
    reorder_quantity INTEGER DEFAULT 0,                -- Количество для дозаказа
    
    -- Физические характеристики
    weight DECIMAL(8,3),                               -- Вес в кг
    dimensions JSONB,                                  -- Размеры в JSON
    
    -- Статус товара
    is_active BOOLEAN DEFAULT TRUE,
    is_featured BOOLEAN DEFAULT FALSE,
    is_digital BOOLEAN DEFAULT FALSE,
    requires_shipping BOOLEAN DEFAULT TRUE,
    
    -- Метаданные
    meta_title VARCHAR(200),
    meta_description TEXT,
    tags TEXT[],                                       -- Массив тегов
    
    -- Временные метки
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    published_at TIMESTAMPTZ,
    
    -- Бизнес-правила
    CONSTRAINT positive_price CHECK (price > 0),
    CONSTRAINT positive_cost CHECK (cost_price IS NULL OR cost_price >= 0),
    CONSTRAINT valid_stock CHECK (stock_quantity >= 0),
    CONSTRAINT valid_reserved CHECK (reserved_quantity >= 0),
    CONSTRAINT reserved_not_more_than_stock CHECK (reserved_quantity <= stock_quantity),
    CONSTRAINT valid_weight CHECK (weight IS NULL OR weight > 0)
);

-- Создание связующей таблицы для отношения многие-ко-многим
CREATE TABLE inventory.product_categories (
    product_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    is_primary BOOLEAN DEFAULT FALSE,                   -- Основная категория
    sort_order INTEGER DEFAULT 0,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    
    -- Составной первичный ключ
    PRIMARY KEY (product_id, category_id),
    
    -- Внешние ключи
    FOREIGN KEY (product_id) REFERENCES inventory.products(id)
        ON DELETE CASCADE                               -- При удалении товара удаляем связи
        ON UPDATE CASCADE,
    FOREIGN KEY (category_id) REFERENCES inventory.categories(id)
        ON DELETE CASCADE                               -- При удалении категории удаляем связи
        ON UPDATE CASCADE,
    
    -- Только одна основная категория на товар
    CONSTRAINT unique_primary_category 
        EXCLUDE (product_id WITH =) WHERE (is_primary = TRUE)
);
```


## Отношения между таблицами: Углубленное изучение

### Отношение один-ко-многим (1:N)

Это **наиболее распространенный тип отношений** в реляционных базах данных. Одна запись в родительской таблице может соответствовать множеству записей в дочерней таблице.

```sql
-- Пример: Один клиент может иметь много заказов
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,                       -- Внешний ключ
    order_number VARCHAR(50) UNIQUE NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) DEFAULT 'pending',
    order_date TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    
    -- Определение внешнего ключа с действиями при изменении/удалении
    FOREIGN KEY (customer_id) REFERENCES customers(id)
        ON DELETE RESTRICT                              -- Запрет удаления клиента с заказами
        ON UPDATE CASCADE,                              -- Автообновление при изменении id клиента
    
    -- Бизнес-правила
    CONSTRAINT positive_amount CHECK (total_amount > 0),
    CONSTRAINT valid_status CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled'))
);

-- Создание индексов для оптимизации JOIN операций
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_orders_date ON orders(order_date);

-- Примеры запросов с отношением 1:N
-- Получить всех клиентов с количеством их заказов
SELECT 
    c.name,
    c.email,
    COUNT(o.id) as order_count,
    COALESCE(SUM(o.total_amount), 0) as total_spent
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id            -- LEFT JOIN включает клиентов без заказов
GROUP BY c.id, c.name, c.email
ORDER BY total_spent DESC;

-- Получить клиентов с заказами за последний месяц
SELECT DISTINCT c.name, c.email
FROM customers c
INNER JOIN orders o ON c.id = o.customer_id           -- INNER JOIN только клиенты с заказами
WHERE o.order_date >= CURRENT_DATE - INTERVAL '1 month'
    AND o.status != 'cancelled';
```


### Отношение один-к-одному (1:1)

Каждая запись в одной таблице соответствует **максимум одной записи** в другой таблице. Используется для разделения данных по логическим или производственным причинам.

```sql
-- Пример: Один пользователь имеет один профиль
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    last_login_at TIMESTAMPTZ
);

CREATE TABLE user_profiles (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL,                    -- UNIQUE обеспечивает отношение 1:1
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    bio TEXT,
    avatar_url VARCHAR(500),
    date_of_birth DATE,
    phone VARCHAR(20),
    
    -- Адресная информация
    street_address TEXT,
    city VARCHAR(100),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    
    -- Настройки
    timezone VARCHAR(50) DEFAULT 'UTC',
    language VARCHAR(10) DEFAULT 'en',
    receive_notifications BOOLEAN DEFAULT TRUE,
    
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    
    -- Внешний ключ с уникальным ограничением
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE                               -- При удалении пользователя удаляем профиль
        ON UPDATE CASCADE
);

-- Альтернативный подход: профиль как первичная таблица
CREATE TABLE user_profiles_alt (
    user_id INTEGER PRIMARY KEY,                        -- Первичный ключ = внешний ключ
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    bio TEXT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- Примеры запросов с отношением 1:1
-- Получить пользователей с их профилями
SELECT 
    u.username,
    u.email,
    p.first_name,
    p.last_name,
    p.bio,
    p.city,
    p.country
FROM users u
LEFT JOIN user_profiles p ON u.id = p.user_id;        -- LEFT JOIN включает пользователей без профилей

-- Найти пользователей без профилей
SELECT u.username, u.email
FROM users u
LEFT JOIN user_profiles p ON u.id = p.user_id
WHERE p.user_id IS NULL;
```


### Отношение многие-ко-многим (M:N)

Записи в одной таблице могут соответствовать **множеству записей** в другой таблице и наоборот. Реализуется через промежуточную таблицу.

```sql
-- Пример: Студенты и курсы (один студент может посещать много курсов, один курс может иметь много студентов)
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    student_number VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE courses (
    id SERIAL PRIMARY KEY,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    credits INTEGER NOT NULL,
    max_students INTEGER,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    
    CONSTRAINT positive_credits CHECK (credits > 0),
    CONSTRAINT positive_max_students CHECK (max_students IS NULL OR max_students > 0)
);

-- Связующая таблица для отношения M:N
CREATE TABLE student_course_enrollments (
    student_id INTEGER NOT NULL,
    course_id INTEGER NOT NULL,
    enrollment_date DATE DEFAULT CURRENT_DATE,
    completion_date DATE,
    grade VARCHAR(5),                                   -- A, B, C, D, F
    status VARCHAR(20) DEFAULT 'enrolled',              -- enrolled, completed, dropped, failed
    credits_earned INTEGER DEFAULT 0,
    
    -- Составной первичный ключ предотвращает дублирование записей
    PRIMARY KEY (student_id, course_id),
    
    -- Внешние ключи
    FOREIGN KEY (student_id) REFERENCES students(id)
        ON DELETE CASCADE                               -- При удалении студента удаляем записи
        ON UPDATE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(id)
        ON DELETE CASCADE                               -- При удалении курса удаляем записи
        ON UPDATE CASCADE,
    
    -- Бизнес-правила
    CONSTRAINT valid_grade CHECK (grade IS NULL OR grade IN ('A', 'B', 'C', 'D', 'F')),
    CONSTRAINT valid_status CHECK (status IN ('enrolled', 'completed', 'dropped', 'failed')),
    CONSTRAINT completion_logic CHECK (
        (status = 'completed' AND completion_date IS NOT NULL AND grade IS NOT NULL) OR
        (status != 'completed')
    ),
    CONSTRAINT chronological_dates CHECK (
        completion_date IS NULL OR completion_date >= enrollment_date
    )
);

-- Индексы для оптимизации запросов
CREATE INDEX idx_enrollments_student ON student_course_enrollments(student_id);
CREATE INDEX idx_enrollments_course ON student_course_enrollments(course_id);
CREATE INDEX idx_enrollments_status ON student_course_enrollments(status);
CREATE INDEX idx_enrollments_date ON student_course_enrollments(enrollment_date);

-- Примеры сложных запросов с отношением M:N
-- Получить всех студентов с их курсами
SELECT 
    s.student_number,
    s.first_name,
    s.last_name,
    c.course_code,
    c.title as course_title,
    e.enrollment_date,
    e.status,
    e.grade
FROM students s
JOIN student_course_enrollments e ON s.id = e.student_id
JOIN courses c ON e.course_id = c.id
ORDER BY s.last_name, s.first_name, c.course_code;

-- Статистика по курсам
SELECT 
    c.course_code,
    c.title,
    COUNT(e.student_id) as enrolled_students,
    AVG(CASE WHEN e.grade = 'A' THEN 4.0
             WHEN e.grade = 'B' THEN 3.0
             WHEN e.grade = 'C' THEN 2.0
             WHEN e.grade = 'D' THEN 1.0
             WHEN e.grade = 'F' THEN 0.0
        END) as average_gpa,
    COUNT(CASE WHEN e.status = 'completed' THEN 1 END) as completed_count,
    COUNT(CASE WHEN e.status = 'dropped' THEN 1 END) as dropped_count
FROM courses c
LEFT JOIN student_course_enrollments e ON c.id = e.course_id
GROUP BY c.id, c.course_code, c.title
ORDER BY enrolled_students DESC;

-- Найти студентов, которые изучают более 5 курсов одновременно
SELECT 
    s.student_number,
    s.first_name,
    s.last_name,
    COUNT(e.course_id) as course_count
FROM students s
JOIN student_course_enrollments e ON s.id = e.student_id
WHERE e.status = 'enrolled'
GROUP BY s.id, s.student_number, s.first_name, s.last_name
HAVING COUNT(e.course_id) > 5
ORDER BY course_count DESC;
```


### Самоссылающиеся отношения

Таблица может ссылаться сама на себя для создания иерархических структур.

```sql
-- Пример: Иерархия сотрудников (менеджеры и подчиненные)
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    employee_number VARCHAR(20) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    job_title VARCHAR(100),
    manager_id INTEGER,                                 -- Ссылка на менеджера
    department_id INTEGER,
    salary DECIMAL(10,2),
    hire_date DATE DEFAULT CURRENT_DATE,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    
    -- Самоссылающийся внешний ключ
    FOREIGN KEY (manager_id) REFERENCES employees(id)
        ON DELETE SET NULL                              -- При удалении менеджера, manager_id = NULL
        ON UPDATE CASCADE,
    
    -- Предотвращение самоссылки
    CONSTRAINT no_self_management CHECK (id != manager_id),
    CONSTRAINT positive_salary CHECK (salary IS NULL OR salary > 0)
);

-- Рекурсивный запрос для получения иерархии
WITH RECURSIVE employee_hierarchy AS (
    -- Базовый случай: топ-менеджеры (без начальника)
    SELECT 
        id,
        employee_number,
        first_name,
        last_name,
        job_title,
        manager_id,
        0 as level,
        CAST(last_name AS TEXT) as path
    FROM employees
    WHERE manager_id IS NULL
    
    UNION ALL
    
    -- Рекурсивный случай: подчиненные
    SELECT 
        e.id,
        e.employee_number,
        e.first_name,
        e.last_name,
        e.job_title,
        e.manager_id,
        eh.level + 1,
        eh.path || ' > ' || e.last_name
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT 
    REPEAT('  ', level) || first_name || ' ' || last_name as hierarchy,
    job_title,
    level,
    path
FROM employee_hierarchy
ORDER BY path;
```

Этот расширенный материал содержит детальные объяснения каждой концепции с практическими примерами кода и комментариями, что поможет кандидату глубже понять SQL и подготовиться к собеседованию на middle уровень.

