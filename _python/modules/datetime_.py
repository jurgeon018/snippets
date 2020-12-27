import datetime
import pytz

datetime.date(2019, 3, 15)
tday = datetime.date.today()
tday.day
tday.month
tday.year
tday.weekday()  # monday 0
tday.isoweekday()  # monday 1
tdelta = datetime.timedelta(days=7)
(tday + tdelta)

datetime.date(2019, 3, 15)
datetime.time(9, 2, 45, 10000)
dt = datetime.datetime(2019, 3, 15, 12, 30, 45, tzinfo=pytz.UTC)
dt.time()
dt.year
dt_today = datetime.datetime.today()
dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
dt_uk = dt_utcnow.astimezone(pytz.timezone('Europe/Kiev'))
print(dt_uk)
