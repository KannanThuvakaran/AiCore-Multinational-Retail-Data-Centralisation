import pandas as pd
from dateutil.parser import parse
    
class DataCleaning:
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def clean_user_data(self):
        # Remove NULL values and duplicates
        self.dataframe = self.dataframe.dropna().drop_duplicates()

        # Clean country code
        self.dataframe['country_code'] = self.dataframe['country_code'].replace('GGB', 'GB')
        self.dataframe = self.dataframe[self.dataframe['country_code'].str.len() == 2]

        # Clean dates
        self.dataframe.loc[:,'date_of_birth'] = pd.to_datetime(self.dataframe['date_of_birth'].apply(parse))
        self.dataframe.loc[:,'join_date'] = pd.to_datetime(self.dataframe['join_date'].apply(parse))

        # Clean phone numbers
        regex = '^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$'
        self.dataframe.loc[:,'phone_number'] = self.dataframe['phone_number'].str.replace('(0)', '', regex=False)
        self.dataframe.loc[:,'phone_number'] = self.dataframe['phone_number'].replace(r'\D+', '', regex=True)

        return self.dataframe

    def clean_card_data(self):
        card_provider_list = ['Diners Club / Carte Blanche', 'American Express', 'JCB 16 digit',
                             'JCB 15 digit', 'Maestro', 'Mastercard', 'Discover',
                             'VISA 19 digit', 'VISA 16 digit', 'VISA 13 digit']

        # Filter card data based on card providers
        self.dataframe = self.dataframe[self.dataframe['card_provider'].isin(card_provider_list)]

        # Clean and format date columns
        self.dataframe.loc[:,'expiry_date'] = pd.to_datetime(self.dataframe['expiry_date'], errors='coerce', format='%m/%y')
        self.dataframe.loc[:,'date_payment_confirmed'] = pd.to_datetime(self.dataframe['date_payment_confirmed'], errors='coerce', format='%Y-%m-%d')

        # Drop NULL values and duplicates
        self.dataframe = self.dataframe.dropna().drop_duplicates()

        return self.dataframe

