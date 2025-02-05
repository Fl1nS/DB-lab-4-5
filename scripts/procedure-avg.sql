DELIMITER //

DROP FUNCTION IF EXISTS get_aggregate_value;
CREATE FUNCTION get_aggregate_value(
    table_name VARCHAR(64),
    column_name VARCHAR(64),
    operation VARCHAR(10)
) RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    DECLARE query_text VARCHAR(255);
    DECLARE result DECIMAL(10,2);

    SET query_text = CONCAT('SELECT ', operation, '(', column_name, ') INTO @result FROM ', table_name);

    PREPARE stmt FROM query_text;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;

    RETURN @result;
END;
//

DROP PROCEDURE IF EXISTS call_aggregate_function;
CREATE PROCEDURE call_aggregate_function(
    table_name VARCHAR(64),
    column_name VARCHAR(64),
    operation VARCHAR(10)
)
BEGIN
    SELECT get_aggregate_value(table_name, column_name, operation) AS result;
END;
//

DELIMITER ;
