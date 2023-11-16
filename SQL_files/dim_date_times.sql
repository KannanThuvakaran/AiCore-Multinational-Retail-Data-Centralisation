SELECT 
    MAX(LENGTH(month)) AS month_code_max,
    MAX(LENGTH(year)) AS year_code_max,
    MAX(LENGTH(day)) AS day_class_code_max,
    MAX(LENGTH(time_period)) AS time_period_class_code_max
FROM dim_date_times;

ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR(2),
ALTER COLUMN year TYPE VARCHAR(4),
ALTER COLUMN day TYPE VARCHAR(2),
ALTER COLUMN time_period TYPE VARCHAR(10),
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID

SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_date_times';

SELECT * FROM dim_date_times;

ALTER TABLE dim_date_times
ADD CONSTRAINT date_id PRIMARY KEY (date_uuid);