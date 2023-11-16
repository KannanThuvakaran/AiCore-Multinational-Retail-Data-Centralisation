ALTER TABLE dim_users_table
ALTER first_name TYPE VARCHAR(255),
ALTER last_name TYPE VARCHAR(255),
ALTER date_of_birth TYPE DATE,
ALTER country_code TYPE VARCHAR(2),
ALTER user_uuid TYPE UUID USING user_uuid::uuid,
ALTER join_date TYPE DATE;

SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_users_table';

SELECT *
FROM dim_users_table;

ALTER TABLE dim_users_table
ADD CONSTRAINT users_id PRIMARY KEY (user_uuid);

