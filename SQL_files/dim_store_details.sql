SELECT MAX(LENGTH(store_code)) AS store_code_max
FROM dim_store_details;

ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE FLOAT USING NULLIF(longitude, 'N/A')::float;

UPDATE dim_store_details
SET 
    latitude = NULLIF(longitude,'N/A')::FLOAT
WHERE longitude = 'N/A';

ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE FLOAT USING longitude::float,
ALTER COLUMN locality TYPE VARCHAR(255),
ALTER COLUMN store_code TYPE VARCHAR(12), 
ALTER COLUMN staff_numbers TYPE SMALLINT USING staff_numbers::smallint,
ALTER COLUMN opening_date TYPE DATE,
ALTER COLUMN store_type TYPE VARCHAR(255),
ALTER COLUMN latitude TYPE FLOAT USING latitude::float,
ALTER COLUMN country_code TYPE VARCHAR(2), 
ALTER COLUMN continent TYPE VARCHAR(255);

SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_store_details';

SELECT *
FROM dim_store_details;

ALTER TABLE dim_store_details
ADD CONSTRAINT store_id PRIMARY KEY (store_code);