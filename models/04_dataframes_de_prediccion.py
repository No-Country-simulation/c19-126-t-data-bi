# ========== Librerias ==========
import os,sys
sys.path.append(os.getcwd())
import pandas as pd
import numpy as np

# ---------- Descarga de acciones ----------
import yfinance as yf

# ========== Carga de datos ==========

stocks = {
    'AAPL': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'AMZN': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'GOOGL': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'JPM': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'META': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'MSFT': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'NVDA': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'TSLA': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'UNH': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'V': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'AIR': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'ASML': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'DTE': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'ITX': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'MC.PA': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'OR.PA': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'RMS.PA': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'SAP': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'SIE': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    'TTE': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    '0700.HK': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    '0857.HK': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    '0941.HK': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    '1398.HK': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    '3988.HK': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    '6758.T': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    '7203.T': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    '8306.T': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    '9432.T': {'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'},
    '9988.HK':{'start': '2014-06-30', 'end': '2024-06-28', 'interval': '1d'}
}

def download_stocks(stock_dict):
    """
    Downloads stock data for given stock symbols and saves them as CSV files.

    Parameters:
    stock_dict (dict): A dictionary where keys are stock symbols (str) and values are dictionaries 
                       with the following keys:
                       - 'start' (str): The start date for the data in 'YYYY-MM-DD' format.
                       - 'end' (str): The end date for the data in 'YYYY-MM-DD' format.
                       - 'interval' (str): The interval for the data (e.g., '1d', '1wk', '1mo').

    Returns:
    dict: A dictionary where keys are stock symbols and values are DataFrames containing the 
          downloaded stock data with 'Date' as the index.
    
    The function also saves each DataFrame as a CSV file in the directory 
    'c19-126-t-data-bi/files/datasets/input/forecasting' with the stock symbol as the filename.
    """
    stock_data = {}
    output_dir = 'c19-126-t-data-bi/files/datasets/input/forecasting'
    os.makedirs(output_dir, exist_ok=True)
    
    for symbol, params in stock_dict.items():
        df = yf.download(symbol, 
                         start=params['start'], 
                         end=params['end'], 
                         progress=False, 
                         interval=params['interval'])
        # df.index = df.iloc[:, 0]
        # df = df.iloc[:, 1:]
        stock_data[symbol] = df
        file_path = os.path.join(output_dir, f'{symbol}.csv')
        df.to_csv(file_path)
    
    return stock_data

# ========== Procesamiento ==========

download_stocks(stocks)
