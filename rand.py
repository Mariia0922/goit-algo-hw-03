import random

def get_numbers_ticket(min=1, max=10):
    try:
        if not 1 <= min <= max <= 10:
            print("Числа діапазону повинні бути в межах від 1 до 1000, де початкове число не більше за кінцеве.")
            return []
        
        quantity = max - min 

        lottery_numbers = sorted(random.sample(range(min, max + 1), quantity))

        return lottery_numbers
    except ValueError:
        print("Введено некоректне число. Будь ласка, введіть ціле число.")
        return []

lottery_numbers = get_numbers_ticket()
if lottery_numbers:
    print("Набір чисел для лотереї:", lottery_numbers)