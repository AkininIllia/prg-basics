total_amount = int(input('Enter amount: '))
amount_without_vat = total_amount / 1.23
vat_23 = total_amount - amount_without_vat
print (f'Amount without VAT: {amount_without_vat:.2f}')
print (f'VAT 23%: {vat_23:.2f}')