Here's a Python function that prints the Fibonacci series up to a given number.

```python
def print_fibonacci(n):
    a, b = 0, 1  # fibonacci initial two numbers

    while a < n:
        print(a, end=' ')
        a, b = b, a+b  # generate next fibonacci number

    print()  # print newline

print_fibonacci(100)
```

When you run this program, it outputs the Fibonacci numbers that are less than the input number (in this case, 100).

Remember that the Fibonacci series is a sequence of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.