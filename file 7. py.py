#11. write a program that generates first n numbers of fibonacci sequqence



def fibonacci_sequence(n):
    fib_sequence = []

    # Handle the base cases
    if n >= 1:
        fib_sequence.append(0)
    if n >= 2:
        fib_sequence.append(1)

    # Generate Fibonacci sequence
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    return fib_sequence


# Example usage:
n = 10  # Replace with any positive integer
sequence = fibonacci_sequence(n)
print(f"The first {n} numbers of the Fibonacci sequence are:")
print(sequence)