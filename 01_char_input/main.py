"""Character Input.

Create a program that asks the user
to enter their name and their age.
Print out a message addressed to them
that tells them the year that they
will turn 100 years old. Note: for
this exercise, the expectation is that
you explicitly write out the year
(and therefore be out of date the next
year). If you want to do this in a
generic way, see exercise 39.
"""

year_of = 2024
name = input("Enter Name: ")
age = int(input("Enter Age: ").strip())

years_remain = 100 - age
hundred_year = year_of + years_remain

print(name + " will be 100 in year " + str(hundred_year) + ".")
