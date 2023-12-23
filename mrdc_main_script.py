from milestone_2_utils.database_connector import DatabaseConnector
from milestone_2_utils.data_extraction import DataExtractor
from milestone_2_utils.data_cleaning import DataCleaning


if __name__ == "__main__":
    # Connect to the AICore database 
    aicore_db_connector = DatabaseConnector(file='db_creds.yaml')
    aicore_database = aicore_db_connector.init_db_engine()

    # Connect to my sales data database 
    sales_data_db_connector = DatabaseConnector(file='sales_data_creds.yaml')
    sales_data_database = sales_data_db_connector.init_db_engine()

    # Extract and clean user data from AICore database
    user_data_df = DataExtractor(aicore_database).read_rds_table('legacy_users')
    cleaned_user_df = DataCleaning(user_data_df).clean_user_data()
    user_data_to_sql = sales_data_db_connector.upload_to_db(cleaned_user_df, 'dim_users_table')

    # Extract, clean, and upload card details to sales data database
    pdf_file = DataExtractor().retrieve_pdf_data("https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
    cleaned_card_df = DataCleaning(dataframe=pdf_file).clean_card_data()
    card_details_to_sql = sales_data_db_connector.upload_to_db(cleaned_card_df, 'dim_card_details')

    # List number of stores, retrieve store data, clean, and upload to sales data database and put your api-key
    number_of_stores = DataExtractor().list_number_of_stores('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores', header={'x-api-key': 'your-api-key'})
    stores_data = DataExtractor().retrieve_stores_data(f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/', number_of_stores, header={'x-api-key': 'your-api-key'})
    cleaned_stores_data = DataCleaning(stores_data).clean_store_data()
    store_data_to_sql = sales_data_db_connector.upload_to_db(cleaned_stores_data, 'dim_store_details')

    # Extract from S3, clean products data, and upload to sales data database
    s3_df = DataExtractor().extract_from_s3('s3://data-handling-public/products.csv', local_path='products.csv', file_format='csv')
    cleaned_s3_data = DataCleaning(s3_df).clean_products_data()
    products_df = sales_data_db_connector.upload_to_db(cleaned_s3_data, 'dim_products')

    # Extract, clean, and upload orders data to sales data database
    orders_data_df = DataExtractor(aicore_database).read_rds_table('orders_table')
    cleaned_orders_df = DataCleaning(orders_data_df).clean_orders_data()
    orders_data_to_sql = sales_data_db_connector.upload_to_db(cleaned_orders_df, 'orders_table')

    # Extract from S3, clean date times, and upload to sales data database
    s3_json_df = DataExtractor().extract_from_s3('s3://data-handling-public/date_details.json', local_path='date_details.json', file_format='json')
    cleaned_date_times = DataCleaning(s3_json_df).clean_date_times()
    date_times_to_sql = sales_data_db_connector.upload_to_db(cleaned_date_times, 'dim_date_times')
