import pandas as pd
import tabula
import requests
import json
import boto3

headers = {'x-api-key': 'yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX'}

class DataExtractor:
    def __init__(self, database=None):
        self.database = database

    def read_rds_table(self, table_name):
        table_data = pd.read_sql_table(table_name, self.database).set_index('index')
        return table_data

    def retrieve_pdf_data(self, pdf_path):
        pdf_df_page = tabula.read_pdf(pdf_path, pages='all')
        pdf_df = pd.concat(pdf_df_page, ignore_index=True)
        return pdf_df
    
    def list_number_of_stores(self, number_of_stores_endpoint, header):
        response = requests.get(number_of_stores_endpoint, headers=header)
        number_of_stores_data = response.json()
        return number_of_stores_data['number_stores']
    
    def retrieve_stores_data(self, store_endpoint, number_of_stores, header):
        store_data = []

        for store_number in range(number_of_stores):
            response = requests.get(f'{store_endpoint}{store_number}', headers=header)
            store_data.append(response.json())

        stores_df = pd.json_normalize(store_data).set_index('index')
        return stores_df
    
    def extract_from_s3(s3_path, local_path):
    # Split S3 path into bucket and key
        bucket, key = s3_path.replace('s3://', '').split('/')   
    # Create an S3 client
        s3 = boto3.client('s3')
    
    # Download the file from S3
        s3.download_file(bucket, key, local_path)
    
    # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(local_path, index_col=0)
    
        return df



number_of_stores = DataExtractor().list_number_of_stores('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores', headers)
stores_data = DataExtractor().retrieve_stores_data(f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/', number_of_stores, headers)

stores_data
