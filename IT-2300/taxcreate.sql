DROP DATABASE IF EXISTS tax;
CREATE DATABASE tax;
use tax;

DROP TABLE IF EXISTS taxAreaAuthority;
CREATE TABLE taxAreaAuthority (
	taxAuthority VARCHAR(10),
	taxArea VARCHAR(10)
);

INSERT INTO taxAreaAuthority VALUES 
	('city1', 'city1'),
	('city2', 'city2'),
	('city3', 'city3'),
	('county1', 'city1'),
	('county1', 'city2'),
	('county2', 'city3'),
	('state1', 'city1'),
	('state1', 'city2'),
	('state1', 'city3')
;

DROP TABLE IF EXISTS taxRates;
CREATE TABLE taxRates (
	taxAuthority VARCHAR(10),
	effective DATE,
	authTaxRate DECIMAL(5, 1)
);

INSERT INTO taxRates VALUES 
	('city1', DATE '1993-01-01', 1),
	('city1', DATE '1994-01-01', 1.5),
	('city2', DATE '1993-09-01', 1.5),
	('city2', DATE '1994-01-01', 2),
	('city2', DATE '1995-01-01', 2.5),
	('city3', DATE '1993-01-01', 1.9),
	('city3', DATE '1993-07-01', 2.3),
	('county1', DATE '1993-01-01', 2.3),
	('county1', DATE '1994-10-01', 2.5),
	('county1', DATE '1995-01-01', 2.7),
	('county2', DATE '1993-01-01', 2.4),
	('county2', DATE '1994-01-01', 2.7),
	('county2', DATE '1995-01-01', 2.8),
	('state1', DATE '1993-01-01', 0.5),
	('state1', DATE '1994-01-01', 0.8),
	('state1', DATE '1994-07-01', 0.9),
	('state1', DATE '1994-10-01', 1.1)
;
