"""Check Palindrome Number.

Write a Python code to check if the given
number is palindrome. A palindrome number
is a number that is the same after
reverse. For example, 545 is the
palindrome number.

Expected Output:

```
original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number
```
"""

def check_palindrome(n):
    """Check Palindrome Number."""
    return str(n) == str(n)[::-1]


def print_palindrome(n):
    """Print Palindrome Number."""
    is_pal = check_palindrome(n)
    print(f"original number {n}")

    if is_pal is True:
        print("Yes. given number is palindrome number")
    else:
        print("No. given number is not palindrome number")


print_palindrome(121)
print_palindrome(125)
