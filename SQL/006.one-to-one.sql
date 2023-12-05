-- crear base de datos one_to_one
DROP SCHEMA IF EXISTS one_to_one;
CREATE SCHEMA one_to_one;
USE one_to_one;

-- crear tabla address
CREATE table address (
	id INT NOT NULL primary KEY auto_increment,
    street VARCHAR(250) NOT NULL,
    postal_code VARCHAR(5),
	city VARCHAR(50)
);

-- crear tabla users
CREATE TABLE `users` (
	id INT NOT NULL primary KEY auto_increment,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(50),
    id_address INT UNIQUE, -- retricción de unicidad
    FOREIGN KEY (id_address) references address(id)
);

select * from address

INSERT INTO address (street, postal_code, city)
VALUES 
	('ARIZA', 29087, 'MADRID'),
    ('CORAZON DE MARIA', 28654, 'MÁLAGA'),
    ('SOLEDAD', 28756, 'SEVILLA')
;

INSERT `users` (first_name, last_name, email, id_address)
VALUES 
	('JOAQUIM', 'LUNA', '1@user.com', 1),
    ('LUISA', 'KENIA', '2@user.com', 1), -- no deja guardar por la restricción one-to-one
    ('IRENE', 'MARIMBONDO', '3@user.com', 2)
;
-- Error Code: 1062. Duplicate entry '1' for key 'users.id_address'

INSERT `users` (first_name, last_name, email, id_address)
VALUES 
	('JOANA', 'LUNA', '2@user.com', 3) -- ID no está ocupado
;

select * from users

-- alterar datos

Insert into `users` (first_name, last_name, email, id_address)
VALUES 
	('JOAQUIM', 'LUNA', '1@user.com', 1),
    ('LUISA', 'KENIA', '2@user.com', 3), 
    ('IRENE', 'MARIMBONDO', '3@user.com', 2)
    ;


-- Ejemplo con dos claves foráneas desde la misma tabla origen