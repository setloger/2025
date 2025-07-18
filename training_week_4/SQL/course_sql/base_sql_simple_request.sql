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

-- 018 WHERE

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

-- 19 AND, OR

SELECT *
FROM products
WHERE unit_price > 25 AND units_in_stock > 40;

SELECT * 
FROM customers 
WHERE city = 'Berlin' OR city = 'London' OR city = 'San Francisco';

SELECT * 
FROM orders 
WHERE shipped_date > '1998-04-30' AND (freight > '100.0' or freight < '10.0'); 

-- 20 BETWEEN

SELECT * 
FROM orders
WHERE freight >=20 AND freight <=40;

SELECT COUNT(*) 
FROM orders
WHERE freight BETWEEN 20 AND 40;

SELECT *
FROM orders
WHERE order_date BETWEEN '1998-01-01' AND '1998-02-01';

-- 21 IN & NOT IN

SELECT company_name, city, country
FROM customers
WHERE country = 'Germany' OR country = 'Mexico' OR country = 'UK';

SELECT company_name, city, country
FROM customers
WHERE country IN ('Germany', 'Mexico', 'UK');

SELECT company_name, city, country
FROM customers
WHERE country NOT IN ('Germany', 'Mexico', 'UK');

-- 21 ORDER BY

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

-- 21 MIN, MAX, AVG

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




