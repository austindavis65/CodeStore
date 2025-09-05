use spj;

#1
SELECT DISTINCT jid
FROM spj
JOIN s ON s.sid = spj.sid 
WHERE s.city = 'London'
;

#2
SELECT DISTINCT jid
FROM spj
WHERE sid IN
(SELECT sid
FROM s WHERE city = 'London')
;

#3
SELECT DISTINCT jid
FROM spj
JOIN p ON p.pid = spj.pid
WHERE p.color = 'Red'

#4
SELECT DISTINCT jid
FROM spj
WHERE pid IN
(SELECT pid
FROM p WHERE color = 'Red')
;

#5
SELECT jid, pid, sid, qty
FROM spj
WHERE qty >
(SELECT AVG(qty)
FROM spj)
;

#7
SELECT 'S5' AS 'sid';
