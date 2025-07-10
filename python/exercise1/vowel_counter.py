#!/usr/bin/env python3

def num_vowels(text):
    """Return the number of vowels in string."""
    vowels = "aeiou"
    num = 0
    for v in vowels:
        num += text.count(v)        
    return num

def num_consonants(text):
    vowels = "aeiou"
    num = 0
    for letter in text:
        if letter.isalpha() and letter not in vowels:
           num += 1
    return num

text = str(input("Enter a sentence: ")).lower()
print("Number of vowels:", num_vowels(text))
print("Number of consonants:", num_consonants(text))

