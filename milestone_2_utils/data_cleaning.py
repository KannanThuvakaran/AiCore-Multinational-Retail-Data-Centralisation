import pandas as pd
from dateutil.parser import parse

class DataCleaning:
    def __init__(self, dataframe):
        """
        Initialize DataCleaning instance.

        Parameters:
        - dataframe (pd.DataFrame): Input DataFrame to be cleaned.
        """
        self.dataframe = dataframe

    def _clean_country_code(self):
        """
        Clean the 'country_code' column by replacing 'GGB' with 'GB'
        and filtering rows based on the length of 'country_code'.
        """
        self.dataframe['country_code'] = self.dataframe['country_code'].replace('GGB', 'GB')
        self.dataframe = self.dataframe[self.dataframe['country_code'].str.len() == 2]

    def _clean_dates(self):
        """
        Parse and clean date columns ('date_of_birth' and 'join_date').
        """
        self.dataframe.loc[:,'date_of_birth'] = pd.to_datetime(self.dataframe['date_of_birth'].apply(parse))
        self.dataframe.loc[:,'join_date'] = pd.to_datetime(self.dataframe['join_date'].apply(parse))

    def _clean_phone_numbers(self):
        """
        Clean the 'phone_number' column by removing '(0)' and non-digit characters.
        """
        regex = '^(\(?\+?[0-9]*\)?)?[0-9_\- \(\)]*$'
        self.dataframe.loc[:,'phone_number'] = self.dataframe['phone_number'].str.replace('(0)', '', regex=False)
        self.dataframe.loc[:,'phone_number'] = self.dataframe['phone_number'].replace(r'\D+', '', regex=True)

    def clean_user_data(self):
        """
        Clean user-related data, including country code, dates, and phone numbers.
        """
        self.dataframe = self.dataframe.dropna().drop_duplicates()
        self._clean_country_code()
        self._clean_dates()
        self._clean_phone_numbers()
        return self.dataframe

    def _filter_card_data(self):
        """
        Filter card data based on a predefined list of card providers.
        """
        card_provider_list = ['Diners Club / Carte Blanche', 'American Express', 'JCB 16 digit',
                             'JCB 15 digit', 'Maestro', 'Mastercard', 'Discover',
                             'VISA 19 digit', 'VISA 16 digit', 'VISA 13 digit']
        self.dataframe = self.dataframe[self.dataframe['card_provider'].isin(card_provider_list)]

    def _clean_and_format_dates(self):
        """
        Clean and format date columns in card-related data.
        """
        self.dataframe.loc[:,'expiry_date'] = pd.to_datetime(self.dataframe['expiry_date'], errors = 'coerce', format='%m/%y')
        self.dataframe.loc[:,'date_payment_confirmed'] = pd.to_datetime(self.dataframe['date_payment_confirmed'], format='mixed')
    def _clean_card_number(self):
        """
        Clean the 'card_number' column by keeping only digits.
        """
        self.dataframe.loc[:, 'card_number'] = self.dataframe['card_number'].apply(lambda x: "".join(filter(str.isdigit, str(x)))) 

    def clean_card_data(self):
        """
        Clean card-related data, including filtering card providers, cleaning dates, and card numbers.
        """
        self._filter_card_data()
        self._clean_and_format_dates()
        self._clean_card_number()
        self.dataframe = self.dataframe = self.dataframe.drop_duplicates()
        return self.dataframe

    def clean_store_data(self):
        """
        Clean store-related data, including country code, dates, and staff numbers.
        """
        self.dataframe = self.dataframe[self.dataframe['country_code'].str.len() == 2]
        self.dataframe.loc[:, 'opening_date'] = pd.to_datetime(self.dataframe['opening_date'], format='mixed')
        self.dataframe.loc[:, 'continent'] = self.dataframe['continent'].replace(['eeEurope', 'eeAmerica'], ['Europe', 'America'])
        self.dataframe = self.dataframe.drop(columns='lat')
        self.dataframe['staff_numbers'] = self.dataframe['staff_numbers'].apply(lambda x: "".join(filter(str.isdigit, str(x))))
        self.dataframe = self.dataframe.drop_duplicates()
        return self.dataframe

    def _convert_product_weights(self):
        """
        Convert and clean the 'weight' column for product-related data.
        """
        replacements = {
            'kg': '',
            'g': '/1000',
            'ml': '/1000',
            'x': '*',
            'oz': '/35.274',
            '77/1000 .': '77/1000'
        }
        self.dataframe.loc[:,'weight'] = self.dataframe['weight'].replace(replacements, regex=True)
        self.dataframe.loc[:,'weight'] = self.dataframe['weight'].str.replace('77/1000 .', '77/1000', regex=True)
        self.dataframe.loc[:,'weight'] = self.dataframe['weight'].apply(lambda x: eval(str(x))).astype(float)
        return self.dataframe

    def clean_products_data(self):
        """
        Clean product-related data, including filtering by 'removed' column and converting weights.
        """
        self.dataframe.loc[:,'removed'] = self.dataframe['removed'].str.replace('Still_avaliable', 'Still_available')
        self.dataframe = self.dataframe[self.dataframe['removed'].isin(['Still_available', 'Removed'])]
        self.dataframe.loc[:, 'date_added'] = pd.to_datetime(self.dataframe['date_added'], errors='coerce', format='%Y-%m-%d')
        self.dataframe = self._convert_product_weights()
        return self.dataframe

    def clean_orders_data(self):
        """
        Clean order-related data by dropping specific columns and removing duplicates.
        """
        self.dataframe = self.dataframe.drop(columns=['level_0', 'first_name', 'last_name', '1'])
        self.dataframe = self.dataframe.drop_duplicates()
        return self.dataframe

    def clean_date_times(self):
        """
        Clean date-time-related data by filtering rows with 'day' length less than or equal to 2,
        dropping null values, and removing duplicates.
        """
        self.dataframe = self.dataframe[self.dataframe['day'].apply(lambda x: len(str(x)) <= 2)]
        self.dataframe = self.dataframe.dropna().drop_duplicates()
        return self.dataframe


