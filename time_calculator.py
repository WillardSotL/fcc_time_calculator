def add_time(start, duration, wkday=None):
# Splitting the time into min, hrs, and time of day
    ampm = start.split()
    time = ampm[0].split(":")
    if ampm[1] == "AM":
        current_hrs = int(time[0])
    else:
        current_hrs = int(time[0])+12
    adv = duration.split(":")

# Minutes calculation
    comb_min = int(time[1]) + int(adv[1])
    hrs = 0
    if comb_min < 60:
        new_min = comb_min
    else:
        while comb_min >= 60:
            hrs = hrs + 1
            comb_min = comb_min - 60
            new_min = comb_min
    if new_min<10:
        new_min = f"0{new_min}"
    else:
        new_min = new_min

# Hours calculation
    comb_hrs = current_hrs + int(adv[0]) + hrs
    days = 0
    if comb_hrs < 24:
        new_hrs = comb_hrs
    else:
        while comb_hrs >= 24:
            days = days + 1
            comb_hrs = comb_hrs - 24
        if comb_hrs == 0:
            new_hrs = 12
        else:
            new_hrs = comb_hrs
    if new_hrs < 12 or new_hrs == 12 and days > 0:
        ap = "AM"
    else:
        ap = "PM"
        if new_hrs > 12:
            new_hrs = new_hrs - 12
        else:
            new_hrs = new_hrs

# Day calculation
    if days <= 0:
        day_desc = ""
    elif days > 0 and days <=1:
        day_desc = " (next day)"
    else:
        day_desc = f" ({days} days later)"

# Weekday Calculation
    days_of_week = {
        "Monday": 1,
        "Tuesday": 2,
        "Wednesday": 3,
        "Thursday": 4,
        "Friday": 5,
        "Saturday": 6,
        "Sunday": 7
    }
    days_of_week_conv = {
        "1": ", Monday",
        "2": ", Tuesday",
        "3": ", Wednesday",
        "4": ", Thursday",
        "5": ", Friday",
        "6": ", Saturday",
        "7": ", Sunday"
    }
# Converting day of week to integer
    if wkday == None:
        wkd = ""
    else:
        wkd_conv = days_of_week.get(str(wkday).title())
        count_days = wkd_conv + days
        if count_days <= 7:
            new_day = count_days
        else:
            while count_days > 7:
                count_days = count_days - 7
            new_day = count_days
        wkd = days_of_week_conv.get(str(new_day))
    new_time = f"{new_hrs}:{new_min} {ap}{wkd}{day_desc}"
    return new_time
