-- create hbnb_test_db database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- create hbnb_test user in localhost with hbnb_test_pwd password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- give hbnb_test all privileges on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- give hbnb_test SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
