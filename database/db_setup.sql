CREATE TABLE editorial (
    editorial_id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    pais VARCHAR(50)
);

CREATE TABLE autor (
    autor_id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL
);

CREATE TABLE libro (
    libro_id SERIAL PRIMARY KEY,
    titulo VARCHAR(255) NOT NULL,
    anio_publicacion INT,
    autor_id INT REFERENCES autor(autor_id),
    editorial_id INT REFERENCES editorial(editorial_id)
);

SELECT 
    libro.titulo, 
    libro.anio_publicacion, 
    autor.nombre AS autor, 
    autor.apellido AS apellido, 
    editorial.nombre AS editorial
FROM libro
JOIN autor ON libro.autor_id = autor.autor_id
JOIN editorial ON libro.editorial_id = editorial.editorial_id;

INSERT INTO editorial (nombre, pais)
VALUES 
    ('Planeta', 'España'),
    ('Anagrama', 'España');

INSERT INTO autor (nombre, apellido)
VALUES 
    ('Gabriel', 'García Márquez'),
    ('Isabel', 'Allende');

INSERT INTO libro (titulo, anio_publicacion, autor_id, editorial_id)
VALUES 
    ('Cien años de soledad', 1967, 1, 1),
    ('La casa de los espíritus', 1982, 2, 1);
