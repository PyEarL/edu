def get_hidden_card(card_number, hide=4):
    card_number = str(card_number)
    stars = str('*' * hide)
    return f'{stars}{card_number[-4:]}'

number = get_hidden_card(1234567890123456)
print(number)