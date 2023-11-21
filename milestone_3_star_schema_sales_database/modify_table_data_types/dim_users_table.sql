-- Alter columns in dim_users_table to update data types
ALTER TABLE dim_users_table
  ALTER first_name TYPE VARCHAR(255),
  ALTER last_name TYPE VARCHAR(255),
  ALTER date_of_birth TYPE DATE,
  ALTER country_code TYPE VARCHAR(2),
  ALTER user_uuid TYPE UUID USING user_uuid::uuid,
  ALTER join_date TYPE DATE;
