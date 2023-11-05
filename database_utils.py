import yaml
from sqlalchemy import create_engine, inspect

class DatabaseConnector:
    def __init__(self, file=None):
        self.file = file
        self.db_creds = self.read_db_creds()
        self.db_engine = self.init_db_engine()
        self.db_table_list = self.list_db_tables()

    def read_db_creds(self):
        with open(self.file, 'r') as f:
            db_creds = yaml.safe_load(f)
            return db_creds
    
    def init_db_engine(self):
        db_engine = create_engine(f"postgresql://{self.db_creds['RDS_USER']}:{self.db_creds['RDS_PASSWORD']}@{self.db_creds['RDS_HOST']}:{self.db_creds['RDS_PORT']}/{self.db_creds['RDS_DATABASE']}")
        return db_engine

    def list_db_tables(self):
        insp = inspect(self.db_engine)
        db_table_list = insp.get_table_names()
        return db_table_list
    
    def upload_to_db(self, clean_dataframe, table_name):
        db_to_sql = clean_dataframe.to_sql(table_name, self.db_engine, if_exists='replace', index=False)
        return db_to_sql
    

