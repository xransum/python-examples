"""Calculate income tax.

Calculate income tax for the given income
by adhering to the rules below

| Taxable Income	| Rate (in %) |
| -------------- | ----------- |
| First $10,000  | 0           |
| Next $10,000   | 10          |
| The remaining  | 20          |

Expected Output:

For example, suppose the income is 45000,
and the income tax payable is

```
10000*0% + 10000*10%  + 25000*20% = $6000
```
"""

def get_income_tax(income):
    """Calculate income tax."""
    new_sum = income
    tax = 0

    if new_sum >= 10000:
        new_sum -= 10000

    if new_sum >= 10000:
        tax += 1000
        new_sum -= 10000

    if new_sum > 0:
        tax += (new_sum * 0.20)

    return tax


print(get_income_tax(45000))