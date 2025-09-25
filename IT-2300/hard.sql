use tax;

SET @target = 'city2';

SELECT taxAuthority
	FROM taxAreaAuthority
	WHERE taxArea = @target AND taxAuthority LIKE 'county_'
	INTO @county;

SELECT taxAuthority
        FROM taxAreaAuthority
        WHERE taxArea = @target AND taxAuthority LIKE 'state_'
        INTO @state;

SELECT @county;
SELECT @state;

SELECT effective
	FROM taxRates
	WHERE taxAuthority = @target AND effective LIKE '1994-__-01'
	INTO @thedate;

SELECT authTaxRate
FROM taxRates
WHERE effective = @thedate
AND taxAuthority = @target
INTO @cityrate;

SELECT authTaxRate
FROM taxRates
WHERE taxAuthority = @county
AND effective <= @thedate
INTO @countyrate;

SELECT authTaxRate
FROM taxRates
WHERE taxAuthority = @state
AND effective = @thedate
INTO @staterate;

SELECT @cityrate;
SELECT @staterate;
SELECT @countyrate;

SELECT ROUND(SUM(@cityrate * @staterate * @countyrate), 2) AS 'Rate';
