from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

halifax_tz = ZoneInfo("America/Halifax")
current_datetime = datetime.now(halifax_tz)
current_date = current_datetime.date()
current_month = current_date.replace(day=1)

tomorrow = current_date + timedelta(days=1)
next_month = (current_month + timedelta(days=31)).replace(day=1)
previous_month = (current_month - timedelta(days=1)).replace(day=1)

print(f'- current_datetime: {current_datetime}')
print(f'- current_date: {current_date}')
print(f'- current_month: {current_month}')
print(f'- tomorrow: {tomorrow}')
print(f'- next_month: {next_month}')
print(f'- previous_month: {previous_month}')
