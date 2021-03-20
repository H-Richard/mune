'''
App entrypoint
'''
import streamlit as st

# pylint: disable=wildcard-import unused-wildcard-import
from utils.datetime import *
from utils.yfinance import load_data
from utils.fbprophet import forecast_raw

from fbprophet.plot import plot_plotly

st.title('MUNE: Stock Analytics')
ticker = st.text_input('Enter a ticker', 'SHOP')
end_time = st.slider('Forecast end date:', TWO_DAYS_FROM_TODAY,
                    TWO_YEARS_FROM_TODAY, value=SIXTY_DAYS_FROM_TODAY)

load_state = st.text('Loading data...')
data_start = data_start_date(end_time)
data = load_data(ticker, data_start)

spx = load_data('^GSPC', data_start)
nasdaq = load_data('^IXIC', data_start)
load_state.text('Loading data... Done!')


load_state.text('Training data...')
m, forecast = forecast_raw(data, total_duration(end_time))
load_state.text('Training data... Done!')

st.subheader('Price Forecast')

fig = plot_plotly(m, forecast)
st.plotly_chart(fig, use_container_width=True)
