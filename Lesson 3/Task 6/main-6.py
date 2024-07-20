# Task 6
from datetime import datetime, timedelta


def date_range(start_date, end_date):
    current_date = start_date
    while current_date <= end_date:
        yield current_date
        current_date += timedelta(days=1)


start_date = datetime(2024, 7, 18)
end_date = datetime(2024, 7, 28)

for date in date_range(start_date, end_date):
    print(date)
