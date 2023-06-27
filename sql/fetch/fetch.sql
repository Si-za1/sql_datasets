-- queries for fetching the data 
-- total amount spent by each customer 


SELECT m.customer_id, SUM(o.price) AS total_spent 
FROM members m 
JOIN sales s ON m.customer_id = s.customer_id
JOIN menu o ON s.product_id = o.product_id
GROUP BY m.customer_id;


-- visited the restaurant 
SELECT customer_id, COUNT(DISTINCT order_date) AS total_visit
FROM sales
GROUP BY customer_id;


-- first item purchased by customer A

-- SELECT m.customer_id, MIN(s.order_date) AS first_purchase_date, menu.product_name AS first_item_purchased
-- FROM sales s
-- JOIN members m ON s.customer_id = m.customer_id
-- JOIN menu ON s.product_id = menu.product_id
-- WHERE m.customer_id = 'A'
-- GROUP BY m.customer_id, menu.product_name;

SELECT menu.product_name, MIN(sales.order_date) AS first_purchase_date
FROM sales
JOIN menu ON sales.product_id = menu.product_id
WHERE sales.customer_id = 'A'
GROUP BY menu.product_name
HAVING MIN(sales.order_date) = (
    SELECT MIN(order_date)
    FROM sales
    WHERE customer_id = 'A'
)


-- What is the most purchased item on the menu and how many times purchased 

-- SELECT menu.product_name AS most_purchased_item, COUNT(*) AS purchase_count
-- FROM sales
-- JOIN menu ON sales.product_id = menu.product_id
-- GROUP BY menu.product_name
-- ORDER BY purchase_count DESC
-- LIMIT 1;

SELECT menu.product_name AS most_purchased_item, COUNT(*) AS purchase_count
FROM (
	SELECT TOP 1 
	FROM sales
	JOIN menu ON sales.product_id = menu.product_id
	 ) as m

GROUP BY  menu.product_name
ORDER BY purchase_count DESC;



--most popular for each customer 
SELECT
    m.customer_id,
    m.product_name AS most_popular_item
FROM (
    SELECT
        s.customer_id,
        s.product_id,
        m.product_name,
        COUNT(*) AS purchase_count,
        RANK() OVER (PARTITION BY s.customer_id ORDER BY COUNT(*) DESC) AS rank
    FROM sales s
    JOIN menu m ON s.product_id = m.product_id
    GROUP BY s.customer_id, s.product_id, m.product_name
) AS m
WHERE m.rank = 1;

