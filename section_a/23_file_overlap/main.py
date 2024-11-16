"""File Overlap.

Given two .txt files that have lists of
numbers in them, find the numbers that are
overlapping. One .txt file has a list of
all prime numbers under 1000, and the
other .txt file has a list of happy
numbers up to 1000.

(If you forgot, prime numbers are numbers
that can’t be divided by any other number.
And yes, happy numbers are a real thing in
mathematics - you can look it up on
Wikipedia. The explanation is easier with
an example, which I will describe below.)
"""
import os


root = os.path.dirname(os.path.abspath(__file__))
primes_file_path = os.path.join(root, "primes.txt")
happys_file_path = os.path.join(root, "happys.txt")


def read_file(file_path):
    """Read contents of a file."""
    with open(file_path, "r") as file:
        return file.read()


primes = [int(n) for n in read_file(primes_file_path).split("\n") if n != ""]
happys = [int(n) for n in read_file(happys_file_path).split("\n") if n != ""]

overlaps = [n for n in primes if n in happys]

print(f"Overlaps: {overlaps}")