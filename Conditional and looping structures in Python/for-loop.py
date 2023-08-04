# For
text = input("Enter a text: ")
VOWELS = "AEIOU"

for vowel in text:
    if vowel.upper() in VOWELS:
        print(vowel, end="")

print()
