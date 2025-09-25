-- Active: 1700245066884@@144.38.219.130@3306
#create database
DROP DATABASE IF EXISTS redFlame;
CREATE DATABASE redFlame;
#create employees
use redFlame;
DROP TABLE IF EXISTS employees;
CREATE TABLE employees (
    empno CHAR(5) PRIMARY KEY,
    dept CHAR(5),
    manager CHAR(1),
    name VARCHAR(30),
    birthdate DATE,
    salary DECIMAL(10,2)
);

#insert data
INSERT INTO employees VALUES
('1', '1', 'Y', 'BOB', DATE'1981-01-01', 50000.00),
('2', '1', 'N', 'BILL', DATE'1982-02-02', 40000.00),
('3', '1', 'N', 'BOYD', DATE'1983-03-03', 70000.00),
('4', '2', 'Y', 'JIM', DATE'1984-04-04', 40000.00),
('5', '2', 'N', 'JANET', DATE'1985-05-05', 50000.00),
('6', '2', 'N', 'JACK', DATE'1986-06-06', 60000.00),
('7', '3', 'Y', 'MARY', DATE'1987-07-07', 50000.00),
('8', '3', 'N', 'MARTHA', DATE'1988-08-08', 70000.00),
('9', '3', 'N', 'MARTY', DATE'1989-09-09', 90000.00)
;

CREATE VIEW d1man AS
    SELECT * FROM employees WHERE dept = '1';

CREATE VIEW d2man AS
    SELECT * FROM employees WHERE dept = '2';

CREATE VIEW d3man AS
    SELECT * FROM employees WHERE dept = '3';

CREATE VIEW admin AS
    SELECT * FROM employees;

CREATE VIEW d1 AS
    SELECT empno, dept, manager, name, birthdate FROM employees WHERE dept = '1';

CREATE VIEW d2 AS
    SELECT empno, dept, manager, name, birthdate FROM employees WHERE dept = '2';

CREATE VIEW d3 AS
    SELECT empno, dept, manager, name, birthdate FROM employees WHERE dept = '3';

CREATE VIEW birthdayman AS
    SELECT * FROM employees;
CREATE USER BOB IDENTIFIED BY 'pass123';

CREATE USER JIM IDENTIFIED BY 'pass123';

CREATE USER MARY IDENTIFIED BY 'pass123';

CREATE USER BILL IDENTIFIED BY 'pass123';

CREATE USER BOYD IDENTIFIED BY 'pass123';

CREATE USER JANET IDENTIFIED BY 'pass123';

CREATE USER JACK IDENTIFIED BY 'pass123';

CREATE USER MARTHA IDENTIFIED BY 'pass123';

CREATE USER MARTY IDENTIFIED BY 'pass123';

/*
GRANT SELECT ON redFlame.d1man TO BOB;

GRANT SELECT ON redFlame.d2man TO JIM;

GRANT SELECT ON redFlame.d3man TO MARY;

GRANT ALL PRIVILEGES ON redFlame.admin TO MARY;

GRANT SELECT ON redFlame.d1 TO BILL;

GRANT SELECT ON redFlame.d1 TO BOYD;

GRANT SELECT ON redFlame.d2 TO JANET;

GRANT SELECT ON redFlame.d2 TO JACK;

GRANT SELECT ON redFlame.d3 TO MARTHA;

GRANT SELECT ON redFlame.d3 TO MARTY;

GRANT SELECT, UPDATE(birthdate) ON redFlame.birthdayman TO MARTHA;
*/