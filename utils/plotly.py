'''
Simple plotly helpers
'''
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def live_plot(data):
  time_column = 'Datetime' if 'Datetime' in data.columns else 'Date'
  fig = make_subplots(specs=[[{'secondary_y': True}]])
  fig.add_trace(go.Candlestick(
    x = data[time_column],
    open = data['Open'], high = data['High'],
    low = data['Low'], close=data['Close']),
    secondary_y = True)
  fig.add_trace(
    go.Bar(x = data[time_column], y=data['Volume']), secondary_y=False)
  fig.layout.yaxis2.showgrid=False
  fig.update_xaxes(
        rangeslider_visible=True,
        rangebreaks=[
          dict(bounds=['sat', 'mon']),  # hide weekends
          dict(bounds=[16, 9.5], pattern='hour'),  # hide after hours
        ])
  fig.update(layout_showlegend=False)
  fig.update_layout(width=1900, height=600,
    margin={ 'l': 40, 'r': 40, 't': 10, 'b': 10 })
  fig.data[0].increasing.line.color = '#26a69a'
  fig.data[0].decreasing.line.color = '#ef5350'
  return fig
