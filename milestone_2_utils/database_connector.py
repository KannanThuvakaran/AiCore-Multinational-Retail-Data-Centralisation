import yaml
from sqlalchemy import create_engine, inspect
import pandas as pd

class DatabaseConnector:
    """
    Connect to a PostgreSQL database, read database credentials from a YAML file,
    initialize a database engine, list database tables, and upload a clean DataFrame to a specified table.

    Parameters:
    - file (str): Path to the YAML file containing database credentials.

    Attributes:
    - file (str): Path to the YAML file containing database credentials.
    - db_creds (dict): Dictionary containing database credentials.
    - db_engine (sqlalchemy.engine.Engine): SQLAlchemy database engine.
    - db_table_list (list): List of table names in the connected database.
    """

    def __init__(self, file=None):
        """
        Initialize DatabaseConnector instance.

        Parameters:
        - file (str): Path to the YAML file containing database credentials.
        """
        self.file = file
        self.db_creds = self.read_db_creds()
        self.db_engine = self.init_db_engine()
        self.db_table_list = self.list_db_tables()

    def read_db_creds(self):
        """
        Read database credentials from the YAML file.

        Returns:
        - dict: Dictionary containing database credentials.
        """
        with open(self.file, 'r') as f:
            db_creds = yaml.safe_load(f)
        return db_creds
    
    def init_db_engine(self):
        """
        Initialize the SQLAlchemy database engine.

        Returns:
        - sqlalchemy.engine.Engine: SQLAlchemy database engine.
        """
        db_engine = create_engine(f"postgresql://{self.db_creds['RDS_USER']}:{self.db_creds['RDS_PASSWORD']}@{self.db_creds['RDS_HOST']}:{self.db_creds['RDS_PORT']}/{self.db_creds['RDS_DATABASE']}")
        return db_engine

    def list_db_tables(self):
        """
        List table names in the connected database.

        Returns:
        - list: List of table names.
        """
        insp = inspect(self.db_engine)
        db_table_list = insp.get_table_names()
        return db_table_list
    
    def upload_to_db(self, clean_dataframe, table_name):
        """
        Upload a clean DataFrame to the specified table in the database.

        Parameters:
        - clean_dataframe (pd.DataFrame): Cleaned DataFrame to upload.
        - table_name (str): Name of the table to upload the DataFrame.

        Returns:
        - str: Information about the upload process.
        """
        db_to_sql = clean_dataframe.to_sql(table_name, self.db_engine, if_exists='replace', index=False)
        return db_to_sql

