"""Fibonacci.

Write a program that asks the user how
many Fibonnaci numbers to generate and
then generates them. Take this opportunity
to think about how you can use functions.
Make sure to ask the user to enter the
number of numbers in the sequence to
generate.

Hint:
    - The Fibonnaci seqence is a sequence
      of numbers where the next number in
      the sequence is the sum of the
      previous two numbers in the
      sequence. The sequence looks like
      this: (1, 1, 2, 3, 5, 8, 13, ...)
"""

def get_fib(total):
    """Get the Fibonnaci seqence to a given total number."""
    seq = []
    
    a, b = 0, 1
    for i in range(total):
        if len(seq) > 1:
            b = seq[-1]
        if len(seq) >= 2:
            a = seq[-2]

        n = a + b
        seq.append(n)
        
    return seq


total = int(input("Total Fibonnaci's: "))
fibs = get_fib(total)
print(fibs)