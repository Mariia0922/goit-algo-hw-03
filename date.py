from datetime import datetime

date = input("Будь ласка, введіть дату у форматі ДД-ММ-РРРР (наприклад, 25-12-2021): ")

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%d-%m-%Y").date()

        current_date = datetime.today().date()

        difference = current_date - input_date

        print(f"кількість днів від заданої дати до поточної є: {difference.days} .")
    except ValueError:
        print("Некоректний формат дати. Будь ласка, спробуйте ще раз.")
        
get_days_from_today(date)







