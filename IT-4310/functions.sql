CREATE OR REPLACE FUNCTION get_sal
  (p_id IN employees.emp_id%TYPE) RETURN varchar2 IS
   v_name empsales.sales%TYPE := NULL;
BEGIN
   SELECT sales INTO v_name
   FROM empsales WHERE emp_id = p_id;
   RETURN v_name;
EXCEPTION
   WHEN NO_DATA_FOUND THEN RETURN NULL;
END get_sal;
/

BEGIN
   DBMS_OUTPUT.PUT_LINE('E01 - ' || get_sal('E01'));
   DBMS_OUTPUT.PUT_LINE('E99 - ' || get_sal('E99'));
END;



