DELIMITER //

DROP PROCEDURE IF EXISTS insert_into_table;
CREATE PROCEDURE insert_into_table(
    IN table_name VARCHAR(64), 
    IN column_list VARCHAR(255), 
    IN values_list VARCHAR(255) 
)
BEGIN
    DECLARE query_text VARCHAR(500);

    SET query_text = CONCAT('INSERT INTO ', table_name, ' (', column_list, ') VALUES (', values_list, ')');

    PREPARE stmt FROM query_text;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END;
//

DELIMITER ;
