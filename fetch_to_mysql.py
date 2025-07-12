import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine

# --- CONFIGURATION ---
TICKER = 'AAPL'  # Change to any ticker you want
PERIOD = '60d'   # e.g., '1y', '5y', 'max'
INTERVAL = '1d'  # e.g., '1d', '1h', '5m'

# SQLite configuration (much simpler!)
DB_PATH = 'data/financial_data.db'
TABLE_NAME = 'historical_prices'

# --- FETCH DATA ---
df = yf.download(TICKER, period=PERIOD, interval=INTERVAL)
if df is None or df.empty:
    raise ValueError(f"No data returned for ticker {TICKER}")
df = df.reset_index()
df['ticker'] = TICKER
df = df[['ticker', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']]
df.columns = ['ticker', 'date', 'open', 'high', 'low', 'close', 'volume']

# --- INSERT INTO SQLite ---
engine = create_engine(f'sqlite:///{DB_PATH}')
df.to_sql(TABLE_NAME, con=engine, if_exists='append', index=False)

print(f"Inserted {len(df)} rows for {TICKER} into {TABLE_NAME}.")
