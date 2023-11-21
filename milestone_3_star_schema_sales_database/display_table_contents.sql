-- Display content for dim_card_details
SELECT * FROM dim_card_details;

-- Display content for dim_date_times
SELECT * FROM dim_date_times;

-- Display content for dim_products
SELECT * FROM dim_products;

-- Display content for dim_store_details
SELECT * FROM dim_store_details;

-- Display content for dim_users_table
SELECT * FROM dim_users_table;

-- Display content for orders_table
SELECT * FROM orders_table;

--

-- Display information for dim_card_details
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_card_details';

-- Display information for dim_date_times
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_date_times';

-- Display information for dim_products
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_products';

-- Display information for dim_store_details
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_store_details';

-- Display information for dim_users_table
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_users_table';

-- Display information for orders_table
SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'orders_table';