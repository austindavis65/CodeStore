#1
show tables;

#2
select * from authors;

#3
SELECT
   emp_id, emp_name
FROM
   employees;

#4
SELECT DISTINCT state FROM publishers;

#5
SELECT
   title_id, title_name, price
FROM
   titles
ORDER BY
   price DESC;

#6
SELECT
   title_id, title_name
FROM
   titles
WHERE
   type = 'children';

#7
SELECT
   title_id, title_name, type
FROM
   titles
WHERE
   type != 'history'
AND
   type != 'biography';

#8
SELECT
   au_id, au_fname, au_lname, phone
FROM
   authors
WHERE
   phone LIKE '___-549-____'
   OR phone LIKE '549-___-____'
   OR phone LIKE '___-___-_549'
   OR phone LIKE '___-___-549_';

#9
SELECT
   au_id, au_fname, au_lname, zip
FROM
   authors
WHERE
   zip LIKE '9____';

#10
SELECT
   au_id, au_fname, au_lname, state
FROM
   authors
WHERE
   state = 'NY'
   OR state = 'CA';
