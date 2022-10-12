1. WHERE
2. IN
3. BETWEEN
4. LIKE
5. %
6. _
Strings should be in 'single quotes';
/*Referencing Table K1 Which represents the world table of countries*/
SELECT population FROM world /*This is the table we are referencing and we are asking specifically for the population 2831741 is what you would get from this query*/
  WHERE name = 'Albania' /*This is the row we are referencing which is selected by askin for the name*/

SELECT name, population FROM world /*This is the row we are referencing which is selected by askin for the name and population*/
  WHERE name IN ('Sweden', 'Norway', 'Denmark');
  /*Asking if any of these names are in the list basically if any of those names are in the list than they will be shown the data asked for that name*/

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
      FROM world
      WHERE name LIKE "Al%" /*This % symbol allows the user to select anything that begins with Al / LIKE is used in conjunction with WHERE to tell it to select names like "Al%"*/
/* The _ symbol can be used to take place of 1 character _ello could return hello*/

Albania	3200000
Algeria	32900000


3. Select the code which shows the countries that end in A or L

SELECT name FROM world
 WHERE name LIKE '%a' OR name LIKE '%l' /*This is using the % sign to fill everything before a and l and then using the OR to select either a or l*/


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

9. Select the code that shows the countries with a population between 10000000 and 20000000

SELECT name, population
  FROM world
 WHERE population BETWEEN 10000000 AND 20000000 /*This is asking for the population to be between 10000000 and 20000000*/


/*SELECT from WORLD tutorial*/
SELECT name, continent, population FROM world /*This is asking for the name, continent, and population from the world table*/

SELECT name, population/area FROM world
  WHERE area > 5000000
SELECT name, population FROM world
  WHERE name = 'France' /*WHERE keyword is used to select a specific row*/
