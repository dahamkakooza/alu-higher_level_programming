-- Check if user_0d_1 exists, if not, create and grant privileges
SELECT IF(EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_1' AND host = 'localhost'), 'User exists', 'User does not exist') AS 'user_0d_1 status';
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Check if user_0d_2 exists, if not, create and grant privileges
SELECT IF(EXISTS (SELECT 1 FROM mysql.user WHERE user = 'user_0d_2' AND host = 'localhost'), 'User exists', 'User does not exist') AS 'user_0d_2 status';
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_2'@'localhost';

-- List all privileges for user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- List all privileges for user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';
