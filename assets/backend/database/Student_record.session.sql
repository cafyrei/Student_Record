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

DESCRIBE administrator;

DROP TABLE world;

SELECT * FROM administrator;
DELETE FROM administrator;

DELETE FROM student_records WHERE student_number = 202524009;

CREATE TABLE student_records(
        student_number INTEGER PRIMARY KEY,
        first_name VARCHAR(100) NOT NULL,
        last_name VARCHAR(100) NOT NULL,
        middle_name VARCHAR(100) NULL,
        phone_no VARCHAR(50) NOT NULL,
        date_of_birth VARCHAR(50) NOT NULL,
        course VARCHAR(50) NOT NULL,
        guardian_name VARCHAR(50) NOT NULL,
        guardian_phone_no VARCHAR(50) NOT NULL,
        student_address TEXT NOT NULL
);

SELECT * FROM student_records;

DROP TABLE student_records;

SELECT first_name, last_name, middle_name FROM student_records;


