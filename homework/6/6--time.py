def timeToMidnight():
    # print(time.localtime())
    from datetime import datetime, timedelta, time

    now = datetime.now()
    midnight = datetime.combine(now + timedelta(days=1), time())
    until_midnight = (midnight - now)
    print(until_midnight)
