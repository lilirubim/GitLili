
USE demo 2;
use demo3
show databases;
show tables;

SELECT * FROM customers;

SELECT * FROM customers WHERE NIF=1;

use sakila;

SELECT * FROM payment WHERE amount < 5;
SELECT * FROM payment WHERE amount > 10;

-- paymont amount entre 5 y 10 euros
SELECT * FROM payment WHERE amount >= 5 AND amount <= 10;
SELECT * FROM payment WHERE amount BETWEEN 5 AND 10; -- incluye 5 y 10
SELECT * FROM payment WHERE payment_date BETWEEN '2005-07-01' AND '2005-07-15';

-- operador OR customer
SELECT * FROM address WHERE	district = 'California' OR district = 'Nagasaki';

-- Filtrar address que contengan la palabra Avenue
-- LIKE

SELECT * FROM address WHERE address LIKE "%Avenue%";

SELECT * FROM customer WHERE email LIKE '%@gmail.com';
SELECT * FROM customer WHERE email NOT LIKE '%@gmail.com';


