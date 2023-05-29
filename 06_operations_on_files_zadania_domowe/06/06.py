# def get_card_number():
#     while True:
#         card_nr = input("Insert card number here ->")
#         card_nr = card_nr.replace(" ", "")
#         card_nr = card_nr.replace("-", "")
#
#         if card_nr.isdigit():
#             print("Yes, can be card number")
#             break
#         else:
#             print("Nope! This is not card number")
#             print("-- Try again! --")
#
#     return card_nr
#
#
# def is_visa(card_num):
#     """Function that checks visa numbers"""
#     return card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13)
#     # if card_num[0] == '4' and (len(card_num) == 16 or len(card_num) == 13):
#     #     return True
#     # else:
#     #     return False
#
#
# def is_mastercard(card_num):
#     """Function that checks mastercard numbers"""
#     start_condition = int(card_num[0:2]) in range(51, 56) or int(card_num[0:4]) in range(2221, 2721)
#
#     return len(card_num) == 16 and start_condition
#     # if len(card_num) == 16 and start_condition:
#     #     return True
#     # else:
#     #     return False
#
#
# def is_amex(card_num):
#     """Function that checks amex numbers"""
#     # American Express card numbers start with 34 or 37 and have 15 digits.
#     return len(card_num) == 15 and card_num[0:2] in ('34', '37')
#     # if len(card_num) == 15 and card_num[0:2] in ('34', '37'):
#     #     return True
#     # else:
#     #     return False
#
#
# def main():
#
#
# number = get_card_number()
# print('💳 :', number)
#
# if is_visa(number):
#     print("This is Visa card number")
# elif is_mastercard(number):
#     print("This is MasterCard card number")
# elif is_amex(number):
#     print("This is AmericanExpress card number")
# else:
#     print("Unknown card number")
#
# # --- main part of the program
#
# main()

filename = 'cards_number.txt'

def card_input():
    with open(filename, 'r', encoding='utf-8') as cards:
        load_cards = cards.readlines()
    return load_cards


def is_visa(card_number):
    return card_number[0] == '4' and (len(card_number) == 16 or len(card_number) == 13)


def is_mastercard(card_number):
    start_condition = int(card_number[0:2]) in range(51, 56) or int(card_number[0:4]) in range(2221, 2721)
    return len(card_number) == 16 and start_condition


def is_amex(card_number):
    return len(card_number) == 15 and card_number[0:2] in ('34', '37')


def read_cards_number(filename) -> list:
    with open(filename) as fp:
        content = fp.readlines()
    return content


def save_cards_number(filename, card_number):
    with open(filename, 'a') as fp:
        fp.write(card_number + '\n')


def main():
    cards_list = read_cards_number('cards_number.txt')

    for card in cards_list:
        card = card.replace(' ', '').strip()
        if is_visa(card):
            print("This is Visa card number")
            save_cards_number('visa.txt', card)
        elif is_mastercard(card):
            print("This is MasterCard card number")
            save_cards_number('mastercard.txt', card)
        elif is_amex(card):
            print("This is AmericanExpress card number")
            save_cards_number('americaexpress.txt', card)
        else:
            print("Unknown card number")
            save_cards_number('unknown.txt', card)

__name__ == '__main__'
main()
