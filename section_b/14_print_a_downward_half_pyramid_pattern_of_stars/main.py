"""Print a downward half-pyramid pattern of stars.

Expected output:

```
* * * * *  
* * * *  
* * *  
* *  
*
```
"""

for x in range(5, 0, -1):
    print("* " * x)