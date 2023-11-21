-- Modify orders_table structure and data

-- Display information about the maximum lengths of columns in orders_table
SELECT 
    -- MAX(LENGTH(card_number)) AS card_number_max,
    MAX(LENGTH(store_code)) AS store_code_max,
    MAX(LENGTH(product_code)) AS product_code_max
FROM orders_table;

-- Alter the data types of certain columns in orders_table
ALTER TABLE orders_table
ALTER date_uuid TYPE UUID USING date_uuid::uuid,
ALTER user_uuid TYPE UUID USING user_uuid::uuid,
ALTER COLUMN card_number TYPE VARCHAR(19),
ALTER store_code TYPE VARCHAR(12),
ALTER product_code TYPE VARCHAR(11),
ALTER product_quantity TYPE SMALLINT USING product_quantity::smallint;


