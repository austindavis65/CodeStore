use books;

#1
SELECT titles.title_id, titles.title_name, publishers.pub_id, publishers.pub_name 
FROM titles
INNER JOIN publishers 
ON titles.pub_id = publishers.pub_id
ORDER BY pub_name
;

#2
SELECT titles.title_id, titles.title_name, authors.au_lname
FROM title_authors
INNER JOIN titles
ON title_authors.title_id = titles.title_id
INNER JOIN authors
ON title_authors.au_id = authors.au_id
WHERE title_authors.au_order = 1
;


#3
SELECT titles.title_id, titles.title_name, publishers.pub_id, publishers.pub_name
FROM titles
INNER JOIN publishers
ON titles.pub_id = publishers.pub_id
WHERE publishers.state = 'CA'
ORDER BY pub_name
;

#4
SELECT DISTINCT type, COUNT(type) AS 'Number'
FROM titles
JOIN publishers pub
ON titles.pub_id = pub.pub_id
WHERE state = 'CA'
GROUP BY type
ORDER BY type
;


#5
SELECT COUNT(emp_id) AS '# Employees', SUM(sales) AS 'Total Sales'
FROM empsales;


#6
SELECT COUNT(empsales.emp_id) AS '# Employees', SUM(sales) AS 'Total Sales'
FROM empsales
LEFT JOIN employees
ON empsales.emp_id = employees.emp_id
;


#7
SELECT empsales.emp_id, emp_name, sales
FROM empsales
LEFT JOIN employees
ON empsales.emp_id = employees.emp_id
;


#8
SELECT empsales.emp_id, emp_name, sales
FROM empsales
JOIN employees
ON empsales.emp_id = employees.emp_id
;


#9
SELECT empsales.emp_id, employees.emp_name, sales
FROM empsales
LEFT JOIN employees ON empsales.emp_id = employees.emp_id
UNION
SELECT empsales.emp_id, employees.emp_name, sales
FROM empsales
RIGHT JOIN employees ON empsales.emp_id = employees.emp_id
;

#10
SELECT hier.emp_id "Emp ID", emp.emp_name "Emp Name", hier.boss_id "Boss ID", boss.emp_name "Boss Name"
FROM hier
LEFT JOIN employees emp
ON emp.emp_id = hier.emp_id
LEFT JOIN employees boss
ON boss.emp_id = hier.boss_id
;
