from settings import load_settings, get_single_setting
from datetime import datetime, timedelta

now = datetime.now()

def get_bedtime():
    settings = load_settings()
    bedtime_str = settings["bedtime"]
    bedtime_time = datetime.strptime(bedtime_str, "%H:%M")
    bedtime_date = bedtime_time.replace(year=now.year, month=now.month, day=now.day)
    
    if now > bedtime_date:
        bedtime_date = bedtime_date + timedelta(days=1)
    
    time_to_bed = bedtime_date - now
    
    seconds = int(time_to_bed.seconds())
    hours = seconds // 3600
    seconds_left = seconds - (hours * 3600)
    minutes = seconds_left // 60

    print(f"{hours}h {minutes}m until bed")




