DECLARE
    i integer;
    j INTEGER;
    ans char(20);
    IS_PRIME CHAR(12);
BEGIN
    ans := '1 NOT PRIME';
    DBMS_OUTPUT.PUT_LINE(ans);
    for i in 2 .. 10 loop
        IS_PRIME := ' PRIME';
        for j in 2 .. i/2 loop
            if  MOD(i,j) = 0 then
                IS_PRIME := ' NOT PRIME';
            end if;
        end loop;
        DBMS_OUTPUT.PUT_LINE(to_char(i) || IS_PRIME);
    end loop;
END;
