from datetime import timedelta
from datetime import datetime
from datetime import date

todayDate = date.today()
todayDateTime = datetime.today()

#subtract hours, years to get the time delta
print(todayDateTime.year - todayDate.year)

#can assign a date
christmas = date(2018,10,25)
print(todayDate-christmas)

#create a time delta
eta = timedelta(days=2, hours=3)
#hours are actually seconds so cannot do .hours so to get hours must do some math
print(eta.seconds/3600)

eta = timedelta(hours=6)
#We can see the delta by adding it to a date
print(todayDateTime)
print(todayDateTime+eta)
print(str(todayDateTime+eta))
#useful to log time

