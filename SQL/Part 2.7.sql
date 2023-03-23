/*
Write a SELECT statement that answers this question:
What is the total quantity purchased for each product within each category? Return these columns

The category_name column from the category table
The product_name column from the products table
The total quantity purchased for each product with orders in the Order_Items table

Use the WITH ROLLUP operator to include rows that give a summary for each category name as well as a row that gives the grand total.

Use the IF and GROUPING functions to replace null values in the category_name and product_name columns with literal values if they’re for summary rows.

*/
SELECT
c.category_name AS 'Category Name',
if( p.product_name is null, 'All Products Sold In Category', p.product_name ) AS 'Product Name', 
COUNT(o.product_id) AS 'Total Category Amount Purchased' 
	FROM products p
	LEFT Join order_items o
		on p.product_id = o.product_id
	LEFT JOIN categories c
		on  p.category_id = c.category_id
GROUP BY c.category_name, p.product_name with rollup;






/*


Error Code: 1055. Expression #1 of SELECT list is not in GROUP BY clause and contains 
nonaggregated column 'my_guitar_shop.p.product_id' which is not functionally dependent on columns in GROUP BY clause

*/