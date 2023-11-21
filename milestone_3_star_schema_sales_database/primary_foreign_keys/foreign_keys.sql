-- Add Foreign Keys for orders_table
ALTER TABLE orders_table
ADD CONSTRAINT orders_user_id FOREIGN KEY (user_uuid) REFERENCES dim_users_table(user_uuid);

ALTER TABLE orders_table
ADD CONSTRAINT orders_store_id FOREIGN KEY (store_code) REFERENCES dim_store_details(store_code);

ALTER TABLE orders_table
ADD CONSTRAINT orders_product_id FOREIGN KEY (product_code) REFERENCES dim_products(product_code);

ALTER TABLE orders_table
ADD CONSTRAINT orders_date_id FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);

ALTER TABLE orders_table
ADD CONSTRAINT orders_card_number_id FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);
