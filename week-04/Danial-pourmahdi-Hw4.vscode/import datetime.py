#q1
import datetime
def restrict_hours(start, end):
  def decorator(funk):
    def warped(*args, **kargs):
      hour = datetime.datetime.now().hour
      if start <= hour < end:
         return funk(*args, **kargs)
      else:
          print("not optimid time")      
    return warped
  return decorator

@restrict_hours(start=9, end=17)
def do_work():
  print("working")

do_work()