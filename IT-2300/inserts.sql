use books;
#1
DROP TABLE IF EXISTS bak_titles;
CREATE TABLE bak_titles AS
   (SELECT * FROM titles)
;

DROP TABLE IF EXISTS bak_publishers;
CREATE TABLE bak_publishers AS
   (SELECT * FROM publishers)
;

DROP TABLE IF EXISTS bak_authors;
CREATE TABLE bak_authors AS
   (SELECT * FROM authors)
;

DROP TABLE IF EXISTS bak_title_authors;
CREATE TABLE bak_title_authors AS
   (SELECT * FROM title_authors)
;

#2
INSERT INTO titles VALUES('T14','OCA',NULL,'P02',NULL,29.95,NULL,NULL,1);
INSERT INTO titles VALUES('T15','OCP',NULL,'P02',NULL,39.95,NULL,NULL,1);
INSERT INTO titles VALUES('T16','A+',NULL,'P02',NULL,29.95,NULL,NULL,1);
INSERT INTO titles VALUES('T17','NET+',NULL,'P02',NULL,29.95,NULL,NULL,1);
INSERT INTO titles VALUES('T18','LINUX+',NULL,'P02',NULL,29.95,NULL,NULL,1);

INSERT INTO title_authors VALUES('T14','A05',1,'1.00');
INSERT INTO title_authors VALUES('T15','A05',1,'1.00');
INSERT INTO title_authors VALUES('T16','A05',1,'1.00');
INSERT INTO title_authors VALUES('T17','A05',1,'1.00');
INSERT INTO title_authors VALUES('T18','A05',1,'1.00');

#3
UPDATE titles
   SET sales = 0
WHERE title_id IN
('T14','T15','T16','T17','T18')
;

#4
UPDATE titles
   SET pubdate = DATE '2011-01-01'
WHERE title_id IN
('T14','T15','T16','T17','T18')
;

#5
UPDATE titles
   SET type = 'computer'
WHERE title_id IN
('T14','T15','T16','T17','T18')
;

#6
DROP TABLE IF EXISTS abc_titles;
CREATE TABLE abc_titles AS
   (SELECT * FROM titles WHERE type = 'psychology')
;

DROP TABLE IF EXISTS abc_publishers;
CREATE TABLE abc_publishers AS
(SELECT * FROM publishers
WHERE pub_id IN
(SELECT pub_id 
FROM titles 
WHERE type = 'psychology'))
;


DROP TABLE IF EXISTS abc_authors;
CREATE TABLE abc_authors AS
(SELECT * FROM authors
WHERE au_id IN
(SELECT au_id
FROM title_authors
WHERE title_id IN
(SELECT title_id
FROM titles
WHERE type = 'psychology')))
;

DROP TABLE IF EXISTS abc_title_authors;
CREATE TABLE abc_title_authors AS
(SELECT * FROM title_authors
WHERE title_id in (select distinct title_id from titles where type = 'psychology'))
;


#7
DELETE FROM titles
WHERE type = 'psychology'
;

DELETE FROM title_authors
WHERE title_id NOT IN (SELECT DISTINCT title_id FROM titles)
;

DELETE FROM authors
WHERE au_id NOT IN (SELECT DISTINCT au_id FROM title_authors)
;

DELETE FROM publishers
WHERE pub_id NOT IN (SELECT DISTINCT pub_id FROM titles)
;

SELECT * FROM publishers;
SELECT * FROM authors;
SELECT * FROM title_authors;
SELECT * FROM titles;
 
SELECT * FROM abc_publishers;
SELECT * FROM abc_authors;
SELECT * FROM abc_title_authors;
SELECT * FROM abc_titles; 

