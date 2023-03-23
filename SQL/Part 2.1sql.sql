/*
Write a SELECT statement that returns these column names and data from the Products table:
product_name               The product_name column
list_price                        The list_price column
discount_percent            The discount_percent column
discount_amount            A column that’s calculated from the previous two columns
discount_price               A column that’s calculated from the previous three columns

Round the discount_amount and discount_price columns to two decimal places.
Sort the result set by the discount_price column in descending sequence. 
Use the LIMIT clause so the result set contains only the first five rows.
Submit a screenshot.*/

SELECT
product_name AS 'The Product Name', 
list_price AS 'The List Price', 
discount_percent AS 'The Discount Precent',
ROUND(list_price * (discount_percent/100), 2) AS 'The Discount Amount',
ROUND(list_price - list_price * (discount_percent/100), 2) AS 'The Discount Price'
FROM products
ORDER BY (list_price - list_price * (discount_percent/100)) DESC
LIMIT 5
