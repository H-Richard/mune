'''
Simple yfinance helpers
'''
import yfinance as yf
import streamlit as st
from utils.datetime import smallest_interval, TODAY

DATE_FORMAT = '%Y-%m-%d'
INDICES = ['BTC-USD', '^GSPC', '^IXIC', '^FTSE']
DATE_FORMAT = '%Y-%m-%d'

@st.cache(allow_output_mutation=True)
def load_data(ticker, start):
  return yf.download(ticker, start.strftime(DATE_FORMAT),
                    TODAY.strftime(DATE_FORMAT),
                    interval=smallest_interval(start)).reset_index()

# Returns a list of data for popular stock indices
def load_indices(start):
  load = lambda x: load_data(x, start)
  return dict(zip(INDICES, [load(index) for index in INDICES]))
