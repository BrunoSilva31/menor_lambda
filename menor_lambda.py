from functools import reduce

numeros = [10, 4, 50, 16]

menor = reduce(lambda a, b: a if a < b else b, numeros)
print(menor)
