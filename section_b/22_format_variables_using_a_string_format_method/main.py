"""Format variables using a string.format() method.

Write a program to use string.format()
method to format the following three
variables as per the expected output

Given:

```python
totalMoney = 1000
quantity = 3
price = 450
```

Expected Output:

```
I have 1000 dollars so I can buy 3 football for 450.00 dollars.
```
"""

totalMoney = 1000
quantity = 3
price = 450
text = "I have {0} dollars so I can buy {1} football for {2} dollars."

print(text.format(totalMoney, quantity, price))