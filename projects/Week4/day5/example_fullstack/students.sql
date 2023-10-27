CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT,
    grade CHAR(1)
);

INSERT INTO students (first_name, last_name, age, grade) VALUES
    ('John', 'Doe', 18, 'A'),
    ('Jane', 'Smith', 19, 'B'),
    ('Bob', 'Johnson', 20, 'C'),
    ('Emily', 'Williams', 18, 'A'),
    ('Michael', 'Brown', 19, 'B');

    SELECT * FROM students ;
