use sakila;

-- select de customer con su respectivos address, street

select * from customer;
select * from address;

-- first_name, email, address, district
select * from customer -- * selecciona todo
join address on customer.address_id = address.address_id;  

select first_name, email, address, district from customer -- especifica las columnas
join address on customer.address_id = address.address_id; 

-- equivale - abreviatura

select c.first_name, c.email, a.address, a.district
from customer c join address a on c.address_id = a.address_id; -- renombra con una letra las tablas, customer = c, address = a

-- 2 joins customer con address y city en un mismo SELECT
select * from customer cu -- todas columnas
join address a on cu.address_id = a.address_id
join city ci on a.city_id = ci.city_id;

select cu.email, a.address, ci.city
from customer cu
join address a on cu.address_id = a.address_id
join city ci on a.city_id = ci.city_id;