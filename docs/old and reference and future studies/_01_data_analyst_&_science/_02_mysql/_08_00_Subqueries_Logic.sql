/*
================================================================================
STEP 08: SUBQUERIES AND CONDITIONAL LOGIC
================================================================================
GOAL:
Learn how to write queries inside queries and use SQL logic constructs like CASE,
IF, EXISTS, ANY, and ALL.
================================================================================
*/

USE world;

/*
--------------------------------------------------------------------------------
1. WHAT IS A SUBQUERY?
--------------------------------------------------------------------------------
- A subquery is a query inside another query
- Inner query runs first, outer query uses its result
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
2. SINGLE-ROW SUBQUERY
--------------------------------------------------------------------------------
- Returns one value
- Often used with =, >, <, >=, <=
--------------------------------------------------------------------------------
*/

SELECT name, population
FROM city
WHERE population > (
    SELECT population
    FROM city
    WHERE name = 'Kabul'
);

/*
--------------------------------------------------------------------------------
3. MULTI-ROW SUBQUERY
--------------------------------------------------------------------------------
- Returns multiple values
- Common operators: IN, ANY, ALL
--------------------------------------------------------------------------------
*/

SELECT name
FROM country
WHERE code IN (
    SELECT countrycode
    FROM city
    WHERE population > 5000000
);

/*
--------------------------------------------------------------------------------
4. CORRELATED SUBQUERY
--------------------------------------------------------------------------------
- Inner query depends on outer query row
- Runs per outer row logically
--------------------------------------------------------------------------------
*/

SELECT c.name
FROM country c
WHERE EXISTS (
    SELECT 1
    FROM city x
    WHERE x.countrycode = c.code
);

/*
--------------------------------------------------------------------------------
5. EXISTS AND NOT EXISTS
--------------------------------------------------------------------------------
- EXISTS checks whether subquery returns at least one row
- NOT EXISTS checks whether subquery returns no rows
--------------------------------------------------------------------------------
*/

SELECT c.name
FROM country c
WHERE NOT EXISTS (
    SELECT 1
    FROM city x
    WHERE x.countrycode = c.code
);

/*
--------------------------------------------------------------------------------
6. ANY AND ALL
--------------------------------------------------------------------------------
- > ANY means greater than at least one value
- < ALL means less than every value
--------------------------------------------------------------------------------
*/

SELECT name, population
FROM country
WHERE population > ANY (
    SELECT population
    FROM country
    WHERE continent = 'North America'
);

/*
--------------------------------------------------------------------------------
7. SECOND HIGHEST VALUE PATTERN
--------------------------------------------------------------------------------
- Subqueries are common for nth highest logic
--------------------------------------------------------------------------------
*/

SELECT MAX(population) AS second_highest_population
FROM country
WHERE population < (
    SELECT MAX(population)
    FROM country
);

/*
--------------------------------------------------------------------------------
8. CASE EXPRESSION
--------------------------------------------------------------------------------
- CASE adds if-then-else style logic in SQL
--------------------------------------------------------------------------------
*/

SELECT
    name,
    population,
    CASE
        WHEN population >= 100000000 THEN 'very_high'
        WHEN population >= 10000000 THEN 'high'
        ELSE 'other'
    END AS population_group
FROM country;

/*
--------------------------------------------------------------------------------
9. IF FUNCTION
--------------------------------------------------------------------------------
- IF(condition, value_if_true, value_if_false)
- MySQL shortcut for simple conditional output
--------------------------------------------------------------------------------
*/

SELECT
    name,
    IF(indepyear IS NULL, 'unknown', 'available') AS indep_status
FROM country;

/*
--------------------------------------------------------------------------------
10. SUBQUERY VS JOIN
--------------------------------------------------------------------------------
- Many subquery problems can also be solved with joins
- Choose based on readability and logic clarity
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
11. COMMON MISTAKES
--------------------------------------------------------------------------------
1. Using = with multi-row subquery
2. Returning more than one row from a single-row subquery
3. Confusing EXISTS with IN
4. Writing slow correlated subqueries without reason
--------------------------------------------------------------------------------
*/

/*
================================================================================
SUMMARY
================================================================================
- Subqueries can return one value or many values
- EXISTS, ANY, ALL support advanced filtering
- CASE and IF provide conditional result logic
================================================================================
*/
