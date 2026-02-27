import yfinance as yf
import pandas as pd
import requests
from io import StringIO

def createHistPrices (start_date = '2000-01-01', end_date = '2026-02-17'):

    historical_prices = pd.read_csv(
    "sp500_close_prices.csv",
    index_col="Date",
    parse_dates=True
    )

    MIN_REQUIRED_NUM_OBS_PER_TICKET = 100

    ticker_counts = historical_prices.count()

    valid_tickers_mask = ticker_counts[ticker_counts >= MIN_REQUIRED_NUM_OBS_PER_TICKET].index

    historical_prices = historical_prices[valid_tickers_mask]

    return historical_prices