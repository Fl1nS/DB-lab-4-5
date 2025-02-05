CREATE TABLE IF NOT EXISTS Pilot_Delete_Log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    deleted_pilot_id INT,
    deleted_pilot_name VARCHAR(100),
    deleted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //
CREATE TRIGGER log_pilot_deletion
AFTER DELETE ON Pilot
FOR EACH ROW
BEGIN
    INSERT INTO Pilot_Delete_Log (deleted_pilot_id, deleted_pilot_name)
    VALUES (OLD.id, OLD.name);
END;
//
DELIMITER ;
