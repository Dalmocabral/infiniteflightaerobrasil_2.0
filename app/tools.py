from datetime import timedelta, time
from flask_babel import format_timedelta

def get_all_time(logbooks):
    counter = timedelta()
    for logbook in logbooks:
        t = timedelta(
            hours=int(logbook.tempo.hour),
            minutes=int(logbook.tempo.minute),
            seconds=int(logbook.tempo.second),
        )
        counter += t
    return format_timedelta(counter)
