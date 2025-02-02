n = int(input("Enter the no of Fibonacci term :"))
fib_sequence = [0, 1]
for i in range(2, n):
    next_term = fib_sequence[-1] + fib_sequence[-2]
    fib_sequence.append(next_term)
print("Fibonacci Series:", fib_sequence[:n])
