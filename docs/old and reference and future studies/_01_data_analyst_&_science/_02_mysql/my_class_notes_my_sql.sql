-- rdbms or dbms->database management system
-- ddl(data definition language)->create,alter,drop,truncate,rename
-- dml(data manipulation lang)->insert,update,delete
-- drl/dql(data retrieval lang/date query lang)->select
-- tcl(transaction control lang)->commit,rollback,save point
-- dcl(data control lang)->grant,revoke(XXXXXXXXXXXXXXX)
-- stored function, stored procedure, triggers
-- *********************************************************
-- sql->structured query language
-- rows,cols
-- *********************************************************
-- create database
-- create database _name,drop database _name
-- create database if not exists _name
create database student;
use student;
create database if not exists student;
drop database student;
create database chuma;
use chuma;
drop database chuma;
-- *********************************************************
-- table
-- create table
create table dets (sno int, name varchar(50));
use world;
describe country;
create table if not exists dets (sno int, name varchar(50));
-- *********************************************************
-- data types
-- numeric->tinyint,smallint,mediumint,int,bigint,float,double,decimal
-- text->char(),varchar(),blog,mediumtext,mediumblog,longtext,longblog,text
-- date/time->date,datetime,timestamp,time

--  String Data Types
-- Data type	Description
-- CHAR(size)	A FIXED length string (can contain letters, numbers, and special characters). The size parameter specifies the column length in characters - can be from 0 to 255. Default is 1
-- VARCHAR(size)	A VARIABLE length string (can contain letters, numbers, and special characters). The size parameter specifies the maximum column length in characters - can be from 0 to 65535
-- BINARY(size)	Equal to CHAR(), but stores binary byte strings. The size parameter specifies the column length in bytes. Default is 1
-- VARBINARY(size)	Equal to VARCHAR(), but stores binary byte strings. The size parameter specifies the maximum column length in bytes.
-- TINYBLOB	For BLOBs (Binary Large OBjects). Max length: 255 bytes
-- TINYTEXT	Holds a string with a maximum length of 255 characters
-- TEXT(size)	Holds a string with a maximum length of 65,535 bytes
-- BLOB(size)	For BLOBs (Binary Large OBjects). Holds up to 65,535 bytes of data
-- MEDIUMTEXT	Holds a string with a maximum length of 16,777,215 characters
-- MEDIUMBLOB	For BLOBs (Binary Large OBjects). Holds up to 16,777,215 bytes of data
-- LONGTEXT	Holds a string with a maximum length of 4,294,967,295 characters
-- LONGBLOB	For BLOBs (Binary Large OBjects). Holds up to 4,294,967,295 bytes of data
-- ENUM(val1, val2, val3, ...)	A string object that can have only one value, chosen from a list of possible values. You can list up to 65535 values in an ENUM list. If a value is inserted that is not in the list, a blank value will be inserted. The values are sorted in the order you enter them
-- SET(val1, val2, val3, ...)	A string object that can have 0 or more values, chosen from a list of possible values. You can list up to 64 values in a SET list

-- Numeric Data Types
-- Data type	Description
-- BIT(size)	A bit-value type. The number of bits per value is specified in size. The size parameter can hold a value from 1 to 64. The default value for size is 1.
-- TINYINT(size)	A very small integer. Signed range is from -128 to 127. Unsigned range is from 0 to 255. The size parameter specifies the maximum display width (which is 255)
-- BOOL	Zero is considered as false, nonzero values are considered as true.
-- BOOLEAN	Equal to BOOL
-- SMALLINT(size)	A small integer. Signed range is from -32768 to 32767. Unsigned range is from 0 to 65535. The size parameter specifies the maximum display width (which is 255)
-- MEDIUMINT(size)	A medium integer. Signed range is from -8388608 to 8388607. Unsigned range is from 0 to 16777215. The size parameter specifies the maximum display width (which is 255)
-- INT(size)	A medium integer. Signed range is from -2147483648 to 2147483647. Unsigned range is from 0 to 4294967295. The size parameter specifies the maximum display width (which is 255)
-- INTEGER(size)	Equal to INT(size)
-- BIGINT(size)	A large integer. Signed range is from -9223372036854775808 to 9223372036854775807. Unsigned range is from 0 to 18446744073709551615. The size parameter specifies the maximum display width (which is 255)
-- FLOAT(size, d)	A floating point number. The total number of digits is specified in size. The number of digits after the decimal point is specified in the d parameter. This syntax is deprecated in MySQL 8.0.17, and it will be removed in future MySQL versions
-- FLOAT(p)	A floating point number. MySQL uses the p value to determine whether to use FLOAT or DOUBLE for the resulting data type. If p is from 0 to 24, the data type becomes FLOAT(). If p is from 25 to 53, the data type becomes DOUBLE()
-- DOUBLE(size, d)	A normal-size floating point number. The total number of digits is specified in size. The number of digits after the decimal point is specified in the d parameter
-- DOUBLE PRECISION(size, d)	 
-- DECIMAL(size, d)	An exact fixed-point number. The total number of digits is specified in size. The number of digits after the decimal point is specified in the d parameter. The maximum number for size is 65. The maximum number for d is 30. The default value for size is 10. The default value for d is 0.
-- DEC(size, d)	Equal to DECIMAL(size,d)
-- Note: All the numeric data types may have an extra option: UNSIGNED or ZEROFILL. If you add the UNSIGNED option, MySQL disallows negative values for the column. If you add the ZEROFILL option, MySQL automatically also adds the UNSIGNED attribute to the column.

-- Date and Time Data Types
-- Data type	Description
-- DATE	A date. Format: YYYY-MM-DD. The supported range is from '1000-01-01' to '9999-12-31'
-- DATETIME(fsp)	A date and time combination. Format: YYYY-MM-DD hh:mm:ss. The supported range is from '1000-01-01 00:00:00' to '9999-12-31 23:59:59'. Adding DEFAULT and ON UPDATE in the column definition to get automatic initialization and updating to the current date and time
-- TIMESTAMP(fsp)	A timestamp. TIMESTAMP values are stored as the number of seconds since the Unix epoch ('1970-01-01 00:00:00' UTC). Format: YYYY-MM-DD hh:mm:ss. The supported range is from '1970-01-01 00:00:01' UTC to '2038-01-09 03:14:07' UTC. Automatic initialization and updating to the current date and time can be specified using DEFAULT CURRENT_TIMESTAMP and ON UPDATE CURRENT_TIMESTAMP in the column definition
-- TIME(fsp)	A time. Format: hh:mm:ss. The supported range is from '-838:59:59' to '838:59:59'
-- YEAR	A year in four-digit format. Values allowed in four-digit format: 1901 to 2155, and 0000. 
-- MySQL 8.0 does not support year in two-digit format.
-- *********************************************************
-- insert into table
insert into det values(1,'rajasekar');
insert into det(sno,name) values(2,'sekar');
--  can insert null values
-- *************************************************************
-- rename table
rename table dets to det;
-- *******************************************************
-- constraints
-- not null, unique, primary key, forigen key, check, default, auto increment
use student;
-- not null
drop table stud1;
create table stud1 (sno int not null, sname varchar(10), marks int);
insert into stud1 values(101,'raj',100);
insert into stud1 values(null,'raj',100); -- error
-- ********************************************************************
-- unique
alter table stud1 add (phone varchar(10) unique);
alter table stud1 add unique (sno,sname);
describe stud1; 
insert into stud1 values(102,'sekar',100,'1234');
insert into stud1 values(102,'sekar',100,'1234'); -- unique error
-- ********************************************************************
-- primary key, combination of unique and not null
-- it wont allow dupllicate or null
create table stud2 (sno int primary key,sname text,mark int);
create table stud2 (sno int, sname text, mark int, primary key (sno));
insert into stud2 values(101,'raja',100);
insert into stud2 values(101,'raja',100);
insert into stud2 values(null,'sekar',90);
-- composite primary key is create primary key on combination of two columns
-- it can be applied only at table level
create table stud3 (sno int, class int,sname text, mark int,
primary key(sno,class));
-- ********************************************************************
-- index-> used to retrieve data from database very fast.
-- user cant see indexes, they are just used to speed up search/queries.
use student;
create index stud_id on stud1(sname);
drop index stud_id on stud1;
select *from stud1;
-- ********************************************************************
-- foregien key->link two table
-- it is field in one table refers to the primary key in another table
-- table with forigen key is child and table with primary is parent
use student;
create table school (sno int primary key, sname text, mark int);
insert into school values(101,'raj',100);
insert into school values(102,'raja',90);
insert into school values(103,'sekar',80);
select * from school;
create table libary(sno int ,foreign key(sno) references school(sno),book varchar(10));
insert into libary values(102,'java');
insert into libary values(108,'c++');
insert into libary values(null,'. net');
select * from libary;
delete from school where sno=102;
delete from libary where sno=102; -- after deleting this data it is possible to delete the parent data
-- cant delete parent table details because of forgien key
-- have to delete child table row of detail then only can delete parent table row
-- ********************************************************************
-- on delete cascade ->can delete the rows from parent table and corresponding child table row as well
create table school2 (sno int primary key, sname text, mark int);
insert into school2 values(101,'raj',100);
insert into school2 values(102,'raja',90);
insert into school2 values(103,'sekar',80);
select * from school2;
create table libary2(sno int ,foreign key(sno) references school2(sno) on delete cascade,book varchar(10));
insert into libary2 values(102,'java');
insert into libary2 values(101,'. net');
select * from libary2;
delete from school2 where sno=102;
-- ********************************************************************
-- check
create table stud3(sno int, sname text, mark int check(mark between 50 and 100), city text check(city in('pondy','chennai')));
insert into stud3 values(101,'raj',90,'pondy');
insert into stud3 values(101,'raj',40,'pondy');
insert into stud3 values(101,'raj',90,'cuddaore');
-- ********************************************************************
-- default
create table orders (id int,orno int, order_date datetime default now());
insert into orders(id,orno) values(1,123);
select *from orders;
-- ********************************************************************
-- auto increment
create table stud4 (sno int primary key auto_increment,sname text, mark int);
-- if auto_increment is not given it will start from defalut 1 can't define in create table
alter table stud4 auto_increment=101;
drop table stud4;
insert into stud4 (sname,mark) values('raj',100);
insert into stud4 (sname,mark) values('sekar',90);
select *from stud4;
delete from stud4 where sno=102;
insert into stud4 (sname,mark) values('raja',90);
-- if some data is delete also it will auto increment the sno.
-- *********************************************************************
-- views
create view country_dup as select name,code,gnp from country; 
select * from country_dup;
drop view country_dup;
-- ********************************************************************
-- select table 
use world;
select *from country;
select continent from country;
select code,name,gnp+gnpold,surfacearea+1.5 from country;
-- as
USE WORLD;
SELECT GNP AS SOMETHING, CODE AS CD FROM COUNTRY;
-- *************************************************************************
--  uncheck the safe

set sql_safe_updates=0;
-- update
set sql_safe_updates=0;
select *from country;
update country set surfacearea=345.56 where name="aruba";
update country set surfacearea=193.00,indepyear=1996 where name="aruba";
update country set indepyear=null where name="aruba";
-- *****************************************************************************
-- alter-> add column, drop colum, modifying colum, rename column
-- add new column into table
alter table det add(data1 int);
-- drop column from table
alter table det drop column _col_name;
-- modifying column (increase/decrese size, can decrease only the data fit to the new size, column should be empty to change datatype)
alter table det modify column name varchar(50);
-- rename column
alter table det rename column name to sname;
-- alter first or after
use world;
select *from world.country;
ALTER TABLE world.country
ADD poda varchar(100) NOT NULL  
AFTER code,
ADD podi int(100) NOT NULL  
AFTER name ;  
-- alter drop column
ALTER TABLE world.country  
DROP COLUMN poda;  
ALTER TABLE world.country
ADD poda varchar(100) NOT NULL  
first ;
select *from world.country;
-- alter rename column
 ALTER TABLE  cus_tbl  
CHANGE COLUMN cus_surname cus_title  
varchar(20) NOT NULL;  
-- *****************************************************************************
-- to use rollback
set autocommit=0;
-- delete & truncate
-- The DELETE command is used to delete particular records from a table. The TRUNCATE command is used to delete the complete data from the table
-- can rollback with delete
delete from country;
commit;
select *from country;
delete from country where sno=2;
-- rollback
rollback;
commit;
-- *****************************************************************************
-- truncate
-- cant rollback with truncate
truncate table det;
-- *****************************************************************************
-- drop table
drop table det;
-- **************************************************
-- filtering
select *from country;
select * from country where surfacearea>200;
select *from country where gnp<=1000;
select *from country where gnpold=584;
select *from country where gnpold is null;
select *from country where gnpold is not null;
select *from country where code='ago';
select distinct region from country;
select distinct* from country;
-- *****************************************************************************
-- logical operator(and,or,not)
select *from country where lifeexpectancy>50 and gnp<500;
select *from country where population>10000 or indepyear is not null;
select *from country where not region='Caribbean';
-- *****************************************************************************
-- operators
-- +	Add	
-- -	Subtract	
-- *	Multiply	
-- /	Divide	
-- %	Modulo	
-- &	Bitwise AND
-- |	Bitwise OR
-- ^	Bitwise exclusive OR
-- =	Equal to	
-- >	Greater than	
-- <	Less than	
-- >=	Greater than or equal to	
-- <=	Less than or equal to	
-- <>	Not equal to
-- *****************************************************************************
-- between & in
select *from country where data1 between 10 and 50;
select *from country where data1 not between 10 and 50;
select *from country where data2 in(30,40);
select *from country where data2 not in (10,50);
-- *****************************************************************************
-- pattern matching operators
-- %->many characters, _ ->single character
select *from country where name like 'r%';
select *from country where name like '%r';
select *from country where name like 'r%r';
select *from country where name like '%j%'; -- rajasekar
select *from country where name not like 'S%';-- Sekar
select *from country where name like '%a_';-- rajasekar
select *from country where name like '______';
-- *****************************************************************************
-- functions
-- string functions, numeric function, date func, aggregate function
-- string functions
select upper(name) from country;
select lower(name) from country;
select length(name) from country;
select *from country where length(name)=5;
select trim(name) from country;
select trim('_' from '_fasf_');
select trim('_' from name) from country;
select instr('rajasekar','r');
select instr(name,'r') from country;
select substr('oracle',2,3);
select substr('oracle',3,3);
select substr('oracle',4,3);
select substring('oracle',2,3);
select concat(name,data1) from country;

-- numberic functions
select abs(-40);
select abs(40);
select sqrt(25);
select mod(10,3);
select power(2,3);
select truncate(40.32423,3);
select truncate(6876,-1);
select truncate(6876,-2);
select truncate(34534523,-5);
select greatest(100,200,300);
select least(100,200,300);

-- date function

-- DATE - format YYYY-MM-DD
-- DATETIME - format: YYYY-MM-DD HH:MI:SS
-- TIMESTAMP - format: YYYY-MM-DD HH:MI:SS
-- YEAR - format YYYY or YY

select curdate();
select current_date();
select curtime();
select current_time();
select now();
select sysdate();
select month("1996-08-19");
select day("1996-08-19");
select year("1996-08-19");
select *from country where year(yr)='1996';
select *from country where monthname(mon)='june';
SELECT * FROM Orders WHERE OrderDate='2008-11-11';

-- aggregate function
select avg(salary) from country;
select sum(salary) from country;
select min(salary) from country;
select max(salary) from country;
select count(*) from country;
-- *****************************************************************************
-- group by
-- group by clause groups records into summary rows
-- group by returns one records for each group
-- group by typically also involves aggregates, count, max,...
-- group by can group by one or more columns
use world;
select Id,Name,district from city group by id;
select countrycode,sum(population) from city group by countrycode;
select district,avg(population) from city group by district;
select region,max(population),min(population) from country group by region;
select countrycode,count(*) from city group by countrycode;
select countrycode,district,count(*) from city group by countrycode,district;
-- *****************************************************************
-- having is used to filter from group by 
-- order of execution
-- select __ from ____ where->group by->having->order by
select countrycode,count(*) from city group by countrycode having count(*)>2;
select countrycode,count(*) from city group by countrycode having sum(population)>200000;
select countrycode,count(*) from city where id>30 group by countrycode having sum(population)>200000;
-- *****************************************************************
-- order by
USE WORLD;
SELECT * FROM city;
select *from city order by countrycode desc;
select *from city order by district;
select * from city order by id desc;
select *from city order by name asc, id desc;
-- *****************************************************************************
-- union,union all,intersect, minus
use student;
create table if not exists a(sname varchar(10),num int(2));
create table if not exists b(num int(2),grade varchar(3));
insert into a values('abc',10);
insert into a values('xyz',11);
insert into a values('pqr',12);
insert into a values('mno',14);
commit;
insert into b values(11,'a');
insert into b values(12,'b');
insert into b values(13,'c');
insert into b values(15,'b');
commit;
select * from a;
select *from b;
select num from a union select num from b;
select num from a union all select num from b;
-- intersect,minus not support in mysql
-- *****************************************************************************
-- join
-- equi join/inner join/simple join,right join,left join,full join,self join
select * from a inner join b on a.num=b.num;
select * from a left outer join b on a.num=b.num;
select * from a right outer join b on a.num=b.num;
select * from a right outer join b on a.num=b.num;
select * from a join b on a.num=b.num;
select * from a join b;
select * from a cross join b;-- combination of left and right join
select * from a,b;-- self join
select a.num as anum , b.num as bnum from a,b where a.num;
select a.num as anum , b.num as bnum from a,b where a.num=b.num;
-- full outer join not supported in mysql
-- *****************************************************************************
-- sub queries
-- outer query, inner query
-- single row sub query(<=,>=,!=), multi row sub query(in,any,all)
use world;
select population from city where district='Kabol';
select population from city where population<1780000;
-- inner query(outer query)
select name,population from city where population<(select population from city where district='Kabol');
-- 2nd high population
use world;
select (population) from country;
select max(population) from country;
select (population) from country where population<(select max(population) from country);
select max(population) from country where population<(select max(population) from country);
-- 3rd highest population
select max(population) from country where population<(select max(population) from country where population <(select max(population) from country));

-- polution more than that of a particulation code
select population from country where code='ABW';
select population from country where population >(select population from country where code='ABW');

-- subquery in,any,all

-- display region with same continent
select * from country where population in (select population from country where continent='North America');
-- display the country whose population is greater than at least on country in contient name
select * from country where population >any (select population from country where continent='North America');
-- display the country whose population is less than at least on country in contient name
select * from country where population <all (select population from country where continent='North America');

-- EXISTS
-- The EXISTS operator returns TRUE if the subquery returns one or more records.
select * from country where population <EXISTS (select population from country where continent='North America');
-- *****************************************************************************
-- CASE
SELECT CODE, NAME,
CASE
    WHEN GNP > 30 THEN 'The quantity is greater than 30'
    WHEN GNP < 30 THEN 'The quantity is 30'
    ELSE 'The quantity is under 30'
END AS GNP
FROM COUNTRY;

SELECT NAME, REGION, CONTINENT
FROM COUNTRY
ORDER BY
(CASE
    WHEN REGION IS NULL THEN CONTINENT
    ELSE REGION
END);
-- *****************************************************************************
-- IFNULL
use world;
SELECT NAME, GNP + (IFNULL(GNPOLD,0))FROM COUNTRY;
SELECT NAME, GNP + (coalesce(GNPOLD,0))FROM COUNTRY;
-- *****************************************************************************
-- limit
use world;
select * from country limit 5;
select * from country limit 5,10;
-- *****************************************************************************
-- show,describe,set,explain

-- show database
show databases;
use world;

-- show tables
show tables from world;
SHOW FULL TABLES; 
 SHOW TABLES FROM mystudentdb LIKE "stud%";  
 
 -- show column
 SHOW COLUMNS FROM mytable_name FROM mydb_name;  
 SHOW COLUMNS FROM student_info LIKE 's%';  
 SHOW FULL COLUMNS FROM student_info; 
show columns from country;
show columns from world.city;
describe world.countrylanguage;
-- expalin the select statement we use
explain select *from country where name like '%a%';
select @@basedir;
-- variable =data
set @str ='rajasekar';
select @str as name;
-- can only save one value, so one cloumn name and one data to return
set @id =(select name from country where code='ABW');
select @id;
-- *****************************************************************
-- if
use world;
select world.country.Name, world.country.Continent, if(continent like '%the%','good','bad') as mgs
from country;
-- *****************************************************************
-- stored functions
-- DELIMITER $$
-- CREATE FUNCTION function_name(
    -- param1,
    -- param2,…
-- )
-- RETURNS datatype
-- [NOT] DETERMINISTIC
-- BEGIN
 -- statements
-- END $$
-- DELIMITER ;

use world;
create function fn(name varchar(50),lname varchar(50))
returns varchar(100) deterministic
return concat(name,' ',lname );

drop function fn;
select code,fn(name,localname)as fn from country;

use student;
DELIMITER $$
CREATE FUNCTION Customer_Occupation(age int)   
RETURNS VARCHAR(20)  
DETERMINISTIC  
BEGIN
DECLARE customer_occupation VARCHAR(20);
	if (age > 35) THEN  
		SET customer_occupation = 'Scientist';  
	eLSEIF (age <= 35 AND   age >= 30) THEN  
		SET customer_occupation = 'Engineer';  
	ELSEIF age < 30 THEN  
		SET customer_occupation = 'Actor';  
	END IF;  
	-- return the customer occupation  
	RETURN (customer_occupation);  
end $$

DELIMITER ;
-- *****************************************************************
DELIMITER //
CREATE FUNCTION Sample (bonus INT)
   RETURNS INT
   BEGIN
      DECLARE income INT;
      SET income = 0;
      myLabel: LOOP
         SET income = income + bonus;
         IF income < 10000 THEN
            ITERATE myLabel;
         END IF;
         LEAVE myLabel;
      END LOOP myLabel;
   RETURN income;
END; //
Delimiter ;

-- loop(loop,while)
-- [label name] : loop
-- statement 
-- end loop [label name];

-- [label name] : loop
-- statement 
-- if condition then
	-- leave [label name]; ->break the loop
-- end if;
	-- statement
-- end loop [label name];

-- while(can use it in funtion)
-- declare @c int=1;
-- while @c<=5
-- begin
-- print @c
-- set @c=@c+1;
-- end;
-- *****************************************************************
-- stored procudres
-- DELIMITER &&  
-- CREATE PROCEDURE procedure_name [[IN | OUT | INOUT] parameter_name datatype [, parameter datatype]) ]    
-- BEGIN    
--     Declaration_section    
--     Executable_section    
-- END &&  
-- DELIMITER ;   

-- IN parameter

-- It is the default mode. It takes a parameter as input, such as an attribute. When we define it, the calling program has to pass an argument to the stored procedure. This parameter's value is always protected.

-- OUT parameters

-- It is used to pass a parameter as output. Its value can be changed inside the stored procedure, and the changed (new) value is passed back to the calling program. It is noted that a procedure cannot access the OUT parameter's initial value when it starts.

-- INOUT parameters

-- It is a combination of IN and OUT parameters. It means the calling program can pass the argument, and the procedure can modify the INOUT parameter, and then passes the new value back to the calling program.

use student;
delimiter //
create procedure allv()
begin
select *from stud3;
end//
delimiter ;

drop procedure allv;
call allv();
call allv;

use world;
select *from country;
DELIMITER &&  
CREATE PROCEDURE get_country ()  
BEGIN  
    SELECT * FROM country WHERE population > 20000;  
END &&  
DELIMITER ;  
call get_country;

-- in
DELIMITER &&  
CREATE PROCEDURE get_code (IN var1 INT)  
BEGIN  
    SELECT * FROM country LIMIT var1;  
END &&  
DELIMITER ;  
drop procedure get_code;
call get_code(5);

-- out
DELIMITER &&  
CREATE PROCEDURE display_max(OUT highest INT)  
BEGIN  
    SELECT MAX(population) INTO highest FROM country;   
END &&  
DELIMITER ;  
call display_max(@val);
select @val;

-- in out
DELIMITER &&  
CREATE PROCEDURE display_pop (INOUT var1 varchar(10))  
BEGIN  
    SELECT population INTO var1 FROM country WHERE code= var1;   
END &&  
DELIMITER ;  
set @m='ABW';
call display_pop(@m);
select @m;

SHOW PROCEDURE STATUS WHERE db = 'world';  
-- *****************************************************************
-- triggers
-- We can define the maximum six types of actions or events in the form of triggers:
-- Before Insert: It is activated before the insertion of data into the table.
-- After Insert: It is activated after the insertion of data into the table.
-- Before Update: It is activated before the update of data in the table.
-- After Update: It is activated after the update of the data in the table.
-- Before Delete: It is activated before the data is removed from the table.
-- After Delete: It is activated after the deletion of data from the table.

-- CREATE TRIGGER trigger_name    
--     (AFTER | BEFORE) (INSERT | UPDATE | DELETE)  
--          ON table_name FOR EACH ROW    
--          BEGIN    
--         --variable declarations    
--         --trigger code    
--         END;     
create database student;
use student;
CREATE TABLE employee(  
    name varchar(45) NOT NULL,    
    occupation varchar(35) NOT NULL,    
    working_date date,  
    working_hours varchar(10)  
);  

INSERT INTO employee VALUES    
('Robin', 'Scientist', '2020-10-04', 12),  
('Warner', 'Engineer', '2020-10-04', 10),  
('Peter', 'Actor', '2020-10-04', 13),  
('Marco', 'Doctor', '2020-10-04', 14),  
('Brayden', 'Teacher', '2020-10-04', 12),  
('Antonio', 'Business', '2020-10-04', 11);  

select *from employee;

DELIMITER //  
Create Trigger before_insert_empworkinghours   
BEFORE INSERT ON employee FOR EACH ROW  
BEGIN  
IF NEW.working_hours < 0 THEN SET NEW.working_hours = 0;  
END IF;  
END //  

INSERT INTO employee VALUES    
('Alexander', 'Actor', '2020-10-012', -13);  

select *from employee;

DROP TRIGGER employeedb.before_update_salaries;  

SHOW TRIGGERS;    
SHOW TRIGGERS FROM student WHERE table = 'employee';  

-- after insert
CREATE TABLE student_info (  
  stud_id int NOT NULL,  
  stud_code varchar(15) DEFAULT NULL,  
  stud_name varchar(35) DEFAULT NULL,  
  subject varchar(25) DEFAULT NULL,  
  marks int DEFAULT NULL,  
  phone varchar(15) DEFAULT NULL,  
  PRIMARY KEY (stud_id)  
)  ;

CREATE TABLE student_detail (  
  stud_id int NOT NULL,  
  stud_code varchar(15) DEFAULT NULL,  
  stud_name varchar(35) DEFAULT NULL,  
  subject varchar(25) DEFAULT NULL,  
  marks int DEFAULT NULL,  
  phone varchar(15) DEFAULT NULL,  
  Lasinserted Time,  
  PRIMARY KEY (stud_id)  
);  

DELIMITER //  
Create Trigger after_insert_details  
AFTER INSERT ON student_info FOR EACH ROW  
BEGIN  
INSERT INTO student_detail VALUES (new.stud_id, new.stud_code,   
new.stud_name, new.subject, new.marks, new.phone, CURTIME());  
END //  

INSERT INTO student_info VALUES   
(10, 110, 'Alexandar', 'Biology', 67, '2347346438');  

-- before update
CREATE TABLE sales_info (  
    id INT AUTO_INCREMENT,  
    product VARCHAR(100) NOT NULL,  
    quantity INT NOT NULL DEFAULT 0,  
    fiscalYear SMALLINT NOT NULL,  
    CHECK(fiscalYear BETWEEN 2000 and 2050),  
    CHECK (quantity >=0),  
    UNIQUE(product, fiscalYear),  
    PRIMARY KEY(id)  
);  

INSERT INTO sales_info(product, quantity, fiscalYear)  
VALUES  
    ('2003 Maruti Suzuki',110, 2020),  
    ('2015 Avenger', 120,2020),  
    ('2018 Honda Shine', 150,2020),  
    ('2014 Apache', 150,2020);  
    
    DELIMITER $$  
  
CREATE TRIGGER before_update_salesInfo  
BEFORE UPDATE  
ON sales_info FOR EACH ROW  
BEGIN  
    DECLARE error_msg VARCHAR(255);  
    SET error_msg = ('The new quantity cannot be greater than 2 times the current quantity');  
    IF new.quantity > old.quantity * 2 THEN  
    SIGNAL SQLSTATE '45000'   
    SET MESSAGE_TEXT = error_msg;  
    END IF;  
END $$  
  
DELIMITER ;  

UPDATE sales_info SET quantity = 125 WHERE id = 2;   
UPDATE sales_info SET quantity = 600 WHERE id = 2;   

select *from sales_info;

-- after update
CREATE TABLE students(    
    id int NOT NULL AUTO_INCREMENT,    
    name varchar(45) NOT NULL,    
    class int NOT NULL,    
    email_id varchar(65) NOT NULL,    
    PRIMARY KEY (id)    
);  

INSERT INTO students (name, class, email_id)     
VALUES ('Stephen', 6, 'stephen@javatpoint.com'),   
('Bob', 7, 'bob@javatpoint.com'),   
('Steven', 8, 'steven@javatpoint.com'),   
('Alexandar', 7, 'alexandar@javatpoint.com');  

CREATE TABLE students_log(    
    user varchar(45) NOT NULL,    
    descreptions varchar(65) NOT NULL  
);  

DELIMITER $$  
  
CREATE TRIGGER after_update_studentsInfo  
AFTER UPDATE  
ON students FOR EACH ROW  
BEGIN  
    INSERT into students_log VALUES (user(),   
    CONCAT('Update Student Record ', OLD.name, ' Previous Class :',  
    OLD.class, ' Present Class ', NEW.class));  
END $$  
  
DELIMITER ;  

-- before delete
CREATE TABLE salaries (  
    emp_num INT PRIMARY KEY,  
    valid_from DATE NOT NULL,  
    amount DEC(8 , 2 ) NOT NULL DEFAULT 0  
);  
INSERT INTO salaries (emp_num, valid_from, amount)  
VALUES  
    (102, '2020-01-10', 45000),  
    (103, '2020-01-10', 65000),  
    (105, '2020-01-10', 55000),  
    (107, '2020-01-10', 70000),  
    (109, '2020-01-10', 40000);  
    
CREATE TABLE salary_archives (  
    id INT PRIMARY KEY AUTO_INCREMENT,  
    emp_num INT,  
    valid_from DATE NOT NULL,  
    amount DEC(18 , 2 ) NOT NULL DEFAULT 0,  
    deleted_time TIMESTAMP DEFAULT NOW()  
);  

DELIMITER $$  
  
CREATE TRIGGER before_delete_salaries  
BEFORE DELETE  
ON salaries FOR EACH ROW  
BEGIN  
    INSERT INTO salary_archives (emp_num, valid_from, amount)  
    VALUES(OLD. emp_num, OLD.valid_from, OLD.amount);  
END$$   
  
DELIMITER ;  

DELETE FROM salaries WHERE emp_num = 105;  

 SELECT * FROM salary_archives;  
 
 DELETE FROM salaries;  
 
 -- after delete
 CREATE TABLE salaries (  
    emp_num INT PRIMARY KEY,  
    valid_from DATE NOT NULL,  
    amount DEC(8 , 2 ) NOT NULL DEFAULT 0  
);  

INSERT INTO salaries (emp_num, valid_from, amount)  
VALUES  
    (102, '2020-01-10', 45000),  
    (103, '2020-01-10', 65000),  
    (105, '2020-01-10', 55000),  
    (107, '2020-01-10', 70000),  
    (109, '2020-01-10', 40000);  
    
CREATE TABLE total_salary_budget(  
    total_budget DECIMAL(10,2) NOT NULL  
);  

 INSERT INTO total_salary_budget (total_budget)  
SELECT SUM(amount) FROM salaries;  

DELIMITER $$  
  
CREATE TRIGGER after_delete_salaries  
AFTER DELETE  
ON salaries FOR EACH ROW  
BEGIN  
   UPDATE total_salary_budget SET total_budget = total_budget - old.amount;  
END$$   
  
DELIMITER ;  

 DELETE FROM salaries WHERE emp_num = 105;  
 SELECT * FROM total_salary_budget;
 
 DELETE FROM salaries;  
-- ****************************** over *********************************** 
-- repair table

-- MySQL Repair Table allows us to repair or fix the corrupted table. The repair table in MySQL provides support only for selected storage engines, not for all. It is to ensure that we have a few privileges like SELECT and INSERT to use this statement. Normally, we should never use the repair table until disastrous things happen with the table. This statement rarely gets all data from the MyISAM table. Therefore, we need to find why our table is corrupted to eliminate the use of this statement.
-- When we execute the REPAIR TABLE statement, it first checks the table that we are going to repair is required an upgradation or not. If required, it will perform upgradation with the same rules as CHECK TABLE ... FOR UPGRADE statement works. It is always good to keep our table's backup before performing the "table repair" option because it might cause a loss of our data.
-- NO_WRITE_TO_BINLOG or LOCAL: It's a place where the server is responsible for writing the REPAIR TABLE statements for the replication slaves. We can optionally specify the optional NO_WRITE_TO_BINLOG/LOCAL keyword to suppress the logging.

-- QUICK: The quick option allows the REPAIR TABLE statement for repairing only the index file. It does not allow to repair of the data file. This type of repair gives the same result as the myisamchk --recover -quick command works.

-- EXTENDED: Instead of creating the index row by row, this option allows MySQL to create one index at a time with sorting. This type of repair gives the same result as the myisamchk --safe-recover command works.

-- USE_FRM: This option is used when the .MYI index file is not found or if its header is corrupted. The USE-FRM option informs MySQL to do not trust the information present in this file header and re-create it by using the information provided from the data dictionary. This type of repair cannot work with the myisamchk command.


create database repair_table;
use repair_table;
drop table vehicle;
CREATE TABLE vehicle (  
    vehicle_no VARCHAR(18) PRIMARY KEY,  
    model_name VARCHAR(45),  
    cost_price DECIMAL(10,2 ),  
    sell_price DECIMAL(10,2)  
);  

INSERT INTO vehicle values (vehicle_no, model_name, cost_price, sell_price)   ;

SELECT * FROM vehicle;  

SELECT table_name, engine   
FROM information_schema.tables   
WHERE table_name = 'vehicle';  

REPAIR TABLE vehicle;  

ALTER TABLE vehicle ENGINE = 'MyISAM';  
-- Now, use the repair table query   
 REPAIR TABLE vehicle;  
 
 -- to use a repair table statement with any QUICK, EXTENDED or USE_FRM options. Thus, we will first create another table named memberships and stored this table in the "MyISAM" storage engine instead of the default one InnoDB.
 
 CREATE TABLE memberships (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    name VARCHAR(55) NOT NULL,  
    email VARCHAR(55) NOT NULL,  
    plan VARCHAR(45) NOT NULL,  
    validity_date DATE NOT NULL  
) ENGINE = MyISAM;   

 INSERT INTO memberships (name, email, plan, validity_date)  
VALUES('Stephen', 'stephen@javatpoint.com', 'Gold', '2020-06-13'),  
      ('Jenifer', 'jenifer@javatpoint.com', 'Platinum', '2020-06-10'),  
      ('david', 'david@javatpoint.com', 'Silver', '2020-06-15');  
      
REPAIR TABLE memberships QUICK EXTENDED;  

REPAIR TABLE service_memberships QUICK EXTENDED;  
      
-- lock and unlock table 
-- A lock is a mechanism associated with a table used to restrict the unauthorized access of the data in a table. MySQL allows a client session to acquire a table lock explicitly to cooperate with other sessions to access the table's data. MySQL also allows table locking to prevent it from unauthorized modification into the same table during a specific period.

-- A session in MySQL can acquire or release locks on the table only for itself. Therefore, one session cannot acquire or release table locks for other sessions. It is to note that we must have a TABLE LOCK and SELECT privileges for table locking.

-- Table Locking in MySQL is mainly used to solve concurrency problems. It will be used while running a transaction, i.e., first read a value from a table (database) and then write it into the table (database).

-- READ LOCK: This lock allows a user to only read the data from a table.

-- WRITE LOCK: This lock allows a user to do both reading and writing into a table.

CREATE TABLE info_table (   
    Id INT NOT NULL AUTO_INCREMENT,   
    Name VARCHAR(50) NOT NULL,   
    Message VARCHAR(80) NOT NULL,  
    PRIMARY KEY (Id)   
);  

INSERT INTO info_table (name, message)   
VALUES('Peter', 'Hi'),  
('Joseph', 'Hello'),  
('Mark', 'Welcome');  
  

 -- CONNECTION_ID() function that gives the current connection id in the first session
 SELECT CONNECTION_ID();  
 
 LOCK TABLE info_table READ;  
 
INSERT INTO info_table (name, message)   
VALUES ('Suzi', 'Hi');  

 SELECT CONNECTION_ID();  
 
-- we can see that once the READ lock is acquired on to the table, we cannot write data to the table in the same session.

-- Now, we will check how the READ lock work from a different session. First, we will connect to the database and see the connection id:

 SELECT CONNECTION_ID();  
 
 INSERT INTO info_table (name, message)   
VALUES ('Stephen', 'Hello');  

 UNLOCK TABLES;  
 
  LOCK TABLE info_table WRITE;  
  
  INSERT INTO info_table (name, message)   
VALUES ('Stephen', 'How R U');  
SELECT * FROM info_table;  
-- We can see that these operations are put into a waiting state. See the detailed information about them using the SHOW PROCESSLIST statement
INSERT INTO info_table (name, message)   
VALUES ('George', 'Welcome');  
  
SELECT * FROM info_table;  

-- *****************************************************************************
-- insert ignore
use student;
CREATE TABLE if not exists Student (  
  Stud_ID int AUTO_INCREMENT PRIMARY KEY,  
  Name varchar(45) DEFAULT NULL,  
  Email varchar(45) NOT NULL UNIQUE,  
  City varchar(25) DEFAULT NULL  
);  

INSERT INTO Student(Stud_ID, Name, Email, City)   
VALUES (4,'Donald', 'donald@javatpoint.com', 'New York'),   
(5, 'Joseph', 'Joseph@javatpoint.com', 'Chicago');  

INSERT IGNORE INTO Student(Stud_ID, Name, Email, City)   
VALUES (4,'Donald', 'donald@javatpoint.com', 'New York'),   
(5, 'Joseph', 'Joseph@javatpoint.com', 'Chicago');  

CREATE TABLE Test (  
    ID int AUTO_INCREMENT PRIMARY KEY,  
    Name varchar(5) NOT NULL  
);  

INSERT INTO Test(Name)  
VALUES ('Peter'), ('John');  

INSERT INTO Test(Name) VALUES ('Stephen');  

select *from test;

INSERT IGNORE INTO Test(Name) VALUES ('Stephen');  

select *from test;

-- insert on duplicate key update

-- The Insert on Duplicate Key Update statement is the extension of the INSERT statement in MySQL. When we specify the ON DUPLICATE KEY UPDATE clause in a SQL statement and a row would cause duplicate error value in a UNIQUE or PRIMARY KEY index column, then updation of the existing row occurs.

-- In other words, when we insert new values into the table, and it causes duplicate row in a UNIQUE OR PRIMARY KEY column, we will get an error message. However, if we use ON DUPLICATE KEY UPDATE clause in a SQL statement, it will update the old row with the new row values, whether it has a unique or primary key column.

CREATE TABLE Student (  
  Stud_ID int AUTO_INCREMENT PRIMARY KEY,  
  Name varchar(45) DEFAULT NULL,  
  Email varchar(45) DEFAULT NULL,  
  City varchar(25) DEFAULT NULL  
);  


INSERT INTO Student(Stud_ID, Name, Email, City)   
VALUES (1,'Stephen', 'stephen@javatpoint.com', 'Texax'),   
(2, 'Joseph', 'Joseph@javatpoint.com', 'Alaska'),   
(3, 'Peter', 'Peter@javatpoint.com', 'california');  

SELECT * FROM Student;  

INSERT INTO Student(Stud_ID, Name, Email, City)   
VALUES (4,'John', 'john@javatpoint.com', 'New York');  

SELECT * FROM Student;  

INSERT INTO Student(Stud_ID, Name, Email, City)   
VALUES (4, 'John', 'john@javatpoint.com', 'New York')  
ON DUPLICATE KEY UPDATE City = 'California';  

SELECT * FROM Student;  

 -- insert into select
 use student;
 create table detail (name varchar(10),age int,phone int);
 insert into detail values('raj',26,2143),('raja',26,234235),('sekar',26,3495634);
 create table dup (name varchar(10),age int);
 
 insert into dup select name ,age from detail;
 
 select *from dup;
 
 -- create temporary table
 -- MySQL has a feature to create a special table called a Temporary Table that allows us to keep temporary data. We can reuse this table several times in a particular session. It is available in MySQL for the user from version 3.23, and above so if we use an older version, this table cannot be used. This table is visible and accessible only for the current session. MySQL deletes this table automatically as long as the current session is closed or the user terminates the connection. We can also use the DROP TABLE command for removing this table explicitly when the user is not going to use it.
 CREATE TEMPORARY TABLE temporary_table_name SELECT * FROM original_table_name LIMIT 0;  
 CREATE TEMPORARY TABLE Students( student_name VARCHAR(40) NOT NULL, total_marks DECIMAL(12,2) NOT NULL DEFAULT 0.00, total_subjects INT UNSIGNED NOT NULL DEFAULT 0);  
 DROP TEMPORARY TABLE top_customers;  
 
 
 -- copy or clone table
 -- We can copy an existing table to a new table using the CREATE TABLE and SELECT statement
 CREATE TABLE duplicate_table LIKE original_table;
 
 CREATE TABLE IF NOT EXISTS duplicate_table   
SELECT * FROM original_table WHERE Year = '2016';  


-- replace->will only work with primary key and uses primary key as reference
use student;
alter table stud3 add primary key(sno);
replace into stud3(sno,sname,mark,city) values (101,'rajasekar',100,'pondy');
