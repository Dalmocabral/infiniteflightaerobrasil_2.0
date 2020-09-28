from flask_babel import format_datetime, format_timedelta
import datetime

def init_app(app):
    app.jinja_env.filters['format_date'] = format_date
    app.jinja_env.filters['format_to_hours'] = format_to_hours


def format_date(date):
    return format_datetime(date, "short")

def format_to_hours(t):
    result = datetime.timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
    return format_timedelta(result)