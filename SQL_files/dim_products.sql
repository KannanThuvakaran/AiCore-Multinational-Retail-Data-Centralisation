UPDATE dim_products
    SET product_price = REPLACE(product_price, '£', '');

ALTER TABLE dim_products
    ADD COLUMN weight_class VARCHAR(14);

UPDATE dim_products
    SET weight_class = 
        CASE 
            WHEN weight < 2 THEN 'Light'
            WHEN weight BETWEEN 2 AND 40 THEN 'Mid_Sized'
            WHEN weight BETWEEN 40 AND 140 THEN 'Heavy'
            WHEN weight >= 140 THEN 'Truck_Required'
        END;

ALTER TABLE dim_products
    RENAME removed TO still_available;

ALTER TABLE dim_products
    ALTER COLUMN still_available TYPE BOOL
        USING (still_available = 'Still_available');

SELECT 
    MAX(LENGTH("EAN")) AS ean_code_max,
    MAX(LENGTH(product_code)) AS product_code_max,
    MAX(LENGTH(weight_class)) AS weight_class_code_max
FROM dim_products;


ALTER TABLE dim_products
    ALTER COLUMN product_price TYPE FLOAT USING product_price::float,
    ALTER COLUMN weight TYPE FLOAT USING weight::float,
    ALTER COLUMN "EAN" TYPE VARCHAR(17),
    ALTER COLUMN product_code TYPE VARCHAR(11), 
    ALTER COLUMN date_added TYPE DATE,
    ALTER COLUMN uuid TYPE UUID USING uuid::UUID,
    ALTER COLUMN still_available TYPE BOOL USING still_available::BOOL,
    ALTER COLUMN weight_class TYPE VARCHAR(14); 

SELECT *
FROM dim_products;

SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_products';

ALTER TABLE dim_products
ADD CONSTRAINT product_id PRIMARY KEY (product_code);