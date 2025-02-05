DELIMITER //
CREATE TRIGGER prevent_delete_flight_history
BEFORE DELETE ON FlightHistory
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Видалення записів з таблиці FlightHistory заборонено!';
END;
//
DELIMITER ;
