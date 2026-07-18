/*
================================================================================
STEP 06: AGGREGATE FUNCTIONS, GROUP BY, AND HAVING
================================================================================
GOAL:
Learn how to summarize many rows into totals, counts, averages, minimums, and
maximums, then organize those summaries using grouping logic.
================================================================================
*/

USE world;

/*
--------------------------------------------------------------------------------
1. WHAT ARE AGGREGATE FUNCTIONS?
--------------------------------------------------------------------------------
- Aggregate functions take many row values and return one summary value.
- They are used for totals, averages, counts, highest values, and lowest values.

COMMON AGGREGATES:
- COUNT()
- SUM()
- AVG()
- MIN()
- MAX()
--------------------------------------------------------------------------------
*/

SELECT COUNT(*) AS total_countries FROM country;

/*
--------------------------------------------------------------------------------
2. COUNT
--------------------------------------------------------------------------------
- COUNT(*) counts all rows
- COUNT(column_name) counts non-NULL values in that column
- COUNT(DISTINCT column_name) counts unique non-NULL values
--------------------------------------------------------------------------------
*/

SELECT COUNT(*) AS total_rows FROM city;
SELECT COUNT(indepyear) AS countries_with_indepyear FROM country;
SELECT COUNT(DISTINCT continent) AS unique_continents FROM country;

/*
--------------------------------------------------------------------------------
3. SUM, AVG, MIN, MAX
--------------------------------------------------------------------------------
- SUM adds numeric values
- AVG finds average numeric value
- MIN finds lowest value
- MAX finds highest value
--------------------------------------------------------------------------------
*/

SELECT SUM(population) AS total_population FROM country;
SELECT AVG(population) AS avg_population FROM country;
SELECT MIN(population) AS min_population FROM country;
SELECT MAX(population) AS max_population FROM country;

/*
--------------------------------------------------------------------------------
4. NULL BEHAVIOR IN AGGREGATES
--------------------------------------------------------------------------------
- Most aggregate functions ignore NULL values
- COUNT(*) still counts rows even if some columns are NULL
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
5. GROUP BY
--------------------------------------------------------------------------------
- GROUP BY splits rows into groups that share the same value
- Aggregate functions then work inside each group
--------------------------------------------------------------------------------
*/

SELECT continent, COUNT(*) AS total_countries
FROM country
GROUP BY continent;

SELECT countrycode, SUM(population) AS total_city_population
FROM city
GROUP BY countrycode;

/*
--------------------------------------------------------------------------------
6. GROUP BY WITH MULTIPLE COLUMNS
--------------------------------------------------------------------------------
- You can group by more than one column
- Each unique combination becomes one group
--------------------------------------------------------------------------------
*/

SELECT countrycode, district, COUNT(*) AS total_cities
FROM city
GROUP BY countrycode, district;

/*
--------------------------------------------------------------------------------
7. RULE OF GROUP BY
--------------------------------------------------------------------------------
- Every selected column must either:
  1. be inside an aggregate function
  2. or appear in GROUP BY
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
8. HAVING
--------------------------------------------------------------------------------
- HAVING filters grouped results
- WHERE filters rows before grouping
- HAVING runs after GROUP BY
--------------------------------------------------------------------------------
*/

SELECT continent, COUNT(*) AS total_countries
FROM country
GROUP BY continent
HAVING COUNT(*) > 10;

SELECT countrycode, SUM(population) AS total_city_population
FROM city
GROUP BY countrycode
HAVING SUM(population) > 1000000;

/*
--------------------------------------------------------------------------------
9. WHERE VS HAVING
--------------------------------------------------------------------------------
WHERE:
- filters rows
- runs before grouping
- cannot use aggregate logic directly

HAVING:
- filters groups
- runs after grouping
- commonly uses COUNT, SUM, AVG, MIN, MAX
--------------------------------------------------------------------------------
*/

SELECT continent, AVG(population) AS avg_population
FROM country
WHERE population > 1000000
GROUP BY continent
HAVING AVG(population) > 5000000;

/*
--------------------------------------------------------------------------------
10. ORDER BY WITH AGGREGATES
--------------------------------------------------------------------------------
- You can sort grouped results using aggregate values or aliases
--------------------------------------------------------------------------------
*/

SELECT continent, COUNT(*) AS total_countries
FROM country
GROUP BY continent
ORDER BY total_countries DESC;

/*
--------------------------------------------------------------------------------
11. DISTINCT VS GROUP BY
--------------------------------------------------------------------------------
DISTINCT:
- removes duplicate rows from selected columns

GROUP BY:
- forms groups and supports aggregate calculations
--------------------------------------------------------------------------------
*/

SELECT DISTINCT continent FROM country;

/*
--------------------------------------------------------------------------------
12. EXECUTION ORDER FOR GROUPED QUERY
--------------------------------------------------------------------------------
1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY
7. LIMIT
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
13. COMMON MISTAKES
--------------------------------------------------------------------------------
1. Using aggregate function in WHERE
2. Forgetting non-aggregate columns in GROUP BY
3. Confusing DISTINCT with GROUP BY
4. Expecting HAVING to replace WHERE always
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
14. BEST PRACTICES
--------------------------------------------------------------------------------
1. Filter early with WHERE when possible
2. Use HAVING only for grouped filters
3. Alias aggregate columns for readability
4. Order grouped reports clearly
--------------------------------------------------------------------------------
*/

/*
================================================================================
SUMMARY
================================================================================
- Aggregate functions summarize many rows
- GROUP BY forms groups
- HAVING filters groups
- WHERE filters rows before grouping
================================================================================
*/
