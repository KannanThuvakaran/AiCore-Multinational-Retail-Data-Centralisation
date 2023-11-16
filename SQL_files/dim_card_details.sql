ALTER TABLE dim_card_details
ALTER expiry_date TYPE VARCHAR(255)

SELECT 
    MAX(LENGTH(card_number)) AS card_number_max,
    MAX(LENGTH(expiry_date)) AS expiry_date_max
FROM dim_card_details;

ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(19),
ALTER COLUMN expiry_date TYPE VARCHAR(19),
ALTER COLUMN date_payment_confirmed TYPE DATE;

SELECT column_name, data_type, character_maximum_length
FROM information_schema.columns
WHERE table_name = 'dim_card_details'

SELECT *
FROM dim_card_details

ALTER TABLE dim_card_details
ADD CONSTRAINT card_number_id PRIMARY KEY (card_number);