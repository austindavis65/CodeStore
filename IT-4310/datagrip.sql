use books;
select * from title_authors;
select * from authors;
select * from titles;
select * from publishers;
select title_authors.au_id, authors.au_fname, authors.au_lname,
       count(*) from title_authors
                join authors on title_authors.au_id = authors.au_id
group by au_id
order by au_id
;

select distinct authors.au_id, authors.au_fname, authors.au_lname
                from authors
join title_authors on title_authors.au_id = authors.au_id
join titles on title_authors.title_id = titles.title_id
where authors.state = 'CA' and titles.type = 'computers'
;
