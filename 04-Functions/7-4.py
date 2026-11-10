def count_letter(text, letter):
    return text.lower().count(letter.lower())

text = "You never get a second chance to make a first impression"
target_letter = 'e'

letter_count = count_letter(text, target_letter)

print(text)
print(f"The number of letter '{target_letter}': {letter_count}")