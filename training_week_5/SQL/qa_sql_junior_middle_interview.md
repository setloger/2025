# SQL: Вопросы для собеседования на Junior и Middle уровни

## Теоретические вопросы для Junior уровня

### 1. Что такое SQL и для чего он используется?

**Ответ:** SQL (Structured Query Language) — это декларативный язык программирования для работы с реляционными базами данных. Используется для создания, изменения и запроса данных в БД[^1].

### 2. Какие основные типы команд SQL существуют?

**Ответ:**

- **DDL (Data Definition Language)**: CREATE, ALTER, DROP
- **DML (Data Manipulation Language)**: SELECT, INSERT, UPDATE, DELETE
- **DCL (Data Control Language)**: GRANT, REVOKE
- **TCL (Transaction Control Language)**: COMMIT, ROLLBACK, SAVEPOINT[^2]


### 3. Что такое первичный ключ (Primary Key)?

**Ответ:** Первичный ключ — это столбец или комбинация столбцов, которые уникально идентифицируют каждую строку в таблице. Не может содержать NULL значений[^2].

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL
);
```


### 4. Что такое внешний ключ (Foreign Key)?

**Ответ:** Внешний ключ — это столбец или группа столбцов, которые создают связь между двумя таблицами, ссылаясь на первичный ключ другой таблицы[^2].

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```


### 5. В чем разница между WHERE и HAVING?

**Ответ:**

- **WHERE** фильтрует строки до группировки
- **HAVING** фильтрует группы после GROUP BY[^3]

```sql
-- WHERE
SELECT * FROM products WHERE price > 100;

-- HAVING
SELECT category, AVG(price) FROM products 
GROUP BY category 
HAVING AVG(price) > 100;
```


### 6. Что такое JOIN и какие типы JOIN существуют?

**Ответ:** JOIN объединяет строки из двух или более таблиц на основе связи между ними[^3]:

- **INNER JOIN**: только совпадающие записи
- **LEFT JOIN**: все записи из левой таблицы
- **RIGHT JOIN**: все записи из правой таблицы
- **FULL JOIN**: все записи из обеих таблиц


### 7. Для чего используется оператор LIKE?

**Ответ:** LIKE используется для поиска строк, соответствующих определенному шаблону[^4]:

- `%` — любое количество символов
- `_` — один символ

```sql
SELECT * FROM users WHERE name LIKE 'John%';  -- начинается с "John"
SELECT * FROM users WHERE name LIKE 'J_hn';   -- J + любой символ + hn
```


### 8. Что такое NULL и как с ним работать?

**Ответ:** NULL — это отсутствие значения. Для проверки используются IS NULL и IS NOT NULL[^5].

```sql
SELECT * FROM users WHERE phone IS NULL;
SELECT * FROM users WHERE phone IS NOT NULL;
```


### 9. Какие агрегатные функции вы знаете?

**Ответ:** Основные агрегатные функции[^1]:

- **COUNT()** — количество записей
- **SUM()** — сумма значений
- **AVG()** — среднее значение
- **MIN()** — минимальное значение
- **MAX()** — максимальное значение


### 10. Что делает команда DISTINCT?

**Ответ:** DISTINCT удаляет дубликаты из результата запроса[^3].

```sql
SELECT DISTINCT city FROM users;  -- только уникальные города
```


### 11. Для чего используется GROUP BY?

**Ответ:** GROUP BY группирует строки с одинаковыми значениями в указанных столбцах для применения агрегатных функций[^3].

```sql
SELECT category, COUNT(*) FROM products GROUP BY category;
```


### 12. Что такое индекс в базе данных?

**Ответ:** Индекс — это структура данных, которая улучшает скорость поиска в таблице, создавая упорядоченные ссылки на строки[^3].

## Теоретические вопросы для Middle уровня

### 1. Что такое ACID и объясните каждое свойство?

**Ответ:** ACID — это набор свойств транзакций[^6]:

- **Atomicity (Атомарность)**: транзакция выполняется полностью или не выполняется вовсе
- **Consistency (Согласованность)**: данные остаются в консистентном состоянии
- **Isolation (Изолированность)**: транзакции не влияют друг на друга
- **Durability (Долговечность)**: результаты сохраняются при сбоях


### 2. Какие уровни изоляции транзакций существуют?

**Ответ:** Четыре уровня изоляции[^5]:

- **READ UNCOMMITTED**: может читать незафиксированные данные
- **READ COMMITTED**: читает только зафиксированные данные
- **REPEATABLE READ**: гарантирует повторяемость чтения
- **SERIALIZABLE**: полная изоляция


### 3. Что такое нормализация и денормализация?

**Ответ:**

- **Нормализация** — процесс организации данных для устранения избыточности и аномалий[^6]
- **Денормализация** — намеренное добавление избыточности для улучшения производительности


### 4. Объясните разницу между коррелированным и некоррелированным подзапросом

**Ответ:**

- **Некоррелированный подзапрос** выполняется один раз независимо от внешнего запроса
- **Коррелированный подзапрос** выполняется для каждой строки внешнего запроса, используя его данные[^6]


### 5. Что такое оконные функции (Window Functions)?

**Ответ:** Оконные функции выполняют вычисления над набором строк, связанных с текущей строкой[^3].

```sql
SELECT name, salary, 
       ROW_NUMBER() OVER (ORDER BY salary DESC) as rank
FROM employees;
```


### 6. Объясните разницу между DELETE, TRUNCATE и DROP

**Ответ:**

- **DELETE** — удаляет строки, можно откатить, медленно
- **TRUNCATE** — удаляет все строки, быстро, нельзя откатить
- **DROP** — удаляет всю таблицу или объект[^5]


### 7. Что такое CTE (Common Table Expression)?

**Ответ:** CTE — это временный именованный результат запроса, который можно использовать в основном запросе[^7].

```sql
WITH high_earners AS (
    SELECT * FROM employees WHERE salary > 100000
)
SELECT * FROM high_earners WHERE department = 'IT';
```


### 8. Как оптимизировать медленные запросы?

**Ответ:** Основные способы оптимизации[^6]:

- Создание подходящих индексов
- Избегание ненужных JOIN
- Использование WHERE вместо HAVING где возможно
- Анализ плана выполнения
- Переписывание подзапросов как JOIN


### 9. Что такое MVCC (Multi-Version Concurrency Control)?

**Ответ:** MVCC — это механизм контроля параллельного доступа, который позволяет читать данные без блокировок, создавая версии строк для каждой транзакции.

### 10. Объясните разницу между кластеризованным и некластеризованным индексом

**Ответ:**

- **Кластеризованный индекс** определяет физический порядок хранения данных (обычно по первичному ключу)
- **Некластеризованный индекс** создает отдельную структуру со ссылками на данные[^3]


### 11. Что такое партиционирование таблиц?

**Ответ:** Партиционирование — это разделение большой таблицы на несколько меньших частей для улучшения производительности и управляемости.

### 12. Как работает планировщик запросов?

**Ответ:** Планировщик анализирует SQL-запрос и создает оптимальный план выполнения, выбирая наилучшие индексы, порядок JOIN и методы доступа к данным.

## Практические задачи для Junior уровня

### 1. Создать таблицу и добавить данные

**Задача:** Создайте таблицу users с полями id, name, email, age и добавьте 3 записи.

**Ответ:**

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    age INTEGER CHECK (age >= 0)
);

INSERT INTO users (name, email, age) VALUES 
('John Doe', 'john@example.com', 25),
('Jane Smith', 'jane@example.com', 30),
('Bob Johnson', 'bob@example.com', 35);
```


### 2. Выбрать пользователей по условию

**Задача:** Найти всех пользователей старше 25 лет, отсортировать по возрасту по убыванию.

**Ответ:**

```sql
SELECT * FROM users 
WHERE age > 25 
ORDER BY age DESC;
```


### 3. Обновить данные

**Задача:** Изменить email пользователя с именем 'John Doe' на 'john.doe@newmail.com'.

**Ответ:**

```sql
UPDATE users 
SET email = 'john.doe@newmail.com' 
WHERE name = 'John Doe';
```


### 4. Подсчитать количество записей

**Задача:** Подсчитать количество пользователей в каждой возрастной группе (до 30 и от 30).

**Ответ:**

```sql
SELECT 
    CASE 
        WHEN age < 30 THEN 'Under 30'
        ELSE '30 and above'
    END as age_group,
    COUNT(*) as user_count
FROM users
GROUP BY 
    CASE 
        WHEN age < 30 THEN 'Under 30'
        ELSE '30 and above'
    END;
```


### 5. Найти максимальное и минимальное значение

**Задача:** Найти самого молодого и самого старого пользователя.

**Ответ:**

```sql
SELECT 
    MIN(age) as youngest_age,
    MAX(age) as oldest_age
FROM users;

-- Или с именами:
SELECT name, age FROM users WHERE age = (SELECT MIN(age) FROM users)
UNION ALL
SELECT name, age FROM users WHERE age = (SELECT MAX(age) FROM users);
```


### 6. Поиск по шаблону

**Задача:** Найти всех пользователей, чьи имена начинаются с 'J'.

**Ответ:**

```sql
SELECT * FROM users WHERE name LIKE 'J%';
```


### 7. Работа с NULL значениями

**Задача:** Найти пользователей, у которых не указан возраст.

**Ответ:**

```sql
SELECT * FROM users WHERE age IS NULL;
```


### 8. Простой JOIN

**Задача:** Создать таблицу orders и вывести имена пользователей с их заказами.

**Ответ:**

```sql
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    product_name VARCHAR(100),
    amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

INSERT INTO orders (user_id, product_name, amount) VALUES 
(1, 'Laptop', 999.99),
(1, 'Mouse', 25.50),
(2, 'Keyboard', 75.00);

SELECT u.name, o.product_name, o.amount
FROM users u
JOIN orders o ON u.id = o.user_id;
```


### 9. Агрегация данных

**Задача:** Подсчитать общую сумму заказов для каждого пользователя.

**Ответ:**

```sql
SELECT 
    u.name,
    COUNT(o.id) as order_count,
    SUM(o.amount) as total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name;
```


### 10. Удаление записей

**Задача:** Удалить всех пользователей младше 25 лет.

**Ответ:**

```sql
DELETE FROM users WHERE age < 25;
```


### 11. Среднее значение

**Задача:** Найти средний возраст пользователей.

**Ответ:**

```sql
SELECT AVG(age) as average_age FROM users;
```


### 12. Ограничение результатов

**Задача:** Вывести первых 5 пользователей, отсортированных по имени.

**Ответ:**

```sql
SELECT * FROM users 
ORDER BY name 
LIMIT 5;
```


## Практические задачи для Middle уровня

### 1. Найти второй по величине оклад

**Задача:** Найти второй по величине оклад из таблицы employees.

**Ответ:**

```sql
-- Способ 1: с подзапросом
SELECT MAX(salary) as second_highest_salary
FROM employees
WHERE salary < (SELECT MAX(salary) FROM employees);

-- Способ 2: с LIMIT и OFFSET
SELECT DISTINCT salary
FROM employees
ORDER BY salary DESC
LIMIT 1 OFFSET 1;

-- Способ 3: с оконной функцией
SELECT salary
FROM (
    SELECT salary,
           DENSE_RANK() OVER (ORDER BY salary DESC) as rank
    FROM employees
) ranked
WHERE rank = 2;
```


### 2. Найти дубликаты в таблице

**Задача:** Найти всех пользователей с одинаковыми email адресами.

**Ответ:**

```sql
-- Подсчет дубликатов
SELECT email, COUNT(*) as duplicate_count
FROM users
GROUP BY email
HAVING COUNT(*) > 1;

-- Получить все записи с дубликатами
SELECT u.*
FROM users u
INNER JOIN (
    SELECT email
    FROM users
    GROUP BY email
    HAVING COUNT(*) > 1
) duplicates ON u.email = duplicates.email
ORDER BY u.email, u.id;
```


### 3. Рекурсивный запрос для иерархии

**Задача:** Получить всех подчиненных менеджера на всех уровнях иерархии.

**Ответ:**

```sql
WITH RECURSIVE employee_hierarchy AS (
    -- Базовый случай: менеджер
    SELECT 
        id, name, manager_id, 0 as level
    FROM employees
    WHERE id = 1  -- ID менеджера
    
    UNION ALL
    
    -- Рекурсивный случай: подчиненные
    SELECT 
        e.id, e.name, e.manager_id, eh.level + 1
    FROM employees e
    INNER JOIN employee_hierarchy eh ON e.manager_id = eh.id
)
SELECT 
    REPEAT('  ', level) || name as hierarchy,
    level
FROM employee_hierarchy
ORDER BY level, name;
```


### 4. Накопительная сумма

**Задача:** Показать накопительную сумму продаж по дням.

**Ответ:**

```sql
SELECT 
    sale_date,
    daily_sales,
    SUM(daily_sales) OVER (
        ORDER BY sale_date 
        ROWS UNBOUNDED PRECEDING
    ) as cumulative_sales
FROM (
    SELECT 
        DATE(order_date) as sale_date,
        SUM(total_amount) as daily_sales
    FROM orders
    GROUP BY DATE(order_date)
) daily_totals
ORDER BY sale_date;
```


### 5. Pivot таблица

**Задача:** Создать сводную таблицу продаж по месяцам и категориям.

**Ответ:**

```sql
SELECT 
    category,
    SUM(CASE WHEN month_num = 1 THEN amount ELSE 0 END) as jan,
    SUM(CASE WHEN month_num = 2 THEN amount ELSE 0 END) as feb,
    SUM(CASE WHEN month_num = 3 THEN amount ELSE 0 END) as mar,
    SUM(CASE WHEN month_num = 4 THEN amount ELSE 0 END) as apr
FROM (
    SELECT 
        p.category,
        EXTRACT(MONTH FROM o.order_date) as month_num,
        SUM(oi.quantity * oi.price) as amount
    FROM orders o
    JOIN order_items oi ON o.id = oi.order_id
    JOIN products p ON oi.product_id = p.id
    WHERE EXTRACT(YEAR FROM o.order_date) = 2024
    GROUP BY p.category, EXTRACT(MONTH FROM o.order_date)
) monthly_sales
GROUP BY category;
```


### 6. Топ N в каждой группе

**Задача:** Найти топ-3 самых дорогих товара в каждой категории.

**Ответ:**

```sql
SELECT category, name, price
FROM (
    SELECT 
        category,
        name,
        price,
        ROW_NUMBER() OVER (PARTITION BY category ORDER BY price DESC) as rn
    FROM products
) ranked
WHERE rn <= 3
ORDER BY category, price DESC;
```


### 7. Заполнение пропусков в датах

**Задача:** Найти пропуски в последовательности дат и заполнить их нулями.

**Ответ:**

```sql
WITH date_series AS (
    SELECT generate_series(
        '2024-01-01'::date,
        '2024-12-31'::date,
        '1 day'::interval
    )::date as date_day
),
daily_sales AS (
    SELECT 
        DATE(order_date) as sale_date,
        SUM(total_amount) as daily_total
    FROM orders
    GROUP BY DATE(order_date)
)
SELECT 
    ds.date_day,
    COALESCE(s.daily_total, 0) as sales_amount
FROM date_series ds
LEFT JOIN daily_sales s ON ds.date_day = s.sale_date
ORDER BY ds.date_day;
```


### 8. Коррелированный подзапрос

**Задача:** Найти сотрудников, которые зарабатывают больше среднего в своем отделе.

**Ответ:**

```sql
SELECT e1.name, e1.salary, e1.department
FROM employees e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department = e1.department
);
```


### 9. Сложный анализ клиентов

**Задача:** Найти топ-10 самых прибыльных клиентов с их статистикой.

**Ответ:**

```sql
SELECT 
    c.name,
    COUNT(o.id) as total_orders,
    SUM(o.total_amount) as total_spent,
    AVG(o.total_amount) as avg_order_value,
    MAX(o.order_date) as last_order_date,
    CURRENT_DATE - MAX(o.order_date) as days_since_last_order,
    CASE 
        WHEN SUM(o.total_amount) > 10000 THEN 'VIP'
        WHEN SUM(o.total_amount) > 5000 THEN 'Premium'
        ELSE 'Regular'
    END as customer_segment
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name
HAVING COUNT(o.id) > 0
ORDER BY total_spent DESC
LIMIT 10;
```


### 10. Временные ряды с трендами

**Задача:** Анализ трендов продаж с предыдущими периодами.

**Ответ:**

```sql
SELECT 
    date_day,
    sales_amount,
    LAG(sales_amount) OVER (ORDER BY date_day) as prev_day_sales,
    sales_amount - LAG(sales_amount) OVER (ORDER BY date_day) as day_change,
    AVG(sales_amount) OVER (
        ORDER BY date_day 
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) as week_avg
FROM (
    SELECT 
        DATE(order_date) as date_day,
        SUM(total_amount) as sales_amount
    FROM orders
    GROUP BY DATE(order_date)
) daily_sales
ORDER BY date_day;
```


### 11. Самосоединение

**Задача:** Найти сотрудников, работающих в одном отделе.

**Ответ:**

```sql
SELECT 
    e1.name as employee1,
    e2.name as employee2,
    e1.department
FROM employees e1
JOIN employees e2 ON e1.department = e2.department
WHERE e1.id < e2.id  -- избегаем дубликатов
ORDER BY e1.department, e1.name;
```


### 12. Оптимизация медленного запроса

**Задача:** Оптимизировать запрос для получения статистики пользователей.

**Ответ:**

```sql
-- Неоптимизированный запрос
SELECT 
    u.name,
    COUNT(o.id) as order_count,
    SUM(o.total_amount) as total_spent
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
WHERE u.created_at >= '2024-01-01'
GROUP BY u.id, u.name
ORDER BY total_spent DESC;

-- Оптимизированная версия с индексами
CREATE INDEX idx_users_created_at ON users(created_at);
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- Переписанный запрос
WITH user_stats AS (
    SELECT 
        u.id,
        u.name,
        COALESCE(order_stats.order_count, 0) as order_count,
        COALESCE(order_stats.total_spent, 0) as total_spent
    FROM users u
    LEFT JOIN (
        SELECT 
            user_id,
            COUNT(*) as order_count,
            SUM(total_amount) as total_spent
        FROM orders
        GROUP BY user_id
    ) order_stats ON u.id = order_stats.user_id
    WHERE u.created_at >= '2024-01-01'
)
SELECT name, order_count, total_spent
FROM user_stats
ORDER BY total_spent DESC;
```

Эти вопросы и задачи основаны на реальных собеседованиях и покрывают основные темы, которые часто встречаются при найме разработчиков на junior и middle позиции[^1][^2][^5][^3]. Они помогут кандидатам подготовиться к техническим интервью и продемонстрировать свои знания SQL на практике.

<div style="text-align: center">⁂</div>

[^1]: https://www.datacamp.com/blog/top-sql-interview-questions-and-answers-for-beginners-and-intermediate-practitioners

[^2]: https://www.geeksforgeeks.org/sql/sql-interview-questions/

[^3]: https://www.reddit.com/r/SQL/comments/191lesk/interview_questions_for_sql/

[^4]: https://www.whizlabs.com/blog/sql-queries-for-beginners/

[^5]: https://www.simplilearn.com/top-sql-interview-questions-and-answers-article

[^6]: https://upesonline.ac.in/blog/advanced-sql-interview-questions

[^7]: https://learnsql.com/blog/advanced-sql-practice/

[^8]: https://www.semanticscholar.org/paper/752dfa4d147880e5eab7f73366a06034d3b0954b

[^9]: https://ejournal.unesa.ac.id/index.php/mathedunesa/article/view/44763

[^10]: https://ejournal.umm.ac.id/index.php/MEJ/article/view/23047

[^11]: https://www.semanticscholar.org/paper/bf5b6cb05f27e736c1cf369584b1e910efd69724

[^12]: https://www.semanticscholar.org/paper/44b3658dbdebf99b098b1abab65c6f774c978b7b

[^13]: http://link.springer.com/10.1007/978-1-4842-0599-0

[^14]: http://journal.uniku.ac.id/index.php/IEFLJ/article/view/9534

[^15]: https://journal.uny.ac.id/index.php/jpep/article/view/48670

[^16]: https://ojs3.unpatti.ac.id/index.php/jupitek/article/view/5989

[^17]: https://knepublishing.com/index.php/KnE-Social/article/view/15952

[^18]: https://resumeworded.com/interview-questions/junior-sql-developer

[^19]: https://www.interviewbit.com/sql-interview-questions/

[^20]: https://dataschool.com/learn-sql/mid-level-practice/

[^21]: https://gist.github.com/monbang/76151aa5f36d5c058f95ce396d992bdb

[^22]: https://www.geeksforgeeks.org/sql/sql-exercises/

[^23]: https://codesignal.com/blog/interview-prep/28-sql-interview-questions-and-answers-from-beginner-to-senior-level/

[^24]: https://www.w3schools.com/sql/sql_exercises.asp

[^25]: https://www.reddit.com/r/SQL/comments/t3j7zm/where_to_practicelearn_sql_at_intermediate_level/

[^26]: https://codefinity.com/blog/The-50-Top-SQL-Interview-Questions-and-Answers

[^27]: https://www.codechef.com/practice/sql-case-studies-topic-wise

[^28]: https://datalemur.com/blog/advanced-sql-interview-questions

[^29]: https://datalemur.com/questions

[^30]: https://www.w3resource.com/sql-exercises/

[^31]: https://www.aclweb.org/anthology/2021.naacl-main.160.pdf

[^32]: https://arxiv.org/html/2402.13288v1

[^33]: https://aclanthology.org/2023.emnlp-main.868.pdf

[^34]: https://arxiv.org/html/2502.12918v2

[^35]: http://arxiv.org/pdf/2410.10680.pdf

[^36]: https://arxiv.org/abs/2301.10315

[^37]: https://dl.acm.org/doi/pdf/10.1145/3654995

[^38]: https://aclanthology.org/2023.acl-short.117.pdf

[^39]: http://arxiv.org/pdf/2503.23157.pdf

[^40]: https://arxiv.org/pdf/2302.05965.pdf

