'''
Simple plotly helpers
'''
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.colors as clrs
from itertools import cycle

COLOR_CYCLE = cycle(clrs.DEFAULT_PLOTLY_COLORS)

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
  hide_range = [dict(bounds=['sat', 'mon'])]
  if time_column == 'Datetime':
    hide_range.append(dict(bounds=[16, 9.5], pattern='hour'))
  fig.update_xaxes(
        rangeslider_visible=False,
        rangebreaks=hide_range)
  fig.update(layout_showlegend=False)
  fig.update_layout(width=1900, height=600,
    margin={ 'l': 40, 'r': 40, 't': 0, 'b': 10 })
  fig.data[0].increasing.line.color = '#26a69a'
  fig.data[0].decreasing.line.color = '#ef5350'
  return fig

def add_indices(fig, indices):
  for index in indices:
    time_column = 'Datetime' if 'Datetime' in index.columns else 'Date'
    color = next(COLOR_CYCLE)
    fig.add_trace(go.Scatter(x = index[time_column], y=index['ScaledOpen'],
      mode='markers', marker=dict(opacity=0.3, size=4, color=color)),
      secondary_y = True)
    fig.add_trace(go.Scatter(x = index[time_column], y=index['MA5'],
      mode='lines', connectgaps=True, line=dict(width=1.8, color=color)),
      secondary_y = True)
