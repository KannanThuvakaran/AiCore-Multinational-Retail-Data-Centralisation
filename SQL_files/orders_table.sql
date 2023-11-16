SELECT 
    MAX(LENGTH(card_number)) AS card_number_max,
    MAX(LENGTH(store_code)) AS store_code_max,
    MAX(LENGTH(product_code)) AS product_code_max
FROM orders_table;

ALTER TABLE orders_table
ALTER date_uuid TYPE UUID USING date_uuid::uuid,
ALTER user_uuid TYPE UUID USING user_uuid::uuid,
ALTER COLUMN card_number TYPE VARCHAR(19),
ALTER store_code TYPE VARCHAR(12),
ALTER product_code TYPE VARCHAR(11),
ALTER product_quantity TYPE SMALLINT USING product_quantity::smallint;

SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'orders_table';

SELECT * FROM orders_table

ALTER TABLE orders_table
ADD CONSTRAINT orders_user_id
FOREIGN KEY (user_uuid) REFERENCES dim_users_table(user_uuid);

ALTER TABLE orders_table
ADD CONSTRAINT orders_store_id
FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code);

ALTER TABLE orders_table
ADD CONSTRAINT orders_product_id
FOREIGN KEY (product_code) REFERENCES dim_products(product_code);

ALTER TABLE orders_table
ADD CONSTRAINT orders_date_id
FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);

ALTER TABLE orders_table
ADD CONSTRAINT orders_card_number_id
FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);
