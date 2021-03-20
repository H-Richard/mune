"""
Simple yfinance helpers
"""
import yfinance as yf
from utils.datetime import smallest_interval, TODAY

DATE_FORMAT = "%Y-%m-%d"

def load_data(ticker, start):
  return yf.download(ticker, start.strftime(DATE_FORMAT),
                    TODAY.strftime(DATE_FORMAT),
                    interval=smallest_interval(start)).reset_index()
