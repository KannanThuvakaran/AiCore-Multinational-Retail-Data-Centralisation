-- Modify dim_store_details table structure

ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE FLOAT USING NULLIF(longitude, 'N/A')::float;

-- Further modify the table structure and clean specific columns
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
