my_str = input("Несколько слов с пробелами: ").split()
for i, word in enumerate(my_str, 1):
    print(f'{i} {word[:10]}')