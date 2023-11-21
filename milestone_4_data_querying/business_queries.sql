-- Task 1: How many stores does the business have and in which countries?

SELECT 
    country_code AS country,
    COUNT(country_code) AS total_no_stores    
FROM 
    dim_store_details
WHERE 
    address != 'N/A'
GROUP BY 
    country_code
ORDER BY 
    total_no_stores DESC


-- Task 2: Which locations currently have the most stores?

SELECT
    locality AS locality,
    COUNT(locality) AS total_no_stores
FROM 
    dim_store_details
WHERE 
    address != 'N/A'
GROUP BY 
    locality
HAVING 
    COUNT(locality) >= 10
ORDER BY 
    total_no_stores DESC;


-- Task 3: Which months produced the largest amount of sales?

SELECT 
    ROUND(SUM(orders_table.product_quantity * dim_products.product_price)::numeric, 2) AS total_sales,
    dim_date_times.month
FROM 
    orders_table
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
JOIN 
    dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
GROUP BY
    dim_date_times.month
ORDER BY 
    total_sales DESC
LIMIT 6;


-- Task 4: How many sales are coming from online?

SELECT
    COUNT(orders_table.product_quantity) AS numbers_of_sales,
    SUM(orders_table.product_quantity) AS product_quantity_count,
    CASE
        WHEN dim_store_details.locality = 'N/A' THEN 'Web'
        ELSE 'Offline'
    END AS location
FROM
    orders_table
JOIN
    dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY
    location
ORDER BY
    numbers_of_sales;


-- Task 5: What percentage of sales come through each type of store?

SELECT
    dim_store_details.store_type AS store_type,
    ROUND(SUM(orders_table.product_quantity * dim_products.product_price)::numeric, 2) AS total_sales,
    ROUND((SUM(orders_table.product_quantity * dim_products.product_price)/
        (SELECT 
            SUM(orders_table.product_quantity * dim_products.product_price)
        FROM 
            orders_table
        JOIN dim_products ON orders_table.product_code = dim_products.product_code) * 100)::numeric, 2) 
    AS "percentage_total(%)"
FROM 
    orders_table
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
JOIN 
    dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY
    store_type
ORDER BY
    "percentage_total(%)" DESC;


--Task 6: Which month in each year produced the highest cost of sales?

SELECT
    ROUND(SUM(orders_table.product_quantity * dim_products.product_price)::numeric, 2) AS total_sales,
    dim_date_times.year AS year,
    dim_date_times.month AS month
FROM 
    orders_table
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
JOIN 
    dim_date_times ON orders_table.date_uuid = dim_date_times.date_uuid
GROUP BY
    year, month
ORDER BY
    total_sales DESC
LIMIT 10;


--Task 7: What is our staff headcount?

SELECT
    SUM(staff_numbers) AS total_staff_numbers,
    country_code as country_code
FROM   
    dim_store_details
GROUP BY
    country_code
ORDER BY
    total_staff_numbers DESC;


--Task 8: Which German store type is selling the most?

SELECT
    ROUND(SUM(orders_table.product_quantity * dim_products.product_price)::numeric, 2) AS total_sales,
    dim_store_details.store_type AS store_type,
    dim_store_details.country_code AS country_code
FROM 
    orders_table
JOIN 
    dim_products ON orders_table.product_code = dim_products.product_code
JOIN 
    dim_store_details ON orders_table.store_code = dim_store_details.store_code
WHERE 
    dim_store_details.country_code = 'DE'
GROUP BY
    store_type, country_code 
ORDER BY
    total_sales ASC


--Task 9: How quickly is the company making sales?

WITH sales_date AS (
    SELECT 
        year,
        sales_date_column,
        LEAD(sales_date_column) OVER (PARTITION BY year ORDER BY sales_date_column) - sales_date_column AS time_between_sales
    FROM (
        SELECT 
            year,
            (CONCAT(year, '-', month, '-', day, ' ', timestamp))::TIMESTAMP AS sales_date_column
        FROM 
            dim_date_times
    )

)
SELECT 
    year,
    AVG(time_between_sales) AS average_time_taken
FROM 
    sales_date
GROUP BY 
    year
ORDER BY 
    average_time_taken DESC
LIMIT 5;


