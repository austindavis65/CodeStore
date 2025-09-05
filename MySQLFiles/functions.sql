use books;
#1
SELECT title_id, title_name, price,
   0.10 AS "Discount",
   ROUND((price * (1 - 0.10)), 2) AS "New price"
FROM titles;

#2
SELECT CONCAT(au_lname, ",", " ", au_fname) AS "Name"
FROM authors; 

#3
SELECT CONCAT(UCASE(LEFT(au_lname, 3)), RIGHT(phone, 4)) AS "Search ID",
   CONCAT(au_lname, ",", " ", au_fname) AS "Name"
FROM authors;

#4
SELECT au_lname,
   CHAR_LENGTH(au_lname) AS "length"
FROM authors;

#5
SELECT title_id, title_name, LEFT(pubdate, 4) AS "year"
FROM titles;

#6
SELECT title_id, title_name, pubdate,
   ADDDATE(pubdate, INTERVAL 28 YEAR) AS 'copyright date'
FROM titles;

#7
SELECT title_id, title_name, price, 
CASE WHEN type = "history" THEN price * (1 - 0.10) ELSE price * (1 - 0.20) END AS "New Price" FROM titles;


#8
SELECT title_id, title_name,
   COALESCE(price, "priceless") AS "Retail"
FROM titles;

#9
SELECT CONCAT(CURDATE(), " ", CURTIME()) AS "Current Time";

#10
SELECT SUBSTR(CURRENT_USER(), POSITION('@' IN CURRENT_USER())+1, 2000) AS "Server";
