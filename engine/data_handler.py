import pandas as pd

class DataHandler:
    def __init__(self, data):
        # data can be either a filepath (string) or a DataFrame
        if isinstance(data, str):
            self.data = pd.read_csv(data, parse_dates=['Date'], index_col='Date')
        else:
            self.data = data
    def get_data(self):
        return self.data
