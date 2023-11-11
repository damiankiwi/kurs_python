def find_missing_digits(phone_number):
    all_digits = set("0123456789")
    phone_digits = set(phone_number)

    missing_digits = all_digits - phone_digits

    return sorted(missing_digits)

mobile_number = input("Podaj numer telefonu: ")

if mobile_number.isdigit():
    missing_digits_list = find_missing_digits(mobile_number)
    if missing_digits_list:
        print(f"Brakujące cyfry w numerze telefonu: {', '.join(missing_digits_list)}")
    else:
        print("Numer telefonu zawiera wszystkie cyfry.")
else:
    print("Podaj poprawny numer telefonu (bez spacji ani innych znaków).")