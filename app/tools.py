from datetime import timedelta
import arrow


def get_all_time(logbooks):
    counter = timedelta()
    for logbook in logbooks:
        t = timedelta(
            hours=int(logbook.tempo.hour),
            minutes=int(logbook.tempo.minute),
            seconds=int(logbook.tempo.second),
        )
        counter += t
    time =  (counter.total_seconds() / 3600)

    return '{0:02.0f}:{1:02.0f}:00'.format(*divmod(float(time) * 60, 60))

def get_all_time2(logbooks):
    counter = timedelta()
    for logbook in logbooks:
        t = timedelta(
            hours=int(logbook.tempo.hour),
            minutes=int(logbook.tempo.minute),
            seconds=int(logbook.tempo.second),
        )
        counter += t
    time =  (counter.total_seconds() / 3600)
    return time