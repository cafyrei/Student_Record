-- Create Table for Administrator
CREATE TABLE IF NOT EXISTS administrator (
    id SMALLINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    admin_account TEXT NOT NULL,
    password_hash TEXT NOT NULL,
    last_login DATETIME DEFAULT NULL,
    account_created DATETIME DEFAULT CURRENT_TIMESTAMP,
    account_update DATE
);
DROP TABLE administrator;
DESCRIBE administrator;
SELECT *
FROM world;