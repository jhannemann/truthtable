# Print Truth Tables

This module exports a single function, print_truth_table,
which takes a boolean function as an argument and prints
the function's truth table.

The function uses the
[inspect](https://docs.python.org/3/library/inspect.html)
module to derive the number and names of the function parameters
automatically.

## Example

```python3
>>> from truthtable import print_truth_table
>>> def AND(x, y):
	return x and y

>>> print_truth_table(AND)
AND(x, y):
x|y|AND
-------
0|0|0
0|1|0
1|0|0
1|1|1
>>> 
```
