DECLARE
    CURSOR cust IS
        SELECT custid, custname
            FROM customers
            ORDER BY custid;
    DAY_CUR DECIMAL(10, 2);
    DAY_CUR_TOT DECIMAL(10, 2);
    DAY_30 DECIMAL(10, 2);
    DAY_30_TOT DECIMAL(10, 2);
    DAY_60 DECIMAL(10, 2);
    DAY_60_TOT DECIMAL(10, 2);
    DAY_90 DECIMAL(10, 2);
    DAY_90_TOT DECIMAL(10, 2);
    DAY_TOT DECIMAL(10, 2);
    DAY_TOT_TOT DECIMAL(10, 2);
BEGIN
    DBMS_OUTPUT.PUT_LINE('+------------------------------------------------------------------------------+');
    DBMS_OUTPUT.PUT_LINE('CustID  CustName            CURRENT    31-60      61-90      91+       TOTAL');
    DBMS_OUTPUT.PUT_LINE('+------------------------------------------------------------------------------+');
    DAY_CUR_TOT := 0.00;
    DAY_30_TOT := 0.00;
    DAY_60_TOT := 0.00;
    DAY_90_TOT := 0.00;
    DAY_TOT_TOT := 0.00;
    FOR rec IN cust LOOP
        SELECT NVL(SUM(amount), 0)
            INTO DAY_CUR
            FROM transactions
            WHERE custid = rec.custid AND tdate < CURRENT_DATE AND tdate > CURRENT_DATE - 30
        ;
        DAY_CUR_TOT := DAY_CUR_TOT + DAY_CUR;
        SELECT NVL(SUM(amount), 0)
            INTO DAY_30
            FROM transactions
            WHERE custid = rec.custid AND tdate < CURRENT_DATE - 30 AND tdate > CURRENT_DATE - 60
        ;
        DAY_30_TOT := DAY_30_TOT + DAY_30;
        SELECT NVL(SUM(amount), 0)
            INTO DAY_60
            FROM transactions
            WHERE custid = rec.custid AND tdate < CURRENT_DATE - 60 AND tdate > CURRENT_DATE - 90
        ;
        DAY_60_TOT := DAY_60_TOT + DAY_60;
        SELECT NVL(SUM(amount), 0)
            INTO DAY_90
            FROM transactions
            WHERE custid = rec.custid AND tdate < CURRENT_DATE - 90
        ;
        DAY_90_TOT := DAY_90_TOT + DAY_90;
        SELECT NVL(SUM(amount), 0)
            INTO DAY_TOT
            FROM transactions
            WHERE custid = rec.custid
        ;
        DAY_TOT_TOT := DAY_TOT_TOT + DAY_TOT;
        DBMS_OUTPUT.PUT_LINE(rec.custid || ' ' || RPAD(rec.custname,15) ||
                             TO_CHAR(DAY_CUR, '9999990.00') || 
                             TO_CHAR(DAY_30, '9999990.00') ||
                             TO_CHAR(DAY_60, '9999990.00') ||
                             TO_CHAR(DAY_90, '9999990.00') ||
                             TO_CHAR(DAY_TOT, '9999990.00')
        );
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('+------------------------------------------------------------------------------+');
    DBMS_OUTPUT.PUT_LINE('TOTALS' || '                 ' ||
                         TO_CHAR(DAY_CUR_TOT, '9999990.00') ||
                         TO_CHAR(DAY_30_TOT, '9999990.00') ||
                         TO_CHAR(DAY_60_TOT, '9999990.00') ||
                         TO_CHAR(DAY_90_TOT, '9999990.00') ||
                         TO_CHAR(DAY_TOT_TOT, '9999990.00')
    );
    DBMS_OUTPUT.PUT_LINE('+------------------------------------------------------------------------------+');
END;

