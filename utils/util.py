'''
General utility helpers
'''
import streamlit as st

@st.cache(show_spinner=False)
def scale_index_value(y, index_max, index_min, data_max, data_min):
  percentage_scale = (index_max / index_min) / (data_max / data_min)
  index_range = index_max - index_min
  data_range = data_max - data_min
  return ((y - index_min) * data_range) * percentage_scale / index_range \
    + data_min

@st.cache(show_spinner=False)
def scale_index(index, data_max, data_min):
  # pylint: disable=too-many-function-args
  scale = lambda y: scale_index_value(y, max(index['Open']), min(index['Open']),
    data_max, data_min)
  index['ScaledOpen'] = index['Open'].apply(scale)
  index['MA5'] = index['ScaledOpen'].rolling(5, min_periods=1).mean()
  return index

@st.cache(show_spinner=False)
def scale_indices(indices, data):
  data_max = max(data['Open'])
  data_min = min(data['Open'])
  scale = lambda t: scale_index(indices[t], data_max, data_min)
  return { ticker: scale(ticker) for ticker in indices }
