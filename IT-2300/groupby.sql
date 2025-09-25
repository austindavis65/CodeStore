#1
SELECT ROUND(AVG(price), 2) AS "Average Price" FROM titles;

#2
SELECT COUNT(title_id) AS "Qty" FROM titles;

#3
SELECT SUM(sales*price) AS "Volume" FROM titles;

#4
SELECT type, ROUND(AVG(pages), 0) AS "Average Pages" FROM titles GROUP BY type ORDER BY type ASC;

#5
SELECT type, ROUND(AVG(pages), 0) AS "Average Pages" FROM titles GROUP BY type HAVING ROUND(AVG(pages), 0) > 500 ORDER BY type ASC;

#6
SELECT type, ROUND(AVG(pages), 0) 
AS "Average Pages" 
FROM titles GROUP BY type HAVING ROUND(AVG(pages), 0) > 500 ORDER BY ROUND(AVG(pages), 0) ASC;

#7
SELECT COUNT(DISTINCT state) AS 'Number of States'
FROM authors;

#8
SELECT DISTINCT state, COUNT(state) AS "# of Authors" FROM authors GROUP BY state ORDER BY state ASC;

#9
SELECT DISTINCT type, COUNT(type) AS "# of Books" FROM titles GROUP BY type HAVING type != 'children' ORDER BY type ASC; 

#10
SELECT DISTINCT type, COUNT(type) AS "# of Books" FROM titles GROUP BY type HAVING type != 'children' AND COUNT(type) >= 3 ORDER BY type ASC;
