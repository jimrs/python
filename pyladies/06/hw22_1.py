def fact(n):
    product = 1
    for i in range(n):
        product *= i+1
    return product

print(fact(10))

