import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

def load_data_from_sqlite(ticker, db_path='data/financial_data.db'):
    engine = create_engine(f'sqlite:///{db_path}')
    query = f"""
    SELECT date, open, high, low, close, volume
    FROM historical_prices
    WHERE ticker = '{ticker}'
    ORDER BY date ASC
    """
    df = pd.read_sql(query, engine, parse_dates=['date'])
    df.set_index('date', inplace=True)
    return df

# Keep the old function name for compatibility
def load_data_from_mysql(ticker, host='localhost', user='your_username', 
password='your_password', database='your_database'):
    return load_data_from_sqlite(ticker)
