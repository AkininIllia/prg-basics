time_24 = input("Enter time (24-hour format): ")

hours_str, minutes_str = time_24.split(":")
hours = int(hours_str)
minutes = int(minutes_str)

if hours >= 12:
    period = "pm"
    if hours > 12:
        hours -= 12
else:
    period = "am"
    if hours == 0:
        hours = 12

print(f"Time in 12-hour format: {hours}:{minutes:02d}{period}")