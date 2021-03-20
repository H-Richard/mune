'''
Simple fbprophet helpers
'''
from fbprophet import Prophet
import streamlit as st

@st.cache
def forecast_raw(data, duration):
  time_column = 'Datetime' if 'Datetime' in data.columns else 'Date'
  if time_column == 'Datetime':
    data[time_column] = data[time_column].dt.tz_localize(None)
  df_train = data[[time_column, 'Close']]\
    .rename(columns={time_column: 'ds', 'Close': 'y'})
  m = Prophet()
  m.fit(df_train)
  future = m.make_future_dataframe(duration.days)
  return m, m.predict(future)
