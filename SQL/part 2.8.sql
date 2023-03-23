/*
Write and execute a script that creates a user with a username using your 
firstname initial and lastname and password of your choosing. 
This user should be able to connect to MySQL from any computer.

This user should have SELECT, INSERT, UPDATE, and DELETE privileges for the Customers, 
Addresses, Orders, and Order_Items tables of the My Guitar Shop database.

However, this user should only have SELECT privileges for the 
Products and Categories tables. Also, this user should not have 
the right to grant privileges to other users.

Check the privileges for the user by using the SHOW GRANTS statement. Submit a screenshot.

*/
DROP USER IF EXISTS MEveland@localhost;

CREATE USER IF NOT EXISTS 'MEveland'@'localhost' IDENTIFIED BY 'password';  -- creates MEveland@%

GRANT SELECT, INSERT, UPDATE, DELETE ON my_guitar_shop.customers TO 'MEveland'@'localhost';

GRANT SELECT, INSERT, UPDATE, DELETE ON my_guitar_shop.addresses TO MEveland@localhost;

GRANT SELECT, INSERT, UPDATE, DELETE ON my_guitar_shop.orders TO MEveland@localhost;

GRANT SELECT, INSERT, UPDATE, DELETE ON my_guitar_shop.order_items TO MEveland@localhost;

GRANT SELECT ON my_guitar_shop.products TO MEveland@localhost;

GRANT SELECT ON my_guitar_shop.categories TO MEveland@localhost;

SHOW GRANTS;
