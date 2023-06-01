# Beata G-python-ez12 — Dziś o 18:16
def check_mail(user_mail, base_mail):
    if user_mail in base_mail:
        return True
    else:
        return False


base_mail = ['jan@gmail.com', 'anna@gmail.com', 'kamil@gmail.com', 'dk@wp.pl']
input_mail = input('podaj adres mailowy: ')

if check_mail(input_mail, base_mail):
    print("Podany adres e-mail znajduje się w bazie maili.")
else:
    print("Podany adres e-mail nie znajduje się w bazie maili.")

# Edyta P-python-ez12 — Dziś o 18:16
# def check_if_mail_on_list(mail, lista):
#     mail_empty = ""
#     for i in lista:
#         if i == mail:
#             print("Mail jest na liście!")
#             mail_empty = mail
#
#     if mail_empty == "":
#         print("Nie ma maila na liście!")