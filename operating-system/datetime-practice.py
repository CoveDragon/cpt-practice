from datetime import datetime, timedelta, timezone

# 1. Get the current local date and time
now = datetime.now()
print("Current Time:", now) 
# Output example: 2026-11-09 16:11:22.123456

# 2. Get current time in UTC (Best practice for internationalization)
utc_now = datetime.now(timezone.utc)
print("UTC Time:", utc_now)

# 3. Create a specific date and time (Year, Month, Day, Hour, Minute)
specific_date = datetime(2026, 12, 25, 8, 30)
print("Specific Date:", specific_date)

# getting local timezone does not work.

# 1. Get a datetime object aware of your local timezone
local_dt = datetime.now().astimezone()

# 2. Extract the timezone information
local_timezone = local_dt.tzinfo
timezone_name = local_dt.tzname()
utc_offset = local_dt.strftime('%z')

# 3. Print the results
print(f"Full Timezone Info: {local_timezone}")
print(f"Timezone Name:       {timezone_name}")
print(f"UTC Offset:          {utc_offset}")

# Final
# Get current time in UTC (Best practice for internationalization)
utc_now = datetime.now(timezone.utc)
print ("UTC Time:", utc_now.strftime("%Y-%m-%d %H:%M:%S"))