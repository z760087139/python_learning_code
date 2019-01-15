import datetime
# current time
current_time = datetime.datetime.now()

# str from time
strtime = current_time.strftime('%F')

# time from str 
time_time = datetime.datetime.strptime('%F')

# get delta time
time2 = datetime.datetime.now()
time_delta = abs(current_time-time2)
delta_min = time_delta.seconds/60

