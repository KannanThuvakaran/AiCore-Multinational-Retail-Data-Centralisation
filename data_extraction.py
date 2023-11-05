import pandas as pd
import tabula
import requests
import json

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
        store_df = []
        for store_number in range(number_of_stores):
            response = requests.get(f'{store_endpoint}{store_number}', headers=header).json()
            store = pd.json_normalize(response)
            store_df.append(store)
        stores_df = pd.concat(store_df).set_index('index')
        return stores_df

number_of_stores = DataExtractor().list_number_of_stores('https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores', headers)
stores_data = DataExtractor().retrieve_stores_data(f'https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/', number_of_stores, headers)

stores_data