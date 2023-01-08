import datetime
import pytz

Tz = pytz.timezone("Asia/Karachi")
START_TIME=datetime.time(8,0,0)
END_TIME=datetime.time(18,0,0)
serving_days_of_week=[1,3,5,6]
break_start_time=datetime.time(12,0,0)
break_end_time=datetime.time(14,45,0)
saturday=6





def is_shop_open(date=datetime.datetime.now(tz=Tz)):
    day_of_week=date.isocalendar()[2] 
    week_of_the_month =date.isocalendar()[1] 
    if  day_of_week in serving_days_of_week and time_in_range(START_TIME,END_TIME,date):
        if day_of_week is saturday and week_of_the_month is 1:                
            return True
        elif day_of_week is not saturday :
            return True
        else:
            return  "Shop will open on monday 8:00 AM"
    else:
       return get_message(START_TIME,END_TIME,date)   
        
        
                        

def time_in_range(start, end, x):
    if start <= end:
        return start <= x.time() <= end and not break_start_time< x.time() < break_end_time
    else:
        return start <= x.time() or x.time() <= end and not break_start_time < x.time()or x.time() < break_end_time
 
    
    

def get_message(start, end, date):
    day_of_week=date.isocalendar()[2] 
    if day_of_week not in serving_days_of_week:
       return   'Working days are Monday, Wednesday and friday'
    elif start < date.time() and date.time() > end:
        return    "Shop timimg is 8:00 AM to 6:00 PM"
    elif date.time()>break_start_time and date.time()<break_end_time:
        return   "Shop will remain close during lunchtime (12:00 - 2:45)"
    