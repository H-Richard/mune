"""
Simple datetime helpers
"""
from datetime import timedelta, date

TODAY = date.today()
TWO_DAYS_FROM_TODAY = TODAY + timedelta(days=2)
SIXTY_DAYS_FROM_TODAY = TODAY + timedelta(days=60)
TWO_YEARS_FROM_TODAY = TODAY + timedelta(days=730)

def smallest_interval(start, end=TODAY):
  # valid intervals: [1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo]
  duration = end - start
  # wont be triggered currently.
  if duration <= timedelta(days=7):
    return "1m"
  if duration <= timedelta(days=60):
    return "5m"
  if duration <= timedelta(days=730):
    return "60m"
  return "1d"

def data_start_date(end):
  return date.today() - (end - date.today()) * 6

def total_duration(end):
  return end - TODAY
