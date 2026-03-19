DROP TABLE IF EXISTS redflame;
CREATE TABLE redflame (
    dept INT,
    manager CHAR(1) CHECK (manager IN ('Y', 'N')),
    name VARCHAR(50),
    birthdate DATE,
    salary DECIMAL(10,2)
);

INSERT INTO redflame (Dept, Manager, Name, Birthdate, Salary) VALUES
(1, 'Y', 'BOB', TO_DATE('1981-01-01','YYYY-MM,DD'), 50000),
(1, 'N', 'BILL', TO_DATE('1982-02-02','YYYY-MM,DD'), 40000),
(1, 'N', 'BOYD', TO_DATE('1983-03-03','YYYY-MM,DD'), 70000),
(2, 'Y', 'JIM', TO_DATE('1984-04-04','YYYY-MM,DD'), 40000),
(2, 'N', 'JANET', TO_DATE('1985-05-05','YYYY-MM,DD'), 50000),
(2, 'N', 'JACK', TO_DATE('1986-06-06','YYYY-MM,DD'), 60000),
(3, 'Y', 'MARY', TO_DATE('1987-07-07','YYYY-MM,DD'), 50000),
(3, 'N', 'MARTHA', TO_DATE('1988-08-08','YYYY-MM,DD'), 70000),
(3, 'N', 'MARTY', TO_DATE('1989-09-09','YYYY-MM,DD'), 90000);



DROP VIEW IF EXISTS d1man;
CREATE VIEW d1man AS
    SELECT * FROM redflame
    WHERE dept = 1;

DROP VIEW IF EXISTS d1emp;
CREATE VIEW d1emp AS
    SELECT dept, manager, name, birthdate
    FROM redflame
    WHERE dept = 1;

DROP VIEW IF EXISTS d2man;
CREATE VIEW d2man AS
    SELECT * FROM redflame
    WHERE dept = 2;

DROP VIEW IF EXISTS d2emp;
CREATE VIEW d2emp AS
    SELECT dept, manager, name, birthdate
    FROM redflame
    WHERE dept = 2;

DROP VIEW IF EXISTS d3man;
CREATE VIEW d3man AS
    SELECT * FROM redflame
    WHERE dept = 3;

DROP VIEW IF EXISTS d3emp;
CREATE VIEW d3emp AS
    SELECT dept, manager, name, birthdate
    FROM redflame
    WHERE dept = 3;

GRANT SELECT ON ADMIN.d1man TO BOB;
GRANT SELECT ON ADMIN.d1emp TO BILL;
GRANT SELECT ON ADMIN.d1emp TO BOYD;
GRANT SELECT ON ADMIN.d2man TO JIM;
GRANT SELECT ON ADMIN.d2emp TO JANET;
GRANT SELECT ON ADMIN.d2emp TO JACK;
GRANT SELECT ON ADMIN.d3man TO MARY;
GRANT SELECT ON ADMIN.d3emp TO MARTHA;
GRANT SELECT ON ADMIN.d3emp TO MARTY;

GRANT ALL ON ADMIN.redflame to MARY;

GRANT UPDATE(BIRTHDATE) ON ADMIN.redflame TO MARTHA;

GRANT SELECT ON ADMIN.REDFLAME TO MARTY;


