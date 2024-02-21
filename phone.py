import re

def normalize_phone(phone_number):
    
    cleaned_number = re.sub(r'[^\d]', '', phone_number)

    
    if len(cleaned_number) == 9:
        normalized_number = '+380' + cleaned_number
    elif len(cleaned_number) == 10 and cleaned_number.startswith('0'):
        normalized_number = '+38' + cleaned_number
    elif len(cleaned_number) == 12 and cleaned_number.startswith('380'):
        normalized_number = '+' + cleaned_number
    else:
        print("Некоректний формат номера.")
        return None

    return normalized_number


raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


for number in raw_numbers:
    normalized_number = normalize_phone(number)
    if normalized_number:
        print(f"Оригінальний номер: {number}, Нормалізований номер: {normalized_number}")