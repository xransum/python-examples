"""String Lists.

Ask the user for a string and print out
whether this string is a palindrome or
not. (A palindrome is a string that reads
the same forwards and backwards.)
"""

words = input("Input a word or phrase: ").strip()
inversed_words = words[::-1]

if words.lower() == inversed_words.lower():
    print(f'"{words}" is a palindrome.')
else:
    print(f'"{words}" is NOT a palindrome.')
