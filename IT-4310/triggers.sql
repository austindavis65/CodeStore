-- clean up
drop table if exists prospects;
drop table if exists marketing_log;
drop trigger if exists updmarketing;

-- create the prospects table
create table prospects (id char(10), name varchar2(30), phone varchar(20));

-- create the log table
create table marketing_log
   (xuser varchar2(30), xtimestamp timestamp(0), xdesc varchar2(30));

-- create the triggers
-- create trigger for update
create trigger updmarketing before update on prospects for each row
declare
begin
   insert into marketing_log (xuser, xtimestamp, xdesc) values (USER, SYSTIMESTAMP, 'Update OLD Record:'
      || :old.id);
   insert into marketing_log (xuser, xtimestamp, xdesc) values (USER, SYSTIMESTAMP, 'Update NEW Record:'
      || :new.id);
end;

-- create delete trigger

create trigger deletemarketing before delete on prospects for each row
    declare
    begin
        insert into marketing_log (xuser, xtimestamp, xdesc) values (USER, SYSTIMESTAMP, 'Deleted old record: ' || :old.id);
    end;

-- create the trigger for insert

create trigger insertmarketing before insert on prospects for each row
    declare
    begin
        insert into marketing_log (xuser, xtimestamp, xdesc) values (USER, SYSTIMESTAMP, 'Created new record: ' || :new.id);
    end;

-- insert, delete and update records in prospects

insert into prospects values ('1234567890', 'Steve Stington', '4355556667');
insert into prospects values ('0987654321', 'John Billington', '4354445556');

update prospects
set name = 'John Billsington'
where id = '0987654321';

delete from prospects
where id = '0987654321'

-- verify that your trigger works

select * from marketing_log

-- submit select * from marketing_log log file for grading.


