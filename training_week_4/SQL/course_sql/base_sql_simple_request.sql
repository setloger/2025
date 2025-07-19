-- 017 SELECT - используется для извлечения данных из таблицы базы данных
-- В SQL ключевое слово FROM указывает источник данных, из которого будет 
-- выполняться выборка. Оно всегда используется в паре с SELECT и определяет, 
-- из какой таблицы, представления или подзапроса брать информацию.

SELECT *
 FROM categories;

SELECT *
 FROM products;

SELECT product_id, product_name, unit_price * units_in_stock
FROM products;

SELECT product_id, product_name, unit_price * units_in_stock + units_on_order
FROM products;

SELECT DISTINCT city, country 
FROM employees;

SELECT COUNT (DISTINCT city)
FROM employees;

-- 018 WHERE - используется для фильтрации строк — оно позволяет задать 
-- условие, по которому выбираются только те записи, что тебе действительно нужны.
    -- Отбирает только те строки, которые соответствуют заданному критерию.
    -- Применяется после FROM, но перед сортировкой или группировкой.
    -- Может использовать арифметические, логические и текстовые условия.

SELECT company_name, contact_name, phone, country
FROM customers
WHERE country = 'USA';

SELECT *
FROM products
WHERE unit_price > 20 and category_id = 7;

SELECT COUNT(*)
FROM products
WHERE unit_price > 20; 

SELECT * 
FROM customers
WHERE city != 'London';

SELECT * 
FROM orders
WHERE order_date >= '1998-01-01';

-- 19 AND, OR - используются в разделе WHERE для логического объединения 
-- условий — чтобы указать, какие записи должны попасть в результат

SELECT *
FROM products
WHERE unit_price > 25 AND units_in_stock > 40;

SELECT * 
FROM customers 
WHERE city = 'Berlin' OR city = 'London' OR city = 'San Francisco';

SELECT * 
FROM orders 
WHERE shipped_date > '1998-04-30' AND (freight > '100.0' or freight < '10.0'); 

-- 20 BETWEEN - используется для проверки, находится ли значение в 
-- заданном диапазоне — включая начальное и конечное значение. Он делает запросы 
-- более читаемыми, особенно при работе с числами, датами и временем.

SELECT * 
FROM orders
WHERE freight >=20 AND freight <=40;

SELECT COUNT(*) 
FROM orders
WHERE freight BETWEEN 20 AND 40;

SELECT *
FROM orders
WHERE order_date BETWEEN '1998-01-01' AND '1998-02-01';

-- 21 IN & NOT IN - используются для сравнения с множеством значений, что 
-- делает запросы компактнее и читаемее. 
    -- IN — Фильтрует значения, которые есть в списке
    -- NOT IN — НЕ входит в список

SELECT company_name, city, country
FROM customers
WHERE country = 'Germany' OR country = 'Mexico' OR country = 'UK';

SELECT company_name, city, country
FROM customers
WHERE country IN ('Germany', 'Mexico', 'UK');

SELECT company_name, city, country
FROM customers
WHERE country NOT IN ('Germany', 'Mexico', 'UK');

-- 22 ORDER BY — это команда в SQL, которая используется для сортировки 
-- результатов запроса по одному или нескольким столбцам.
    -- По умолчанию сортирует по возрастанию (ASC)
    -- Можно указать сортировку по убыванию (DESC)

SELECT DISTINCT country
FROM customers;

SELECT DISTINCT country
FROM customers
ORDER BY country;

SELECT DISTINCT country
FROM customers
ORDER BY country ASC -- по умолчанию A до Z;

SELECT DISTINCT country
FROM customers
ORDER BY country DESC -- по убыванию;

SELECT DISTINCT country, city
FROM customers
ORDER BY country DESC, city;

-- 23 MIN, MAX, AVG - это агрегатные функции, которые применяются к 
-- числовым столбцам и позволяют выполнять быструю статистику по данным

SELECT ship_city, order_date
FROM orders 
WHERE ship_city = 'London'
ORDER BY order_date;

SELECT MIN(order_date)
FROM orders 
WHERE ship_city = 'London';

SELECT MAX(order_date)
FROM orders 
WHERE ship_city = 'London';

SELECT AVG(unit_price)
FROM products 
WHERE discontinued != 1;

SELECT SUM(units_in_stock)
FROM products 
WHERE discontinued != 1;

-- 24 LIKE - используется для поиска строк, соответствующих заданному шаблону. 
-- Это особенно удобно, если нужно найти значения, содержащие часть текста, 
-- начинающиеся или заканчивающиеся на определённые символы. Используется в  
-- SQL с  термином pattern matching (сопоставление с шаблоном) означает поиск 
-- значений, которые соответствуют определённому текстовому шаблону, а не 
-- строго равны. Это особенно полезно, когда ты хочешь найти данные по части 
-- строки, подстроке, началу/концу, маске и т.д.
    -- % — соответствует любому количеству символов
    -- _ — соответствует одному символу

SELECT last_name, first_name
FROM employees
WHERE first_name LIKE '%t';

SELECT last_name, first_name
FROM employees
WHERE first_name LIKE 'N%';

-- 25 LIMIT - используется для ограничения количества возвращаемых строк в 
-- результате запроса. Это особенно полезно, когда тебе нужно взять только первые 
-- n записей — например, для постраничного вывода, превью или теста


SELECT product_name, unit_price
FROM products
LIMIT 10

-- 26 Check on NULL - ля проверки на NULL используется оператор IS NULL или 
-- IS NOT NULL — это способ узнать, содержит ли столбец пустое значение, 
-- то есть значение, которое отсутствует.

SELECT ship_city, ship_region, ship_country
FROM orders
WHERE ship_region IS NULL;

SELECT ship_city, ship_region, ship_country
FROM orders
WHERE ship_region IS NOT NULL;

-- 27 GROUP BY - используется для группировки строк по определённым столбцам, 
-- чтобы применять агрегатные функции (COUNT, AVG, SUM, MIN, MAX) к 
-- каждой группе отдельно.

SELECT ship_country, COUNT(*)
FROM orders
WHERE freight > 50
GROUP BY ship_country
ORDER BY COUNT(*) DESC;

SELECT category_id, SUM(units_in_stock)
FROM products
GROUP BY category_id
ORDER BY SUM(units_in_stock);

SELECT category_id, SUM(units_in_stock)
FROM products
GROUP BY category_id
ORDER BY SUM(units_in_stock) DESC
LIMIT 5;

-- 28 HAVING - оператор HAVING используется для фильтрации результатов 
-- после группировки — то есть применяется к агрегатным функциям 
-- (COUNT, SUM, AVG, и т. д.), когда ты используешь GROUP BY
-- Чем отличается от WHERE?
-- WHERE работает до группировки — фильтрует строки
-- HAVING работает после группировки — фильтрует группы

SELECT category_id, SUM(unit_price * units_in_stock) as RESULT
FROM products
WHERE discontinued != 1
GROUP BY category_id
HAVING SUM(unit_price * units_in_stock) > 5000
ORDER BY SUM(unit_price * units_in_stock) DESC 

-- 29 UNION оператор UNION используется для объединения результатов двух 
-- (или более) SELECT-запросов в одну таблицу, где строки идут друг за другом. 
-- Это помогает собрать данные из разных источников — например, из двух 
-- таблиц или двух фильтров — в один список


SELECT country
FROM customers
UNION
SELECT country
FROM employees

-- 30 INTERSECT - INTERSECT используется для получения пересечения 
-- результатов двух SELECT-запросов — то есть, он возвращает только те строки, 
-- которые есть в обоих результатах.

SELECT country
FROM customers
INTERSECT
SELECT country
FROM suppliers

