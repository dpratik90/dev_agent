In Python, a function to generate Fibonacci sequence up to a given number could look like this:

```python
def print_fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# use the function
print_fibonacci(50)
```
This script will print all Fibonacci numbers under 50. In the Fibonacci sequence, the next number is the sum of the last two. The sequence starts with 0 and 1. This implementation takes advantage of Python's simultaneous assignment feature to easily generate the sequence.