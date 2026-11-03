###
# Counts vowels in the text
#
text = "This is a sample text."
vowels = "aeiouAEIOU"
vowel_count = 0

# Count vowels in the text
while text:
    char = text[0]
    if char in vowels:
        vowel_count += 1
    text = text[1:]

print(f"The number of vowels in the text is: {vowel_count}")
