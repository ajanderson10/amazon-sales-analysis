-- 1. Overall price statistics
SELECT
    ROUND(AVG(actual_price), 2) AS avg_price,
    ROUND(MIN(actual_price), 2) AS min_price,
    ROUND(MAX(actual_price), 2) AS max_price,
    ROUND(AVG(discount_pct), 2) AS avg_discount_pct
FROM amazon_db.products;

-- 2. Top 10 most discounted products
SELECT name, actual_price, discount_price, discount_pct
FROM amazon_db.products
ORDER BY discount_pct DESC
LIMIT 10;

-- 3. Top 10 highest rated products (min 100 reviews)
SELECT name
, ratings, no_of_ratings, actual_price
FROM amazon_db.products
WHERE no_of_ratings >= 100
ORDER BY ratings DESC
LIMIT 10;

-- 4. Top 10 most reviewed products
SELECT name, no_of_ratings, ratings, actual_price
FROM amazon_db.products
ORDER BY no_of_ratings DESC
LIMIT 10;

-- 5. Products by price range
SELECT
    CASE
        WHEN actual_price
< 500 THEN 'Under 500'
        WHEN actual_price BETWEEN 500 AND 999 THEN '500-1000'
        WHEN actual_price BETWEEN 1000 AND 2499 THEN '1000-2500'
        WHEN actual_price BETWEEN 2500 AND 4999 THEN '2500-5000'
        ELSE 'Over 5000'
END AS price_range,
    COUNT
(*) AS product_count,
    ROUND
(AVG
(discount_pct), 2) AS avg_discount
FROM amazon_db.products
GROUP BY price_range
ORDER BY product_count DESC;
