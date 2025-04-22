In Python, we can create a simple function to generate and print the Fibonacci series up to a specific number. The Fibonacci series is where each number in the series is the sum of the two preceding ones. The series starts with 0 and 1.

Here's a simple code snippet in Python.

```python
def print_fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

# Use the function
print_fibonacci(20)
```
This function starts the series with 0 and 1. In each iteration of the loop, it prints out the current number (`a`), then adjusts `a` and `b` to refer to the next two numbers in the series. It continues doing this until it reaches a number greater than `n`. 

You can call the function `print_fibonacci(n)` passing the desired number `n` up to which you want to print the Fibonacci series. In this example, it will print the Fibonacci numbers up to 20.

Please replace the number `20` with any other number up to which you want to generate the Fibonacci series.
