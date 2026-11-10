def hide(card_number):
    return card_number[:2] + "*" * 10 + card_number[-4:]

card = "5290312400019022"
masked_card = hide(card)

print(masked_card)