word = "Education"
vowels = "aeiou"
vowel_count = 0
for letter in word:
    if letter.lower() in vowels:
        vowel_count += 1
print(vowel_count)