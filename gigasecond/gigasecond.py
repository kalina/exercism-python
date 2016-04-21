import datetime

def add_gigasecond(a):
  gigasecond = 10**9
  return a + datetime.timedelta(seconds=gigasecond)
