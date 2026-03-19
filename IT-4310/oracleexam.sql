-- 1 Create mt_City table

DROP TABLE IF EXISTS mt_City;
CREATE TABLE mt_City (
    id number PRIMARY KEY,
    name varchar2(50),
    stateid number
);

-- 2 Create mt_State table

DROP TABLE IF EXISTS mt_State;
CREATE TABLE mt_State (
    id NUMBER PRIMARY KEY,
    name VARCHAR2(50)
);

-- 3 Create mt_Employees table

DROP TABLE IF EXISTS mt_Employees;
CREATE TABLE mt_Employees (
    id         number primary key,
    name       varchar2(50),
    email      varchar2(50),
    mobile     varchar2(10),
    salary     number(10, 2),
    department varchar2(50),
    cityid     number,
    stateid    number
);

-- 4 Populate mt_City table

INSERT INTO mt_City VALUES (1, 'New Delhi', 1);
INSERT INTO mt_City VALUES (2, 'Agra', 2);
INSERT INTO mt_City VALUES (3, 'Lucknow', 2);
INSERT INTO mt_City VALUES (4, 'Noida', 2);
INSERT INTO mt_City VALUES (5, 'Mumbai', 3);
INSERT INTO mt_City VALUES (6, 'Pune', 3);
INSERT INTO mt_City VALUES (7, 'Bhopal', 4);
INSERT INTO mt_City VALUES (8, 'Indore', 4);

-- 5 Populate mt_State table

INSERT INTO mt_State VALUES (1,'Delhi');
INSERT INTO mt_State VALUES (2,'U.P.');
INSERT INTO mt_State VALUES (3,'Maharastra');
INSERT INTO mt_State VALUES (4,'M.P.');

-- 6 Populate mt_Employees table

INSERT INTO mt_Employees VALUES (1, 'John', 'john@gmail.com', 9988778899, 35000.00, 'DotNet', 1, 1);
INSERT INTO mt_Employees VALUES (2, 'Peter', 'peter@gmail.com',  9988778800, 40000.00, 'Android',   1,1);
INSERT INTO mt_Employees VALUES (3, 'Mohan', 'mohan@gmail.com',  9988778888, 25000.00, 'Java',      2,     2);
INSERT INTO mt_Employees VALUES (4, 'Sohan', 'sohan@gmail.com',  9988778855, 80000.00, 'DotNet',    1,     1);
INSERT INTO mt_Employees VALUES (5, 'Ram',   'ram@gmail.com',    9988777700, 35000.00, 'Android',   2,     2);
INSERT INTO mt_Employees VALUES (6, 'Ajay',  'ajay@gmail.com',   9988778811, 50000.00, 'DotNet',    3,     2);
INSERT INTO mt_Employees VALUES (7, 'Sumit', 'sumit@gmail.com',  7588778899, 35000.00, 'Python',    2,     2);
INSERT INTO mt_Employees VALUES (8, 'Martin','martin@gmail.com', 9011778899, 75000.00, 'DotNet',    6,     3);
INSERT INTO mt_Employees VALUES (9, 'Sanjay','sanjay@gmail.com', 9888778899, 35000.00, 'Java',      2,     2);
INSERT INTO mt_Employees VALUES (10, 'Rohit', 'rohit@gmail.com',  9088778899, 45000.00, 'DotNet',    1,     1);
INSERT INTO mt_Employees VALUES (11, 'Mukesh','mukesh@gmail.com', 9500778899, 65000.00, 'Android',   7,     4);


-- 7.1. Get second highest salary from the mt_Employee table. (only one number)

SELECT salary
FROM (
    SELECT salary, ROWNUM rown
    FROM (
        SELECT DISTINCT salary
        FROM mt_Employees
        ORDER BY salary DESC
    )
)
WHERE rown = 2;

-- 7.2. Get details of all mt_Employee who are working in 'New Delhi'.

SELECT * FROM mt_Employees e
JOIN mt_City c on e.stateid = c.stateid
WHERE c.name = 'New Delhi';

-- 7.3. Get the last record from the mt_Employee table (only one record)

SELECT * FROM mt_Employees
WHERE id = (SELECT MAX(id) FROM mt_Employees);

-- 7.4. Get Number of employees in Each Department

select department, count(*) as Count
from mt_Employees group by department;

-- 7.5. Create table mt_bak_Employee and Copy all data from the mt_Employee table

DROP TABLE IF EXISTS mt_bak_Employee;
CREATE TABLE mt_bak_Employee AS
    (
        SELECT * FROM mt_Employees
    );

-- 7.6. Display the sum of salaries from mt_Employee based on department.

select department, sum(salary)
from mt_Employees group by department;

-- 7.7. Get 3rd highest salary from the mt_Employee table (only one number)

SELECT salary
FROM (
    SELECT salary, ROWNUM rown
    FROM (
        SELECT DISTINCT salary
        FROM mt_Employees
        ORDER BY salary DESC
    )
)
WHERE rown = 3;

-- 7.8. Find all print all the data from all Employee whose name starts with 'S'.

SELECT * FROM mt_Employees
WHERE name like 'S%';

-- 7.9. Add new Column(DOB date ) in the Employee table.

ALTER TABLE mt_Employees
ADD DOB date;

-- 7.10 Drop the DOB column from Employee table.

ALTER TABLE mt_Employees
DROP COLUMN DOB;


