def add_daily_temp(weekly_temps, temp, day):
    """this function is used to print average temperture"""
    if day not in weekly_temps:
        weekly_temps[day]=temp
    return weekly_temps
weekly_temps={}
weekly_temps=add_daily_temp(weekly_temps, 35, 'Sunday')
weekly_temps=add_daily_temp(weekly_temps, 39, 'Monday')
weekly_temps=add_daily_temp(weekly_temps, 45, 'sunday')
print(weekly_temps)

