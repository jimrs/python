def fibonacci(n):
    sequence = list()
    sequence.extend([1, 1])     # jako append, nebere 1 objekt, ale iterable

    for i in range(2, n):
        sequence.append(sequence[i-2] + sequence[i-1])

    return sequence

n = int(input('Zadej cislo n pro vypis n clenu Fibonacciho posloupnosti: '))
print(fibonacci(n))