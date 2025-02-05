DELIMITER //
CREATE TRIGGER prevent_update_aircraft
BEFORE UPDATE ON Aircraft
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Оновлення записів у таблиці Aircraft заборонено!';
END;
//
DELIMITER ;
