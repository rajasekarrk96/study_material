/*
================================================================================
STEP 11: VARIABLES, FUNCTIONS, PROCEDURES, AND LOOPS
================================================================================
GOAL:
Learn database programming basics using user variables, stored functions,
stored procedures, parameters, and control flow.
================================================================================
*/

USE student;

/*
--------------------------------------------------------------------------------
1. USER VARIABLES
--------------------------------------------------------------------------------
- Session-level variables
- Start with @
--------------------------------------------------------------------------------
*/

SET @name_value = 'raj';
SELECT @name_value;

/*
--------------------------------------------------------------------------------
2. DELIMITER
--------------------------------------------------------------------------------
- Used when writing multi-statement procedures or functions
- Helps MySQL know where object definition ends
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
3. STORED FUNCTION
--------------------------------------------------------------------------------
- Returns one value
- Can take input parameters
- Useful for reusable calculation logic
--------------------------------------------------------------------------------
*/

/*
Example:
DELIMITER $$
CREATE FUNCTION fn_full_name(fname VARCHAR(50), lname VARCHAR(50))
RETURNS VARCHAR(120)
DETERMINISTIC
BEGIN
    RETURN CONCAT(fname, ' ', lname);
END $$
DELIMITER ;
*/

/*
--------------------------------------------------------------------------------
4. STORED PROCEDURE
--------------------------------------------------------------------------------
- Reusable database program
- Can return result sets or modify data
- Can use IN, OUT, INOUT parameters
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
5. IN, OUT, INOUT
--------------------------------------------------------------------------------
IN:
- input only

OUT:
- output only

INOUT:
- input and output both
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
6. DECLARE, SET, IF, ELSEIF
--------------------------------------------------------------------------------
- Used inside stored programs
- Supports procedural logic
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
7. LOOPS
--------------------------------------------------------------------------------
- LOOP
- WHILE
- REPEAT
- Use LEAVE to exit
- Use ITERATE to continue loop
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
8. FUNCTION VS PROCEDURE
--------------------------------------------------------------------------------
FUNCTION:
- returns one value
- often used inside SELECT

PROCEDURE:
- can perform broader operations
- called using CALL
--------------------------------------------------------------------------------
*/

/*
--------------------------------------------------------------------------------
9. COMMON MISTAKES
--------------------------------------------------------------------------------
1. Forgetting delimiter change
2. Returning wrong datatype from function
3. Confusing function usage with procedure call
4. Creating non-deterministic function without understanding behavior
--------------------------------------------------------------------------------
*/

/*
================================================================================
SUMMARY
================================================================================
- Variables hold session values
- Functions return one value
- Procedures can perform broader logic
- Parameters and loops support procedural programming
================================================================================
*/
