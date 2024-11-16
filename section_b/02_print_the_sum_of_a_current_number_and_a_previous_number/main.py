"""Print the Sum of a Current Number and a Previous number.

Write a Python code to iterate the first
10 numbers, and in each iteration, print
the sum of the current and previous
number.
"""

total_range = 10

print("Printing current and previous number sum in a range(%i)" % total_range)

for i in range(total_range):
    prev = 0
    if i > 0:
        prev = i - 1

    num_sum = i + prev
    print("Current Number %i Previous Number  %i  Sum:  %i" % (i, prev, num_sum))
