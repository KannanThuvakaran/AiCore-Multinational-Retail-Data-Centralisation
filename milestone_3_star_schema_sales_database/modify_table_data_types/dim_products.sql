-- Modify dim_products table structure and data

-- Update product_price by removing currency symbol '£'
UPDATE dim_products
SET product_price = REPLACE(product_price, '£', '');

-- Add a new column weight_class to categorize products based on weight
ALTER TABLE dim_products
ADD COLUMN weight_class VARCHAR(14);

-- Set values for the weight_class column based on weight ranges
UPDATE dim_products
SET weight_class = 
    CASE 
        WHEN weight < 2 THEN 'Light'
        WHEN weight BETWEEN 2 AND 40 THEN 'Mid_Sized'
        WHEN weight BETWEEN 40 AND 140 THEN 'Heavy'
        WHEN weight >= 140 THEN 'Truck_Required'
    END;

-- Rename the column 'removed' to 'still_available'
ALTER TABLE dim_products
RENAME removed TO still_available;

-- Convert the data type of still_available column to BOOL
ALTER TABLE dim_products
ALTER COLUMN still_available TYPE BOOL
    USING (still_available = 'Still_available');

-- Display information about the columns in dim_products
SELECT 
    MAX(LENGTH("EAN")) AS ean_code_max,
    MAX(LENGTH(product_code)) AS product_code_max,
    MAX(LENGTH(weight_class)) AS weight_class_code_max
FROM dim_products;

-- Further modify the table structure and clean specific columns
ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT USING product_price::float,
ALTER COLUMN weight TYPE FLOAT USING weight::float,
ALTER COLUMN "EAN" TYPE VARCHAR(17),
ALTER COLUMN product_code TYPE VARCHAR(11), 
ALTER COLUMN date_added TYPE DATE,
ALTER COLUMN uuid TYPE UUID USING uuid::UUID,
ALTER COLUMN still_available TYPE BOOL USING still_available::BOOL,
ALTER COLUMN weight_class TYPE VARCHAR(14); 
