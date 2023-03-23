/*
Write a SELECT statement that answers this question:\

Which customers have ordered more than one product?

Return these columns:
The email_address column from the Customers table
The count of distinct products from the customer’s orders

Sort the result set in ascending sequence by the email_address column. Submit a screenshot.

*/
SELECT c.email_address, COUNT(DISTINCT i.product_id) as item_count

FROM customers c
	inner join orders o
		on c.customer_id = o.customer_id
	inner Join order_items i
		on o.order_id = i.order_id
GROUP BY c.email_address
HAVING item_count > 1 

