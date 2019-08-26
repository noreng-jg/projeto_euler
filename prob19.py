month_days=dict(zip(range(1,13),[31,'a',31, 30,31,30, 31,31,30,31,30,31]))

def leap_year(year):
    return (year%400==0) or (year%4==0) or not (year%100==0)

registers={}
days_acums=0

for year in range(1900,2001):
    month_days[2]=29 if leap_year(year) else 28
    for month in month_days.keys():
        for day in range(1,month_days[month]+1):
            registers[year,month,day]=days_acums%7 #0 for mondays, 6 for sundays
            days_acums+=1

sum_first_day_month=0

for register in registers.keys():
    if register[0]>=1901 and register[2]==1 and registers[register]==6:
                sum_first_day_month+=1

print (sum_first_day_month)



