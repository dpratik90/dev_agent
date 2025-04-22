Sure, I will write a Python function for your requirement.

```python
def print_fibonacci(n):
    # variable initialization
    a, b = 0, 1
    
    while a < n:
        print(a, end=' ')
        a, b = b, a+b # update values

# test the function
print_fibonacci(50)
```

This function will print all the Fibonacci numbers less than the given number. For example, when it is 50, the function will print: 0 1 1 2 3 5 8 13 21 34