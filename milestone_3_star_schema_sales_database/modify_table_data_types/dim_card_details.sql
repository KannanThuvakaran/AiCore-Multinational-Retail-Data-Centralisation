-- Modify dim_card_details table structure and data

-- Alter the data type of the expiry_date column to VARCHAR(255)
ALTER TABLE dim_card_details
ALTER expiry_date TYPE VARCHAR(255);

-- Display information about the maximum lengths of columns in dim_card_details
SELECT 
    MAX(LENGTH(card_number)) AS card_number_max,
    MAX(LENGTH(expiry_date)) AS expiry_date_max
FROM dim_card_details;

-- Alter the data types of certain columns in dim_card_details
ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE VARCHAR(19),
ALTER COLUMN expiry_date TYPE VARCHAR(19),
ALTER COLUMN date_payment_confirmed TYPE DATE;
