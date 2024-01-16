-- create hbnb_dev_db database if not exist
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- create hbnb_dev user in localhost with hbnb_dev_pwd password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- create another database, for example, hbnb_test_db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- give hbnb_dev all privileges on the database hbnb_dev_db
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- create another user, for example, hbnb_test_user
CREATE USER IF NOT EXISTS 'hbnb_test_user'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- give hbnb_test_user all privileges on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test_user'@'localhost';

-- give hbnb_dev SELECT privilege on the database performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
