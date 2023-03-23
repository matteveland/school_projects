/*Write a SELECT statement that returns the product_name and list_price columns from the Products table.
Return one row for each product that has the same list price as another product.

Hint: Use a self-join to check that the product_id columns aren’t equal but the list_price columns are equal.

Sort the result set by the product_name column. Submit a screenshot.*/
SELECT p.product_name, p.list_price
	FROM products p
    
		JOIN products pp
			on p.product_id != pp.product_id
            AND p.list_price = pp.list_price
order by p.product_name ASC;

