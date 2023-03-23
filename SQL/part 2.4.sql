/*Write a SELECT statement that returns these two columns:
category_name        The category_name column from the Categories table

product_id               The product_id column from the Products table

Return one row for each category that has never been used.
Hint: Use an outer join and only return rows where the product_id column contains a null value. Submit a screenshot.*/

SELECT
c.category_name AS Catergory_Name,
p.product_id AS Product_Id
FROM categories c
LEFT JOIN products p
	ON c.category_id = p.category_id 
where p.product_id IS NULL