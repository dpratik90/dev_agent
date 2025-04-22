Sure, here is a simple Python function that prints the Fibonacci series up to the given number of terms:

```python
def print_fibonacci(n_terms):
    if n_terms <= 0:
        print("Please provide a positive integer.")
    elif n_terms == 1:
        print("Fibonacci sequence up to", n_terms, ":")
        print(0)
    else:
        print("Fibonacci sequence up to", n_terms, ":")
        term1, term2 = 0, 1
        count = 0
        while count < n_terms:
            print(term1)
            next_term = term1 + term2
            # swap values
            term1 = term2
            term2 = next_term
            count += 1
```

You can use the function `print_fibonacci(n_terms)` where `n_terms` is the number of terms in the Fibonacci sequence you want to print. For example, `print_fibonacci(5)` will print the first five terms of the Fibonacci sequence:

```
0
1
1
2
3
```