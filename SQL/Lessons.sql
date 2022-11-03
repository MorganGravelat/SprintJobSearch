1. WHERE
2. IN
3. BETWEEN
4. AND/OR/NOT|!=
4_2. LIKE
5. %
6. _
7. *
8. DISTINCT
9. COUNT()
10.ORDER BY ASC/DESC
11. LIMIT

Strings should be in 'single quotes';
/*Referencing Table K1 Which represents the world table of countries*/
SELECT population FROM world /*This is the table we are referencing and we are asking specifically for the population 2831741 is what you would get from this query*/
  WHERE name = 'Albania' /*This is the row we are referencing which is selected by askin for the name*/

SELECT name, population FROM world /*This is the row we are referencing which is selected by askin for the name and population*/
  WHERE name IN ('Sweden', 'Norway', 'Denmark');
  /*Asking if any of these names are in the list basically if any of those names are in the list than they will be shown the data asked for that name*/

SELECT color FROM table
WHERE color IN('red','blue','green')

SELECT * FROM payment
WHERE amount IN (0.99, 1.98, 1.99); /*Returns 3301 rows of payments where amount of payment is one of those amounts*/
/*Could use NOT IN to get the opposite*/

SELECT * FROM customer
WHERE first_name IN ('John','Jake','Julie');


SELECT * FROM customer
WHERE first_name ILIKE 'j%' AND last_name ILIKE 's%'; /*Could give Julie Sanchez ILIKE is case insensitive*/


SELECT name, area FROM world
  WHERE area BETWEEN 250000 AND 300000 /*This is asking for the name and area of the world table and asking for the area to be between 250000 and 300000*/
/*This is going to display the name and area of any country whos area is between those two numbers on the world table.*/

/*QUIZ*/
1. Select the code which produces this table
name	population
Bahrain	1234571
Swaziland	1220000
Timor-Leste	1066409

SELECT name, population
  FROM world
 WHERE population BETWEEN 1000000 AND 1250000 /*Between method shown above*/

2. Pick the result you would obtain from this code:

      SELECT name, population
      FROM worlda
      WHERE name LIKE "Al%" /* 5  This % symbol allows the user to select anything that begins with Al / LIKE is used in conjunction with WHERE to tell it to select names like "Al%"*/
/* 6  The _ symbol can be used to take place of 1 character _ello could return hello*/

Albania	3200000
Algeria	32900000


3. Select the code which shows the countries that end in A or L

SELECT name FROM world
 WHERE name LIKE '%a' OR name LIKE '%l' /*This is using the % sign to fill everything before a and l and then using the OR to select either a or l*/

SELECT COUNT(*) FROM customer
WHERE first_name LIKE '%e' /* Drake Belle and Eve have e at the end and satisfy the LIKE condition */
WHERE name like '_her%'; /* This can return C_her%yl T_her%esa S_her%ri etc.*/
SELECT * FROM film
WHERE title LIKE 'Airport Po_lock';

SELECT * FROM film
WHERE title ILIKE '%Truman%'

4. Pick the result from the query
SELECT name,length(name) /*This is asking for the length of the name after displaying the name*/
FROM world
WHERE length(name)=5 and region='Europe'


name	length(name)
Italy	5
Malta	5
Spain	5

5. Here are the first few rows of the world table:


name	region	area	population	gdp
Afghanistan	South Asia	652225	26000000
Albania	Europe	28728	3200000	6656000000
Algeria	Middle East	2400000	32900000	75012000000
Andorra	Europe	468	64000
...
SELECT name, area*2 FROM world WHERE population = 64000 /*You can ask for the area * 2 as a column in the table*/
RESULT: Andorra	936

6. Select the code that would show the countries with an area larger than 50000 and a population smaller than 10000000

SELECT name, area, population
FROM world
WHERE area > 50000 AND population < 10000000

7. Select the code that shows the population density of China, Australia, Nigeria and France
SELECT name, population/area
  FROM world
 WHERE name IN ('China', 'Nigeria', 'France', 'Australia') /*This is asking for areas that have the name of China, Nigeria, France, and Australia*/


8. Select the code that shows the countries with a population density greater than 100

SELECT name, population/area
  FROM world
 WHERE population/area > 100 /*This is asking for the population/area to be greater than 100*/

SELECT * FROM customer
WHERE first_name='Jared';

9. Select the code that shows the countries with a population between 10000000 and 20000000

SELECT name, population
  FROM world
 WHERE population BETWEEN 10000000 AND 20000000 /*This is asking for the population to be between 10000000 and 20000000*/

SELECT name, choice FROM table
WHERE name = 'David' AND choice = 'A' /*This is asking for the name and choice to be David and A*/
/*SELECT from WORLD tutorial*/
SELECT name, continent, population FROM world /*This is asking for the name, continent, and population from the world table*/

SELECT COUNT(title) FROM film /*This is asking for the count of the title column in the film table who meet this criteria below*/
WHERE rental_rate > 4 AND replacement_cost <= 19.99
AND rating='R'; /*This is asking for the rental rate to be greater than 4 and the replacement cost to be less than or equal to 19.99 and the rating to be R*/

SELECT name, population/area FROM world
  WHERE area > 5000000 AND NOT population > 25000000 /*This is asking for the name, population/area from the world table and asking for the area to be greater than 5000000 and the population to be less than 25000000*/

SELECT name, population FROM world
  WHERE name = 'France' /*WHERE keyword is used to select a specific row*/

SELECT name , region
  FROM world

  WHERE area < 2000
    AND gdp > 5000000000


/* 7  Say you weant everything * keyword */
SELECT * FROM world /*This is asking for everything from the world table*/

/* 8  DISTINCT KEYWORD*/
SELECT DISTINCT column FROM table /* This shows how to use DISTINCT to get any data that is unique from a tables column such as unique first names*/
SELECT DISTINCT(rental_rate) FROM film; /*This is asking for the unique rental rates from the film table*/
/* DISTINCT will remove multiple of any first name and might cancel out multiple people named david*/
/* if you wanted to find the ratings in the dvdrental database */
SELECT COUNT(rating) FROM film; /* 1000 ratings are in the 1000 films on the dvdrental database*/
SELECT COUNT(DISTINCT rating) FROM film; /*  This is asking for the count of unique ratings in the film table which are 5*/

SELECT count(DISTINCT(district)) FROM address/* Shows a count of all the unique districts */


SELECT COUNT(title) FROM film
WHERE rental_rate > 4 AND replacement_cost <= 19.99
AND rating != 'R'; /*This is another way to say NOT  the other way is AND rating NOT 'R';*/

SELECT first_name
FROM customer
ORDER BY first_name ASC; /*This is asking for the first name from the customer table and ordering it by first name*/

SELECT first_name
FROM customer
ORDER BY first_name; /*ASC is default for ORDER BY*/

/* 9  ORDER BY DESCENDING*/
SELECT store_id,first_name,last_name
FROM customer
ORDER BY store_id DESC;

/* 10  ORDER BY MULTIPLE COLUMNS*/
SELECT store_id,first_name,last_name
FROM customer
ORDER BY store_id,first_name;

SELECT store_id,first_name,last_name
FROM customer
ORDER BY store_id DESC,first_name ASC; /*This is asking for the store_id, first_name, and last_name from the customer table and ordering it by store_id descending and first_name ascending*/
SELECT first_name,last_name
FROM customer
ORDER BY store_id DESC,first_name ASC; /*You do not need store_id to be displayed to order by it */

/* 11  LIMIT*/
SELECT customer_id FROM payment
ORDER BY payment_date
LIMIT 10; /*This is asking for the top 10 payments from the payment table and ordering them by payment date ascending*/

/* 12  BETWEEN*/

SELECT title FROM film
WHERE length BETWEEN 50 AND 100 /*This is asking for the title from the film table and asking for the length to be between 50 and 100*/
/* length >= 50 AND length <= 100*/
/* You can also do dates with BETWEEN*/
WHERE date BETWEEN '2007-01-01' AND '2007-02-01' /*This is asking for the date to be between 2007-01-01 and 2007-02-01*/
/* You will need to be careful when using BETWEEN aand >= <=*/
SELECT * FROM payment
WHERE payment_date BETWEEN '2007-02-01' AND '2007-02-15';



/* Common Aggregate Functions */
    AVG() - Returns the average value /*returns flaoting point value many decimal places */
    COUNT() - Returns the number of rows /*returns integer value */
    MAX() - Returns the largest value
    MIN() - Returns the smallest value
    SUM() - Returns the sum
/* Aggregate fgunction calls happen only in the SELECT clause or the HAVING clause */
