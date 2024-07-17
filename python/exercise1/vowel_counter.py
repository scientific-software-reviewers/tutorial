#!/usr/bin/env python3

def num_vowels(text):
    """Return the number of vowels in string."""
    vowels = "aeiou"
    num = 0
    for v in vowels:
        num += text.lower().count(v)        
    return num

def num_consonants(text):
    vowels = "aeiou"
    num_consonants = 0
    for letter in text:
        if letter not in vowels:
            num_consonants += text.lower().count(letter) 
            #print("consonant", letter)
    
text = str(input("Enter a sentence: "))

print("Number of vowels", num_vowels(text))
print("Number of consonants", num_consonants(text))


