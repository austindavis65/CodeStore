# create the database
drop database if exists spj;
create database spj;

# create the tables
use spj;
drop table if exists s;
create table s
(
sid char(2),
sname varchar(10),
status varchar(2),
city varchar(10)
);
drop table if exists p;
create table p
(
pid char(2),
pname varchar(10),
color varchar(10),
weight decimal(5,1),
city varchar(10)
);
drop table if exists j;
create table j
(
jid char(2),
jname varchar(10),
city varchar(10)
);
drop table if exists spj;
create table spj
(
sid char(2),
pid char(2),
jid char(2),
qty integer
);

# fill the supplier table
insert into s values
('S1','Smith','20','London');
insert into s values
('S2','Jones','10','Paris');
insert into s values
('S3','Blake','30','Paris');
insert into s values
('S4','Clark','20','London');
insert into s values
('S5','Adams','30','Athens');


# fill the product table
insert into p values
('P1','Nut','Red',12.0,'London');
insert into p values
('P2','Bolt','Green',17.0,'Paris');
insert into p values
('P3','Screw','Blue',17.0,'Rome');
insert into p values
('P4','Screw','Red',14.0,'London');
insert into p values
('P5','Cam','Blue',12.0,'Paris');
insert into p values
('P6','Cog','Red',19.0,'London');


# fill the job table
insert into j values
('J1','Sorter','Paris');
insert into j values
('J2','Display','Rome');
insert into j values
('J3','OCR','Athens');
insert into j values
('J4','Console','Athens');
insert into j values
('J5','RAID','London');
insert into j values
('J6','EDS','Oslo');
insert into j values
('J7','Tape','London');


# fill the Supplier/Parts/Job link table
insert into spj values
('S1','P1','J1',200),
('S1','P1','J4',700),
('S2','P3','J1',400),
('S2','P3','J2',200),
('S2','P3','J3',200),
('S2','P3','J4',500),
('S2','P3','J5',600),
('S2','P3','J6',400),
('S2','P3','J7',800),
('S3','P3','J1',200),
('S3','P4','J2',500),
('S4','P6','J3',300),
('S4','P6','J7',300),
('S5','P2','J2',200),
('S5','P2','J4',100),
('S5','P5','J5',500),
('S5','P5','J7',100),
('S5','P6','J2',200),
('S5','P1','J4',100),
('S5','P3','J4',200),
('S5','P4','J4',800),
('S5','P5','J4',400),
('S5','P6','J4',500);
