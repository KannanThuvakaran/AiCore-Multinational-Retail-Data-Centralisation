-- Modify dim_date_times table structure and data

-- Display information about the maximum lengths of columns in dim_date_times
SELECT 
    MAX(LENGTH(month)) AS month_code_max,
    MAX(LENGTH(year)) AS year_code_max,
    MAX(LENGTH(day)) AS day_class_code_max,
    MAX(LENGTH(time_period)) AS time_period_class_code_max
FROM dim_date_times;

-- Alter the data types of certain columns in dim_date_times
ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(2),
ALTER COLUMN year TYPE VARCHAR(4),
ALTER COLUMN day TYPE VARCHAR(2),
ALTER COLUMN time_period TYPE VARCHAR(10),
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;
