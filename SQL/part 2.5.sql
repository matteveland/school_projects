/*
Write an INSERT statement that adds this row to the Customers table:
email_address:         rick@raven.com
password:                (empty string)
first_name:                Rick
last_name:                 Raven
Use a column list for this statement. Submit a screenshot.
*/

INSERT INTO customers (email_address, password, first_name, last_name, shipping_address_id, billing_address_id)
VALUES ('rick@raven.com', '', 'Rick', 'Raven', NULL, NULL)