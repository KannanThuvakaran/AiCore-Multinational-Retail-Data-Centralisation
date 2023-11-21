import pandas as pd
import tabula
import requests
import json
import boto3

class DataExtractor:
    def __init__(self, database=None):
        """
        Initialize the DataExtractor with a database connection.

        Parameters:
        - database: Database connection object.
        """
        self.database = database

    def read_rds_table(self, table_name):
        """
        Read data from an RDS table.

        Parameters:
        - table_name: Name of the RDS table.

        Returns:
        - pd.DataFrame: Data from the RDS table.
        """
        table_data = pd.read_sql_table(table_name, self.database).set_index('index')
        return table_data

    def retrieve_pdf_data(self, pdf_path):
        """
        Retrieve data from a PDF file.

        Parameters:
        - pdf_path: Path to the PDF file.

        Returns:
        - pd.DataFrame: Data from the PDF file.
        """
        pdf_df_page = tabula.read_pdf(pdf_path, pages='all')
        pdf_df = pd.concat(pdf_df_page, ignore_index=True)
        return pdf_df
    
    def list_number_of_stores(self, number_of_stores_endpoint, header):
        """
        List the number of stores.

        Parameters:
        - number_of_stores_endpoint: API endpoint for retrieving the number of stores.
        - header: Request header.

        Returns:
        - int: Number of stores.
        """
        response = requests.get(number_of_stores_endpoint, headers=header)
        number_of_stores_data = response.json()
        return number_of_stores_data['number_stores']
    
    def retrieve_stores_data(self, store_endpoint, number_of_stores, header):
        """
        Retrieve data for multiple stores.

        Parameters:
        - store_endpoint: API endpoint for retrieving store data.
        - number_of_stores: Number of stores to retrieve.
        - header: Request header.

        Returns:
        - pd.DataFrame: Data for multiple stores.
        """
        store_df = []
        for store_number in range(number_of_stores):
            response = requests.get(f'{store_endpoint}{store_number}', headers=header).json()
            store = pd.json_normalize(response)
            store_df.append(store)
        stores_df = pd.concat(store_df).set_index('index')
        return stores_df
    
    def extract_from_s3(self, s3_path, local_path, file_format):
        """
        Extract data from a file stored on Amazon S3.

        Parameters:
        - s3_path: S3 path to the file.
        - local_path: Local path to save the downloaded file.
        - file_format: Format of the file ('csv' or 'json').

        Returns:
        - pd.DataFrame: Data from the file.
        """
        bucket, key = s3_path.replace('s3://', '').split('/')   
        s3 = boto3.client('s3')
        s3.download_file(bucket, key, local_path)

        if file_format.lower() == 'csv':
            return pd.read_csv(local_path, index_col=0)
        elif file_format.lower() == 'json':
            return pd.read_json(local_path)
        else:
            raise ValueError("Unsupported file format. Only 'csv' or 'json' are supported.")

