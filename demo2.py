from datetime import datetime
from zoneinfo import ZoneInfo

utc_time = datetime.now(ZoneInfo("UTC"))
jakarta_time = datetime.now(ZoneInfo("Asia/Jakarta"))

print("UTC time :", utc_time.strftime("%H:%M:%S"))
print("Jakarta time :", jakarta_time.strftime("%H:%M:%S"))