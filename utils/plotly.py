'''
Simple plotly helpers
'''
import plotly.graph_objects as go
from itertools import cycle

COLOR_CYCLE = cycle([
    '#1f77b4',  # ocean blue
    '#9467bd',  # muted purple
    '#17becf',  # lighter blue
    '#e377c2',  # raspberry yogurt pink
    '#00cc96',  # more or less green
    '#7f7f7f',  # middle gray
    '#bcbd22',  # curry yellow-green
    ])

def live_plot(fig, data):
  time_column = 'Datetime' if 'Datetime' in data.columns else 'Date'
  fig.add_trace(go.Bar(
    name = 'volume', x = data[time_column], showlegend=False,
    y=data['Volume']), secondary_y=False)
  fig.add_trace(go.Candlestick(
    name = 'live data',
    x = data[time_column], showlegend=False,
    open = data['Open'], high = data['High'],
    low = data['Low'], close=data['Close']),
    secondary_y = True)
  fig.layout.yaxis2.showgrid=False
  hide_range = [dict(bounds=['sat', 'mon'])]
  if time_column == 'Datetime':
    hide_range.append(dict(bounds=[16, 9.5], pattern='hour'))
  fig.update_xaxes(
        rangeslider_visible=False,
        rangebreaks=hide_range)
  fig.update_layout(legend=dict(
    orientation='h',
    yanchor='bottom',
    y=1.02,
    xanchor='right',
    x=1
))
  fig.update_layout(width=1900, height=600,
    margin={ 'l': 40, 'r': 40, 't': 0, 'b': 10 })
  fig.data[len(fig.data) - 1].increasing.line.color = '#26a69a'
  fig.data[len(fig.data) - 1].decreasing.line.color = '#ef5350'
  return fig

def add_indices(fig, indices):
  for (ticker, index) in indices.items():
    time_column = 'Datetime' if 'Datetime' in index.columns else 'Date'
    color = next(COLOR_CYCLE)
    fig.add_trace(go.Scatter(
      name=f'{ticker} scaled open',
      x = index[time_column], y=index['ScaledOpen'], mode='markers',
      marker=dict(opacity=0.3, size=4, color=color), showlegend=False),
      secondary_y = True)
    fig.add_trace(go.Scatter(
      name=f'{ticker} MA5', x = index[time_column], y=index['MA5'],
      mode='lines', connectgaps=True, line=dict(width=1.8, color=color)),
      secondary_y = True)
  return fig
