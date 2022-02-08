# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print([num * 3 for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]])
print([num for num in range(11) if num % 2 == 0])
print([num for num in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if num % 2 != 0])
print([num / 2 if num % 2 == 0 else num * 2 for num in range(1, 11)])
