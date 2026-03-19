show databases;
use books;
select type, count(*) from titles group by type;
