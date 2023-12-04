-- one-to-one

DROP SCHEMA IF EXISTS many_to_one1;
CREATE SCHEMA many_to_one1;
USE many_to_one1;

-- Create table author

CREATE TABLE author (
	author_id INT NOT NULL PRIMARY KEY auto_increment,
    first_name VARCHAR(50),
    email VARCHAR(50),
    biography TEXT
);

-- CREATE TABLE book
create table book (
	book_id int not null primary key auto_increment,
    title VARCHAR(300),
    Sinopsis TEXT,
    num_pages INT,
    author_id INT, -- columna para asociar (foreign key) en book la tabla autor
    FOREIGN KEY (author_id) references author(author_id) -- Foreign key con nombre autogenerado
);

-- Foreign key con nombre especificado
-- CONSTRAINT fk_book_author FOREIGN KEY (author_id) REFERENCES author(author_id)

INSERT INTO `author`(first_name, email, biography) 
VALUES 
('author1', 'a1@company.com', 'Biografía inventada'),
('author2', 'a2@company.com', 'Biografía inventada'),
('author3', 'a3@company.com', 'Biografía inventada');

select * from author;

INSERT INTO book(title, sinopsis, num_pages, author_id)
VALUES
('book 1', 'loremm ipsum dolor', 500, 1), -- Author 1
('book 2', 'descripcion guay', 950, 2), -- Author 2
('book 3', 'loremm ipsum dolor', 700, 1), -- Author 1
('book 4', 'sin razon para todo del corazón', 650, 3); -- Author 3

select * from book;



