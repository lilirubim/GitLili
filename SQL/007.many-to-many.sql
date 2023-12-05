-- many-to-many

DROP SCHEMA IF EXISTS many_to_many;
CREATE SCHEMA many_to_many;
USE many_to_many;

-- crear tabla libro
CREATE TABLE book (
	id int not null primary key auto_increment,
    title VARCHAR(300),
    author VARCHAR(100),
    num_pages INT
);


-- crear tabla categoria
CREATE TABLE category (
	id int not null primary key auto_increment,
    name VARCHAR(50),
    min_age INT
);

-- crear tabla libro_categoria
CREATE TABLE book_category(
	id_book INT,
    id_category INT,
    primary key (id_book, id_category), -- clave primaria compuesta, para que no se repita tal combinación
    FOREIGN KEY (id_book) references book(id),
    FOREIGN KEY (id_category) references category(id)
);

insert into book (title, author, num_pages) 
values 
	('Darby O''Gill and the Little People', 'Mable', 100),
    ('Shakedown', 'Tarrance', 200),
    ('Xtro', 'Obadiah', 312
);

insert into category (name, min_age)
values 
('poetry', 18),
('novel', 14),
('cronic', 12);

select * from book;
select * from category;
select * from book_category;

INSERT INTO book_category (id_book, id_category)
VALUES 
	(1,1), -- asocia poetry a book1
    (1,2), -- asocia novel a book1
    (3,1)
;

-- Resultado: