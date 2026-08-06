---
id: "05_09"
title: "Stored Procedures Functions Triggers and Events"
course: "MySQL"
module: 4
module_title: "Programmability"
lesson: 9
version: "2.0"
difficulty: "advanced"
duration_minutes: 60
tags: ["STORED-PROCEDURE", "FUNCTION", "TRIGGER", "EVENT", "IN-OUT-INOUT", "DELIMITER", "DECLARE", "IF", "LOOP", "CALL", "BEFORE-AFTER"]
prerequisites: []
lab_required: true
---

## Topics Covered

### 1. Stored Procedures
```sql
DELIMITER //
CREATE PROCEDURE get_dept_summary(IN dept_id INT, OUT total DECIMAL(15,2))
BEGIN
    SELECT SUM(salary) INTO total
    FROM employees WHERE dept_id = dept_id AND is_active = 1;
END //
DELIMITER ;

CALL get_dept_summary(3, @total);
SELECT @total;
```

### 2. User-Defined Functions
```sql
DELIMITER //
CREATE FUNCTION full_name(first VARCHAR(50), last VARCHAR(50))
RETURNS VARCHAR(101) DETERMINISTIC
BEGIN
    RETURN CONCAT(first, ' ', last);
END //
DELIMITER ;

SELECT full_name(first_name, last_name) FROM employees;
```

### 3. Triggers
```sql
DELIMITER //
CREATE TRIGGER after_order_insert
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE customers SET total_orders = total_orders + 1
    WHERE id = NEW.customer_id;

    INSERT INTO audit_log(action, entity, entity_id, ts)
    VALUES ('INSERT', 'orders', NEW.id, NOW());
END //
DELIMITER ;
```

### 4. Events (Scheduled Jobs)
```sql
SET GLOBAL event_scheduler = ON;

CREATE EVENT cleanup_sessions
ON SCHEDULE EVERY 1 HOUR
DO
    DELETE FROM sessions WHERE expires_at < NOW();
```

## Lab
Build a complete order processing system using: stored procedure (create order + update inventory), trigger (audit log + customer stats), event (nightly cleanup of expired carts).
