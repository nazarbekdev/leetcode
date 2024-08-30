Select customers.name AS Customers
FROM customers LEFT JOIN orders ON customers.id = orders.customerId
WHERE orders.customerId IS NULL;