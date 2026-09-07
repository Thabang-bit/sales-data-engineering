-- 1. Show all sales
SELECT *
FROM sales;

-- 2. Calculate total revenue
SELECT SUM(revenue) AS total_revenue
FROM sales;

-- 3. Revenue by product
SELECT
    product,
    SUM(revenue) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC;

-- 4. Revenue by customer
SELECT
    customer,
    SUM(revenue) AS total_spent
FROM sales
GROUP BY customer
ORDER BY total_spent DESC;