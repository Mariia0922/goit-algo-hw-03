from datetime import datetime, timedelta


users = [
    {"name": "Анна", "birthday": "2004-02-28"},
    {"name": "Іван", "birthday": "1800-02-24"},
    {"name": "Марія", "birthday": "1760-01-14"},
    {"name": "Олег", "birthday": "1600-02-26"},
]

def find_upcoming_birthdays(users):
    today = datetime.now()
    upcoming_birthdays = []

    
    for user in users:
        birthday_this_year = datetime.strptime(user["birthday"][5:], "%m-%d").replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        
        
        delta = (birthday_this_year - today).days

        
        if 0 <= delta <= 7:
            if birthday_this_year.weekday() in [5, 6]:  # Субота або неділя
                while birthday_this_year.weekday() != 0:
                    birthday_this_year += timedelta(days=1)
            
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": birthday_this_year.strftime("%Y-%m-%d")
            })

    return upcoming_birthdays


birthdays_next_week = find_upcoming_birthdays(users)
if birthdays_next_week:
    for birthday_info in birthdays_next_week:
        print(f"{birthday_info['name']} має день народження {birthday_info['congratulation_date']}, потрібно привітати.")
else:
    print("На наступний тиждень дні народження відсутні.")
