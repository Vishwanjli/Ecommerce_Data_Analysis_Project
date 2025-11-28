CREATE DATABASE ecommerce_db;
USE ecommerce_db;
CREATE TABLE ecommerce (
    order_id VARCHAR(50),
    product_name VARCHAR(255),
    category VARCHAR(100),
    price_rs DECIMAL(10,2),
    discount_percent DECIMAL(10,2),
    final_price_rs DECIMAL(10,2),
    order_date DATE,
    customer_id VARCHAR(50)
);
SELECT product_name, COUNT(*) AS total_orders
FROM ecommerce
GROUP BY product_name
ORDER BY total_orders DESC
LIMIT 10;
SELECT 
    DATE_FORMAT(order_date, '%Y-%m') AS month,
    SUM(final_price_rs) AS total_sales,
    COUNT(*) AS total_orders
FROM ecommerce
GROUP BY month
ORDER BY month;
SELECT 
    customer_id,
    COUNT(*) AS purchase_count
FROM ecommerce
GROUP BY customer_id
ORDER BY purchase_count DESC;
WITH cte_sales AS (
    SELECT product_name, final_price_rs
    FROM ecommerce
)
SELECT *
FROM cte_sales;

