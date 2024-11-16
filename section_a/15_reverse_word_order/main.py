"""Reverse Word Order.

Write a program (using functions!) that
asks the user for a long string containing
multiple words. Print back to the user the
same string, except with the words in
backwards order. For example, say I type
the string:
'''
My name is Michele
'''

Then I would see the string:
'''
Michele is name My
'''

shown back to me.
"""

def inverse_words(txt):
    """Inverse the word order of ths given text."""
    words = txt.split(" ")
    reordered = []

    for w in words[::-1]:
        reordered.append(w)

    return " ".join(reordered)


txt = input("Input a long string containing multiple words: ")
reordered = inverse_words(txt)

print(reordered)