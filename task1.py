from datetime import date
import calendar

day=date.today().day;
month=date.today().month;
temperature=-5;
print(f"Сегодня {day} {calendar.month_name[month]}. На улице {temperature} градусов.")
if temperature<0:
    print("Холодно, лучше остаться дома")