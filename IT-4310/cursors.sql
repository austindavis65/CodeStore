declare
    comments varchar(20);
    empname varchar(20);
    cursor cur_emp IS
        select empsales.emp_id, employees.emp_name, empsales.sales
        from employees
        right join empsales on empsales.emp_id = employees.emp_id;
begin
    for v_emp_record in cur_emp loop
        if v_emp_record.sales >= 0 and v_emp_record.sales < 401 then
            comments := 'Poor Sales';
        elsif v_emp_record.sales >= 401 and v_emp_record.sales < 601 then
            comments := 'Average Sales';
        elsif v_emp_record.sales >= 601 then
            comments := 'Great Sales';
        end if;
        if v_emp_record.emp_name is not null then
            empname := v_emp_record.emp_name;
        else
            empname := '???';
        end if;
        dbms_output.PUT_LINE(v_emp_record.emp_id || ' ' || '-' || ' '
            || empname || ' ' || v_emp_record.sales || ' ' || comments);
        end loop;
end;



