/*Write a SELECT statement that returns these column names and data from the Order_Items table:
item_id                           The item_id column
item_price                      The item_price column
discount_amount            The discount_amount column
quantity                          The quantity column
price_total                       A column that’s calculated by multiplying the item price by the quantity
discount_total                  A column that’s calculated by multiplying the discount amount by the quantity
item_total                         A column that’s calculated by subtracting the discount amount from the item price
									and then multiplying by the quantity

Only return rows where the item_total is greater than 500.
Sort the result set by the item_total column in descending sequence. 
Submit a screenshot.
*/
SELECT
item_id As 'The Item_Id Column',
item_price AS 'The Item_Price Column',
discount_amount AS 'The Discount_Amount Column',
quantity AS 'The Quanity_Column',
(item_price * quantity) AS 'Price Total Column',
(discount_amount * quantity) AS 'Discount Total Column',
((item_price - discount_amount) * quantity) AS 'Item Total Column'
from order_items
WHERE ((item_price - discount_amount) * quantity) > 500
ORDER by ((item_price - discount_amount) * quantity) DESC