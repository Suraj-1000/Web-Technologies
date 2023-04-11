def get_weekend_avg_temp(weekly_temp):
    weekly_temp=[temp for day, temp in weekly_temp.items()if day.lower()in ['sunday', 'monday']]
    return sum(weekly_temp)/len(weekly_temp)if len(weekly_temp)> 0 else None
weekly_temp= {'sunday':19, 'monday':21,'tuesday':25, 'wednesday':29,'thursday':31, 'friday':25, 'saturday':35}
weekend_avg_temp=get_weekend_avg_temp(weekly_temp)

if weekend_avg_temp is not None:
    print("the average temerature of the weekend",weekend_avg_temp, "degrees")
else:
    print("no weekend temeprature")

