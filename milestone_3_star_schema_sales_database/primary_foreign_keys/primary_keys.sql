-- Add Primary Key for dim_card_details
ALTER TABLE dim_card_details
ADD CONSTRAINT card_number_id PRIMARY KEY (card_number);

-- Add Primary Key for dim_date_times
ALTER TABLE dim_date_times
ADD CONSTRAINT date_id PRIMARY KEY (date_uuid);

-- Add Primary Key for dim_products
ALTER TABLE dim_products
ADD CONSTRAINT product_id PRIMARY KEY (product_code);

-- Add Primary Key for dim_store_details
ALTER TABLE dim_store_details
ADD CONSTRAINT store_id PRIMARY KEY (store_code);

-- Add Primary Key for dim_users_table
ALTER TABLE dim_users_table
ADD CONSTRAINT users_id PRIMARY KEY (user_uuid);
