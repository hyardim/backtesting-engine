import pandas as pd

class DataHandler:
    def __init__(self, filepath):
        self.data = pd.read_csv(filepath, parse_dates=['Date'], index_col='Date')
    def get_data(self):
        return self.data
